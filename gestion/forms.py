
from django import forms
from .models import Copropriete, Coproprietaire, AssembléeGenerale, Travaux

class CoproprieteForm(forms.ModelForm):
    class Meta:
        model = Copropriete
        fields = ['nom', 'adresse', 'nombre_lots']

class CoproprietaireForm(forms.ModelForm):
    class Meta:
        model = Coproprietaire
        fields = ['nom', 'email', 'telephone', 'copropriete']

class AssembléeGeneraleForm(forms.ModelForm):
    class Meta:
        model = AssembléeGenerale
        fields = ['copropriete', 'date', 'ordre_du_jour', 'proces_verbal']

class TravauxForm(forms.ModelForm):
    class Meta:
        model = Travaux
        fields = ['copropriete', 'description', 'date_debut', 'date_fin', 'cout']