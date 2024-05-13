from django.shortcuts import HttpResponse,redirect,render
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request,"myapp/home.html")


def reg(request):
    if request.method == 'POST':
        form = RegsForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data.get('name')
            email1 = form.cleaned_data.get('email')
            phone1 = form.cleaned_data.get('phone')
            adress1 = form.cleaned_data.get('adress')
            city1 = form.cleaned_data.get('city')
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists. Please choose a different one....")
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email1, password=password)
            user.name = name1
            user.phone = phone1
            user.adress = adress1
            user.city = city1
            user.is_active = 1
            user.is_staff = 0
            user.save()
            login(request, user)
            return redirect(log) 
        else:
            return render(request, "myapp/reg.html", {'form': form})
    form = RegsForm()
    return render(request, "myapp/reg.html", {'form': form})

    

def log(request):
    if request.method=='POST':
        x=LogsForm(request.POST)
        if x.is_valid():
            username = x.cleaned_data.get('username') 
            password = x.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None and user.is_superuser:
                login(request,user)
                return redirect(admin)
            elif user is not None and user.is_staff==0 and user.is_active==1:
                login(request,user)
                return redirect(purchase)
            else:
                return HttpResponse('sorry invalid')
    else:
        return render(request,"myapp/log.html")
    
    

def edit_prof(request,username):
    if request.method == 'POST':
        name1=request.POST['name']
        email1=request.POST['email']
        phone1=request.POST['phone']
        address1=request.POST['adress']
        city1=request.POST['city']
        username1=request.POST['username']
        pword1=request.POST['password']
        data=User.objects.filter(username=username)
        data.update(name=name1,email=email1,phone=phone1,adress=address1,city=city1,username=username1,password=pword1)
        return redirect(purchase)
    else:
        x=User.objects.get(username=username)
        return render(request,'myapp/editprof.html',{'item':x})


def dlt_prof(request,username):
    data=User.objects.filter(username=username)
    data.delete()
    return redirect(home)


def edit_product(request,id):
    if request.method == 'POST':
        name1=request.POST['name']
        price=request.POST['price']
        data=product.objects.filter(id=id)
        data.update(name=name1,price=price)
        return redirect(admin_prod)
    else:
        x=product.objects.get(id=id)
        return render(request,'myapp/edit_prod.html',{'edit':x})
    

def deleteprod(request,id):
    x=product.objects.get(id=id)
    x.delete()
    return redirect(admin_prod)


def edit_cat(request,id):
    if request.method == 'POST':
        name1=request.POST['name']
        data=categories.objects.filter(id=id)
        data.update(name=name1)
        return redirect(admin_cat)
    else:
        x=categories.objects.get(id=id)
        return render(request,'myapp/edit_cat.html',{'edit':x})


def deletecat(request,id):
    x=categories.objects.get(id=id)
    x.delete()
    return redirect(admin_cat)
    


def purchase(request):
    x=categories.objects.all()
    return render(request,"myapp/purchase.html",{"cat":x})



def profile(request,username):
    x=User.objects.get(username=username)
    y=len(Cart.objects.filter(user=request.user,status="cart"))
    return render(request,"myapp/profile.html",{'data':x,'y':y})

def allprofile(request):
    x=User.objects.filter(is_staff=0)
    return render(request,"myapp/allprofile.html",{'list':x})

def admin(request):
    return render(request,"myapp/admin.html")


def access(request):
    if request.method=="POST":
        x=category(request.POST,request.FILES)
        if x.is_valid():
            x.save()
            frm=category()
            return redirect(admin_cat)
            # return HttpResponse("done")
        else:
            return HttpResponse("Invalid")
    else:
        frm=category()
        return render (request,"myapp/access.html",{"form":frm})



def allproducts(request):
    if request.method=="POST":
        form=FileModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(admin_prod)
        else:
            print(form.errors)
            return HttpResponse("Not inserted - Form validation error")
    else:
        frm=FileModelForm()
        cat=categories.objects.all()
        return render (request,"myapp/all_form.html",{"form":frm,'cat':cat}) 

  
    

def all(request,id):
    ac=categories.objects.get(id=id)
    x=product.objects.filter(categories=ac)
    y=len(Cart.objects.filter(user=request.user,status="cart"))
    return render(request,"myapp/all.html",{'view':x,'y':y})


def adm_cat_prod(request,id):
    ac=categories.objects.get(id=id)
    x=product.objects.filter(categories=ac)
    return render(request,"myapp/pro_cat_admn.html",{'view':x})


def admin_prod(request):
    x=product.objects.all()
    return render(request,"myapp/adm_products.html",{"pro":x})

def admin_cat(request):
    x=categories.objects.all()
    return render(request,"myapp/admn_cat.html",{"cats":x})

def accessview(request):
    y=categories.objects.all()
    return render(request,"myapp/accessories.html",{'item':y})

def cartview(request):
    x=Cart.objects.filter(user=request.user,status="cart")
    y=len(Cart.objects.filter(user=request.user,status="cart"))
    total=Cart.objects.filter(user=request.user,status='cart').aggregate(tot=Sum("product__price"))
    return render(request,"myapp/cartview.html",{'cart':x,'total':total,'y':y})
    

def addcart(request,id):
    pro=product.objects.get(id=id)
    user=request.user
    Cart.objects.create(product=pro,user=user)
    return redirect(fullpro)


def deletecartitem(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.error(request,"Cart item Removed...")
    return redirect(cartview)


def checkout(request):
    if request.method=='POST':
        neworder=Order()
        neworder.user=request.user
        neworder.address=request.POST.get("address")
        neworder.phone=request.POST.get("phone")
        neworder.save()
        cart=Cart.objects.filter(user=request.user)
        for i in cart:
            Orderitem.objects.create(
                user=request.user,
                order=neworder,
                products=i.product,
                price=i.product.price
            )
        cart.delete()
        return redirect(orderview)
    else:
        return render(request,"myapp/checkout.html")


def orderview(request):
    x=Orderitem.objects.filter(user=request.user)
    return render(request,"myapp/orderview.html",{'ord':x})



def cancel_order(request,id):
    order=Orderitem.objects.get(id=id)
    order.status="cancelled"
    order.save()
    return redirect(orderview)

    
def viewlist(request):
    x=Orderitem.objects.all()
    return render(request,'myapp/admn_ordlist.html',{'view':x})


def fullpro(request):
    y=len(Cart.objects.filter(user=request.user,status="cart"))
    x=product.objects.all()
    return render(request,'myapp/fullpro.html',{'view':x,'y':y})


def search(request):
    if request.method=='GET':
        search=request.GET.get('search')
        pr=product.objects.filter(name__icontains=search)
        y=len(Cart.objects.filter(user=request.user,status="cart"))
        return render (request,'myapp/search.html',{'pro':pr,'y':y})
    else:
        return HttpResponse('not found')



def searchcat(request):
    if request.method=='GET':
        search=request.GET.get('search')
        cat=categories.objects.filter(name__icontains=search)
        return render (request,'myapp/searchcat.html',{'cat':cat})
    else:
        return HttpResponse('not found')


def prooo(request):
    return render(request,'myapp/prooo.html')