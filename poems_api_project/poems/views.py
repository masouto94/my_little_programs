from django.shortcuts import render, get_object_or_404
from .models import Author
# Create your views here.
from django.views import generic

class AuthorsView(generic.ListView):
    template_name = "poems/authors.html"
    context_object_name = "authors_list"

    def get_queryset(self):
        return Author.objects.all()
    

def author(request, author_id):
    author = get_object_or_404(Author,pk=author_id)
    context = {
        "author": author
    }
    return render(request,"poems/author_detail.html",context)