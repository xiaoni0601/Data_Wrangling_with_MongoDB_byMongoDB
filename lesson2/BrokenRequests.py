import requests
from bs4 import BeautifulSoup
import lxml

s = requests.Session()
s.headers.update({'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"})

r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")


soup = BeautifulSoup(r.text, features='lxml')
viewstate_element = soup.find(id="__VIEWSTATE")
viewstate = viewstate_element["value"]
eventvalidation_element = soup.find(id="__EVENTVALIDATION")
eventvalidation =eventvalidation_element["value"]
viewstategenerator_element = soup.find(id="__VIEWSTATEGENERATOR")
viewstategenerator = viewstategenerator_element["value"]

r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data = (
                   ("__EVENTTARGET", ""),
                   ("__EVENTARGUMENT", ""),
                   ("__VIEWSTATE", viewstate),
                   ("__VIEWSTATEGENERATOR",viewstategenerator),
                   ("__EVENTVALIDATION", eventvalidation),
                   ("CarrierList", "NK"),
                   ("AirportList", "BOS"),
                   ("Submit", "Submit")
                  ))
                   

f = open("NK_and_logan_airport.html", "w")
f.write(r.text)
