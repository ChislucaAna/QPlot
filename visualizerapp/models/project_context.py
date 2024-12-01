from django.db import models
from django.contrib.auth.models import User

class ProjectContext(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context_data = models.JSONField()  # Store session data as JSON

    def __str__(self):
        return f"Project Context for {self.user}"