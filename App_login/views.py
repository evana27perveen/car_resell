from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from App_cars.models import CarModel
from App_login.forms import ProfileForm, SignupForm, ProfileUpdateForm, ContactForm
from App_login.models import Profile, ContactModel


# Create your views here.
from chat.models import SellerMessages, Message, Room


def registrations_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:login'))
    content = {
        'form': form,
    }
    return render(request, 'App_login/signup.html', context=content)


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('App_cars:home'))
    content = {
        'form': form,
    }
    return render(request, 'App_login/login.html', context=content)


def logout_views(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_cars:home'))


def my_profile(request):
    try:
        message_requests = SellerMessages.objects.filter(seller_name=request.user)
    except:
        message_requests = None

    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = None
    if request.method == 'POST':
        car_title = request.POST.get('title')
        year = request.POST.get('year')
        mileage = request.POST.get('mileage')
        buying_price = request.POST.get('buying_price')
        asking_price = request.POST.get('selling_price')
        usage_period = request.POST.get('usage_period')
        exterior_color = request.POST.get('exterior_color')
        interior_color = request.POST.get('interior_color')
        kmpl = request.POST.get('kmpl')
        fuel_type = request.POST.get('fuel-type')
        transmission = request.POST.get('transmission')
        engine = request.POST.get('engine')
        vin = request.POST.get('vin')
        convenience = request.POST.get('convenience')
        entertainment = request.POST.get('entertainment')
        safety = request.POST.get('safety')
        description = request.POST.get('description')
        front_image = request.FILES.get('front-image')
        back_image = request.FILES.get('back-image')
        left_image = request.FILES.get('left-image')
        right_image = request.FILES.get('right-image')
        engine_image = request.FILES.get('engine-image')
        interior_image1 = request.FILES.get('interior-image1')
        interior_image2 = request.FILES.get('interior-image2')
        interior_image3 = request.FILES.get('interior-image3')
        interior_image4 = request.FILES.get('interior-image4')
        license_image = request.FILES.get('car-licence-image')
        buying_document_image = request.FILES.get('buying-document-image')
        car_video = request.FILES.get('car-video')
        try:
            op_image1 = request.FILES.get('op-image1')
        except:
            op_image1 = None
        try:
            op_image2 = request.FILES.get('op-image2')
        except:
            op_image2 = None

        new_car = CarModel(
            owner=request.user, title=car_title, year=year, mileage=mileage, buying_price=buying_price,
            selling_price=asking_price, usage_period=usage_period, exterior_colour=exterior_color,
            interior_colour=interior_color, kmpl=kmpl, fuel_type=fuel_type, transmission=transmission,
            engine=engine, VIN=vin, convenience=convenience, entertainment=entertainment, safety=safety,
            description=description, front_image=front_image, back_image=back_image, left_side_image=left_image,
            right_side_image=right_image, engine_image=engine_image, interior_image1=interior_image1,
            interior_image2=interior_image2, interior_image3=interior_image3, interior_image4=interior_image4,
            image1=op_image1, image2=op_image2, license_image=license_image,
            buying_document_image=buying_document_image, Car_video=car_video, selling_status=False
        )
        new_car.save()
        return HttpResponseRedirect(reverse('App_cars:car-store'))

    content = {
        'profile': profile,
        'message_requests': message_requests,
    }
    return render(request, 'App_login/my_profile.html', context=content)


def profile_settings(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = None

    form = ProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            this_form = form.save(commit=False)
            this_form.user = request.user
            this_form.save()
            return HttpResponseRedirect(reverse('App_login:my-profile'))

    content = {
        'form': form,
    }
    return render(request, 'App_login/profile_settings.html', context=content)


def contact_sys(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        sender = ContactModel(full_name=full_name, email=email, phone_number=phone_number, message=message)
        sender.save()
    return render(request, "App_login/contact.html")


def about_views(request):
    return render(request, 'App_login/about.html')


def my_chats(request):
    chats = Message.objects.filter(user=request.user)
    room = Room.objects.all()
    room_set = [x.name for x in room]
    chatRoom = []
    for i in chats:
        if i.room.name in room_set:
            chatRoom.append(i.room.name)
    chatRoom = list(set(chatRoom))
    content = {
        'chats': chatRoom
    }
    return render(request, 'chat/My_chats.html', context=content)
