from django.shortcuts import redirect, render
from lists.models import Item

def landing_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'landing.html', {'items': items})
