from django.shortcuts import render     #odpowiada za wyswietlanie html
from django.http import HttpResponse
from .models import Produkty, Kategoria

# Create your views here.

def index(request):
    wszystkie = Produkty.objects.all()      #wybranie wszystkiego czyli jak select *
    jeden = Produkty.objects.get(pk=2)     #wybieranie jednego produktu przez get
    kateg = Produkty.objects.filter(kategoria=1)    #filtrowanie po kategorii o id 4
    kat_name = Kategoria.objects.get(id=2)
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)

    #context = { 'wszystkie' : wszystkie,
    #           'kategorie' : kategorie}
    #return render(request, 'szablon.html', context)

def kategoria (request, id):        # /kategoria/1 to wyswietla o id=1
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def produkt (request, id):        # /produkt/1 to wyswietla o id=1
    produkt_user = Produkty.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user) + "</h1>" + \
            "<p>" + str(produkt_user.opis) + "</p>" + \
            "<p>" + str(produkt_user.cena) + "</p."
    return HttpResponse(napis)