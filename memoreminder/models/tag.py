from django.db import models

from .time_model import TimeModel


class Tag(TimeModel):
    creator_user = models.ForeignKey(
        'memoreminder.MemoUser',
        on_delete=models.CASCADE,
        verbose_name='کاربر'
    )

    name = models.CharField(
        max_length=60,
        verbose_name='نام'
    )

    color = models.CharField(
        max_length=50,
        verbose_name='رنگ'
    )

    def __str__(self):
        return f'{self.id}-{self.creator_user}-{self.name}'

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = "تگ ها"
