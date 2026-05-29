from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)

    objective = models.TextField()

    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    cgpa = models.CharField(max_length=20)
    passing_year = models.CharField(max_length=20)

    skills = models.TextField()

    projects = models.TextField()

    experience = models.TextField()

    certifications = models.TextField()

    achievements = models.TextField()

    languages = models.CharField(max_length=200)

    def __str__(self):
        return self.name