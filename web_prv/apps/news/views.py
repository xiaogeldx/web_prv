from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'news/index.html')

def news_detail(request):
    return render(request,'news/news_detail.html')

def search(request):
    return render(request,'news/search.html')
