from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib import admin

from pyverse import Pyverse
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True,blank=True)
    
    @admin.display(
        boolean = True,
        ordering="name"
    )

    def __str__(self):
        return self.name


class Rule(models.Model):
    #Allow verse metric, strophe metric, total verses, order. maybe specific models to be added to poemType?
    name = models.CharField(max_length=50)

    def assert_rule(self, text):
        pass

    def __str__(self):
        return self.name

class VerseMetric(Rule):
    size = models.PositiveSmallIntegerField(default=0)
    total_verses = models.PositiveSmallIntegerField(default=0)

    def _calculate_total_verses(self, text:"Poem"):
        if self.total_verses == 0:
            return True
        return len(text.get_verses()) == self.total_verses
    
    def _check_all_verses_equal(self, text:"Poem"):
        if self.size == 0:
            return True
        return all([length[1] == self.size for length in text.get_syllables()])
    
    def assert_rule(self, text:"Poem"):
        return all([
            self._check_all_verses_equal(text),
            self._calculate_total_verses(text)
            ])

class StropheMetric(Rule):
    size = models.PositiveSmallIntegerField(default=0)
    verses_per_strophe = models.JSONField()

    def _calculate_verse_ratio(self, text:"Poem"):
        if not self.verses_per_strophe:
            return True
        strophes = text.get_strophes()
        for index, size in enumerate(self.verses_per_strophe.values()):
            if size != strophes[index]:
                return False
        return True
    
    def _calculate_total_strophes(self, text:"Poem"):
        if self.size == 0:
            return True
        return len(text.get_strophes()) == self.size
    
    def assert_rule(self, text:"Poem"):
        return all([
                self._calculate_total_strophes(text),
                self._calculate_verse_ratio(text)
             ])

class NoRule(Rule):
    def assert_rule(self, text:"Poem"):
        return True
    
class PoemType(models.Model):
    name = models.CharField(max_length=50)
    rules = models.ManyToManyField(Rule)

    def check_rules(self,  text:"Poem") -> bool:
        return all(rule.assert_rule(text) for rule in self.rules)

    def __str__(self):
        return self.name 

class Poem(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    text = models.TextField()
    poem_type = models.ManyToManyField(PoemType)
    
    def __str__(self):
        return self.title
    
    def get_poem_types(self):
        return ",".join([p.name for p in self.poem_type.all()])
    
    def is_pure(self):
        ruleset = [result for result in self.poem_type.check_rules(text = self ,strict=True)]
        return all(ruleset)
    
    def get_strophes(self):
        return [strophe for strophe in self.text.split("\n\n")]

    def get_verses(self):
        return [verse for verse in self.text.split("\n")]

    def get_syllables(self):
        return [(index,Pyverse(verse).count,) for index,verse in enumerate(self.get_verses())]
    