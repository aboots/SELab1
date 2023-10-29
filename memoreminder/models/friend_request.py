from django.db import models

from .time_model import TimeModel


class FriendRequest(TimeModel):
    STATUS_ACCEPTED = 'accepted'
    STATUS_REJECTED = 'rejected'
    STATUS_PENDING = 'pending'
    STATUS_CH = (
        (STATUS_ACCEPTED, "تایید"),
        (STATUS_REJECTED, "رد"),
        (STATUS_PENDING, "در حال بررسی"),
    )

    from_user = models.ForeignKey(
        'memoreminder.MemoUser',
        on_delete=models.CASCADE,
        related_name='friend_request_sent',
        verbose_name='از کاربر'
    )

    to_user = models.ForeignKey(
        'memoreminder.MemoUser',
        on_delete=models.CASCADE,
        related_name='friend_request_received',
        verbose_name='به کاربر'
    )

    status = models.CharField(
        choices=STATUS_CH,
        default=STATUS_PENDING,
        max_length=50,
        verbose_name='وضعیت'
    )

    def __str__(self):
        return f'{self.from_user}-to-{self.to_user}'

    def save(self, *args, **kwargs):
        old_obj = FriendRequest.objects.filter(pk=self.pk).first()
        if old_obj and old_obj.status == self.STATUS_PENDING and self.status == self.STATUS_ACCEPTED:
            self.from_user.friends.add(self.to_user)
        return super(FriendRequest, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'درخواست دوستی'
        verbose_name_plural = "درخواست های دوستی"
