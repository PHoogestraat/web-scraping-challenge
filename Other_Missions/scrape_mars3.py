#  convert Jupyter notebook to python scirpt

# Dependencies and Setup
from bs4 import BeautifulSoup as bs

from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import time
import pymongo
from splinter import Browser

# Choose the executable path to driver
# executable_path = {"executable_path": ChromeDriverManager().install()}
# browser = Browser("chrome", **executable_path, headless=False)

##################################################################################
# Visit Nasa news url through splinter module
# extracts latest news itme
###################################################################################


# conect to browser
# Choose the executable path to driver


def scrape_info():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)

    url_news = "https://mars.nasa.gov/news/"
    browser.visit(url_news)
    time.sleep(10)

    # HTML Object
    # engages parser
    html_news = browser.html
    soup = bs(html_news, "html.parser")
    
############################################################################
# Scrape the latest News Title and Paragraph Text
#############################################################################
    current_news_title = soup.find_all("div", class_ = "content_title")[1].text
    current_news_paragraph = soup.find("div", class_ = "article_teaser_body").text

    mars_data_dic["current_news_title"] = current_news_title
    mars_data_dic["current_news_paragraph"] = current_news_paragraph
   
    return mars_data_dic
    


########################## main code
# Define dictionary
mars_data_dic = {}

# call funtion
scrape_info()
test_dict = {'news_title': 'MOXIE Could Help Future Rockets Launch Off Mars', 'text': "NASA's Perseverance rover carries a device to convert Martian air into oxygen that, if produced on a larger scale, could be used not just for breathing, but also for fuel."}
# test
print("##########################")
print(mars_data_dic)
print("##########################")
print(test_dict)