from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class TimeStampedModel(models.Model):
    last_edited = models.DateTimeField(editable=False, )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.last_edited = datetime.now()
        super().save()

    class Meta:
        abstract = True


class Device(TimeStampedModel):
    type = models.IntegerField(choices=(
        (1, "Android"),
        (2, "iOS")
    ))

    device_id = models.CharField(unique=True,max_length=300)
