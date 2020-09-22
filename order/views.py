from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import VegProduct, NonVegProduct, VeganProduct, Orders

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def login(request):
    if request.method == 'POST':    
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password = password)

        if user is not None:
            auth.login(request, user)
            return render (request, 'index.html')
        else:
            messages.info(request, 'Username or password incorrect')
            return redirect('/order/login')
    else:
        return render(request, 'login.html')



def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_no = request.POST['number']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirm']
        email = request.POST['email']
        

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken!')
                return redirect('/order/register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken!')
                return redirect('/order/register')
            else:
                user = User.objects.create_user( first_name = first_name, username= username, password = password, email = email, last_name = last_name)
                user.save()
                messages.info(request, 'Account created!')
                # return render(request, 'index.html')
        else:
            messages.info(request, 'Password not matching')
        return redirect('/order')
    else:
        return render(request, 'register.html',{})

def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def veg(request):
    products = VegProduct.objects.all()
    n = len(products)

    params = {'range': range(1,n), 'product': products}
    return render(request, 'veg.html',params)

def nonveg(request):
    products = NonVegProduct.objects.all()
    n = len(products)

    params = {'range': range(1,n), 'product': products}
    return render(request, 'nonveg.html', params)

def vegan(request):
    products = VeganProduct.objects.all()
    n = len(products)

    params = {'range': range(1,n), 'product': products}
    return render(request, 'vegan.html',params)

def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        contact_no = request.POST.get('contact_no','')
        address = request.POST.get('address1','') +" " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        order = Orders(items_json = items_json, name = name, email = email, address = address, city = city, state = state, zip_code = zip_code, contact_no = contact_no)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html',{'thank' : thank, 'id': id})
        
    return render(request, 'checkout.html')