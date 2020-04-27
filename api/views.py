from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import requests, json

def home(request):
    return render (request, 'home.html')

def logout_form (request):
    logout(request)
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form}) 

def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})    

def retrieve_data(request):
    response = requests.get('https://geodata.tampere.fi/geoserver/maankaytto/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=maankaytto:WFS_KENTTA_MVIEW&outputFormat=json')
    jsondata = response.json()

    return render(request, 'api.html', {
        'jsondata': jsondata
    })
    
def visualization(request):
    response = requests.get('https://geodata.tampere.fi/geoserver/maankaytto/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=maankaytto:WFS_KENTTA_MVIEW&outputFormat=json')
    jsondata = response.json()
    

    summer = 0
    winter = 0
    summerwinter = 0

    grass = 0
    sand = 0
    turf = 0
    asphalt = 0
    not_known = 0

    for season in jsondata['features']:
        if season['properties']['KP_KAUSI'] == 'KESÄ':
            summer += 1
        elif season['properties']['KP_KAUSI'] == 'TALVI':
            winter += 1
        else:
            summerwinter += 1
        

    for surface in jsondata['features']:
        if surface['properties']['PINTAMATERIAALI'] == 'NURMI':
            grass += 1
        elif surface['properties']['PINTAMATERIAALI'] == 'HIEKKA':
            sand += 1
        elif surface['properties']['PINTAMATERIAALI'] == 'KEINONURMI':
            turf += 1
        elif surface['properties']['PINTAMATERIAALI'] == 'ASFALTTI':
            asphalt += 1
        else:
            not_known += 1

    context = {
        'jsondata':jsondata, 'grass':grass, 'sand':sand, 'turf':turf, 'asphalt':asphalt, 'not_known':not_known, 'summer': summer, 'winter': winter, 'summerwinter': summerwinter
    } 

    return render  (request, 'visualization.html', context)
            
