from django.db import models


class PlainText(models.Model):
    text = models.TextField(verbose_name="plain text")
    link = models.URLField(verbose_name="plain text link", unique=True)
    expiry = models.DateTimeField(verbose_name="expires in", blank=True, null=True)
