from App_Subscription.models import Membership
from django import forms


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['membership_period', ]
