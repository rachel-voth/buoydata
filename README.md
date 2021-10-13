# Surf Buoy Data Project

This is a Django project for visualizing historical buoy data from [NOAA 46087](https://www.ndbc.noaa.gov/station_page.php?station=46087) in Neah Bay, Washington.

So far the project is simply a database with a Buoy model and a script that takes a .txt file from the NOAA site and inserts the cleaned data into the database.

## Setup

- Clone the repo
- Have Python, virtualenvwrapper, and Docker installed. I use asdf to manage my python versions and used Python 3.10 for this project.
- From the root directory:
  - `docker-compose up -d`
  - `mkvirtualenv <virtualenv-name>`
  - `pip install -r requirements.txt`
  - `python manage.py migrate`
  - `python manage.py seed2020`
  - `python manage.py runserver`
