from django.shortcuts import render, get_object_or_404
from .models import Author
# Create your views here.
from django.views import generic

class AuthorsView(generic.ListView):
    template_name = "poems/authors.html"
    context_object_name = "authors_list"

    def get_queryset(self):
        return Author.objects.all()

def authors(request):
    authors = Author.objects.all()
    context = {
        "authors_list": authors
    }
    return render(request,"poems/authors.html",context)