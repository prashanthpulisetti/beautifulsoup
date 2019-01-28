import bs4
from urllib.request import urlopen as uReq
import bs4

my_url ='<give your url which you want to dump>'
uClient = uReq(my_url)
page_html = uClient.text
page_soup =soup(page_html,"html.paser")
print(soup.find_all('script'))
