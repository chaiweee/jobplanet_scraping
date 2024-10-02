#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 09:42:18 2023

@author: tanchaiwee
"""

# web scrape
# write to csv
# load data from csv for cleaning
# save result to db
# do simple eda


from web_scraping import web_scraper
from write_to_csv import write_to_csv
#from data_cleaning import clean_data
#from db_connect import insert_into_db, select_from_db


result_set = web_scraper(2)
print(result_set)

result_file = write_to_csv(result_set)
print(result_file)

#clean_data(result_file)


## more to do
# include company data from landing page such as 기업형태(중소기업, 대기업), 사원수, 설립날
# from the data, can analyze around the size, age of the company
# see how the size/ age affects the average salary
# include different industries

# get data from job search, eg. 'data analyst'
# from job introduction get the skills needed, find out which skills are the most needed
