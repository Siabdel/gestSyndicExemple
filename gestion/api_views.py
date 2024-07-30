
from rest_framework import viewsets
from .models import Copropriete, Coproprietaire, AssembléeGenerale, Travaux
from .serializers import CoproprieteSerializer, CoproprietaireSerializer, AssembléeGeneraleSerializer, TravauxSerializer

class CoproprieteViewSet(viewsets.ModelViewSet):
    queryset = Copropriete.objects.all()
    serializer_class = CoproprieteSerializer

class CoproprietaireViewSet(viewsets.ModelViewSet):
    queryset = Coproprietaire.objects.all()
    serializer_class = CoproprietaireSerializer

class AssembléeGeneraleViewSet(viewsets.ModelViewSet):
    queryset = AssembléeGenerale.objects.all()
    serializer_class = AssembléeGeneraleSerializer

class TravauxViewSet(viewsets.ModelViewSet):
    queryset = Travaux.objects.all()
    serializer_class = TravauxSerializer