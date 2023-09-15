from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import Item
from .templates.forms import ItemForm


# Create your views here.


def index(request):
    items = Item.objects.all()
    template = loader.get_template("food/index.html")
    context = {
        'items': items,
    }

    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse("<h1>Item view</h1>")


def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    template = loader.get_template("food/detail.html")
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request,"food/item-form.html", {"form": form})


def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request,"food/item-form.html", {"form": form})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    # form = ItemForm(request.POST or None, instance=item)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    return render(request,"food/item-delete.html", {'item': item})
