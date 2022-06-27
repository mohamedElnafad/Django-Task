from dataclasses import field
from django.shortcuts import render,get_object_or_404,redirect
from .models import Itmes, User, NewProduct
from django.forms import  modelform_factory
from django import forms

# Create your views here.
def Itmes(request):

    return render(request, "product/products.html", {
            "range": range(5),
            "products": Itmes})



def ItemDetails(request, id):
    item = get_object_or_404(Itmes, pk=id)
    return render(request, 'product/Product-details.html',
                  {"product": item})


class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = {'Name','Email','Password'}

def Add_New_User(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = UserForm()
    return  render(request,'product/new_user.html',{"form":form})


class ProductForm(forms.ModelForm):
    class Meta:
        model = NewProduct
        # fields = {'Name','Description','Image'}
        fields = {"Image", "Description","Name"}

def Add_New_Product(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = ProductForm()
    return  render(request,'product/new_product.html',{"form":form})