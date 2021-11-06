import os
import csv
from pprint import pprint
from ftplib import FTP
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from hotbox.models import Source, Reading


class Command(BaseCommand):
    help = "Import one day of Readings from a Source"

    def add_arguments(self, parser):
        parser.add_argument("source_id", type=int)
        parser.add_argument("date")

    def handle(self, *args, **options):
        date = options["date"]
        dateFormatted = datetime.strptime(date, "%y%m%d").strftime("%B %-d, %Y")

        try:
            source_id = options["source_id"]
            source = Source.objects.get(pk=source_id)
        except Source.DoesNotExist:
            raise CommandError('Source "%s" does not exist' % source_id)

        self.stdout.write(
            self.style.SUCCESS(
                'Importing data from "%s" for %s' % (source.name, dateFormatted)
            )
        )

        file = "LOG_Trends_1004_%s.txt" % date
        sourcePath = "%s/%s" % (source.path, file)

        localDir = "%s/%s" % (settings.BASE_DIR, "tmp")
        destinationPath = "%s/%s" % (localDir, file)

        if not os.path.exists(localDir):
            os.makedirs(localDir)

        print("%s -> %s" % (sourcePath, destinationPath))

        try:
            ftp = FTP(source.host)
            ftp.set_pasv(False)
            ftp.login()
            ftp.retrbinary("RETR %s" % sourcePath, open(destinationPath, "wb").write)
            ftp.quit()
        except:
            raise CommandError('Error connecting to FTP host "%s"' % source.host)

        with open(destinationPath, encoding="utf-16") as file:
            for line in csv.DictReader(file, delimiter="\t"):
                pprint(line)
                date = datetime.strptime(line["Date"], "%H:%M:%S %m-%d-%Y")
                reading = Reading(date=date, source=source, data=line)
                reading.save()
