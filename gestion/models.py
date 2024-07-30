
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Copropriete, Coproprietaire, AssembléeGenerale, Travaux
from .forms import CoproprieteForm, CoproprietaireForm, AssembléeGeneraleForm, TravauxForm

class CoproprieteListView(ListView):
    model = Copropriete
    template_name = 'copropriete_list.html'

class CoproprieteDetailView(DetailView):
    model = Copropriete
    template_name = 'copropriete_detail.html'

class CoproprieteCreateView(CreateView):
    model = Copropriete
    form_class = CoproprieteForm
    template_name = 'copropriete_form.html'

class CoproprietaireListView(ListView):
    model = Coproprietaire
    template_name = 'coproprietaire_list.html'

# Ajoutez d'autres vues similaires pour les autres modèles