import bs4
import pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import lxml

n = []
l = []
p_r = []

cur_page = 1
max_page = 1
q = 0
while cur_page <= max_page:
     req = requests.get(f'https://realt.by/sale/flats/page={cur_page}')
     ht = BeautifulSoup(req.content, 'html.parser')
     bs = BeautifulSoup(req.text, 'lxml')
     ht = BeautifulSoup(req.content, 'html.parser')
     #prices = bs.find_all('div', class_='col-auto text-truncate')
     aparts = ht.find_all("div", class_='teaser-tile teaser-tile-right')
     prices0 = bs.find_all('div', class_='desc-mini desc-mini-bottom')
     #prices1 = bs.find_all('div', class_='col-auto text-truncate')
     #prices2 = bs.find('span', class_="negotiable")

     for apt in aparts:
          ap = apt.find('a', class_='teaser-title')
          lnk = ap['href']
          if not 'news' in ap['href']:
               ap = ' '.join(ap.text.split())
               n.append(ap)
               l.append(lnk)

     for qaz in prices0:
          if qaz.find('span', class_="negotiable") is not None:
               #print(' '.join(qaz.text.split()))
               p_r.append(' '.join(qaz.text.split()))
          else:
               pr = qaz.text.split()
               if 'торг' in pr:
                    pr.pop()
               #print(' '.join(pr))
               p_r.append(' '.join(pr))

     cur_page += 1

print(n, len(n))
print(l, len(l))
print(p_r, len(p_r))

d = {'Name':n,
     'Link': l,
     'Price': p_r
     }
p = pandas.DataFrame(d)
writer = pandas.ExcelWriter('output.xlsx')
p.to_excel(writer, 'Люди')
writer.save()