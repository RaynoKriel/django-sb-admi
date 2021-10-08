from django.db import models
from django.urls import reverse
# Create your models here.



class projects(models.Model):
    id          = models.BigAutoField(primary_key=True)
    project     = models.TextField()
    description = models.TextField()
    created     = models.TextField()
    modified    = models.TextField()
    user        = models.TextField()
    status      = models.TextField()


def get_absolute_url(self):
	# f"/projects/{self.id}/"
	return reverse("projects:project-detail", kwargs={"id": self.id})
