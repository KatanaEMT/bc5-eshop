"""
URL configuration for eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings  # 1
from django.conf.urls.static import static
from costumerapp.views import *
from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('user/', user_lst, name='user-lst'),
    path('user/<int:id>/', user_detail, name='user-detail'),
    path('product-detail/<int:id>/', product_detail, name='product-detail'),
    path('product-create/', product_create, name='product-create'),
    path('costumers/', costumer_view, name="costumer-view"),
    path('costumers_create/', costumers_create, name="costumers-create"),
    path('profile/', profile, name="profile"),
    path('profile_create/', profile_create, name="profile-create"),
    path('profile/<int:id>/', profile_detail, name="profile-detail"),
    path('news/', news_list, name='news-list'),
    path('news-detail/<int:id>/', news_detail, name='news-detail'),
    path('new_create/', new_create, name='new-create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
