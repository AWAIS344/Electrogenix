from django.shortcuts import render

from .models import Inverter

# Create your views here.

def Product(request):
    inverters=Inverter.objects.all()
    context={"inverters":inverters}

    return render(request,"products/products.html",context)

def Product_Detail(request,id):

    invertor=Inverter.objects.get(id=id)
    context={"invertor":invertor}
    return render(request,"products/products_details.html",context)
