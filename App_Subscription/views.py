from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from sslcommerz_python.payment import SSLCSession

from App_Subscription.models import Membership
from App_login.models import Profile
from App_Subscription.forms import MembershipForm
from datetime import datetime


# Create your views here.
@login_required
def checkout(request):
    Ismember = False
    try:
        membership = Membership.objects.get(member=request.user)
        if membership.memberShip:
            Ismember = True
        else:
            Ismember = False
    except:
        membership = None
    profileFullFilled = False
    try:
        profile = Profile.objects.get(user=request.user)
        if profile.is_fully_filled():
            profileFullFilled = True
        else:
            profileFullFilled = False
    except:
        profile = None
    form = MembershipForm(instance=membership)
    if request.method == 'POST':
        form = MembershipForm(data=request.POST, instance=membership)
        if form.is_valid():
            this_form = form.save(commit=False)
            this_form.member = request.user
            period = int(form.cleaned_data.get('membership_period'))
            now_time = datetime.today()
            day = now_time.day
            month = now_time.month
            year = now_time.year
            if period == 12:
                year += 1
                cost = 10000
            elif period == 36:
                year += 3
                cost = 20000
            else:
                month += 1
                cost = 5000
                if month > 12:
                    month = 1
                    year += 1
            end_period = datetime(day=day, month=month, year=year)
            this_form.end_membership = end_period
            this_form.membership_cost = cost
            this_form.save()
            return HttpResponseRedirect(reverse('App_Subscription:checkout'))

    content = {
        'form': form,
        'membership': membership,
        'profile': profile,
        'profileFullFilled': profileFullFilled,
        'Ismember': Ismember,
    }
    return render(request, 'App_Subscription/checkout_page.html', context=content)


@csrf_exempt
def payment(request):
    profile = Profile.objects.get(user=request.user)
    membership = Membership.objects.get(member=request.user, memberShip=False)
    print(membership)
    fees = membership.membership_cost

    if not profile.is_fully_filled():
        messages.info(request, "Please complete your profile details.")
        return redirect('App_Login:profile')

    status_url = request.build_absolute_uri(reverse('App_Subscription:payment-completed'))
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='mamon5eda079f699bb',
                            sslc_store_pass='mamon5eda079f699bb@ssl')
    mypayment.set_urls(success_url=status_url, fail_url=status_url,
                       cancel_url=status_url, ipn_url=status_url)
    mypayment.set_product_integration(total_amount=Decimal(fees), currency='BDT',
                                      product_category='Subscription',
                                      product_name='Subscription Fees', num_of_item=1,
                                      shipping_method='No Shipping', product_profile='None')

    current_user = request.user
    address_1 = f"{profile.House}, {profile.city}, {profile.zipcode}, {profile.country}"
    mypayment.set_customer_info(name=profile.full_name, email=current_user.email,
                                address1=address_1,
                                address2=address_1, city=profile.city,
                                postcode=profile.zipcode, country=profile.country,
                                phone=profile.mobile_phone)

    mypayment.set_shipping_info(shipping_to=profile.full_name, address=address_1,
                                city=profile.city, postcode=profile.zipcode,
                                country=profile.country)
    response_data = mypayment.init_payment()
    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def completed_payment(request):
    if request.method == 'POST':
        payment_data = request.POST
        print(payment_data)
        status = payment_data['status']
        if status == 'VALID':
            return HttpResponseRedirect(reverse('App_Subscription:purchased'))
    return render(request, 'App_Subscription/payment_completed.html')


@login_required
def purchased_(request):
    membership = Membership.objects.get(member=request.user, memberShip=False)
    membership.memberShip = True
    membership.save()
    return redirect('App_cars:home')
