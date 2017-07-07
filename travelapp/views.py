from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.http import Http404
from travelapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from travelapp.forms import SignUpForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import BookingForm


# Create your views here.


def index(request):
      return HttpResponse("HELLO USER")
       
def state(request):
          tmp = State.objects.all()#get(id = 1)
         
          rendered = render(request,'travelapp/states.html',{'state':tmp})
          return HttpResponse(rendered)
          
def  city(request):
          tmp1 = City.objects.all()
          rendered = render(request,'travelapp/city.html',{'city':tmp1})
          return HttpResponse(rendered)
          
def placemap(request):
          tmp = PlaceMap.objects.all()#get(id = 1)
          rendered = render(request,'travelapp/placemap.html',{'placemap':tmp})
          return HttpResponse(rendered)
       
def disp_image(request):
          rendered = render(request,'travelapp/disp_image.html')
          return HttpResponse(rendered)
          
def homepage(request):
          rendered = render(request,'travelapp/homepage.html')
          return HttpResponse(rendered)
          
def placestoeat(request):
          rendered = render(request,'travelapp/placestoeat.html')
          return HttpResponse(rendered)
          
def attractions(request):
          rendered = render(request,'travelapp/attractions.html')
          return HttpResponse(rendered)
def shopping(request):
          rendered = render(request,'travelapp/shopping.html')
          return HttpResponse(rendered)                   


def homepage1(request):
          tmp = Packages.objects.all()#order_by('stateid').distinct('stateid')
          return render(request,'travelapp/homepage1.html',{'state':tmp})
          #return HttpResponse(rendered)
          
def home(request):
          tmp = Packages.objects.all()#order_by('stateid').distinct('stateid')
          return render(request,'travelapp/home.html',{'state':tmp})          
          
def bookingslist(request):
          tmp = Booking.objects.all()#order_by('stateid').distinct('stateid')
          return render(request,'travelapp/bookingslist.html',{'state':tmp})
          #return HttpResponse(rendered)

def booknow(request):
          tmp = Packages.objects.all()#order_by('stateid').distinct('stateid')
          return render(request,'travelapp/book_forms.html',{'state':tmp})

def  success(request):
          tmp = Packages.objects.all()#order_by('stateid').distinct('stateid')
          return render(request,'travelapp/booking_done.html',{'state':tmp})


def cancelbook(request):
          return render(request,'travelapp/cancelbook.html',{})
          #return HttpResponse(rendered)
          
                    
def viewareas(request, c_name):
          state = State.objects.filter(state = c_name)
          tmp = Packages.objects.filter(stateid = state)
          #amount = Amount.objects.filter(packageid = tmp)
          #context = {'state':tmp, 'amounts':amount}
          return render(request,'travelapp/viewareas.html', {'state':tmp})
          
          
"""def viewareas(request):
          if request.method == "POST":
              placename = request.POST
              print(placename)
          state = State.objects.filter(state = placename)
          tmp = Packages.objects.filter(stateid = state)
          #amount = Amount.objects.filter(packageid = tmp)
          #context = {'state':tmp, 'amounts':amount}
          return render(request,'travelapp/viewareas.html', {'state':tmp})"""
          
def description(request, d_name):
          area = Area.objects.filter(area = d_name)
          areaid = PlaceMap.objects.filter(areaid = area)
          tmp = Packages.objects.filter(mapid = areaid)
          #tmp = Packages.objects.all()
          #amount = Amount.objects.filter(packageid = tmp)
          #context = {'state':tmp, 'amounts':amount}
          return render(request,'travelapp/description.html', {'state':tmp})

def search(request):
    query = request.GET.get('q')
    """try:
        query = string(query)
    except ValueError:
        query = None
        results = None"""
    
    result = Packages.objects.get(id=1)
    return render_to_response('results.html', {"results": result,}, context_instance=RequestContex(request))
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('travelapp/homepage1')
    else:
        form = SignUpForm()
    return render(request, 'travelapp/signup.html', {'form': form})
    
def bookings(request):
    if request.method == 'POST':
       form = BookingForm(request.POST)

       if form.is_valid():
          form.save()
          travelling_date = form.cleaned_data.get('travelling_date')
          amount = form.cleaned_data.get('amount')
          return redirect('travelapp/success')
          
          print("success")

         # form1 = AmountForm(request.POST)
          #if form1.is_valid():
          #   form1.save()
          return redirect( 'travelapp/success.html')

         #return Httpresponse("registered")

    else:

        form = BookingForm()

    return render(request, 'travelapp/registration.html', {'form':form})
    
def registration(request):
        rendered = render(request,'travelapp/registration.html',{})
        return HttpResponse(rendered)
        
def success(request):
        rendered = render(request,'travelapp/success.html',{})
        return HttpResponse(rendered)
        
   
   
   
        
        


