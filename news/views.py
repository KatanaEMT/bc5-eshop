from django.shortcuts import render
from .models import New


def news_list(request):
    news_queryset = New.objects.all()
    return render(request, 'news_list.html', {'news': news_queryset})
