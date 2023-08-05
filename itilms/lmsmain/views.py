from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm
from .forms import CategoryForm

# Create your views here
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    if request.method == 'POST':
        formm = CategoryForm(request.POST)
        if formm.is_valid():
            formm.save()
    totalbooksold=0
    for i in Book.objects.values('status','price'):
        if i['status']=='sold':
            if i['price'] != None:
                totalbooksold += int(i['price'])
    #-------
    totalbookrental = 0
    for i in Book.objects.values('status', 'rent_price'):
        if i['status'] == 'rent':
            if i['rent_price'] != None:
                totalbookrental += int(i['rent_price'])
    # -------
    fullprofits = totalbooksold + totalbookrental
    context={
        'cat' : Category.objects.all(),
        'book' : Book.objects.all(),
        'form':BookForm(),
        'fc':CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'sb':Book.objects.filter(status='sold').count(),
        'rb':Book.objects.filter(status='rent').count(),
        'ab':Book.objects.filter(status='available').count(),
        'fb':fullprofits,
        'tr':totalbooksold,
        'ts':totalbookrental,
    }
    return render(request,'pages/index.html',context)
def books(request):
    title=None
    search=Book.objects.all()
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search=search.filter(title__icontains=title)
   
    context={
        'cat' : Category.objects.all(),
        'book' : search,
        'fc':CategoryForm(),
        
        
    }
    return render(request,'pages/books.html',context)

def update(request,id):
    bid=Book.objects.get(id=id)
    if request.method == 'POST':
        formu = BookForm(request.POST, request.FILES,instance=bid)
        if formu.is_valid():
            formu.save()
            return redirect('/')
        
    else:
        formu = BookForm(instance=bid)
    context={
        
        'form':formu,    
        
    }
    return render(request,'pages/update.html',context)
def delete(request,id):
    bidd=Book.objects.get(id=id)
    if request.method == 'POST':
        bidd.delete()
        return redirect('/')
        
    
    return render(request,'pages/delete.html')
             
    