# This Python file uses the following encoding: utf-8import jsonimport loggingfrom collections import OrderedDictfrom rest_framework.renderers import JSONRendererfrom rest_framework.response import Responsefrom rest_framework.views import APIViewfrom .models import Cmdatalog = logging.getLogger(__name__)log.debug("")FLOAT_DATA_FORMAT = '{:,.2f}'class FilterCrimeListJson(APIView):    renderer_classes = (JSONRenderer,)    @staticmethod    def get(request):        crimecat = int(request.GET.get('crimecat'))        if crimecat == 0:            filtered_crimes = Cmdata.objects.all()            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)        elif crimecat == 1:            crimecat = u"Robbery"            filtered_crimes = Cmdata.objects.filter(crimecat=crimecat)            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)        elif crimecat == 2:            crimecat = u"Violent Crime"            filtered_crimes = Cmdata.objects.filter(crimecat=crimecat)            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)        elif crimecat == 3:            crimecat = u"Burglary"            filtered_crimes = Cmdata.objects.filter(crimecat=crimecat)            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)        elif crimecat == 4:            crimecat = u"Wounding and Serious Assault"            filtered_crimes = Cmdata.objects.filter(crimecat=crimecat)            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)        elif crimecat == 5:            crimecat = u"Criminal Intimidation"            filtered_crimes = Cmdata.objects.filter(crimecat=crimecat)            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)        elif crimecat == 6:            crimecat = u"Rape"            filtered_crimes = Cmdata.objects.filter(crimecat=crimecat)            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)        elif crimecat == 7:            crimecat = u"Serious Drug Offenses"            filtered_crimes = Cmdata.objects.filter(crimecat=crimecat)            data_list = []            auto_id = 0            for entry in filtered_crimes:                log.debug(entry.crimecat)                it = entry.issuetime                it.strftime('%Y-%m-%d %H:%M')                it = str(it)[0:16]                data_list.append(                    {'id': auto_id,                     'issue_time': it,                     'location': entry.location,                     'crime': entry.crime,                     'crimecat': entry.crimecat,                     'latitude': entry.latitude,                     'longitude': entry.longitude,                     'title': entry.title,                     'URL': entry.URL}                )                auto_id += 1            length_of_records = auto_id            content = {'data_list': data_list, 'length_of_records': length_of_records}            return Response(content)