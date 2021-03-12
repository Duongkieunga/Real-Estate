import os, bs4, html, json, codecs
from bs4 import BeautifulSoup

class Dothi:
    path = "/home/nga/Documents/20193/Project/request/Datas/dothi.net"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                # filename = "1.html"
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # return

    def saveFile(self, filename, info):
        # with open('./Clean_datas/dothi.net/'+filename.split('.')[0]+'.txt','w') as f:
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()

        element = bs.find("div",{"class":"product-detail"})
        info['title'] = element.find("h1").text.strip()

        # address, type
        items = element.find("div",{"class":"pd-location"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        try:
            info['type'] = items[1].strip()
            info['address'] = items[2].strip()
        except:
            info['type'] = items[0].strip()
            info['address'] = items[1].strip()
        # price, area
        items = element.find("div",{"class":"pd-price"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        info[items[0].strip()] = items[1].strip()
        info[items[2].strip()] = items[3].strip().replace('\xa0',' ')
        # description
        info['description'] =""
        items = element.find("div",{"class":"pd-desc-content"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        for item in items:
            info['description']+= item.strip()+"\n"
        # dac diem bat dong san
        items = element.find("table",{"id":"tbl1"}).find_all("tr")
        for item in items:
            item = item.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            try:
                info[item[0].strip()] = item[1].strip()
                # print(item)
            except:
                info[item[0].strip()] =None

        # thong tin lien he
        items = element.find("table",{"id":"tbl2"}).find_all("tr")
        for item in items:
            item = item.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            try:
                info[item[0].strip()] = html.unescape(item[1].strip()[21:-9])
                # print(item)
            except:
                info[item[0].strip()] =None
        # print(info)
        return
        return self.saveFile(filename, info)

bds = Dothi()
s = "&#108;&#101;&#118;&#105;&#110;&#104;&#53;&#50;&#50;&#53;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;"
