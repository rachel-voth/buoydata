import csv
import datetime
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from buoy.models import Buoy


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # filepath should be in relation to manage.py in root dir
        filepath = "./2020.txt"
        bulk_buoy_list = []

        with open(filepath) as f:
            csv_reader = csv.reader(f, delimiter="\t")
            # skip header rows
            next(csv_reader)
            next(csv_reader)
            # parse Buoy columns
            for row in csv_reader:
                # split on spaces
                split_row = row[0].split(" ")
                # remove bad data (empty strings)
                cleaned_row = list(filter(None, split_row))
                # put the first 5 elements together as a datetime
                year = int(cleaned_row[0])
                month = int(cleaned_row[1])
                day = int(cleaned_row[2])
                hour = int(cleaned_row[3])
                minute = int(cleaned_row[4])
                reading_datetime = make_aware(
                    datetime.datetime(year, month, day, hour, minute)
                )
                # assign the rest of the columns
                wind_direction = cleaned_row[5]
                wind_speed = cleaned_row[6]
                gust = cleaned_row[7]
                wave_height = cleaned_row[8]
                dominant_period = cleaned_row[9]
                average_period = cleaned_row[10]
                mean_wave_direction = cleaned_row[11]

                buoy_row = Buoy(
                    reading_datetime=reading_datetime,
                    wind_direction=wind_direction,
                    wind_speed=wind_speed,
                    gust=gust,
                    wave_height=wave_height,
                    dominant_period=dominant_period,
                    average_period=average_period,
                    mean_wave_direction=mean_wave_direction,
                )

                bulk_buoy_list.append(buoy_row)
        try:
            Buoy.objects.bulk_create(bulk_buoy_list)
        except BaseException as err:
            print(f"Buoy bulk create failed for {filepath} - {err}")
