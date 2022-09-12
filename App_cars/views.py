from django.db.models import Q
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from App_Subscription.models import Membership
from App_cars.forms import BlogModelForm, ReviewForm
from App_cars.models import CarModel, BlogModel, Review
from App_login.models import Profile


def home(request):
    cars = CarModel.objects.filter(selling_status=False).order_by('-created_date')[:6]
    blogs = BlogModel.objects.all().order_by('-created_date')[:3]
    content = {
        'cars': cars,
        'blogs': blogs
    }
    return render(request, "App_cars/home.html", context=content)


def services(request):
    return render(request, 'services.html')


def car_store(request):
    cars = CarModel.objects.filter(selling_status=False)
    content = {
        'cars': cars,
    }
    return render(request, 'App_cars/car-store.html', context=content)


def car_search(request):
    car_list = []
    all_cars = CarModel.objects.filter(selling_status=False)
    car_highest_price = max([float(x.selling_price[:-3]) for x in all_cars])
    highest_usages = 5
    if request.method == 'GET':
        usage_period = request.GET.get('usage-period')
        if int(usage_period) == 0:
            usage_period = highest_usages
        fuel = request.GET.get('fuel-type')
        year = request.GET.get('year')
        engine = request.GET.get('engine-model')
        price_range = request.GET.get('price-range')
        mileage = request.GET.get('mileage')
        doors = request.GET.get('doors')
        number_of_seats = request.GET.get('number-of-seats')
        cars = CarModel.objects.filter(
            Q(usage_period__icontains=usage_period) | Q(fuel_type__icontains=fuel) | Q(year__icontains=year) |
            Q(engine__icontains=engine) | Q(mileage__icontains=mileage) | Q(description__icontains=doors) |
            Q(description__icontains=number_of_seats)
        )
        for i in cars:
            selling_price = float(i.selling_price[:-3])
            price_range = float(price_range)
            if price_range > 40.00:
                price_range = car_highest_price
            if selling_price < price_range:
                car_list.append(i)
    content = {
        'cars': car_list
    }
    return render(request, 'App_cars/car-search.html', context=content)


def car_details(request, pk):
    car = CarModel.objects.get(id=pk)
    try:
        membership = Membership.objects.get(member=request.user)
    except:
        membership = None

    owner = car.owner
    seller_profile = Profile.objects.get(user=owner)
    content = {
        'car': car,
        'membership': membership,
        'seller_profile': seller_profile,
    }
    return render(request, 'App_cars/car_details.html', context=content)


def blog_views(request):
    blogs = BlogModel.objects.all()
    form = BlogModelForm()
    content = {
        'form': form,
        'blogs': blogs,
    }
    if request.method == 'POST' and 'blog-post' in request.POST:
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            this_blog = form.save(commit=False)
            this_blog.writer = request.user
            this_blog.save()
            return HttpResponseRedirect(reverse('App_cars:blog'))

    if request.method == 'POST' and 'search-btn' in request.POST:
        search_content = request.POST.get('search-content')
        print(f"search content: {search_content}")
        searched_blog = BlogModel.objects.filter(
            Q(writer__username__icontains=search_content) | Q(blog__icontains=search_content) | Q(
                title__icontains=search_content))
        content['search_blog'] = searched_blog

    return render(request, 'App_cars/blog.html', context=content)


def blog_details(request, pk):
    blog = BlogModel.objects.get(id=pk)
    content = {
        'blog': blog,
    }
    return render(request, 'App_cars/blog_details.html', context=content)


def review(request):
    reviews = Review.objects.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            this_form = form.save(commit=False)
            this_form.buyer = request.user
            this_form.save()
            return HttpResponseRedirect(reverse('App_cars:reviews'))
    content = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'App_cars/reviews.html', context=content)


def checkviewFalse(request):
    if request.method == 'GET':
        room_name = request.GET.get('room_name')
        username = request.GET.get('username')
        seller = request.GET.get('seller_name')
        print(room_name)
        print(seller)
        print(username)
        return redirect('App_cars:car-store')
