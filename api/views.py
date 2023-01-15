from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from api.models import Techs, CandidateTechs, Candidates
from .export import Export


class ExportPDF(APIView):
    def get(self, request):
        queryset = Techs.objects.all().order_by('title')
        instance = queryset.get(pk=request.data["pk"])

        lc = [{"name": Candidates.objects.get(id=candidate_techs.candidate_id).name, "years": candidate_techs.years,
               "tech": instance.title} for candidate_techs in
              CandidateTechs.objects.filter(tech=instance).all().order_by('-years')]

        return Export.export_pdf(lc)
