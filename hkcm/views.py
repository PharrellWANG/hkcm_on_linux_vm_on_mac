# This Python file uses the following encoding: utf-8
import json
import logging
from collections import OrderedDict

from django.shortcuts import render

from .models import Cmdata

log = logging.getLogger(__name__)
log.debug("")


def map_page(request):
    outer_dic = OrderedDict()
    all_records = Cmdata.objects.all()
    auto_id = 0
    for entry in all_records:
        # log.debug("====")
        # log.debug(auto_id)
        # log.debug(entry)

        inner_dic = OrderedDict()

        it = entry.issuetime
        it.strftime('%Y-%m-%d %H:%M')
        it = str(it)[0:16]
        inner_dic["id"] = auto_id
        inner_dic["issue_time"] = it
        inner_dic["location"] = entry.location
        inner_dic["crime"] = entry.crime
        inner_dic["crimecat"] = entry.crimecat
        inner_dic["latitude"] = entry.latitude
        inner_dic["longitude"] = entry.longitude
        inner_dic["title"] = entry.title
        inner_dic["URL"] = entry.URL
        outer_dic[auto_id] = inner_dic
        auto_id += 1
    length_of_records = auto_id
    log.debug(auto_id)
    outer_dic = json.dumps(outer_dic)

    crimecat_selector = [{'name': "總體罪案(All)", 'value': 0},
                         {'name': "劫案(Robbery)", 'value': 1},
                         {'name': "暴力罪案(Violent Crime)", 'value': 2},
                         {'name': "爆竊案(Burglary)", 'value': 3},
                         {'name': "傷人及嚴重毆打(Wounding and Serious Assault)", 'value': 4},
                         {'name': "刑事恐嚇(Criminal Intimidation)", 'value': 5},
                         {'name': "強姦及非禮(Rape)", 'value': 6},
                         {'name': "嚴重毒品罪行(Serious Drug Offenses)", 'value': 7}]

    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})
    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})
    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})
    # crimecat_selector.append({'name': "總體罪案", 'value': "All"})

    content = {
        'outer_dic': outer_dic,
        'le': length_of_records,
        'crimecat_selector': crimecat_selector,
    }

    return render(request, 'index.html', content)


def charts(request):
    list_of_crimes = Cmdata.objects.all()
    total_crimes = list_of_crimes.count()
    caw = 0
    eastern = 0
    kowloon_city = 0
    kwai_tsing = 0
    kt = 0
    north = 0
    sk = 0
    st = 0
    ssp = 0
    southern = 0
    tp = 0
    tw = 0
    tm = 0
    wc = 0
    wts = 0
    ytm = 0
    yl = 0
    island = 0

    for x in list_of_crimes:
        if str(x.district) == 'Central & Western':
            caw += 1
        elif str(x.district) == 'Eastern':
            eastern += 1
        elif str(x.district) == 'Kowloon City':
            kowloon_city += 1
        elif str(x.district) == 'Kwai Tsing':
            kwai_tsing += 1
        elif str(x.district) == 'Kwun Tong':
            kt += 1
        elif str(x.district) == 'North':
            north += 1
        elif str(x.district) == 'Sai Kung':
            sk += 1
        elif str(x.district) == 'Sha Tin':
            st += 1
        elif str(x.district) == 'Sham Shui Po':
            ssp += 1
        elif str(x.district) == 'Southern':
            southern += 1
        elif str(x.district) == 'Tai Po':
            tp += 1
        elif str(x.district) == 'Tsuen Wan':
            tw += 1
        elif str(x.district) == 'Tuen Mun':
            tm += 1
        elif str(x.district) == 'Wan Chai':
            wc += 1
        elif str(x.district) == 'Wong Tai Sin':
            wts += 1
        elif str(x.district) == 'Yau Tsim Mong':
            ytm += 1
        elif str(x.district) == 'Yuen Long':
            yl += 1
        elif str(x.district) == 'Island':
            island += 1

    list_for_finding_maximum_crime_region = [caw, eastern, kwai_tsing, kowloon_city, kt, sk, north, ssp, tp, tw, tm, wc,
                                             wts, ytm, yl, island, st, southern]
    maximum_crime_number = max(list_for_finding_maximum_crime_region)
    location_name_of_maximum_crime = "Yau Tsim Mong"
    if maximum_crime_number == ytm:
        location_name_of_maximum_crime = "Yau Tsim Mong"
    elif maximum_crime_number == caw:
        location_name_of_maximum_crime = "Central & Western"
    elif maximum_crime_number == eastern:
        location_name_of_maximum_crime = "Eastern"
    elif maximum_crime_number == kwai_tsing:
        location_name_of_maximum_crime = "Kwai Tsing"
    elif maximum_crime_number == kowloon_city:
        location_name_of_maximum_crime = "Kowloon City"
    elif maximum_crime_number == kt:
        location_name_of_maximum_crime = "Kwun Tong"
    elif maximum_crime_number == sk:
        location_name_of_maximum_crime = "Sai Kung"
    elif maximum_crime_number == north:
        location_name_of_maximum_crime = "North"
    elif maximum_crime_number == ssp:
        location_name_of_maximum_crime = "Sham Shui Po"
    elif maximum_crime_number == tp:
        location_name_of_maximum_crime = "Tai Po"
    elif maximum_crime_number == tw:
        location_name_of_maximum_crime = "Tsuen Wan"
    elif maximum_crime_number == tm:
        location_name_of_maximum_crime = "Tuen Mun"
    elif maximum_crime_number == wc:
        location_name_of_maximum_crime = "Wan Chai"
    elif maximum_crime_number == wts:
        location_name_of_maximum_crime = "Wong Tai Sin"
    elif maximum_crime_number == island:
        location_name_of_maximum_crime = "Island"
    elif maximum_crime_number == yl:
        location_name_of_maximum_crime = "Yuen Long"
    elif maximum_crime_number == st:
        location_name_of_maximum_crime = "Sha Tin"
    elif maximum_crime_number == southern:
        location_name_of_maximum_crime = "Southern"

    loc = location_name_of_maximum_crime
    log.debug(maximum_crime_number)
    log.debug(total_crimes)
    max_rate = round(float(maximum_crime_number)/total_crimes, 3)
    log.debug(max_rate)
    log.debug(type(max_rate))
    content = {
        'max_rate': max_rate,
        'loc': loc,
        'maximum_crime_number': maximum_crime_number,
        'total_crimes': total_crimes,
        'caw': caw,
        'eastern': eastern,
        'kowloon_city': kowloon_city,
        'kwai_tsing': kwai_tsing,
        'kt': kt,
        'north': north,
        'sk': sk,
        'st': st,
        'ssp': ssp,
        'southern': southern,
        'tp': tp,
        'tw': tw,
        'tm': tm,
        'wc': wc,
        'wts': wts,
        'ytm': ytm,
        'yl': yl,
        'island': island
    }

    return render(request, 'charts.html', content)
