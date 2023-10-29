from django.db import models

from .time_model import TimeModel


class Post(TimeModel):
    MODE_PUBLIC = 'public'
    MODE_PRIVATE = 'private'

    MODES = (
        (MODE_PRIVATE, 'خصوصی'),
        (MODE_PUBLIC, 'عمومی'),
    )

    creator_user = models.ForeignKey(
        'memoreminder.MemoUser',
        on_delete=models.CASCADE,
        related_name='owned_posts',
        verbose_name='کاربر'
    )

    title = models.CharField(
        max_length=60,
        verbose_name='عنوان'
    )

    text = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='متن'
    )

    tagged_people = models.ManyToManyField(
        to='memoreminder.MemoUser',
        related_name='post_where_tagged',
        null=True,
        blank=True,
        verbose_name='افراد تگ شده در خاطره'
    )

    tags = models.ManyToManyField(
        to='memoreminder.Tag',
        null=True,
        blank=True,
        verbose_name='تگ ها'
    )

    lat = models.FloatField(
        null=True,
        blank=True,
        verbose_name='عرض جغرافیایی'
    )

    lon = models.FloatField(
        null=True,
        blank=True,
        verbose_name='طول جغرافیایی'
    )

    mode = models.CharField(
        max_length=50,
        default=MODE_PUBLIC,
        choices=MODES,
        verbose_name='حالت'
    )

    def __str__(self):
        return f'{self.id}-{self.creator_user}-{self.title}'

    class Meta:
        verbose_name = 'خاطره'
        verbose_name_plural = "خاطره ها"
