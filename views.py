from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST ['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        User = User.objects.create_User(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        User.save();
        print('user created')
        return redirect('home')
    else:
        return render(request,'register.html')

