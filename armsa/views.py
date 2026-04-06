from django.http.response import HttpResponse
from django.shortcuts import render

def first_page(request):
    main_str = "<h1>Hello, World!</h1>"
    return render(request, '/index.html')