from django.db import models

# Create your models here.

# Introduction model for a brief introduction section
class Introduction(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

# AboutMe model for personal information and links
class AboutMe(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Education model for academic qualifications
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=4) 
    description = models.TextField(max_length=300, default='No description')

    def __str__(self):
        return f"{self.degree} from {self.institution} ({self.graduation_year}) {self.description}"

# Skills model for showcasing skills with Markdown description
class Skills(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

# Experience model for work experience
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

# Project model for showcasing projects
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    link = models.URLField()

