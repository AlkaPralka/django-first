from django.db import models

# title will be a short string field to hold the name of your project.
# description will be a larger string field to hold a longer piece of text.
# technology will be a string field, but its contents will be limited to a select number of choices.
# image will be an image field that holds the file path where the image is stored.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
