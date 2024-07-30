
from rest_framework import serializers
from .models import Copropriete, Coproprietaire, AssembléeGenerale, Travaux

class CoproprieteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copropriete
        fields = '__all__'

class CoproprietaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coproprietaire
        fields = '__all__'

class AssembléeGeneraleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssembléeGenerale
        fields = '__all__'

class TravauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travaux
        fields = '__all__'