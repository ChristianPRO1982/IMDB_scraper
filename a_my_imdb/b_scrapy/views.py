from django.shortcuts import render


def scrapy_index(request):
    return render(request, 'scrapy/scrapy_index.html')