from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=150, default='No bio mentioned')

class board(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=200)

class checklist(models.Model):
    board = models.ForeignKey(board, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)

class card(models.Model):
    checklist = models.ForeignKey(checklist, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField
    