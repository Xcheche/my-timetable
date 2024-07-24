from django.db import models

# Create your models here.

MONTH_CHOICES = [
    ('jan', 'January'),
    ('feb', 'February'),
    ('marc', 'March'),
    ('apr', 'April'),
    ('may', 'May'),
    ('jun', 'June'),
    ('july', 'July'),
    ('aug', 'August'),
    ('sep', 'September'),
    ('oct', 'October'),
    ('nov', 'November'),
    ('dec', 'December'),
]


DAY_CHOICES = [
    ('sun', 'Sunday'),
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday'),
]
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    day = models.CharField(max_length=7, choices=DAY_CHOICES, default='sun',blank=True)
    month = models.CharField(max_length=12, choices=MONTH_CHOICES, default='jan',blank=True)


    def __str__(self):
        return self.title