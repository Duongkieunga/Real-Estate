import os, bs4, html, re, json, codecs
from bs4 import BeautifulSoup

class Muabannhadat:
    path = "/home/nga/Documents/20193/Project/request/Datas/muabannhadat.vn"
    # path = ""
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                self.extract(BeautifulSoup(open(self.path+'./'+filename,'r').read(),'html.parser'), filename) # 
                return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()

        # mua bán, nhà phố
        info['type'] = bs.find("nav",{"class":"mb-4 text-grey-darker"}).find_all("li")[1].text.strip()
        info['title'] = bs.find("h1",{"class":"text-lg md:text-2xl inline"}).text.strip()
        info['address'] = bs.find("h4",{"class":"text-sm mb-4 text-grey-darker font-thin"}).text.strip()

        elements = bs.find("div",{"class":"flex flex-wrap justify-between md:justify-start w-full md:w-auto mb-4 overflow-hidden"})
        for element in elements.findChildren(recursive=False):
            value = ""
            items = element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            for item in items:
                value += item.strip()+" "
            info[element['aria-label']] = value
        
        items = bs.find("div",{"class":"flex items-center"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        try:
            info['price'] = items[0].strip()
        except:
            pass
        try:
            info['price/area'] = ' '.join([item.strip() for item in items[1:]])
        except:
            pass
        info['description'] = '\n'.join([item.strip() for item in bs.find("section",{"data-cy":"listing-description-section"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)])
        try:
            info['phone'] = re.search("\"chat_id\":\"\d{10,11}\"", str(bs))[0][11:-1]
        except:
            # "mobile_number":"+84365611994"
            info['phone'] = re.search("\"mobile_number\":\"\+{0,1}\d{10,11}\"", str(bs))[0][17:-1]
        # thong tin co ban
        elements = bs.find("ul", {"class":"list-reset flex flex-wrap md:-mr-5"}).find_all("li")
        for element in elements:
            items = element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            info[items[0].strip()] = items[1].strip()
        # tien ich
        try:
            elements = bs.find("div",{"data-cy":"listing-amenities-component"})
            for element in elements.findChildren(recursive=False):
                
                info[element.find("h3").text.strip()] = ", ".join([item.text.strip() for item in element.find_all("div",{"class":"flex-auto overflow-hidden break-words"})])
        except:
            pass
        
        return self.saveFile(filename, info)

bds = Muabannhadat()
