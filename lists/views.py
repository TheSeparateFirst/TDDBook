from django.http import HttpResponse
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
