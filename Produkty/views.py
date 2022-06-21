from django.shortcuts import render     #odpowiada za wyswietlanie html
import requests
from .models import Produkty, Kategoria, City
from .forms import CityForm
from rest_framework import viewsets
from .serializer import ProduktySerializer
from django.shortcuts import redirect           #przekierowania na inne strony
from django.contrib.auth.models import User     #czynnosci zwiazane z uzytkownikiem
from django.contrib.auth import authenticate
from django.contrib import auth                 #autoryzacja
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    cities = City.objects.all()

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9262cb1fde2e60a6a863e3b34790ebaf'
    #url = 'https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=9262cb1fde2e60a6a863e3b34790ebaf'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city': city,
            'temperature': round((city_weather['main']['temp']-32)/1.8, 1),
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'windspeed': city_weather['wind']['speed']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather.html', context)




class ProduktyViewSet(viewsets.ModelViewSet):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer


def signup_page(request):
    context = {}
    if request.method == 'POST':
        # Request for sign up
        # Check if user is available
        try:
            user = User.objects.get(username=request.POST['username'])
            context['error'] = 'Podana nazwa użytkownika już istnieje! Proszę podać inną nazwę użytkownika.'
            return render(request, 'signup.html', context)
        except User.DoesNotExist:
            # sprawdzenie poprawnosci podania 2 raz hasla
            if request.POST['password1'] != request.POST['password2']:
                context['error'] = 'Podane hasła nie są takie same! Proszę wprowadzić identyczne hasła.'
                return render(request, 'signup.html', context)
            else:
                # Create new user
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # Automatic login after signing up
                auth.login(request, user)
                # Go to home page
                return redirect('home')
    else:
        return render(request, 'signup.html', context)


def login_page(request):
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.POST.get('redir'):
                return redirect(f"{request.POST.get('redir')}")
            else:
                return redirect('home')
        else:
            context['error'] = 'Podane hasło lub login są błędne! Podaj poprawne dane.'
            if request.POST.get('redir'):
                context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
                context['nextURL'] = request.GET.get('next')
            return render(request, 'login.html', context)
    else:
        if request.GET.get('next'):
            context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
            context['nextURL'] = request.GET.get('next')
        return render(request, 'login.html', context)


def logout_page(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')



def indexx(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    if request.user.is_authenticated:
        # Do something for authenticated users.
        dane['userStatus'] = 'zalogowany'
    else:
        # Do something for anonymous users.
        dane['userStatus'] = 'niezalogowany'

    return render(request, 'szablon.html', dane)


def kategoria (request, id):        # /kategoria/1 to wyswietla o id=1
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)   #wszystkie produkty z wybranej kategorii
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user' : kategoria_user,
            'kategoria_produkt' : kategoria_produkt,
            'kategorie' : kategorie }
    return render(request, 'kategoria_produkt.html', dane)

def produkt (request, id):        # /produkt/1 to wyswietla o id=1
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user' : produkt_user,
            'kategorie' : kategorie}
    return render(request, 'produkt.html', dane)

    #wyszukiwarka
def search(request):
    q=request.GET['q']
    kategorie = Kategoria.objects.all()
    dane = Produkty.objects.filter(nazwa__icontains=q).exclude(nazwa__exact='').order_by('-id')
    print(dane)
    context = {
        'dane': dane,
        'kategorie':kategorie,
    }
    return render(request, 'search.html', context)

@login_required
def galeria (request):
    return render(request, 'galeria.html')

def szablon (request):
    return render(request, 'szablon.html')

def kontakt (request):
    return render(request, 'kontakt.html')