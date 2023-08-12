Booking.com Web Scraping Bot
Welcome to the Booking.com Web Scraping Bot repository! This project is designed to provide users with a convenient way to extract and analyze hotel information from Booking.com. The repository contains a set of Python scripts that collectively form a web scraping bot capable of fetching hotel data, applying filters, and generating insightful reports.

Introduction - >  
The Booking.com Web Scraping Bot is a powerful tool that automates the process of collecting hotel information from the Booking.com website. The primary component is the run.py script, which acts as a frontend for users and allows them to interact with the bot. The bot offers various actions, such as applying filters based on star ratings, review scores, and sorting options.

Usage  - >  
To use the Booking.com Web Scraping Bot, follow these steps:

Clone the repository to your local machine.
Install the required dependencies (see Installation).
Configure the necessary settings (see Configuration).
Run the run.py script to initiate the bot's front end.
Follow the on-screen prompts to specify your preferences and actions.
The bot will then carry out the requested actions, interact with the Booking.com website, and generate a detailed report of the collected hotel data.

Files and Directories  - >  
run.py: The main script that serves as the user interface for the web scraping bot.
filters.py: Contains methods for applying filters to the Booking.com search results, such as star rating, review score, and sorting options.
constants.py: Stores essential constants like the driver path and the base URL of the Booking.com website.
booking.py: Handles the core functionality of loading the website, managing pop-ups, selecting currency, performing searches, and collecting hotel data. It also utilizes methods from filters.py to refine the search results.
booking_report.py: Gathers detailed information about targeted hotels, which is later used to generate comprehensive reports.
__init__.py: Initializes the project as a Python module.
