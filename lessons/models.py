from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    english = models.TextField()
    spanish = models.TextField()
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.title
