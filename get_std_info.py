from bs4 import BeautifulSoup as bs
import os
import requests

host = "https://portal.abu.edu.ng"

def get_acc_info(s):
    acc_page = s.get(host+"/abudashboard/sites/accommodation/accommodation.php")
    page = acc_page.content
    soup = bs(str(page), "html.parser")
    link = soup.a["href"]
    link = link[2:]
    undertaking = s.get(host+link)
    stdid, date, year = get_values(undertaking.content)
    payload = {"stdid":stdid, "date":date, "session":year, "checkbox":"on",\
    "button":"I Accept", "MM_insert":"form2", "token":link[59:]}
    return payload

def get_values(page):
    main_soup = bs(str(page), "html.parser")
    stdid = main_soup.find("input", attrs={"id":"stdid"})
    soup = bs(str(stdid), "html.parser")
    stdid = soup.input["value"]
    date = main_soup.find("input", attrs={"id":"date"})
    soup = bs(str(date), "html.parser")
    date = soup.input["value"]
    year = main_soup.find("input", attrs={"id":"session"})
    soup = bs(str(year), "html.parser")
    year = soup.input["value"]
    return stdid, date, year


if __name__=="__main__":
    get_acc_info(s)
