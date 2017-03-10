# This Python file uses the following encoding: utf-8# !/usr/bin/env python""" title: data extractor for crime map """import osimport djangoos.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj_hkcm.settings")django.setup()import urllibimport loggingfrom django.utils import timezoneimport geocoderfrom bs4 import BeautifulSoupimport pytzfrom hkcm.models import Cmdatafrom datetime import datetimeimport requestsimport emailinglog = logging.getLogger(__name__)# print ("--")if __name__ == "__main__":    start = timezone.localtime(timezone.now())    print("=============================")    print('$>>>>> start at:    %s' % start)    print("$----> Crawler starting... #####")    with open('/home/ubuntu/proj_hkcm/txt_csv_files/Lib1_ListOfCrime.txt', 'r+') as fc:        crimelines = [line[:-1] for line in fc]  # for escaping the newline next to the location string    with open('/home/ubuntu/proj_hkcm/txt_csv_files/Lib2_ListOfLocation.txt', 'r+') as fl:        localines = [line[:-1] for line in fl]  # for escaping the newline next to the location string    # req = Request('https://www.hk01.com/section/%E6%B8%AF%E8%81%9E',    #               headers={'User-Agent': 'Mozilla/5.0'})    # page = urlopen(req).read()    url_list = [        'https://www.hk01.com/section/%E6%B8%AF%E8%81%9E',        'https://www.hk01.com/tag/9565',  # 走私        'https://www.hk01.com/tag/4199',  # 淋紅油，刑毀        'https://www.hk01.com/tag/343',  # 強姦        'https://www.hk01.com/tag/352',  # 爆竊        'https://www.hk01.com/tag/342',  # 非禮        'https://www.hk01.com/tag/5692',  # 搶劫        'https://www.hk01.com/tag/11098',  # drug        'https://www.hk01.com/tag/5379',  # deception        'https://www.hk01.com/tag/1748',  # 偷拍        'https://www.hk01.com/tag/6293',  # 恐吓        'https://www.hk01.com/tag/3233',  # 持刀伤人        'https://www.hk01.com/tag/3233#i=0p=2',    ]    for url in url_list:        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content        soup = BeautifulSoup(page, 'lxml')        collection = soup.find_all("div", class_="blog_listing__item")        total_number_of_news = 0        length_of_collection = len(collection)        total_number_of_news += length_of_collection        print("         #1. Number of news found: " + str(total_number_of_news))        # orig_stdout = sys.stdout        # f1 = open('/home/ubuntu/proj_hkcm/txt_csv_files/TitleUrlPairs.txt', 'w')        # sys.stdout = f1        counter = 0        for member in collection:            issue_time = "not defined yet"            data_rec = ()            counter += 1            print(counter)            title = member.find("h3")            title = title.string            title = title.encode('utf8')            print("title: " + title)            ref = member.find('a').get('href')            # for reading url containing Traditional Chinese words            refpart2 = ref[21:]            s = refpart2            # print("???????")            # print(type(s))            # print(s)            s = s.encode('utf8')            # print(type(s))            # print(s)            s = urllib.quote(s)            url = 'https://www.hk01.com/%s' % s            # print(url)            # req2 = urllib2.Request(url)            page2 = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content            # req2.add_header('User-Agent', 'Mozilla/5.0')            # page2 = urllib2.urlopen(req2).read()            soup2 = BeautifulSoup(page2, 'lxml')            for crime in crimelines:                if crime not in title:                    continue                else:  # crime in the title                    if "爆竊" == crime or "肇禍" == crime:                        crimecat = "burglary"                    elif "紅油" == crime or "爆水管" == crime or "攻擊" == crime or "持械攻擊" == crime \                            or "持械大混戰" == crime or "刑毀" == crime or "射爆" == crime or "狙擊" == crime:                        crimecat = "violent crime"                    elif "兇殺" == crime or "謀殺" == crime or "殺人" == crime or "猝死" == crime or "亡" == crime:                        crimecat = "homicide"                    elif "搶劫" == crime or "搶掠" == crime or "行搶" == crime \                            or "劫" == crime or "劫案" == crime or "搶" == crime:                        crimecat = "robbery"                    elif "互砍" == crime \                            or "斬傷" == crime \                            or "刀傷" == crime \                            or "斬" == crime \                            or "伏擊" == crime \                            or "剪狂插" == crime \                            or "捱斬" == crime \                            or "斬人" == crime \                            or "打人" == crime \                            or "逞兇" == crime \                            or "卡位戰" == crime \                            or "持刀追斬" == crime \                            or "襲警" == crime \                            or "偷拍" == crime \                            or "傷人" == crime \                            or "家暴" == crime or "家庭暴力" == crime or "酒後駕車" == crime \                            or "酒駕" == crime or "毆打" == crime or "騷亂" == crime \                            or "暴力" == crime or "縱火" == crime:                        crimecat = "wounding and serious assault"                    elif "走私" == crime or "緝毒" == crime or "毒駕" == crime or "毒品" == crime or "毒品買賣" == crime \                            or "買賣毒品" == crime or "毒品走私" == crime or "走私毒品" == crime or "吸食毒品" == crime \                            or '冰毒' == crime or '藏毒' == crime or '戒毒' == crime or '運毒' == crime or '毒' == crime:                        crimecat = "serious drug offenses"                    elif "恐嚇" == crime:                        crimecat = "criminal intimidation"                    elif "鹹豬手" == crime or "姦" == crime or "強暴" == crime or "賣淫" == crime or "性交易" == crime \                            or "強姦" == crime or "非禮" == crime or "騷擾" == crime or "性暴力" == crime:                        crimecat = "rape"                    elif "偷竊" == crime or "盜竊" == crime or "闖空門" == crime:                        crimecat = "all thefts"                    elif "扒竊" == crime or "打荷包" == crime:                        crimecat = "pickpocketing"                    elif "失車" == crime or "劫車" == crime:                        crimecat = "motor vehicles reported missing"                    elif '騙' == crime or '訛' == crime or '偷渡' == crime or "勒索" == crime or "詐騙" == crime or "行騙" == crime \                            or "物業騙案" == crime or "圍標案" == crime or "侵權" == crime:                        crimecat = "deception"                    # else:                    #     crimecat = "others"                    if 3 == 2:                        # tod---->  loop the titles in DB,                        # compare to the current title,                        # if duplicated, "continue";else go go go.                        continue                        # pass                    else:                        counter_x = 0                        flag_x = False                        for location in localines:                            counter_x += 1                            # print(counter_x)                            if location not in title:                                contents = []                                content1 = member.find(class_="blog_listing__item__content__caption")                                content2 = soup2.find(class_='article_summary_pt')                                # print("hoho-----=========````````````2341234123421312341234123412341234123412341234")                                # print(content2)                                content3 = soup2.find_all(class_='article_content__module')                                for x in content3:                                    # print("===================")                                    # print("===================")                                    # print(x)                                    # print("")                                    contents.append(x)                                # for x in content4:                                    # print("===================")                                    # print("===================")                                    # print(x)                                    # print("")                                    # contents.append(x)                                contents.append(content1)                                contents.append(content2)                                # print("length======>")                                # print(len(contents))                                for content in contents:                                    content = str(content)                                    # print("===================")                                    # print(content)                                    # print("")                                    if location not in content:                                        continue                                    else:                                        g = geocoder.google(location)                                        # print(g)                                        try:                                            lat = g.latlng[0]                                            lng = g.latlng[1]                                        except IndexError:                                            break                                        time_twins = soup2.find_all("div", class_="date")                                        for tag in time_twins:                                            issue_time = tag.text.strip()[34:]                                            break                                        try:                                            issue_time = datetime.strptime(issue_time, '%Y-%m-%d %H:%M')                                            issue_time = pytz.utc.localize(issue_time)                                        except ValueError:                                            issue_time = timezone.localtime(timezone.now())                                            issue_time = datetime.strftime(issue_time, '%Y-%m-%d %H:%M')                                            issue_time = datetime.strptime(issue_time, '%Y-%m-%d %H:%M')                                            issue_time = pytz.utc.localize(issue_time)                                        record = Cmdata(issuetime=issue_time,                                                        location=location,                                                        crime=crime,                                                        crimecat=crimecat,                                                        latitude=lat,                                                        longitude=lng,                                                        title=title,                                                        URL=url)                                        try:                                            record.save()                                            flag_x = True                                        except:                                            pass                                        break                                if flag_x:                                    break                                else:                                    continue                            else:  # location in title                                g = geocoder.google(location)                                # print (g)                                lat = g.latlng[0]                                lng = g.latlng[1]                                time_twins = soup2.find_all("div", class_="date")                                for tag in time_twins:                                    issue_time = tag.text.strip()[18:35]                                    # print("=============================")                                    # print(tag)                                    # print(issue_time)                                    break                                # print("========$$$$$$$$$")                                # print(issue_time)                                issue_time = datetime.strptime(issue_time, '%Y-%m-%d %H:%M')                                issue_time = pytz.utc.localize(issue_time)                                record = Cmdata(issuetime=issue_time,                                                location=location,                                                crime=crime,                                                crimecat=crimecat,                                                latitude=lat,                                                longitude=lng,                                                title=title,                                                URL=url)                                try:                                    record.save()                                    flag_x = True                                except:                                    pass                            break                if flag_x:                    break                else:                    continue        end = timezone.localtime(timezone.now())        print("     #2. Time lapsed: " + str(end - start))        print("")        print("$----> data extractor ending... #####")        print('$>>>>> Ending time:  %s' % end)    end = timezone.localtime(timezone.now())    my_emailing = emailing.GeneralEmail()    my_emailing.email_for_time_report(str(end - start))