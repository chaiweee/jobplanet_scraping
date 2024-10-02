#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:16:40 2023

@author: tanchaiwee
"""

from selenium import webdriver ##셀레니움 할때 사용
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs ##셀레니움 할떄 사용
import time ##시간 지연
import re ##정규표현식쓸때 사용
from tqdm.notebook import tqdm ##진행상황 표시
from selenium.webdriver.common.keys import Keys ## 버튼 클릭하게 해주는 패키지
import math ##페이지수 계산할때 숫자 올림을 사용하였는데 그때 사용함

def web_scraper(page_num):
    print('Web scraping in progress...')
    ## 크롬 드라이버 실행
    chrome_options = Options()
    chrome_options.add_argument('--log-level=1')
    # chrome_service = Service("/Users/tanchaiwee/Documents/project/DataAnalysis_Project/DataCleaning/chromedriver_mac64/chromedriver")
    chrome_service = Service("C:/Users/Tan Chai Wee/문서/Personal/Project/Jun23_jobplanet_scrape/jobplanet_scraping/chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    
    #chrome_path='/Users/tanchaiwee/Documents/project/DataAnalysis_Project/DataCleaning/chromedriver_mac64/chromedriver'  ##크롬드라이버 위치
    #driver = webdriver.Chrome(chrome_path) ##크롬 실행
    driver.set_window_size(800, 600)
    
    
    # url = "https://www.jobplanet.co.kr/companies?industry_id=700"
    url = "https://www.jobplanet.co.kr/companies?"
    
    ##사이트 이동
    #driver.get(url) ## driver.get은 원하는 주소로 이동
    time.sleep(2) ## 페이지 로딩으로 인해 시간지연
    
    company_list = []
    
    for i in range(1, page_num): ## 1부터 5페이지까지만 하기위해
        print('Scraping page ', i)
        time.sleep(3)
        set_url_1 = url + '&page=' ## 잡플래닛 url 주소
        set_url_2 = i ## 페이지
        set_url = set_url_1 + str(set_url_2) ## str 안하면 텍스트 + 숫자이므로 에러가 발생
        try:
            driver.get(set_url) ## url 이동 (1페이지부터 5페이지까지)
            html = driver.page_source ## 페이지 소스 가져오기
            html_soup = bs(html,'html.parser') ##html로 보기
            time.sleep(2)
        except:
            print('Fail to get html')
            
        company_name = html_soup.find_all('dt',{'class':'us_titb_l3'})
        location = html_soup.find_all('span', {'class': 'us_stxt_1'})    
        #review_counts = html_soup.find_all('dl', {'class':'content_col2_4'})[0].find('dt')
        #rating = html_soup.find_all('span',{'class':'gfvalue'})[0].get_text()
        #avg_salary = html_soup.find_all('strong',{'class':'notranslate'})
        #print(new_loc)
        print('newly added: location ', location)
        
        loc_list = []
        for k in range(1, len(location),2):
            loca = html_soup.find_all('span', {'class': 'us_stxt_1'})[k].get_text()
            # print('loca: ',loca)
            loc_list.append(loca)

        cate_list = []
        for m in range(0, len(location),2):
            catego = html_soup.find_all('span', {'class': 'us_stxt_1'})[m].get_text()
            # print('catego: ',catego)
            cate_list.append(catego)
    
        
        for j in range(len(company_name)): 
            company = company_name[j].find('a').get_text()
            #location = html_soup.find_all('span', {'class': 'us_stxt_1'})[1].get_text()
            location = loc_list[j]
            category = cate_list[j]
            review_counts = html_soup.find_all('dl', {'class':'content_col2_4'})[j].find('dt').get_text()
            rating = html_soup.find_all('span',{'class':'gfvalue'})[j].get_text()
            avg_salary = html_soup.find_all('strong',{'class':'notranslate'})[j].get_text()
            time.sleep(2)
        
            company_list.append(
                {
                    'Company Name': company,
                    'Location': location,
                    'Category': category,
                    'Review Counts': review_counts,
                    'Rating': rating,
                    'Average Salary': avg_salary
                })
        
        print('Finish scraping page ', i)
    
    print('Finish web scraping')
    return company_list
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
