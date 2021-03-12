import os, bs4, html, json, codecs
from bs4 import BeautifulSoup

class Rongbay:
    path = "/home/nga/Documents/20193/Project/request/Datas/rongbay.com"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                filename = "127.html"
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()

        info['type'] = bs.find("span", {"class":"nameScate"}).text.strip()
        info['title'] = bs.find("h1",{"class":"title font_28"}).text.strip()
        element = bs.find("p",{'class':"note info_item_popup cl_888 font_13"})
        key = None
        for item in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != '') and (text.strip() != '-'), recursive=True):
            if key is None:
                info[item.strip()] = None
                key = item.strip()
            else:
                info[key] = item.strip()
                key = None
        # -----
        elements = bs.find("div",{'class':"box_infor_ct roboto_regular font_14 cl_333 seo1554192587"}).find_all("li")
        for items in elements:
            values = items.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            if len(values)==1:
                info[values[0].split(":")[0].strip()] = values[0].split(":")[1].strip()
            else:
                info[values[0].strip()] = " ".join([item.strip() for item in values[1:]])
        items = bs.find("p", {"class":"cl_666"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        info[items[0].strip()] = items[1].strip()
        # contact
        info['name(email)'] = bs.find("a", {"class":"name_store icon_bds"}).text.strip()
        info['phone'] = bs.find("p", {"class":"mobile_hide show_mobile roboto_regular"}).text.strip()
        element = bs.find("div", {"class":"info_text"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        info['description'] = "\n".join([item.strip() for item in element])
        print(info)        
        return
        return self.saveFile(filename, info)

bds = Rongbay()
