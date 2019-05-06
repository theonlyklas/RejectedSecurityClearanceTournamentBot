import os
import requests
from bs4 import BeautifulSoup
import pdb
import time

BASE_SECURITY_CLEARANCE_URL = "http://ogc.osd.mil/doha/industrial/"

men_dict = dict()
women_dict = dict()

"""
class Person:
    ag

class Woman super Person:
"""

class Case:
    def __init__(self, case_text, decision):
        self.case_text = case_text
        self.decision = decision


def process_cases(cases):
    pdb.set_trace()


def get_security_clearance_decision_data(startDate = None, endDate = None):
    page = requests.get(BASE_SECURITY_CLEARANCE_URL)
    
    while (200 != page.status_code):
        time.sleep(1)
        page = requests.get(BASE_SECURITY_CLEARANCE_URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.select('h4 a')

    security_clearance_decision_years_online = []
    for link in links:
        security_clearance_decision_years_online.append(link.contents)

    for year in security_clearance_decision_years_online:
        year_page = requests.get(BASE_SECURITY_CLEARANCE_URL +  str(year[0]) + '.html')

        time_to_sleep = 0
        while (200 != year_page.status_code):
            time_to_sleep += 1
            time.sleep()
            year_page = requests.get(BASE_SECURITY_CLEARANCE_URL)

        soup = BeautifulSoup(year_page.content, 'html.parser')

        cases = soup.find_all(class_="case")

        pdb.set_trace()
        process_cases(cases)


# def addPeopleToDictionaries(dirName, genderDictionary):
#     for filename in os.listdir(dirName):

def main():
    get_security_clearance_decision_data()

main()