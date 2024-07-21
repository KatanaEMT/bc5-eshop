from django.shortcuts import render, HttpResponse
from .models import *
from costumerapp.models import *
from django.contrib.auth.models import User
from .forms import ProductForm


def homepage(request):
    # SELECT * FROM Product;
    product_list = Product.objects.all()
    
    context = {"products": product_list}
    
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html', context)


def user_lst(request):
    user_lst = User.objects.all()
    context = {"user_lst": user_lst}
    return render(request, 'user_lst.html', context)


def user_detail(request, id):
    user_info = User.objects.get(id=id)
    context = {"user": user_info}
    # if request.method == "GET":
    return render(request, 'user_detail.html', context)


# def user_cabinet(request, id):
#     user = User.objects.get(id=id)
#     context = {"user": user}
#     return render(request, 'cabinet.html', context)



def product_detail(request, id):
    # SELECT * FROM Product WHERE id = $id; -- где id - число с url
    product_object = Product.objects.get(id=id)

    # Увеличение просмотра
    product_object.views_qty += 1

    # Уникальные просмотры
    if request.user.is_authenticated:
        user = request.user
        if not Costumer.objects.filter(user=user).exists():
            costumer = Costumer.objects.create(
                name=user.username,
                age=0,
                gender='-',
                user=user,
            )
        costumer = user.costumer
        product_object.costumer_views.add(costumer)
        # product_object.costumer_views.add(request.user.costumer)

    # Сохранение в БД
    product_object.save()

    context = {
        "product": product_object,
    }
    return render(request, 'product_detail.html', context)


def product_create(request):
    context = {}
    context["product_form"] = ProductForm()

    if request.method == "GET":
        return render(request, 'product_create.html', context)
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse("Успешно сохранено!")
        return HttpResponse("Ошибка валидации!")


