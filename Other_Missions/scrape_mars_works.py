#  convert Jupyter notebook to python scirpt

# Dependencies and Setup
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import time
import pymongo

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
    time.sleep(5)
    
    #mars_data_dic = {}


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
    
    



#########################################################################
############
############ JPL Mars Space images

    #     featured_image_url
 # Visit Nasa news url through splinter module
################################################      Wait until page is fully loaded !!!!!!!!!!!!!!!!!!!!
    url_pic = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_pic)
    
    fix = "https://www.jpl.nasa.gov/"


    # HTML Object
    html_pic = browser.html
    pic_soup = bs(html_pic, "html.parser")


    #GET TARGET IMAGE- A bit sloppy, pulls more than it should
    
    target_image = pic_soup.find("article")["style"]
    # Cleans up text
    time.sleep(5)
    target_image = target_image.replace("background-image: url('/", "")
    target_image = target_image.replace("');", "")

    featured_image_url = fix + target_image
    
    mars_data_dic["featured_image_url"] = featured_image_url

######################################################################
############
############ Mars Facts
    
    # Get data from Mars Facts web page as described in the insturcitons
    url = "https://space-facts.com/mars/"
    
    # get a table
    table = pd.read_html(url)
    # create a dataframe
    mars_df = table[0]
    mars_df = mars_df.rename(columns={0:"Observation", 1: "Data"})

    # convert to ta HTML
    mars_table = mars_df.to_html()

    # get rid of extra lines
    mars_table = mars_table.replace('\n', '')

    mars_data_dic["mars_facts"] = mars_table
######################################################################


############
############ Mars Hemisphseres
    
    

    # connecting to USGS Astrogeology site
    hem_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)
    # engages parser
    html_hem = browser.html
    hem_soup = bs(html_hem, "html.parser")


    # stores data form web site to be extracted from in a for loop
    spheres = hem_soup.find_all("div", class_="item")
    

    #############################
    ########## For loop to build dictionary for Hemisphere names and picutes
    ##########   Pictues does not work at this time.
    # List to hold dictinary of title names for each url link.
    hem_list = []

    # for loop used to extract data from spheres (extracted data from web site)

    for sph in spheres:    
        sp1 = sph.find("h3").text
        # this will need to be replaced with diffrent code
        html = browser.html
        soup = bs(html, "html.parser")
        browser.links.find_by_partial_text(sp1).click()

        html = browser.html
        soup = bs(html, "html.parser")
        link_ref = soup.find("a", text = "Sample").get("href")
       # End of where new code needs to go
    

   
        hem_list.append({"title:": sp1, "img_url": link_ref})
        browser.visit(hem_url)

    mars_data_dic["Hemisphere_pic"] = hem_list
    browser.quit()
    
    return mars_data_dic




########################## main code
# Define dictionary
mars_data_dic = {}

# call funtion
#scrape_info()

# test
#print("##########################")
#print(mars_data_dic)
#print(target_image)
#print("##########################")
