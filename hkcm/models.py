from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Cmdata(models.Model):
    issuetime = models.DateTimeField(null=True)
    location = models.CharField(max_length=50)
    crime = models.CharField(max_length=50)
    crimecat = models.CharField(max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    title = models.CharField(max_length=500)
    URL = models.CharField(max_length=5000)

    class Meta:
        unique_together = ('title', 'location', 'crime')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.issuetime >= timezone.now() - datetime.timedelta(days=3)


@python_2_unicode_compatible
class Crimemapinfo(models.Model):
    # id = models.AutoField()
    issuetime = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    crime = models.CharField(max_length=50, blank=True, null=True)
    crimecat = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    title = models.CharField(max_length=50)
    url = models.CharField(db_column='URL', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crimemapinfo'
        unique_together = (('id', 'title'), ('issuetime', 'location', 'crime'),)

    def __str__(self):
        return self.crime

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
