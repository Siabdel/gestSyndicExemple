
from django import forms
from .models import Copropriete, Coproprietaire, AssembleeGenerale, Travaux

class CoproprieteForm(forms.ModelForm):
    class Meta:
        model = Copropriete
        fields = ['nom', 'adresse', 'nombre_lots']

class CoproprietaireForm(forms.ModelForm):
    class Meta:
        model = Coproprietaire
        fields = ['nom', 'email', 'telephone', 'copropriete']

class AssembleeGeneraleForm(forms.ModelForm):
    class Meta:
        model = AssembleeGenerale
        fields = ['copropriete', 'date', 'ordre_du_jour', 'proces_verbal']

class TravauxForm(forms.ModelForm):
    class Meta:
        model = Travaux
        fields = ['copropriete', 'description', 'date_debut', 'date_fin', 'cout']