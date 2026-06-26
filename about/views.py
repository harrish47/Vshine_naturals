from django.shortcuts import render, redirect

def about_details(request):
    return render(request, 'about.html')