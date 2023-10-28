from django.db import models

from .time_model import TimeModel


class Comment(TimeModel):
    memo_user = models.ForeignKey(
        'memoreminder.MemoUser',
        on_delete=models.CASCADE,
        verbose_name='کاربر'
    )

    text = models.TextField(
        max_length=300,
        verbose_name='متن'
    )

    post = models.ForeignKey(
        'memoreminder.Post',
        on_delete=models.CASCADE,
        verbose_name='خاطره'
    )

    def __str__(self):
        return f'{self.id}-{self.memo_user}'

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = "کامنت ها"
