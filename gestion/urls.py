
from django.urls import path, include
from .routes import router
from gestion import views


urlpatterns = [
    path('', views.home, name='home'),
    path('coproprietes/', views.CoproprieteListView.as_view(), name='copropriete_list'),
    path('coproprietaires/', views.CoproprietaireListView.as_view(), name='coproprietaire_list'),
    path('assemblees/', views.AssembleeListView.as_view(), name='assemblee_list'),
    path('travaux/', views.TravauxListView.as_view(), name='travaux_list'),
    ## routes
    path('api/', include(router.urls)),
]