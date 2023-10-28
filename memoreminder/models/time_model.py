from django.db import models


class TimeModel(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="زمان ساخت"
    )

    modified = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name="آخرین زمان تغییر"
    )

    class Meta:
        ordering = ('-created',)
        abstract = True
