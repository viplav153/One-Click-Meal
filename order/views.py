from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

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
                return redirect('order/login')
        else:
            messages.info(request, 'Password not matching')
        return redirect('/order')
    else:
        return render(request, 'register.html',{})

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def veg(request):
    return render(request, 'veg.html')

def nonveg(request):
    return render(request, 'nonveg.html')

def vegan(request):
    return render(request, 'vegan.html')