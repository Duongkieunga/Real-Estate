import urllib.request, json , csv, base64, requests, time, re, html
import pandas as pd 
from pandas.io.json import json_normalize
# 1327 145 367
# cg 1010 chung cu
# 12086: Ha Dong
# 12073: Hoan Kiem
# 12074: Ba dinh
# 12075: DOng da
# 12076 hai ba trung
# 12077 thanh xuan
# 12078 tay ho
# 12079 cau giay
# 12080 hoang mai
# 12081 long bien
# 12121 nam tu lien
# 12129 bac tu liem
# 12086, 12073, 12074, 12075, 12076, 12077, 12078, 12079, 
district = [12080, 12081,12121, 12129]

# print(set_id)
def chung_cu():
    set_id = set()
    with open("set_id_chotot.txt","r") as f:
        for line in f.readlines():
            set_id.add(line.split('\n')[0])
            
    for dis in district:
        # break

        # print('\n\n\n------------------------------------------------------------\n\n\n')

        for i in range(200):
            homepage = "https://gateway.chotot.com/v1/public/ad-listing"
            page = "https://gateway.chotot.com/v1/public/ad-listing?region_v2=12000&area_v2="+str(dis)+"&cg=1010&limit=20&o="+str(i*20)+"&st=s,k&page="+str(i+1)
            # print(page)
    # 75465883
            try:
                with urllib.request.urlopen(page) as url:
                    data = json.loads(url.read().decode())
            except:
                continue

            if len(data['ads']) == 0:
                break

            for j in range(len(data['ads'])):
                if str(data['ads'][j]['list_id']) in set_id:
                    # print('------')
                    continue

                # print(data['ads'][j]['list_id'])

                try:
                    with urllib.request.urlopen("https://gateway.chotot.com/v1/public/ad-listing/"+str(data['ads'][j]['list_id'])) as url1:
                        data1 = json.loads(url1.read().decode())
                except:
                    continue
                res = dict()
                for key1 in list(data1.keys())[:2]:
                    try:
                        for key2 in data1[key1].keys():
                            res[key2]= data1[key1][key2]
                    except:
                        for idx in range(len(data1[key1])):
                            res[data1[key1][idx]['id']]= data1[key1][idx]['value']
                # print(res.keys())
                # break
                try:
                    # res['Images']=[]
                    # for val in res['images']:
                    #     res['Images'].append(base64.b64encode(requests.get(val).content)+b'\n'+base64.b64encode(val.encode('utf-8')))
                    del res['images']
                except:
                    pass
                
                df = pd.DataFrame([res],columns=columns)
                try:
                    df1 = pd.read_csv("chototDS.csv")
                    df = pd.concat([df1, df], ignore_index=True, sort = False)
                except:
                    pass
                df.to_csv("chototDS.csv", index=False)
                set_id.add(str(data['ads'][j]['list_id']))
                with open("set_id_chotot.txt","a") as f_id:
                    f_id.write(str(data['ads'][j]['list_id'])+'\n')
                time.sleep(0.5)
        #     break
        # break
def Du_an():
    set_id = set()
    with open("set_id_chotot_du_an.txt","r") as f:
        for line in f.readlines():
            set_id.add(line.split('\n')[0])

    for dis in district:
        # break
        # print('\n\n\n------------------------------------------------------------\n\n\n')

        for i in range(200):
            homepage = "https://gateway.chotot.com/v1/public/xproperty/projects/"
            page = "https://gateway.chotot.com/v1/public/xproperty/projects/_search?offset="+str(i*20)+"&status=active&region_v2=12000&area_v2="+str(dis)+"&limit=20&st=s,k@page="+str(i+1)
            # print(page)
    # 75465883
            try:
                with urllib.request.urlopen(page) as url:
                    data = json.loads(url.read().decode())
            except:
                continue

            if len(data['projects']) == 0:
                break
            # print(len(data['projects']))
            # break
            for j in range(len(data['projects'])):
                if str(data['projects'][j]['id']) in set_id:
                    # print('------')
                    continue

                # print(data['projects'][j]['id'])

                try:
                    with urllib.request.urlopen(homepage+str(data['projects'][j]['id'])) as url1:
                        data1 = json.loads(url1.read().decode())
                except:
                    continue
                res = dict()
                for key1 in list(data1.keys()):
                    if (key1 == "ad_stats") or (key1 == "stats"):
                        continue
                    if 'introduction' in key1:
                        res[key1]= html.unescape(re.sub(re.compile('<.*?>'), '  ', data1[key1])).replace('\xa0',' ')
                        continue
                    if key1 == 'project_images':
                        res[key1]=[]
                        nImages = len(data1[key1])
                        if nImages >8:
                            nImages = 8
                        for idx in range(nImages):
                            res[key1].append(base64.b64encode(requests.get(data1[key1][idx]['url']).content)+b'\n'+base64.b64encode((data1[key1][idx]['url']).encode('utf-8')))
                        continue
                    if (key1 == 'facilities') or (key1 == 'surrounding'):
                        res[key1]=[]
                        for idx in range(len(data1[key1])):
                            try:
                                res[key1].append(data1[key1][idx]['name'])
                            except:
                                pass
                        continue
                    res[key1]= data1[key1]

                # continue
                # print(res)
                # break
            # break
                # print(res.keys())
                # break
                # try:
                    # res['Images']=[]
                    # for val in res['images']:
                    #     res['Images'].append(base64.b64encode(requests.get(val).content)+b'\n'+base64.b64encode(val.encode('utf-8')))
                    # del res['images']
                # except:
                    # pass

                columns = list(res.keys())
                df = pd.DataFrame([res],columns=columns)
                try:
                    df1 = pd.read_csv("chototDSProject.csv")
                    df = pd.concat([df1, df], ignore_index=True, sort = False)
                except:
                    pass
                df.to_csv("chototDSProject.csv", index=False)
                set_id.add(str(data['projects'][j]['id']))
                with open("set_id_chotot_du_an.txt","a") as f_id:
                    f_id.write(str(data['projects'][j]['id'])+'\n')
                time.sleep(0.5)
        #         break
            # break
        # break
Du_an()