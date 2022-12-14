from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from Restaurant.models import Restaurant

# Create your models here.
class User(AbstractUser):
    # description = models.TextField(blank=True)
    # nickname = models.CharField(max_length=40, blank=True)
    # image = ProcessedImageField(
    #     upload_to="images/",
    #     blank=True,
    #     processors=[Thumbnail(200, 200)],
    #     format="JPEG",
    #     options={"quality": 80},
    # )

    hp = models.IntegerField(verbose_name="핸드폰번호", null=True)
    email = models.EmailField(max_length=128, verbose_name="이메일", null=True)
    user_wishlist = models.ManyToManyField(Restaurant, related_name="user_wishlist")
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 200)],
        format="PNG",
        options={"quality": 50},
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"


# class Profile(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     image = ProcessedImageField(
#         blank=True,
#         processors=[Thumbnail(200, 200)],
#         format="JPEG",
#         options={"quality": 50},
#     )

# class Wishlist(models.Model):
#     user_id    = models.ForeignKey(User, on_delete = models.CASCADE)
#     restaurant_id = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
