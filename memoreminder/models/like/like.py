from django.db import models

from memoreminder.models.time_model import TimeModel


class AbstractLike(TimeModel):
    memo_user = models.ForeignKey(
        'memoreminder.MemoUser',
        on_delete=models.CASCADE,
        verbose_name='کاربر'
    )

    class Meta:
        abstract = True
