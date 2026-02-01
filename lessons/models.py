from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    english_text = models.TextField()
    spanish_text = models.TextField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lessons",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.english_text[:50]
