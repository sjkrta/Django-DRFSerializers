from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(
        max_length=3,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('N/A', 'Rather not say')],
        default='N/A'
    )
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
