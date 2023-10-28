from django.db import models

from .like import AbstractLike


class CommentLike(AbstractLike):
    comment = models.ForeignKey(
        'memoreminder.Comment',
        on_delete=models.CASCADE,
        verbose_name='کامنت'
    )

    def __str__(self):
        return f'{self.id}-{self.memo_user}'

    class Meta:
        verbose_name = 'لایک برای کامنت'
        verbose_name_plural = "لایک های کامنت ها"
        unique_together = ('comment', 'memo_user')

