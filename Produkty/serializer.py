from .models import Produkty, Kategoria
from rest_framework import serializers

class ProduktySerializer(serializers.ModelSerializer):

    #url = serializers.HyperlinkedIdentityField(view_name="Produkty:user-detail")

    class Meta:
        model = Produkty
        fields = ['nazwa', 'producent', 'kategoria', 'opis', 'cena']

