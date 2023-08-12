
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import re
class BookingReport:
    
    def __init__(self,main_box:WebElement):
        self.main_box=main_box
        self.deal_boxes = self.main_box.find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')

        
    def pull_details(self):
        
            collection=[]
            for deal_box in self.deal_boxes:
                title = deal_box.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').get_attribute('innerHTML').strip()
                
                
                try:
                    rating_element =  deal_box.find_element(By.CLASS_NAME, "b5cd09854e.d10a6220b4") 
                    comment_element =  deal_box.find_element(By.CLASS_NAME, "b5cd09854e.f0d4d6a2f5.e46e88563a")  
                    no_of_reviews_element = deal_box.find_element(By.CLASS_NAME, "d8eab2cf7f.c90c0a70d3.db63693c62")  
                    
                    rating = rating_element.text
                    comment = comment_element.text
                    no_of_reviews = no_of_reviews_element.text
                except:
                    # print("its me")
                    rating=None
                    comment=None
                    no_of_reviews=None
                    
                
                
                div = deal_box.find_element(By.CSS_SELECTOR,'div[data-testid="availability-group"]')
                sub_div = div.find_element(By.CSS_SELECTOR,'div[data-testid="availability-rate-wrapper"]')
                price_info_div =sub_div.find_element(By.CSS_SELECTOR,'div[data-testid="availability-rate-information"]')
                price = price_info_div.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').get_attribute('innerHTML').strip()
                price = price.replace("&nbsp;", "")
                gst = price_info_div.find_element(By.CSS_SELECTOR,'div[data-testid="taxes-and-charges"]').get_attribute('innerHTML').strip()
                gst = gst.replace("&nbsp;", "")
                

                collection.append([title,rating,comment,no_of_reviews,price,gst])
            return collection
