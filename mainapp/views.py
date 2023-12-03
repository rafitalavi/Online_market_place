from django.shortcuts import render , redirect
from item.models import Category , Item
from .forms import SignupForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:9]
    categories = Category.objects.all()
    return render(request,'mainapp/index.html',{'categories': categories, 'items': items})
def contact(request):
    return render(request,'mainapp/contact.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            print(form.errors)
    else:    

        form = SignupForm()
    return render(request, 'mainapp/signup.html',{'form':form})   
 