from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=10)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

