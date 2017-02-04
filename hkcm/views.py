# This Python file uses the following encoding: utf-8
from django.http import HttpResponse
from django.shortcuts import render

from .models import Cmdata

import logging
log = logging.getLogger(__name__)
log.debug("")


def index(request):
    return HttpResponse("Hello, world. You're at the hong kong crime map index.")


def map_page(request):
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []

    latitude = Cmdata.objects.values_list('latitude')
    for x in latitude:
        x = x[0]
        a1.append(x)
    log.debug(type(a1[1]))

    longitude = Cmdata.objects.values_list('longitude')
    for x in longitude:
        x = x[0]
        a2.append(x)

    issue_time = Cmdata.objects.values_list('issuetime')
    for x in issue_time:
        x = x[0]
        x.strftime('%Y-%m-%d %H:%M')
        # print x
        a3.append(x)

    valid_a4 = []
    crime = Cmdata.objects.values_list('crime')
    for x in crime:
        x = x[0]
        a4.append(x)
    length_of_a4 = len(a4)
    for i in range(length_of_a4):
        x = a4[i].encode('utf-8')
        valid_a4.append(x)
    a4 = valid_a4
    log.debug(type(a4))

    log.debug(a4[3])
    log.debug(type(a4[3]))
    z = a4[3]
    # z = '"' + z + '"'
    # x = "你好"
    # log.debug(type(x))

    location = Cmdata.objects.values_list('location')
    for x in location:
        x = x[0]
        a5.append(x)

    title = Cmdata.objects.values_list('title')
    for x in title:
        x = x[0]
        a6.append(x)

    url = Cmdata.objects.values_list('URL')
    for x in url:
        x = x[0]
        a7.append(x)
    log.debug(a7[3])
    log.debug(type(a7[3]))

    length_of_a1 = len(a1)

    content = {
        'a1': a1,
        'a2': a2,
        'a3': a3,
        'a4': a4,
        'a5': a5,
        'a6': a6,
        'a7': a7,
        'length_a1': length_of_a1,
        'z': z,
        # 'length_a2': length_of_a2,
        # 'length_a3':length_of_a3,
        # 'length_a4': length_of_a4,
        # 'length_a3': length_of_a3,

    }

    return render(request, 'index.html', content)
