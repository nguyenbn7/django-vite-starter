import os

from django import template
from django.conf import settings
from django.templatetags.static import static as django_static

register = template.Library()


@register.simple_tag
def static(path: str):
    """
    A wrapper of django's static tag. Use vite dev server url to get static real time
    """
    if not path:
        raise Exception("file name can not be empty")

    if settings.DEBUG:
        if not settings.VITE_DEV_URL:
            raise Exception("Can not find 'VITE_DEV_URL' in settings")

        if not isinstance(settings.VITE_DEV_URL, str):
            raise Exception("'VITE_DEV_URL' should be a string")

        if path[0] == "/":
            path = path[1:]

        if settings.VITE_DEV_URL[-1] != "/":
            return f"{settings.VITE_DEV_URL}/{path}"

        return f"{settings.VITE_DEV_URL}{path}"

    return django_static(path)


@register.simple_tag
def vite_dev_url():
    if settings.VITE_DEV_URL[-1] != "/":
        return f"{settings.VITE_DEV_URL}/"

    return settings.VITE_DEV_URL
