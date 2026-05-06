from django.db import models
from django.contrib.auth.models import User

MOODS = (
    ('Grief', 'Grief'),
    ('Nostalgia', 'Nostalgia'),
    ('Regret', 'Regret'),
    ('Hope', 'Hope'),
    ('Rage', 'Rage'),
    ('Peace', 'Peace'),
    ('Reflection', 'Reflection'),
)

class Entry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    mood = models.CharField(max_length=20, choices=MOODS)
    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title