from bs4 import BeautifulSoup
from .models import *
import requests
import csv

def first():
    job.objects.all().delete()
    r = requests.get("http://jkssb.nic.in/WriteReadData/File/Home.htm")

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    article = soup.find("div", {"class": "top"}).findAll('li')
    i = 1
    for element in article:
        for a in element.find_all('a', href=True):
            if i < 11:
                print i
                item_link = a.text
                item_text = "http://jkssb.nic.in/" + a['href']
                i += 1
                jobs = job(
                    title= item_link,
                    link= item_text,
                )
                print jobs.title
                print jobs.link
                jobs.save()
            else:
                return


