from django.shortcuts import render
from item.models import Category , Item
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:9]
    categories = Category.objects.all()
    return render(request,'mainapp/index.html',{'categories': categories, 'items': items})
def contact(request):
    return render(request,'mainapp/contact.html')