from django.shortcuts import render,HttpResponse,redirect
from .models import Hydb,UserDevices
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def AppLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            userdevice = UserDevices.objects.get(user=user)
            return HttpResponse(userdevice.device_id.device_id)
        else:
            return HttpResponse("can't login now please check username or password")

def home(request):
    return HttpResponse("Welcome")

def gettemp(request,pk):
    tempe = Hydb.objects.get(device_id=pk)
    return HttpResponse(str(tempe.temp))

def setTemp(request,pk,temp):
    tempe = Hydb.objects.get(device_id=pk)
    tempe.temp = float(temp)
    tempe.save()
    return redirect('gettemp',pk)

def getwtemp(request,pk):
    tempe = Hydb.objects.get(device_id=pk)
    return HttpResponse(str(tempe.temp_w))

def setwTemp(request,pk,temp_w):
    tempe = Hydb.objects.get(device_id=pk)
    tempe.temp_w = float(temp_w)
    tempe.save()
    return redirect('getwtemp',pk)

def gethumid(request,pk):
    tempe = Hydb.objects.get(device_id=pk)
    return HttpResponse(str(tempe.humid))

def sethumid(request,pk,humid):
    tempe = Hydb.objects.get(device_id=pk)
    tempe.humid= float(humid)
    tempe.save()
    return redirect('gethumid',pk)

def getwlevel(request,pk):
    tempe = Hydb.objects.get(device_id=pk)
    return HttpResponse(str(tempe.w_level))

def setwlevel(request,pk,w_level):
    tempe = Hydb.objects.get(device_id=pk)
    tempe.w_level = float(w_level)
    tempe.save()
    return redirect('getwlevel',pk)

def getpumpstat(request,pk):
    tempe = Hydb.objects.get(device_id=pk)
    if tempe.pump==0:
        return HttpResponse("Pump is off")
    else:
        return HttpResponse("Pump is On")

def Togglepump(request,pk):
    tempe = Hydb.objects.get(device_id=pk)
    if tempe.pump==0:
        tempe.pump=1
        tempe.save()
        return redirect('getpumpstat',pk)
    else:
        tempe.pump=0
        tempe.save()
        return redirect('getpumpstat',pk)



