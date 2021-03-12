import bs4, json, requests, unicodedata, codecs
from bs4 import BeautifulSoup

class Alonhadat2:
    homepage = "https://alonhadat.com.vn"
    address = dict()
    
    def request(self, url):
        html = requests.get(url).text
        return BeautifulSoup(html, 'html.parser')

    def extract(self):
        
        bs = self.request("https://alonhadat.com.vn/handler/Handler.ashx?command=2&matinh=1")
        
        for item in list(bs.find_all("option"))[1:]:
            district = item.text.lower().replace("quận","").replace("huyện","").replace("thị xã","").strip()
            self.address[district] = dict()
            district_code = item.get("value")
            start_urls = ["https://alonhadat.com.vn/handler/Handler.ashx?command=3&mahuyen=","https://alonhadat.com.vn/handler/Handler.ashx?command=4&mahuyen=","https://alonhadat.com.vn/handler/Handler.ashx?command=16&mahuyen="]
            
            # ward
            self.address[district]['ward'] = list()
            bs_ward = self.request(start_urls[0]+district_code)
            for value in list(bs_ward.find_all("option"))[1:-1]:
                ward = value.text.lower()
                if ('phường' not in ward) and ('xã' not in ward) and ('thị trấn' not in ward):
                    print(ward) # empty
                self.address[district]['ward'].append(ward.replace('phường',"").replace('xã',"").replace('thị trấn',"").strip())
            
            # street
            self.address[district]['street'] = list()
            bs_street = self.request(start_urls[1]+district_code)
            for value in list(bs_street.find_all("option"))[1:-1]:
                street = value.text.lower()
                if ('đường' not in street) and ('phố' not in street):
                    # print(street, district) # ngõ, quốc lộ, đại lộ, tỉnh lộ: quốc lộ 70, tỉnh lộ 70
                    pass
                self.address[district]['street'].append(street.replace('đường',"").replace('phố',"").strip())
            
            # project
            self.address[district]['project'] = list()
            bs_project = self.request(start_urls[2]+district_code)
            for value in list(bs_project.find_all("option"))[1:-1]:
                project = value.text.lower()
                # print(project)
                self.address[district]['project'].append(project.strip())
            # return
        json.dump(self.address, codecs.open("address_alonhadat2.txt","w", encoding="utf8"), ensure_ascii=False)
        # with open("alonhadat_com_vn_address.html","w", encoding="utf8") as f:
        #     f.write(bs.prettify())

alo =Alonhadat2()
alo.extract()

class Alonhadat1:
    homepage = "https://alonhadat.com.vn"
    address = dict()
    
    def __init__(self):
        pass
    
    def request(self, url):
        html = requests.get(url).text
        return BeautifulSoup(html, 'html.parser')

    def getLinkDistricts(self, url):
        bs = self.request(url)

        # with open("alonhadat_com_vn_address.html","w", encoding="utf8") as f:
        #     f.write(bs.prettify())

        # get link quan, huyen, thi xa
        start_urls = list()
        for url in list(bs.find("ul",{"style":"max-height:100%"}).find_all("li"))[1:]:
            district = url.find("b").text.replace("Quận ",'').replace("Thị xã ",'').replace("Huyện ",'').lower()
            self.getAddress(district, self.homepage+url.find("a")["href"])
            
        json.dump(self.address,codecs.open("address_alonhadat.txt","w"), ensure_ascii=False)
    
    def getAddress(self,district, url):
        self.address[district] = dict()
        bs = self.request(url)
        
        ward_street = list(bs.find_all("div",{"class":"item temp-navigation"}))
        # ward 
        self.address[district]['ward'] = list()
        for ward in ward_street[0].find_all("b"):
            ward = unicodedata.normalize('NFC',ward.text.strip().lower())
            if 'phường ' in ward:
                self.address[district]['ward'].append(ward.replace('phường ','').lower())
            elif 'thị trấn ' in ward:
                self.address[district]['ward'].append(ward.replace('thị trấn ','').lower())
            elif 'xã ' in ward:
                self.address[district]['ward'].append(ward.replace('xã ','').lower())
            else:
                print(district, ward) #empty

        # street
        self.address[district]['street'] =set()
        for street in ward_street[1].find_all("b"):
            street = unicodedata.normalize('NFC',street.text.strip().lower())
            if 'đường' in street:
                street = street.replace('đường ','')
                # print(street) có quốc lộ, tỉnh lộ 
            elif 'phố ' in street:
                street = street.replace('phố ','')
            elif 'ngõ' in street:
                pass 
            elif 'đại lộ ' in street:
                pass
            if 'quốc lộ ' in street:
                # pass
                street = street.replace('quốc lộ ','')
            if 'tỉnh lộ ' in street:
                # pass
                street = street.replace('tỉnh lộ ', '')
            
                # street = street.replace('đại lộ ', '')
                # print(street)
            # else:
            #     print(district,"--", street) # empty
            
            self.address[district]['street'].add(street)
        self.address[district]['street'] = list(self.address[district]['street'])
            
# url= "https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/ha-noi/407/quan-ba-dinh.html"
# alo =Alonhadat1()
# alo.getLinkDistricts(url)
