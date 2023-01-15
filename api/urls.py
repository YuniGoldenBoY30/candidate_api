from django.urls import path

from rest_framework import routers

from .viewsets import CandidateViewSet, TechViewSet
from .views import ExportPDF

router = routers.SimpleRouter()

router.register('candidates', CandidateViewSet)
router.register('techs', TechViewSet)

urlpatterns = [
    path('report/<slug:export>/', ExportPDF.as_view(), name="export"),
    # path('report/<slug:export>/<int:pk>/', ExportPDF.as_view(), name="export"),
]
urlpatterns += router.urls
