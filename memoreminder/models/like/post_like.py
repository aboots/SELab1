from django.db import models

from .like import AbstractLike


class PostLike(AbstractLike):
    post = models.ForeignKey(
        'memoreminder.Post',
        on_delete=models.CASCADE,
        verbose_name='خاطره'
    )

    def __str__(self):
        return f'{self.id}-{self.memo_user}'

    class Meta:
        verbose_name = 'لایک برای پست'
        verbose_name_plural = "لایک های پست ها"
        unique_together = ('post', 'memo_user')
