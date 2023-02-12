import time

import requests
from bs4 import BeautifulSoup



def find_jobs():
    website_URL = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=data+analyst&txtLocation=").text
    soup = BeautifulSoup(website_URL, 'lxml')
    Jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(Jobs):
        Published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in Published_date:
            companyName = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            More_info = job.header.h2.a['href']
            with open(f'Posts/{index}.txt','w') as f:
                f.write(f"Company name: {companyName.strip()} \n")
                f.write(f"Required Skills: {skills.strip()} \n")
                f.write(f"More info: {More_info}")
            print(f'File {index} Saved')


if __name__ == '__main__':
    while(True):
        find_jobs()
        Wait_Time= 10
        print(f'waiting for {Wait_Time} minutes...')
        time.sleep(Wait_Time*60)
