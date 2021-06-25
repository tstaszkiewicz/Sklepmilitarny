from django.shortcuts import render     #odpowiada za wyswietlanie html
from .models import Produkty, Kategoria


# Create your views here.

def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
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

def galeria (request):
    return render(request, 'galeria.html')

def szablon (request):
    return render(request, 'szablon.html')

def kontakt (request):
    return render(request, 'kontakt.html')