import os, re, codecs, requests
import bs4, base64, json
from bs4 import BeautifulSoup
from PIL import Image
# import cv2
from io import BytesIO

url ="https://st.chotot.com/imaginary/543ea14fda6a6b035c5a6acd07d2850db350d498/property_project/500_overview_1/thumbnail?width=1000&type=jpeg"
with open("img.txt","rb") as f:
    data = f.read()
print(base64.b64decode(data.rsplit(b'\n')[-1]).decode("utf-8"))

img = Image.open(BytesIO(base64.b64decode(data.rsplit(b'\n')[0])))
img.save("1.png",'PNG')

# with open("img.txt","wb") as f:
#     f.write(base64.b64encode(requests.get(url).content)+b'\n'+base64.b64encode(url.encode('utf-8')))
# data = base64.b64encode(requests.get(url).content)+b'\n'+base64.b64encode(url.encode('utf-8'))




# print(os.getcwd())
# source = "src/resources/batdongsan.com.vn/biet_thu_lien_ke/1.html"

# with open(source,'r',encoding='utf-8') as f:
#     data = f.read()

# soup = BeautifulSoup(data,'html5lib')
# print(soup.find('title').text.encode('latin1').decode('utf-8'))
