from rest_framework import routers

from .viewsets import CandidateViewSet, TechViewSet

router = routers.SimpleRouter()

router.register('candidates', CandidateViewSet)
router.register('techs', TechViewSet)

urlpatterns = []
urlpatterns += router.urls
