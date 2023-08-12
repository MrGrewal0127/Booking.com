from booking.booking import Booking
import time

try:
    
        # currency = input('Enter Your Currency like [INR, USD, CAD etc..] - ')
        # destination = input ("Enter you destination - ")    
        # print("Dates are only valid for this and next month..")
        # check_in_date = input('Enter your check in date [YYYY-MM-DD] - ')
        # check_out_date = input('Enter your check out date [YYYY-MM-DD] - ')
        # adults = int(input("Enter no of adults - "))
        # childrens = int(input("Enter no of children - "))
        # rooms = int(input("Enter the no of rooms required - "))

        # print("Choose one of the following: \n",
        #     "1. Sort by Lowest Prices \n",
        #     "2. Sort by Property Ratings \n",
        #     "3. Sort by Top Reviews \n",
        #     "4. sort by BestReviews and Lowest prices \n")
        # sortby = int(input(
        #     "Enter your choice - "
        # ))
        # star_str = input("Enter a list of stars ratings(1-5) eg. [ 5,4,3 ] - ")
        # stars = star_str.split(',')
        # review_str = input("Enter a list of review ratings(6-9) eg. [ 7,8,9 ] - ")
        # review_score = review_str.split(',')
        with Booking() as bot:
            bot.land_first_page()
            bot.cancel_signin()
            # bot.currency_changer(currency) 
            bot.search_place_to_go(destination="Gurgaon")
            bot.select_dates(check_in_date="2023-07-15",check_out_date="2023-07-19")
            bot. select_room_config(adult=4,children=0,room=2)
            bot.click_search()
            bot.apply_filters(stars=['3','4'],review_score=['7'],sortby=1)
            bot.refresh()
            bot.report_result(destination="Gurgaon",check_in_date="2023-07-15",check_out_date="2023-07-19",adults=4,childrens=0,rooms=2)


except Exception as e:
    if 'in PATH' in str(e):
        print(
            
            'You are trying to run bot from command line \n'
            'Please add to Path your selenium driver \n'
            'Windows : \n'
            '   Set  PATH =%PATH%;path-to-your-folder \n \n'
        )
    else:
        raise
   