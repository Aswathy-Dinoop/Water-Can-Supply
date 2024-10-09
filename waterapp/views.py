from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from waterapp.models import UserType,Registration
# from django.contrib import messages

# Create your views here.
class index(TemplateView):
    template_name='index.html'
class register(TemplateView):
    template_name='register.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address'] 
        district = request.POST['district']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'register.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

            reg = Registration()# call the model
            reg.user = user
            reg.name=name
            reg.email=email
            reg.phone = phone
            reg.address=address
            reg.district=district
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            # messages="Registered Successfully"
            return redirect('/',{'message':"Registered Successfully"})
class loginview(TemplateView):
    template_name='login.html'
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                
            else:
                # messages.add_message(request, messages.INFO, "Hello world.")
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})