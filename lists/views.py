from django.shortcuts import redirect, render
from lists.models import Item

def landing_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list/')
    return render(request, 'landing.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
