from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=50)
    participants = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return self.name


class List(models.Model):
    title = models.CharField(max_length=40)
    board = models.ForeignKey(Board)

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

