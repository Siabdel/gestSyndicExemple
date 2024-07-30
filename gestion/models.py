
from django.db import models

class Copropriete(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=300)
    nombre_lots = models.IntegerField()

class Coproprietaire(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)

class BudgetPrevisionnel(models.Model):
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    annee = models.IntegerField()
    montant_prevu = models.DecimalField(max_digits=10, decimal_places=2)
    montant_reel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class AppelFonds(models.Model):
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    date_appel = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_limite = models.DateField()

class AssembleeGenerale(models.Model):
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    date = models.DateField()
    ordre_du_jour = models.TextField()
    proces_verbal = models.TextField(null=True, blank=True)

class Travaux(models.Model):
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    cout = models.DecimalField(max_digits=10, decimal_places=2)

class Sinistre(models.Model):
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    description = models.TextField()
    date_sinistre = models.DateField()
    date_resolution = models.DateField(null=True, blank=True)
    cout = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class ContratMaintenance(models.Model):
    copropriete = models.ForeignKey(Copropriete, on_delete=models.CASCADE)
    fournisseur = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    cout_annuel = models.DecimalField(max_digits=10, decimal_places=2)