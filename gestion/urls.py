
from django.urls import path, include
from .views import CoproprieteListView, CoproprieteDetailView, CoproprieteCreateView, CoproprietaireListView
from .routes import router

urlpatterns = [
    path('coproprietes/', CoproprieteListView.as_view(), name='copropriete_list'),
    path('coproprietes/<int:pk>/', CoproprieteDetailView.as_view(), name='copropriete_detail'),
    path('coproprietes/new/', CoproprieteCreateView.as_view(), name='copropriete_create'),
    path('coproprietaires/', CoproprietaireListView.as_view(), name='coproprietaire_list'),
    path('api/', include(router.urls)),
]