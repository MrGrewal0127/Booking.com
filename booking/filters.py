from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
class BookingFilters:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    
    def apply_star_filter(self,stars):
        try:
            star_div = self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="class"]')
            for s in stars:
                if s == '1':
                    star_req = star_div.find_element(By.CSS_SELECTOR,'div[data-filters-item="class:class=1"]')
                elif s=='2':
                    star_req = star_div.find_element(By.CSS_SELECTOR,'div[data-filters-item="class:class=2"]')
                elif s=='3':
                    star_req = star_div.find_element(By.CSS_SELECTOR,'div[data-filters-item="class:class=3"]')
                elif s=='4':
                    star_req = star_div.find_element(By.CSS_SELECTOR,'div[data-filters-item="class:class=4"]')
                elif s=='5':
                    star_req = star_div.find_element(By.CSS_SELECTOR,'div[data-filters-item="class:class=5"]')
                else:
                    continue
                star_req.click()
                
        except Exception as error:
            # Handle other types of exceptions
            print("An error occurred.")
            print(f"Error details: {error}")    
    def apply_review_score_filter(self,review_rating):
        # 9+ - wonderful
        # 8+ - very good
        # 7+ - good
        # 6+ - pleasant
        try:
            # review_div =  self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="review_score"]')
            for s in review_rating:
                if s == '9':
                    review_req = self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-item="review_score:review_score=90"]')
                elif s=='8':
                    review_req = self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-item="review_score:review_score=80"]')
                elif s=='7':
                    review_req = self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-item="review_score:review_score=70"]')
                elif s=='6':
                    review_req = self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-item="review_score:review_score=60"]')
                else:
                    continue
                review_req.click()
        except Exception as error:
            # Handle other types of exceptions
            print("An error occurred.")
            print(f"Error details: {error}")
                    
    def sortBy_LowPrice_First(self):
        sortby = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sortby.click()
        div = self.driver.find_element(By.CSS_SELECTOR,'div[data-testid="sorters-dropdown"]')
        low_price_first = div.find_element(By.CSS_SELECTOR,'button[data-id="price"]')
        low_price_first.click()

        
    def sortBy_PropertyRating(self):
        sortby = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sortby.click()
        div = self.driver.find_element(By.CSS_SELECTOR,'div[data-testid="sorters-dropdown"]')
        PropertyRating = div.find_element(By.CSS_SELECTOR,'button[data-id="class"]')
        PropertyRating.click()

        
    def sortBy_Top_Reviews(self):
        sortby = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sortby.click()
        div = self.driver.find_element(By.CSS_SELECTOR,'div[data-testid="sorters-dropdown"]')
        Top_Reviews = div.find_element(By.CSS_SELECTOR,'button[data-id="bayesian_review_score"]')
        Top_Reviews.click()


    def sortBy_BestReviews_LowestPrice(self):
        sortby = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sortby.click()
        div = self.driver.find_element(By.CSS_SELECTOR,'div[data-testid="sorters-dropdown"]')
        BestReviews_LowestPrice = div.find_element(By.CSS_SELECTOR,'button[data-id="review_score_and_price"]')
        BestReviews_LowestPrice.click()
            