from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import CandidateTechs, Candidates, Techs
from .serializers import TechSerializers, CandidateSerializers, TechCandidateSerializers


class TechViewSet(viewsets.ModelViewSet):
    queryset = Techs.objects.all().order_by('title')
    serializer_class = TechSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        lc = [{"name": Candidates.objects.get(id=candidate_techs.candidate_id).name, "years": candidate_techs.years,
               "tech": instance.title} for candidate_techs in
              CandidateTechs.objects.filter(tech=instance).all().order_by('-years')]

        return Response(lc, status=status.HTTP_200_OK)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidates.objects.all().order_by('id')
    serializer_class = CandidateSerializers

    def create(self, request, *args, **kwargs):
        cand_serilizer = CandidateSerializers(data=request.data)
        if cand_serilizer.is_valid():
            candidate = cand_serilizer.save()
            list_tech_data = request.data["techs"]
            if list_tech_data:
                for techs in list_tech_data:
                    tech = Techs.objects.get(title=techs['title'])
                    CandidateTechs.objects.create(
                        candidate=candidate,
                        tech=tech,
                        years=int(techs["years"])
                    )
        return Response({"data": "successfully created"}, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        lc = [{
            "id": candidate.id,
            "name": candidate.name,
            "lastname": candidate.lastname,
            "ci": candidate.ci,
            "address": candidate.address,
            "age": candidate.age,
            "gender": candidate.gender,
            "techs": [{"title": Techs.objects.get(id=candidate_techs.tech_id).title, "years": candidate_techs.years}
                      for candidate_techs in CandidateTechs.objects.filter(candidate=candidate).all()]
        } for candidate in self.queryset]

        return Response(lc, status=status.HTTP_200_OK)
