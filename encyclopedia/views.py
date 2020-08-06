from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import random

from .forms import EditForm
from .forms import CreateForm
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):

    if util.get_entry(name) == None:
        return HttpResponse(status=404)
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(name),
            "name": name.capitalize()
        })


def create(request):
    form = CreateForm(request.POST)

    # process the data when received
    if request.method == 'POST':
        form = CreateForm(request.POST)  # not right
        if form.is_valid():
            # you should be able to extract inputs from the form here
            # content = form.content  # not right
            name = form.cleaned_data.get("created_title")
            content = form.cleaned_data.get("created_page")
            util.save_entry(name, content)
            return render(request, "encyclopedia/entry.html", {
                "entry": util.get_entry(name),
                "name": name.capitalize()
            })
    # loads the page initially
    return render(request, "encyclopedia/create.html", {
        "form": form
    })


def pickrand(request):
    entries = util.list_entries()
    pick = random.choice(entries)
    return entry(request, pick)


def edit(request, name):
    #initial = {'edited_form': 'This is default text.'}
    # load the form when the page is opened
    form = EditForm(request.POST)

    # process the data when received
    if request.method == 'POST':
        form = EditForm(request.POST)  # not right
        if form.is_valid():
            # you should be able to extract inputs from the form here
            # content = form.content  # not right
            content = form.cleaned_data.get("edited_page")
            util.save_entry(name, content)
            return render(request, "encyclopedia/entry.html", {
                "entry": util.get_entry(name),
                "name": name.capitalize()
            })
    # loads the page initially
    return render(request, "encyclopedia/edit.html", {
        "name": name,
        "entry": util.get_entry(name),
        "form": form
    })


# search still displays the wrong results
def search(request):
    if request.method == 'GET':
        search = request.GET.get('search-text')
        if util.get_entry(search) != None:
            return entry(request, search)
        else:
            entries = util.list_entries()
            for n in entries:
                if not search in n:
                    entries.remove(n)
            return render(request, "encyclopedia/search.html", {
                "search_text": search,
                "search_results": entries
            })
