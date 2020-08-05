from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import random


from .forms import NameForm
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
    return render(request, "encyclopedia/create.html")


def pickrand(request):
    entries = util.list_entries()
    pick = random.choice(entries)
    return entry(request, pick)


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
