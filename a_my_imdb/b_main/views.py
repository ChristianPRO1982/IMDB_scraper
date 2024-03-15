from django.shortcuts import render

def home_page(request):
    return render(request, 'b_main/home_page.html')