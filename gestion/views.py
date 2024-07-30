from django.shortcuts import render
from django.views.generic import ListView
from .models import Copropriete, Coproprietaire, AssembleeGenerale, Travaux

def home(request):
    return render(request, 'home_page.html')

class CoproprieteListView(ListView):
    model = Copropriete
    template_name = 'copropriete_list.html'

class CoproprietaireListView(ListView):
    model = Coproprietaire
    template_name = 'coproprietaire_list.html'

class AssembleeListView(ListView):
    model = AssembleeGenerale
    template_name = 'assemblee_list.html'

class TravauxListView(ListView):
    model = Travaux
    template_name = 'travaux_list.html'