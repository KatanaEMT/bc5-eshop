from django.shortcuts import render, redirect
from .models import Costumer, Profile


def costumer_view(request):
    costumer_list = Costumer.objects.all()
    context = {"costumer_list": costumer_list}
    return render(request, 'costumers.html', context)


def profile(request):
    profile_list = Profile.objects.all()
    context = {"profile": profile_list}
    return render(request, 'profile_lst.html', context)


def profile_detail(request, id):
    profile_info = Profile.objects.get(id=id)
    context = {"profile": profile_info}
    # if request.method == "GET":
    return render(request, 'profile_detail.html', context)


def costumers_create(request):
    if request.method == "GET":
        return render(request, 'costumers_create.html')
    elif request.method == "POST":
        # считывание данных с формы
        data = request.POST
        name = data["new_name"]
        age = data["new_age"]
        gender = data["new_gender"]
        # user = data["user"]


        # сохрание этих данных в
        new_object = Costumer.objects.create(
            name=name,
            age=age,
            gender=gender,
            # user=user
        )
        return redirect(f'/costumers/')


def profile_create(request):
    if request.method == "GET":
        return render(request, 'profile_create.html')
    elif request.method == "POST":
        data = request.POST
        bio = data["new_bio"]
        social_link = data["new_social_link"]
        phone_number = data["new_phone_number"]

        new_object = Profile.objects.create(
            bio=bio,
            social_link=social_link,
            phone_number=phone_number,
        )
        return redirect(f'/profile/{new_object.id}/')