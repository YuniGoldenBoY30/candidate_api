from rest_framework import serializers

from .models import Techs, Candidates, CandidateTechs


class CandidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = '__all__'


class TechSerializers(serializers.ModelSerializer):
    class Meta:
        model = Techs
        fields = '__all__'


class TechCandidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = CandidateTechs
        fields = '__all__'

