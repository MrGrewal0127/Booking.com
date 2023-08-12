import booking.constants as const
import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from booking.filters import BookingFilters
from selenium.webdriver.support.ui import Select
from booking.booking_report import BookingReport
from prettytable import PrettyTable
import pandas as pd
from unidecode import unidecode

class Booking(webdriver.Chrome):
    
    def __init__(self,teardown=False):
        os.environ['PATH'] += const.DRIVER_PATH
        self.teardown=teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()
       
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)        
            
    def cancel_signin(self):
        try:
            cancel_signin = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            cancel_signin.click()
        except:
            print("no element found")
        
     
    def currency_changer(self,currency=None):
        try:
            currency_selector = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
            currency_selector.click()
            div_elements = self.find_elements(By.CSS_SELECTOR, 'div.ea1163d21f')
           
            for div in div_elements:
                if(div.text==currency):
                    button_element = div.find_element(By.XPATH, './ancestor::button')
                    button_element.click()
                    break
        except:
            print('currency item not found')
        
    
    def search_place_to_go(self,destination):
        try:
            select_place = self.find_element(By.ID,':Ra9:')
            select_place.clear()
            select_place.send_keys(destination)
            button = self.find_element(By.CSS_SELECTOR,'button[data-testid="date-display-field-start"]')
            button.click()

        except:
            print("destination is not found")

    def select_dates(self ,check_in_date,check_out_date):
        try:
            check_in = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"].b21c1c6c83')
            check_in.click()
            check_out = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"].b21c1c6c83')
            check_out.click()
        except:
            print('date not able to select')
            
    def select_room_config(self,adult,children,room):
        try:
            
            config =self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
            config.click()
            numbers = re.findall(r'\d+', config.text)

            adults = int(numbers[0])
            childrens = int(numbers[1])
            rooms = int(numbers[2])
            adults_dec = self.find_element(By.CSS_SELECTOR,'button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.cd7aa7c891')
            for i in range(adults - 1):
                adults_dec.click()
                
            val_inc = self.find_elements(By.CSS_SELECTOR,'button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.d64a4ea64d')
            
            for i in range(adult-1):
                val_inc[0].click()
            for i in range(children):
                val_inc[1].click()
               
               
            if(children>=1):
                div_age = self.find_element(By.CSS_SELECTOR, 'div.d6bfadf8de')
                div_select = div_age.find_elements(By.TAG_NAME,'select')
                for select in div_select:
                    a = input('Enter age of children - ')
                    select_element = Select(select)
                    select_element.select_by_value(a)
            


            for i in range(room-1):
                val_inc[2].click()  
            done = self.find_element(By.CSS_SELECTOR,'button.fc63351294.a822bdf511.e2b4ffd73d.f7db01295e.c938084447.a9a04704ee.d285d0ebe9')
            done.click()
        except Exception as error:
            print("An error occurred.")
            print(f"Error details: {error}")


    def click_search(self):
        search=self.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        search.click()
        
    def apply_filters(self,stars,review_score,sortby):
        filters = BookingFilters(driver=self)
 
        if sortby == 1:
            filters.sortBy_LowPrice_First()
        elif sortby == 2:
            filters.sortBy_PropertyRating()
        elif sortby == 3:    
            filters.sortBy_Top_Reviews()
        elif sortby == 4:
            filters.sortBy_BestReviews_LowestPrice()    
        filters.apply_star_filter(stars)
        filters.apply_review_score_filter(review_score)
        
        
    def report_result(self,destination,check_in_date,check_out_date,adults,childrens,rooms):
        try:
            
            table = PrettyTable(        
                field_names=["Hotel_Name","Rating","Comments","No_of_reviews","Price","Gst"]
            )
            list = self.find_element(By.CSS_SELECTOR,'div[data-arp-properties-list="1"]')
            report = BookingReport(list)
            pagination = list.find_element(By.CSS_SELECTOR, 'div[data-testid="pagination"]')
            next_page_button = pagination.find_element(By.CSS_SELECTOR,'button[aria-label="Next page"]')
            last_page = list.find_elements(By.CSS_SELECTOR,'button.fc63351294.f9c5690c58')
            no_ofpages = last_page[len(last_page)-1].get_attribute('innerText').strip()
            print(f"Total no of pages = {no_ofpages} ")
            no_of_page_movements = int(no_ofpages)-1
            table.add_rows(report.pull_details())
            page=1
            print(f"page[{page}] scanning done")
            for i in range(no_of_page_movements):
                pagination = list.find_element(By.CSS_SELECTOR, 'div[data-testid="pagination"]')
                next_page_button = pagination.find_element(By.CSS_SELECTOR,'button[aria-label="Next page"]')
                next_page_button.click()
                
                self.refresh()
                list = self.find_element(By.CSS_SELECTOR,'div[data-arp-properties-list="1"]')
                report = BookingReport(list)
                table.add_rows(report.pull_details())
                page=i+2
                print(f"page[{page}] scanning done")
                
            
            print("\n\n\n\n")
            print(f"Your Destination: {destination}\n",
                  f"Check-in-Date: {check_in_date}\n",
                  f"Check-out-Date: {check_out_date}\n",
                  f"No of Adults: {adults}\n",
                  f"No of Children: {childrens}\n",
                  f"No of Rooms Required: {rooms}"),
            f"No of pages scanned: {page}"
            print(table)


            output_file = f'{destination}.csv'

            for row in table._rows:
                encoded_row = [cell.encode('utf-8') if isinstance(cell, str) else cell for cell in row]
                table_data.append(encoded_row)

            df = pd.DataFrame(table_data, columns=table.field_names)

            output_file = 'table_data.csv'

            df.to_csv(output_file, index=False, encoding='utf-8')
            

        except Exception as e:
            print('Some error occured')
            print("\n\n\n\n")
            print(f"Your Destination: {destination}\n",
                  f"Check-in-Date: {check_in_date}\n",
                  f"Check-out-Date: {check_out_date}\n",
                  f"No of Adults: {adults}\n",
                  f"No of Children: {childrens}\n",
                  f"No of Rooms Required: {rooms}"),
            f"No of pages scanned: {page}"
            print(table)
            output_file = f'{destination}.csv'

            table_data = []
            for row in table._rows:
                encoded_row = [cell.encode('utf-8') if isinstance(cell, str) else cell for cell in row]
                table_data.append(encoded_row)

            df = pd.DataFrame(table_data, columns=table.field_names)

            output_file = 'table_data.csv'

            df.to_csv(output_file, index=False, encoding='utf-8')
