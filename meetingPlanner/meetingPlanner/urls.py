"""meetingPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from website.views import Home
from items.views import Itmes, ItemDetails, Add_New_User, Add_New_Product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('home.html', Home),
    path('products.html', Itmes),
    path('product_details/<int:id>', ItemDetails),
    path('new_user.html', Add_New_User),
    path('new_product.html', Add_New_Product),
]
