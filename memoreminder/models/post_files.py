from django.db import models

from .time_model import TimeModel
from ..helpers import OnUploadRename


class PostFile(TimeModel):
    file = models.FileField(
        upload_to=OnUploadRename('post/'),
        null=True,
        blank=True,
        verbose_name='فایل'
    )

    post = models.ForeignKey(
        'memoreminder.Post',
        on_delete=models.CASCADE,
        verbose_name='خاطره'
    )

    file_raw = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='لینک فایل'
    )

    def __str__(self):
        return f'{self.id}-{self.post.pk}-{self.post.creator_user.username}'

    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = "فایل ها"
