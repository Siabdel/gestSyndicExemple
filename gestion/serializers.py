
from rest_framework import serializers
from .models import Copropriete, Coproprietaire, AssembleeGenerale, Travaux

class CoproprieteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copropriete
        fields = '__all__'

class CoproprietaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coproprietaire
        fields = '__all__'

class AssembleeGeneraleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssembleeGenerale
        fields = '__all__'

class TravauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travaux
        fields = '__all__'