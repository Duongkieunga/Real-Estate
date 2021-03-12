import os, bs4, html, json, codecs
from bs4 import BeautifulSoup

class Muaban:
    path = "/home/nga/Documents/20193/Project/request/Datas/muaban.net"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()

        # title
        info['title'] = bs.find("h1", {"class":"title"}).text.strip()
        # price
        try:
            info['price'] = bs.find("div", {"class":"price-container__value"}).text.strip()
        except:
            pass

        # Dia diem, Ngay dang
        info['address'] = bs.find("span", {"class":"location-clock__location"}).text.strip()
        info['startDate'] = bs.find("span", {"class":"location-clock__clock"}).text.strip()
        info['name'] = bs.find("div", {"class":"user-info__fullname"}).text.strip()
        info['phone'] = bs.find("div", {"class":"mobile-container__value"}).find("span")['mobile']
        # description
        info['description'] = ""
        element = bs.find("div",{"class":"body-container"})
        for chil in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True):
            info['description'] += chil.strip()+"\n"
        # dia chi, dien tich, phap ly,..
        items = bs.find("div",{"class":"tect-content-block"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        key = None
        for item in items:
            if key is None:
                key = item.strip()
                info[key] = None
            else:
                info[key] = item.strip()
                key = None
        return self.saveFile(filename, info)

bds = Muaban()
