import os, bs4, html, re, json, codecs
from bs4 import BeautifulSoup

class Nhadat:
    path = "/home/nga/Documents/20193/Project/request/Datas/nhadat.net"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()
        # title
        info['title'] = bs.find("h1",{"class":"title_h1"}).text.strip()
        info['address'] = bs.find("div",{"class":"adrest"}).text.strip()
        area_price = bs.find("div",{"class":"area_price pull-right text-right"}).find("p").text.strip().split('/')
        info['area'], info['price'] = area_price[0].strip(), area_price[1].strip()
        info['price/area'] = bs.find("div",{"class":"area_price pull-right text-right"}).find_all("p")[1].text.strip().split(':')[1]
        info['phone'] = bs.find("input", {"id":"_post_user_phone"})['value']
        info['name'] = bs.find("input",{"id":"_post_user_name"})['value']
        info['email'] = bs.find("input",{"id":"_post_user_email"})['value']
        info['date'] = re.findall("\d{2}/\d{2}/\d{4}", str(bs))[1]
        elements = bs.find_all("div",{"class":"col-xs-6 clearfix"})
        for items in elements:
            item = items.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            try:
                info[item[0].strip()] = item[1].strip()
            except:
                info[item[0].strip()] = 1 # chinh chu

        info['description'] = "\n".join([item.strip() for item in bs.find("p", {"class":"text"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)])
        # tien ich, tien ich trong khu vuc
        try:
            element = bs.find("div",{"class":"row utility"})
            info['tien ich'] = ""
            for item in element.find_all("li",{"class":"active"}):
                info['tien ich'] += item.text.strip()
                 # print(item.text.strip())
        except:
            pass
        try:
            element = bs.find_all("div",{"class":"row utility"})[1]
            info['tien ich trong khu vuc'] = ""
            for item in element.find_all("li",{"class":"active"}):
                info['tien ich trong khu vuc'] += item.text.strip()
                # print(item.text.strip())
        except:
            pass
        # print(info)            
        return
        return self.saveFile(filename, info)

bds = Nhadat()
