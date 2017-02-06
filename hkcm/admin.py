from django.contrib import admin

from .models import Cmdata, DistrictsForAllLocationsinLocaList, DistrictsClassification, HongKongEighteenDistricts

admin.site.register(Cmdata)
admin.site.register(DistrictsForAllLocationsinLocaList)
admin.site.register(DistrictsClassification)
admin.site.register(HongKongEighteenDistricts)
