from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    instrument = models.CharField(max_length=255)

class Album(models.Model):
    name = models.CharField(max_length=255)
    musician = models.ForeignKey("Musician", on_delete=models.CASCADE, related_name="albums")
    tags = models.ManyToManyField("Tag", related_name="albums")

class Bio(models.Model):
    hometown = models.CharField(max_length=255)
    musician = models.OneToOneField("Musician", on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=255)