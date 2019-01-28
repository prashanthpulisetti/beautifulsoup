#/usr/bin/env python 
import requests
from bs4 import BeautifulSoup
#import sys

#urls = open("/home/prashanth/Downloads/50000url.csv").split("\n")
with open ("/home/prashanth/Desktop/p1/Malicious_domains_10000.csv", "r") as myfile:
        data=myfile.readlines()
        for url in data:
                try:
                        r= requests.get(url.replace("\n", ""))
                        html_content = r.text
                        soup = BeautifulSoup(html_content,"html.parser")
                        #sys.stdout=open("javascript.js","a")
                        print(soup.find_all('script'))
                        #sys.stdout.close()



                except:
                        print(url)

