# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from webshop.checkout.models import BaseOrderInfo


class UserProfile(BaseOrderInfo):
    """Профиль пользователя"""
    user = models.ForeignKey(User, unique=True)
    icon = models.FileField(_(u'Image'), upload_to='accounts/images/',
                             help_text=u'Фото', blank=True , default="accounts/images/default.jpg")

    def __unicode__(self):
        return _(u'Профиль: ') + self.user.username

    class Meta:
        verbose_name_plural = _(u'Профили пользователей')
