from django.shortcuts import render, get_object_or_404
from .models import Author,Poem
# Create your views here.
from django.views import generic
from django.utils.translation import gettext as _

class AuthorsView(generic.ListView):
    template_name = "poems/authors.html"
    context_object_name = "authors_list"

    def get_queryset(self):
        return Author.objects.all()
    
class PoemsView(generic.ListView):
    template_name = "poems/poems.html"
    context_object_name = "poems_list"

    def get_queryset(self):
        return Poem.objects.all()
    
class HomeView(generic.TemplateView):
    template_name = "poems/home.html"

    
def author(request, author_id):
    author = get_object_or_404(Author,pk=author_id)
    context = {
        "author": author,
        "poems": Poem.objects.filter(author=author_id)
    }
    return render(request,"poems/author_detail.html",context)