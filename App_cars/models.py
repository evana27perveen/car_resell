from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models


# Create your models here.


def image_compressor(image):
    img = Image.open(image)
    img.save(image, quality=60, optimize=True)
    return img


usage_time_choice = (
    ('1 Year', "1 year"),
    ('2 Year', "2 year"),
    ('3 Year', "3 year"),
    ('4 Year', "4 year"),
    ('5 Year', "5 year"),
    ('More than 5 Year', "More than 5 year"),
)


class CarModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='car_owner')
    title = models.CharField(max_length=200, verbose_name='brand+model+year')
    year = models.CharField(max_length=20)
    mileage = models.CharField(max_length=50)
    buying_price = models.CharField(max_length=20)
    selling_price = models.CharField(max_length=20)
    usage_period = models.CharField(max_length=20, choices=usage_time_choice)
    exterior_colour = models.CharField(max_length=200)
    interior_colour = models.CharField(max_length=200)
    kmpl = models.CharField(max_length=200, verbose_name='kilometer per liter')
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=200, verbose_name='Automatic / Manual')
    engine = models.CharField(max_length=100)
    VIN = models.CharField(max_length=100, verbose_name='Vehicle Identification Number')
    convenience = models.CharField(max_length=200)
    entertainment = models.CharField(max_length=200)
    safety = models.CharField(max_length=200)
    selling_status = models.BooleanField(default=False)
    description = models.TextField()
    front_image = models.ImageField(upload_to='car_image/')
    back_image = models.ImageField(upload_to='car_image/')
    left_side_image = models.ImageField(upload_to='car_image/')
    right_side_image = models.ImageField(upload_to='car_image/')
    engine_image = models.ImageField(upload_to='car_image/')
    interior_image1 = models.ImageField(upload_to='car_image/')
    interior_image2 = models.ImageField(upload_to='car_image/')
    interior_image3 = models.ImageField(upload_to='car_image/')
    interior_image4 = models.ImageField(upload_to='car_image/')
    image1 = models.ImageField(upload_to='car_image/', verbose_name="Optional image", blank=True, null=True)
    image2 = models.ImageField(upload_to='car_image/', verbose_name="Optional image", blank=True, null=True)
    license_image = models.ImageField(upload_to='car_image/', verbose_name='car license')
    buying_document_image = models.ImageField(upload_to='car_image/', verbose_name='Car buying document')
    Car_video = models.FileField(upload_to="car_video/")
    created_date = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     front_image_ = image_compressor(self.front_image)
    #     self.front_image = front_image_
    #     back_image_ = image_compressor(self.back_image)
    #     self.back_image = back_image_
    #     left_side_image_ = image_compressor(self.left_side_image)
    #     self.left_side_image = left_side_image_
    #     right_side_image_ = image_compressor(self.right_side_image)
    #     self.right_side_image = right_side_image_
    #     engine_image_ = image_compressor(self.engine_image)
    #     self.engine_image = engine_image_
    #     interior_image1_ = image_compressor(self.interior_image1)
    #     self.interior_image1 = interior_image1_
    #     interior_image2_ = image_compressor(self.interior_image2)
    #     self.interior_image2 = interior_image2_
    #     interior_image3_ = image_compressor(self.interior_image3)
    #     self.interior_image3 = interior_image3_
    #     interior_image4_ = image_compressor(self.interior_image4)
    #     self.interior_image4 = interior_image4_
    #     if self.image1:
    #         image1_ = image_compressor(self.image1)
    #         self.image1 = image1_
    #     if self.image2:
    #         image2_ = image_compressor(self.image2)
    #         self.image2 = image2_
    #     license_image_ = image_compressor(self.license_image)
    #     self.license_image = license_image_
    #     buying_document_image_ = image_compressor(self.buying_document_image)
    #     self.buying_document_image = buying_document_image_
    #     return super(CarModel, self).save(*args, **kwargs)


class BlogModel(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_writer")
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='car_blog_images/')
    blog = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Review(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='car_buyer')
    car = models.CharField(max_length=100)
    car_image = models.ImageField(upload_to='reviewed_images')
    review = models.TextField()
