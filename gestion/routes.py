from rest_framework.routers import DefaultRouter
from .api_views import CoproprieteViewSet, CoproprietaireViewSet, AssembléeGeneraleViewSet, TravauxViewSet

router = DefaultRouter()
router.register(r'coproprietes', CoproprieteViewSet)
router.register(r'coproprietaires', CoproprietaireViewSet)
router.register(r'assemblees', AssembléeGeneraleViewSet)
router.register(r'travaux', TravauxViewSet)