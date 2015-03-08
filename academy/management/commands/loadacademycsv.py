import os
import csv
import random
from django.conf import settings
from academy.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        Invite.objects.all().delete()
        csv_path = os.path.join(settings.BASE_DIR, "academy_invites_2014.csv")
        csv_file = open(csv_path, "rb")
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            reporter = random.choice(
                ['clark-kent', 'lois-lane']
            )
            obj = Invite.objects.create(
                name=row['Name'], #this is the part where we match the lowercase name in the model to the uppercase name in the database/csv
                branch=row['Branch'], #ditto. this is about ensuring consistency in our database.
                reporter=reporter
            )
            print obj.name