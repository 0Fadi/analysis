#import libraries
from operator import length_hint
from tkinter import E
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv

#some variables
name_of_job = []
time = []
links = []
page = 0
job_time = []
address = []
company = []


#while loop to scrap data from multiple pages
while True:

    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=data%20analysis&start={page}")
    src = result.content
    soup = BeautifulSoup(src , "lxml")
    
    limit =int(soup.find("strong").text)
    
    if (page > limit //15):
        print ("ended , terminate")
        break


    name_of_jobs = soup.find_all("h2",{"class":"css-m604qf"})
    posted_new = soup.find_all("div",{"class":"css-4c4ojb"})
    posted_old = soup.find_all("div",{"class":"css-do6t5g"})
    posted = (*posted_new,*posted_old)
    da = (posted_new+posted_old)
    job_times = soup.find_all("span",{"class":"css-1ve4b75 eoyjyou0"})
    job_address = soup.find_all("span",{"class":"css-5wys0k"})
    company_name = soup.find_all("a",{"class":"css-17s97q8"})


    for i in range (len(name_of_jobs)):
        name_of_job.append(name_of_jobs[i].text)
        time.append(posted[i].text)
        job_time.append(job_times[i].text)
        address.append(job_address[i].text)
        company_text = company_name[i].text.replace("-","")
        company.append(company_text)
        links.append("https://wuzzuf.net"+name_of_jobs [i].find("a").attrs['href'])
        

    page += 1
    print ("next")


#export data as csv file
file_list = [name_of_job,time,job_time,address,company,links]
exported = zip_longest(*file_list)
with open ("C:/Users/FAM/downloads/scrapwazzuf.csv","w")as myfile:
    wr = csv.writer(myfile)
    wr.writerow (["job name","posted time","job time","job address","company name","link"])
    wr.writerows(exported)
