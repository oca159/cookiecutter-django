from __future__ import absolute_import

from celery import shared_task

# http://docs.celeryproject.org/en/3.1/django/first-steps-with-django.html

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)