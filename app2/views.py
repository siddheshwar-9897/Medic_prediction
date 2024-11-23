from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.forms import RegisterForm





def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def form(request):
    return render(request,'form.html')


def result(request):
    if request.method=='POST':
        glucose=request.POST['glucose']
        blood_pressure=request.POST['bloodpressure']
        skin_thickness=request.POST['skinthickness']
        insulin=request.POST['insulin']
        bmi=request.POST['bmi']
        dpf=request.POST['diabetespedigreefunction']
        age=request.POST['age']

        lis=[glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]
        print(lis)

        #training mode
        from joblib import load
        model=load('C:\\Users\\91932\\OneDrive\\Desktop\\d jango\\secondproject\\model.joblinb')


        #make prediction
        result=model.predict([lis])
        print(result)

        if result[0]==0:
            print('no')
            value='Negative'

        else:
            print("yes")
            value='Postive'

    return render(request,'result.html',{
        'ans':value,
        'title':'predict'

    })
        
            




def register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login_view')
    else:
         form= RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('form/')
    else:
        form =AuthenticationForm()
    return render(request,'login.html',{'form':form})  

def logout1(request):
    logout(request)
    messages.success(request,"logged out sucessfully")
    return redirect('/')  





# def About(request):
#     return HttpResponse("welcome")

# Create your views here.
