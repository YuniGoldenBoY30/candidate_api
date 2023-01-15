# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid

from django.db import models


class CandidateTechs(models.Model):
    candidate = models.OneToOneField('Candidates', models.DO_NOTHING, primary_key=True)
    tech = models.ForeignKey('Techs', models.DO_NOTHING)
    years = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'candidate_techs'
        unique_together = (('candidate', 'tech'),)


class Candidates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    ci = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'candidates'


class Techs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'techs'
