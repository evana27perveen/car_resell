from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.
phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_(
    "Enter a valid international mobile phone number starting with +(country code)"))


def compress_image(image):
    img = Image.open(image)
    img_io = BytesIO()
    img.save(img_io, 'JPEG', quality=60)
    new_img = File(img_io, name=image.name)
    return new_img


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=264, blank=True, null=True)
    full_name = models.CharField(max_length=264, blank=True, null=True)
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True,
                                    null=True)
    country = models.CharField(max_length=20)
    House = models.TextField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.username + "'s Profile"

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        profile_picture = Image.open(self.profile_picture.path)
        if profile_picture.height > 300 or profile_picture.width > 300:
            profile_picture.thumbnail((300, 250))
            profile_picture.save(self.profile_picture.path)


class ContactModel(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.full_name + "has sent you a message."
