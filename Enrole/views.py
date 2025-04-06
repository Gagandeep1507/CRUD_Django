from django.shortcuts import render , redirect
from .models import User
from .forms import Userform

# Create your views here.


def Home(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            register = User(Name=name, Email=email)
            register.save()
            form = Userform()    
    else:
        form = Userform()
    student = User.objects.all()
    return render(request, 'home.html', {'form': form , 'student': student})

# Delete function
def Delete(request, id):
    if request.method == "POST":
        usr = User.objects.get(pk=id)
        usr.delete()
        return redirect('Home')


# update function
def Update(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        form = Userform(request.POST,instance= data)
        if form.is_valid():
            form.save()
    else:
        data = User.objects.get(pk=id)
        form = Userform(request.POST,instance= data)
    return render(request, 'update.html' , {'form': form})
