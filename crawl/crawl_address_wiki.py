from bs4 import BeautifulSoup
import re , os, bs4, requests, json, codecs
class Address:

    address=dict()
    homepage ="https://vi.wikipedia.org"

    def __init__(self):
        pass
            
    def getPages(self, url):
        html = requests.get(url).text
        return BeautifulSoup(html, "html.parser")
    
    def extract(self, url):
        bs = self.getPages(url)

        # district
        link_district = list()
        element = bs.find_all("table", {"class":"wikitable sortable","cellpadding":1})
        for table in element:
            districts = table.find_all("a")
            for district in districts:
                self.extractWard(district.text.strip().lower(), district['href'])
                # return
        json.dump(self.address, codecs.open("address_wiki.txt","w", encoding="utf8"), ensure_ascii=False)
    def extractWard(self, district, url):
        # print(district)
        self.address[district] = dict()

        bs = self.getPages(self.homepage + url)

        # toa do
        try:
            self.address[district]['geo'] = bs.find("span",{"class":"geo-dec"}).text
        except:
            self.address[district]['geo'] = None
        # if district == 'sơn tây':
        

        # street
        un_street = False
        self.address[district]['street'] = list()
        try:
            element = bs.find('div',{'class':'div-col columns column-width'})

            for chil in element.find_all("li"):
                self.address[district]['street'].append(chil.text.strip().lower())
                # print(chil.text)
        except:
            try:
                element = bs.find("table",{'class':'multicol'})
                for chil in element.find_all("li"):
                    self.address[district]['street'].append(chil.text.strip().lower())
                    # print(chil.text)
            except:
                un_street= True

        # ward
        self.address[district]['ward'] = list()
        # element = bs.find("td",{"class":"navbox-list navbox-odd"}).find_all("a")
        # for ward in element:
        #     self.address[district]['ward'].append(ward.text.lower())
        element = bs.find("div",{"class":"mw-parser-output"})
        flag_ward = False
        flag_street = False
        for chil in element.findChildren():
            if chil.name == "h2":
                try:
                    if list(chil.find_all("span"))[1].text == 'Hành chính':
                        flag_ward=True
                        continue
                    if list(chil.find_all("span"))[1].text == 'Đường phố':
                        flag_street=True
                        continue
                except:
                    pass
            if flag_ward== True and chil.name == "p":
                for ward in chil.find_all("a"):
                    self.address[district]['ward'].append(ward.text.strip().lower())
                    # print(ward.text)
                if un_street == False:
                    break
            if flag_street == True and chil.name == "ul":
                for street in chil.find_all("a"):
                    self.address[district]['street'].append(street.text.strip().lower())
                    # print(district, street.text)
                break
        if len(self.address[district]['street'])==0:
            print(district)
            """
            sơn tây
            phú xuyên
            thạch thất
            thanh oai
            thường tín
            ứng hòa
            """
        
        

# url = "https://vi.wikipedia.org/wiki/H%C3%A0_N%E1%BB%99i"
# add = Address()
# add.extract(url)
  
# with open("wiki_address.html","w") as f:
#     f.write(BeautifulSoup(requests.get("https://vi.wikipedia.org/wiki/Ba_%C4%90%C3%ACnh").text,'html.parser').prettify())