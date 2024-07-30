from rest_framework.routers import DefaultRouter
from .api_views import CoproprieteViewSet, CoproprietaireViewSet, AssembleeGeneraleViewSet, TravauxViewSet

router = DefaultRouter()
router.register(r'coproprietes', CoproprieteViewSet)
router.register(r'coproprietaires', CoproprietaireViewSet)
router.register(r'assemblees', AssembleeGeneraleViewSet)
router.register(r'travaux', TravauxViewSet)