
from rest_framework import viewsets
from .models import Copropriete, Coproprietaire, AssembleeGenerale, Travaux
from .serializers import CoproprieteSerializer, CoproprietaireSerializer, AssembleeGeneraleSerializer, TravauxSerializer

class CoproprieteViewSet(viewsets.ModelViewSet):
    queryset = Copropriete.objects.all()
    serializer_class = CoproprieteSerializer

class CoproprietaireViewSet(viewsets.ModelViewSet):
    queryset = Coproprietaire.objects.all()
    serializer_class = CoproprietaireSerializer

class AssembleeGeneraleViewSet(viewsets.ModelViewSet):
    queryset = AssembleeGenerale.objects.all()
    serializer_class = AssembleeGeneraleSerializer

class TravauxViewSet(viewsets.ModelViewSet):
    queryset = Travaux.objects.all()
    serializer_class = TravauxSerializer