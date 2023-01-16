from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination

from .models import CandidateTechs, Candidates, Techs
from .serializers import TechSerializers, CandidateSerializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class TechViewSet(viewsets.ModelViewSet):
    queryset = Techs.objects.all().order_by('title')
    serializer_class = TechSerializers

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(pk=kwargs.get('pk'))
            lc = [{"name": Candidates.objects.get(id=candidate_techs.candidate_id).name, "years": candidate_techs.years,
                   "tech": instance.title} for candidate_techs in
                  CandidateTechs.objects.filter(tech=instance).all().order_by('-years')]
            return Response(lc, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"data": "El valor q intenta acceder no existe"}, status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "Error, try again " + str(e)}, status.HTTP_404_NOT_FOUND)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidates.objects.all().order_by('id')
    serializer_class = CandidateSerializers
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        try:
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
        except Exception as e:
            return Response({"data": "Error, try again " + str(e)}, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(pk=kwargs.get('pk'))
            name = self.queryset.get(pk=kwargs.get('pk')).name
            ct = CandidateTechs.objects.filter(candidate_id=instance).all()
            if ct.exists():
                ct.delete()
                return Response({"data": f"{name} se ha eliminado satisfactoriamente"}, status=200)
            else:
                Candidates.delete(instance)
                return Response({"data": f"{name} se ha eliminado satisfactoriamente"}, status=200)
        except ObjectDoesNotExist:
            return Response({"data": f"El candidato no existe en la base de datos"}, status=200)
        except Exception as e:
            return Response({"data": str(e)}, status=200)

    def retrieve(self, request, *args, **kwargs):
        try:
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
            } for candidate in self.queryset.filter(pk=kwargs.get('pk'))]
            return Response(lc, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"data": " El recurso no existe"}, status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "Error, try again " + str(e)}, status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        try:
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
        except Exception as e:
            return Response({"data": "Error, try again " + str(e)}, status.HTTP_404_NOT_FOUND)
