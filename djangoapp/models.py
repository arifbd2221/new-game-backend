from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    profile_pic_id = models.PositiveSmallIntegerField(default=1)
    
    class Meta:
        unique_together = ['email', 'phone']


class GameScore(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    score = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
