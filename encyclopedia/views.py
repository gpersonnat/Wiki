from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from markdown import markdown
from . import util
from django import forms
from django.urls import reverse
from django.shortcuts import redirect
from . import helpers
from . forms import createPage, editPage
import random


def index(request): 
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def display(request, title):
    entry = util.get_entry(title)
    if entry == None: 
        return render(request, "encyclopedia/entry.html", {
           "no_entry": True,
           "title": title      
        })
    html = markdown(entry)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html
    })
        
def search(request):
    """User search results"""
    title = request.POST.get("q")

    # Check if user inputted search result
    if not title:
        return render(request, "encyclopedia/results.html", {
            "no_entry": True
        })

    # Checks if title is in substring
    list_of_entries = helpers.convert_list_lowercase(util.list_entries())
    if title.lower() in list_of_entries:
        return redirect("encyclopedia:display", title=title)
    else:  
        return render(request, "encyclopedia/results.html", {
            "title": title,
            "entries": helpers.list_substring(util.list_entries(), title)
        })

def create_page(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = createPage(request.POST)
        if form.is_valid():
            if form.cleaned_data["title"].lower() in helpers.convert_list_lowercase(util.list_entries()):
                return render(request, "encyclopedia/create_page.html", {
                "form": createPage(),
                "error": "Title already exists"
            })
            util.save_entry(form.cleaned_data["title"], form.cleaned_data["content"])
            return redirect("encyclopedia:display", title=form.cleaned_data["title"])
        else: 
            return render(request, "encyclopedia/create_page.html", {
            "form": createPage()
        })        
    else:
        return render(request, "encyclopedia/create_page.html", {
            "form": createPage()
        })


def edit_page(request, entry):
    if request.method == "POST":
        form = editPage(request.POST)
        if form.is_valid():
            util.save_entry(entry, form.cleaned_data["content"])
            return redirect("encyclopedia:display", entry)
    else:
        return render(request, "encyclopedia/edit_page.html", {
            "form": editPage(initial={'content': markdown(util.get_entry(entry))}),
            "title": entry
         })

def random_page(request):
    list_of_entries = util.list_entries()
    random.shuffle(list_of_entries)
    print(list_of_entries[0])
    return redirect("encyclopedia:display", list_of_entries[0])




    


