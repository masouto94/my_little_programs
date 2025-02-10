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
    
    def assert_rule(self, text:str):
        return all([length[1] == self.size for length in text.get_syllables()])

class NoRule(Rule):
    def assert_rule(self, text:str):
        return True
    
class PoemType(models.Model):
    name = models.CharField(max_length=50)
    rules = models.ManyToManyField(Rule)

    def check_rules(self, text:str, strict:bool = True ) -> bool:
        pass

    def __str__(self):
        return self.name 
    
class FreePoem(PoemType):

    def check_rules(self, text:str, strict:bool) -> bool:
        return True
    
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
    