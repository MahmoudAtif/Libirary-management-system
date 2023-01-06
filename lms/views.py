from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from time import sleep

# Create your views here.


def register(request):   

    if request.user.is_authenticated:
        return redirect('index')
    else:    
        form =Register()
        if request.method=='POST':
            form = Register(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Success Registeration for '+ user)
                sleep(2)
                return redirect('login')
        context={
            # 'Signup_form':Signup(),
            'form': form,
        }

        return render(request,'pages/register.html',context)


def loginpage(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Username or Password is incorrect')
            
        context={
            
        }
            
        return render(request , 'pages/login.html',context)


def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    pro=Book.objects.all()
    cat=Category.objects.all()
    
    if request.method=='POST':
        data=BookForm(request.POST,request.FILES)
        if data.is_valid():
            data.save()

        category_data=CategoryForm(request.POST)
        if category_data.is_valid():
            category_data.save()

   
    if request.method=='GET':
        data_search=request.GET.get('search')
        result=pro.filter(book_name=data_search)
        # return redirect('search')


    context={
        'pro':pro,
        'book_form':BookForm(),
        'category_form':CategoryForm(),
        'cat':cat,
        'result':result,
    }    
    return render(request,'pages/index.html',context)




@login_required(login_url='login')
def books(request):
     pro=Book.objects.all()
     cat=Category.objects.all()
     context={
        'pro':pro,
        'book_form':BookForm(),
        'category_form':CategoryForm(),
        'cat':cat,
     }
     return render(request,'pages/books.html',context)


@login_required(login_url='login')
def update(request, id):
    cat=Category.objects.all()

    book_id=Book.objects.get(id=id)
    if request.method== 'POST':
        book_data=BookForm(request.POST , request.FILES , instance=book_id)
        if book_data.is_valid():
            book_data.save()

    else:
        book_data=BookForm(instance=book_id)
    
    context={
    'category_form':CategoryForm(),
    'cat':cat,
    'form': book_data
    }
    return render(request,'pages/update.html',context)






@login_required(login_url='login')
def delete(request,id):
    book_id=Book.objects.get(id=id)
    if request.method=='POST':
        book_id.delete()
        return redirect('index')

    return render(request,'pages/delete.html')








