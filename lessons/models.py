from django.conf import settings
from django.db import models

class Lesson(models.Model):
    english_text = models.TextField()
    spanish_text = models.TextField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lessons",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.english_text[:50]
