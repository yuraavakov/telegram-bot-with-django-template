from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='User ID in the messenger',
        unique=True
    )
    name = models.TextField(
        verbose_name='User name in the messenger'
    )

    def __str__(self):
        return f'#{self.external_id} {self.name}'

    class Meta:
        verbose_name = 'Profile'


class Message(models.Model):
    profile = models.ForeignKey(
        to='adminpanel.Profile',
        verbose_name='Sender profile',
        on_delete=models.PROTECT
    )
    text = models.TextField(
        verbose_name='Message text'
    )
    created_date = models.DateTimeField(
        verbose_name='Date and time of creation',
        auto_now_add=True
    )

    def __str__(self):
        return f'Message ({self.pk}) from "{self.profile.name}"'

    class Meta:
        verbose_name = 'Message'
