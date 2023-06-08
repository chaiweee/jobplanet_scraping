#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:16:40 2023

@author: tanchaiwee
"""

from selenium import webdriver ##셀레니움 할때 사용
from bs4 import BeautifulSoup as bs ##셀레니움 할떄 사용
import time ##시간 지연
import pandas as pd
import requests
import re ##정규표현식쓸때 사용
from tqdm.notebook import tqdm ##진행상황 표시
from selenium.webdriver.common.keys import Keys ## 버튼 클릭하게 해주는 패키지
import math ##페이지수 계산할때 숫자 올림을 사용하였는데 그때 사용함


## 크롬 드라이버 실행
url = "https://www.jobplanet.co.kr/companies?industry_id=700"
response = requests.get(url)
html_text = response.text

html = bs(html_text, 'html.parser')

#print(html)

tmp = html.find_all('dt', {'class':'us_titb_l3'})[0].find('a').get_text()
print(tmp)
#chrome_path='C/Users/tanchaiwee/Documents/project/DataAnalysis_Project/WebScraping_DataCleaning/chromedriver'  ##크롬드라이버 위치

#driver = webdriver.Chrome(chrome_path) ##크롬 실행
#driver.set_window_size(1120, 1000)

##사이트 이동
#driver.get(url) ## driver.get은 원하는 주소로 이동
time.sleep(2) ## 페이지 로딩으로 인해 시간지연


# 로그인(이 코드는 동아리 사람이 공유해줌)
#driver.find_element_by_name('user[email]').send_keys('아이디 입력하기')
#driver.find_element_by_name('user[password]').send_keys('비밀번호 입력하기')
#driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div/form/div/div[2]/div/section[2]/fieldset/button").click()
#time.sleep(2)



#jobs = []
#num_jobs = 5

#while len(jobs) < num_jobs: 
#    time.sleep(3)
    
#    try:
#        company_name = driver.find_element_by_xpath('.//dt[@class="us_titb_l3"]').text
#        print(company_name)
#        location = driver.find_element_by_xpath('.//div[@class="us_stxt_1"]').text
#        review_count = driver.find_element_by_xpath('.//div[contains(@class, "content_col2_4")]').text
#        rating = driver.find_element_by_xpath('.//div[@class="gfvalue"]').text
#        average_salary = driver.find_element_by_xpath('.//div[@class="notranslate"]').text
#        collected_successfully = True
#    except:
#        time.sleep(3)
#    break
        
#    print(company_name, location, review_count, rating, average_salary)
    
#    jobs.append({"Company Name" : company_name,
#            "Location" : location,
#            "Review Counts": review_count,
#            "Rating" : rating,
#            "Average Salary" : average_salary})
    