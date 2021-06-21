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


def kategoria (request, id):        # /kategoria/1 to wyswietla o id=1
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)   #wszystkie produkty z wybranej kategorii
    # aktualna lista kategorii aby menu caly czas dzialalo
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user' : kategoria_user,
            'kategoria_produkt' : kategoria_produkt,
            'kategorie' : kategorie }
    return render(request, 'kategoria_produkt.html', dane)

def produkt (request, id):        # /produkt/1 to wyswietla o id=1
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user' : produkt_user, 'kategorie' : kategorie}
    return render(request, 'produkt.html', dane)