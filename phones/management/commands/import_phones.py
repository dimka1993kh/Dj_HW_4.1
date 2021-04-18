import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import date
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # print(line[4].split('-'))
                year, month, day = line[4].split('-')

                phone = Phone.objects.create(
                    name=line[1],
                    price=line[3], 
                    image=line[2], 
                    release_date=date(int(year), int(month), int(day)), 
                    lte_exists=line[5], 
                    slug=slugify(line[1])
                    )
