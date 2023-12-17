from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    response=requests.get('https://fakestoreapi.com/products').json()
    return render(request,'index.html',{'response':response})
