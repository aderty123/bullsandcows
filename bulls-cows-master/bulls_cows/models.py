from django.db import models
from django import forms

import uuid


class Player(models.Model):
    player_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    player_name = models.TextField(default="New Awesome User")


    # def player_id(self):
    #     return self.id.__str__()

    def __str__(self):
        """A string representation of the model."""
        return f"Player: {self.player_name}"    


class ScoreBoard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    won = models.BooleanField(default=False)
    secret_num = models.PositiveIntegerField()

    def __str__(self):
        """A string representation of the model."""
        return f"id: {self.user_id} secret: {self.secret_num} won: {self.won}"


class ScoreCard(models.Model):
    score_board = models.ForeignKey(ScoreBoard, on_delete=models.CASCADE)

    user_num = models.CharField(max_length=4)
    bulls = models.CharField(max_length=1)
    cows = models.CharField(max_length=1)

    def __str__(self):
        """A string representation of the model."""
        return f"user: {self.user_num} bulls: {self.bulls} cows: {self.cows}"
