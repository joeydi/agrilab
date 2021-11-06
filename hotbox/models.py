from django.db import models


# This represents a single "device", e.g. Hotbox 1
class Source(models.Model):
    name = models.CharField(max_length=200)
    host = models.CharField(max_length=200, blank=True)
    port = models.CharField(max_length=200, blank=True)
    path = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


# This represents a single row in the log
# All CSV columns are saved as a JSON object
class Reading(models.Model):
    date = models.DateTimeField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return self.date.strftime("%B %-d, %Y")
