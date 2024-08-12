from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import login, logout,authenticate

from web.forms import Registration_Form
from web.forms import UserProfile_Form
from web.forms import Login_Form
from web.forms import BMRForm

from web.models import User
from web.models import UserProfile_Model

# Create your views here.

class Home_View(View):
    def get(self,request,*args,**kwargs):
        form=BMRForm()
        return render(request,'index.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=BMRForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            bmr = None
            bmi = None
            if gender == 'male':
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            else:
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            
            height_in_meters = height / 100  # convert cm to meters
            bmi = weight / (height_in_meters ** 2)

        return render(request, 'index.html', {'form': form, 'bmr': bmr,'bmi': bmi})
    
class Registration_View(View):
    def get(self,request,*args,**kwargs):
        form=Registration_Form()
        return render(request,'reg.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=Registration_Form(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            form=Registration_Form()
            return redirect('log')
        
class Update_UserProfile_View(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        data=UserProfile_Model.objects.get(id=id)
        form = UserProfile_Form(instance=data)
        return render(request, 'profile.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        data=UserProfile_Model.objects.get(id=id)
        form = UserProfile_Form(request.POST,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('cal')
        else:
            form = UserProfile_Form(instance=data)
            return render(request, 'profile.html', {'form': form})
        
class Login_View(View):
    def get(Self,request,*args,**kwargs):
        form=Login_Form()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=Login_Form(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')

            user_obj=authenticate(username=u_name,password=pswd)
            if user_obj:
                login(request,user_obj)
                return redirect('food')
            else:
                form=Login_Form()
                return render(request,'login.html',{'form':form})
            
class Logout_View(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')
    
class Food_Add_View(View):
    def get(self,request,*args,**kwargs):
        data=UserProfile_Model.objects.get(user_id=request.user)
        return render(request,'food.html',{'data':data})

