from django.shortcuts import render
from .models import New
from core.models import Product
from costumerapp .models import Costumer


def news_list(request):
    news_queryset = New.objects.all()
    return render(request, 'news_list.html', {'news': news_queryset})


def news_detail(request, id):
    # SELECT * FROM Product WHERE id = $id; -- где id - число с url
    new_object = New.objects.get(id=id)

    new_object.views_qty += 1

    user = request.user
    costumer = user.costumer
    new_object.costumer_views.add(costumer)
    # Сохранение в БД
    new_object.save()
    context = {
        "new": new_object,
    }
    return render(request, 'news_detail.html', context)
