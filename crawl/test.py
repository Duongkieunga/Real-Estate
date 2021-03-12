import requests, re
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()
headers={
    'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
url = 'https://www.amazon.com/s/ref=lp_549726_nr_n_0?fst=as%3Aoff&rh=n%3A283155%2Cn%3A%211000%2Cn%3A5%2Cn%3A549726%2Cn%3A886498&bbn=549726&ie=UTF8&qid=1604227762&rnid=549726'
# html = requests.get(url, headers=headers, verify=False).text
# while "Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies." in html:
#     print('-----------')
#     html = requests.get(url, headers=headers, verify=False).text
# bs = BeautifulSoup(html, 'html.parser')
# with open('amazon.html','w',encoding='utf-8') as f:
#     f.write(bs.prettify())

# def gen():
#     for i in range(5):
#         yield i, i+1

# for u, v in gen():
#     print(u, v)

s = """<li class="a-last"><a href="/s?i=stripbooks&amp;rh=n%3A283155%2Cn%3A1000%2Cn%3A3%2Cn%3A2624%2Cn%3A886498&amp;page=3&amp;qid=1604252789&amp;ref=sr_pg_2">Next<span class="a-letter-space"></span><span class="a-letter-space"></span>→</a></li></ul></div>"""
print()