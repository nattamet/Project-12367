from django.db import models

class Student(models.Model):
    MAJOR_CHOICES = [
        ('ict', 'ICT'),
        ('cpe', 'CPE'),
        ('csi', 'CSI'),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    major = models.CharField(max_length=80, choices=MAJOR_CHOICES, default='ict')
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.student_id} - {self.name}"
