from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import googlemaps
import xlwt
gmaps = googlemaps.Client(key='AIzaSyDTmbgCfthF9-72UegUiopK6w42EjIxRb8')
url="http://www.niitahmedabad.com/"
url2="https://www.niitmaninagar.com/contact.php"
html=urlopen(url)
gn=BeautifulSoup(html.read(),"lxml");
g=str(gn)
patnum=re.compile('[+][0-9]{2}[-][0-9]{8}')
matnum=patnum.findall(g)
print(matnum)
pat=re.compile(r'[\w.+-]+@[\w.+-]+')
mat=pat.findall(g)
frames=gn.find_all("iframe")
#print(frames)
for iframe in frames:
    response = urlopen(iframe.attrs['src'])
    iframe_soup = BeautifulSoup(response,"lxml")
    #print(iframe_soup)
m=str(iframe_soup)
pattern=re.compile("[0-9][0-9][.]\d+[,][0-9][0-9][.]\d+")
matcher=pattern.findall(m)
#print(matcher[0])
reverse_geocode_result = gmaps.reverse_geocode((matcher[0]))[0]
print(reverse_geocode_result['formatted_address'])
name=input("Enter name of organization:")
workbook=xlwt.Workbook(encoding="utf-8")
sheet1=workbook.add_sheet(name)
sheet1.write(0,0,name)
sheet1.write(0,1,mat[0])
sheet1.write(0,2,reverse_geocode_result['formatted_address'])
workbook.save(name+".xls")
print("Created workbook for "+name)








