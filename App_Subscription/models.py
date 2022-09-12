from django.contrib.auth.models import User
from django.db import models

# Create your models here.
time_period = (
    ('1', '1 Month'),
    ('12', '12 Months'),
    ('36', '3 Years'),
)


class Membership(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, name="member")
    memberShip = models.BooleanField(default=False, blank=True, null=True)
    membership_period = models.CharField(max_length=100, choices=time_period)
    membership_cost = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    end_membership = models.DateField()

    def __str__(self):
        if self.memberShip:
            return f"{self.member}'s Membership is valid for {self.membership_period}"
        else:
            return f"{self.member}'s Membership is not valid"
