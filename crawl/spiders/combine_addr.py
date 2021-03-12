import codecs, json, os, unicodedata

addr_wiki = json.load(open("address_wiki.txt","r", encoding='utf8'))
addr_alo = json.load(open("address_alonhadat.txt","r", encoding='utf8'))
# print(addr_wiki.keys() == addr_alo.keys())
address = dict()
addr =['ward','geo','street']
for district in addr_alo.keys():
    address[district] = dict()
    for ward in addr:
        if ward == 'geo':
            try:
                value = addr_wiki[district][ward]
            except:
                value = None
        else:
#             try:
            value = list(set(addr_wiki[district][ward]).union(set(addr_alo[district][ward]))) 
#             except:
#                 print(district, ward)      
            address[district][ward] = [unicodedata.normalize("NFD",item) for item in value]

json.dump(address, codecs.open("address.txt","w", encoding="utf8"), ensure_ascii=False)

            
    