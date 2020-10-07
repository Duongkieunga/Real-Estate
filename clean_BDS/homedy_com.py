import os, bs4, html, re, json, codecs
from bs4 import BeautifulSoup

class Homedy:
    path = "/home/nga/Documents/20193/Project/request/Datas/homedy.com"
    def __init__(self):
        for _,_, filenames in os.walk(self.path):
            for filename in filenames:
                print(filename)
                # filename = "169.html"
                self.extract(BeautifulSoup(open(self.path+'/'+filename,'r').read(),'html.parser'), filename)
                # return

    def saveFile(self, filename, info):
        json.dump(info, codecs.open('./'+filename.split('.')[0]+'.txt','w'),ensure_ascii=False)

    def extract(self, bs, filename):
        info = dict()
        element = bs.find("div",{"class":"col-sm-8"})
        # title
        info['title'] = element.find("h1").text.strip()
        # id, type, ngay dang, ngay het han, phone, phong tam, nha vs
        items = element.find("div",{"class":"product-info"}).find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
        info['id'] = items[1].strip()
        info['type'] = re.search("sub_category_1: \"(\w+,*\s*)+\"", str(bs))[0][17:-1]
        info['startDate'] = re.findall("\d{4}-\d{2}-\d{2}", str(bs))[1]
        info['endDate'] = re.findall("\d{4}-\d{2}-\d{2}", str(bs))[2]
        info['phone'] = re.findall('\d{10}', re.findall("agent_phone: \"\d{10}\"", str(bs))[0])[0]
        info['name'] = bs.find("div",{"class":"info"}).find("div",{"class":"name"}).text.strip()
        
        try:
            key = None
            for chil in element.find("ul",{"class":"utilities"}).findChildren(recursive=True):
                if (chil.name == 'span') and (chil.get("class") is not None):
                    info[chil.get("class")[0]] = None
                    key = chil.get("class")[0]
                else:
                    if key is not None:
                        info[key] = chil.text.strip()
                        key = None
        except:
            pass
        # gia, dientich, gia/dientich
        element = bs.find_all("div",{"class":"row"})
        for chil in element:
            items = chil.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            value = ""
            for item in items[1:]:
                value += item.strip()+" "
            info[items[0].strip()] = value

        # location - review, cua Quan, Huyen, THi tran
        element = bs.find("div", {"class":"text-location"}).find_all("div",{"class":"text"})
        for chil in element:
            items = chil.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            try:
                info[items[0].strip()] = items[2].strip()
            except:
                info[items[0].strip()] = items[1].strip()
        
        # description 
        element = bs.find("div",{"class":"description readmore"})
        info['description'] = ""
        for item in element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True):
            info['description'] += item.strip() +"\n"
        # Noi that
        try:
            element = bs.find("div", {"class":"utilities-detail furniture"}).find("div",{"class":"content"})
            items = element.find_all(text= lambda text: (not isinstance(text, bs4.element.Comment)) and (text.strip() != ''), recursive=True)
            info['Nội thất'] = ""
            for item in items:
                info['Nội thất'] += item.strip()+"\n"
        except:
            pass
        # print(info)
        return
        return self.saveFile(filename, info)

bds = Homedy()