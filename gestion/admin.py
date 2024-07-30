
from django.contrib import admin
from .models import Copropriete, Coproprietaire, BudgetPrevisionnel, AppelFonds, AssembleeGenerale, Travaux, Sinistre, ContratMaintenance

admin.site.register(Copropriete)
admin.site.register(Coproprietaire)
admin.site.register(BudgetPrevisionnel)
admin.site.register(AppelFonds)
admin.site.register(AssembleeGenerale)
admin.site.register(Travaux)
admin.site.register(Sinistre)
admin.site.register(ContratMaintenance)