from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Index, Car, Order, OrderedCar, Contact
from .form import OrderForm


def index(request):
    index = Index.objects.order_by('-id')
    return render(request, 'index.html', {
      'index': index
    })


def cars(request):
    cars = Car.objects.order_by('id')
    return render(request, 'cars.html', {
        'cars': cars
    })

def oldest_cars(request):
    cars = Car.objects.order_by('rok')
    return render(request, 'cars.html', {
        'cars': cars
    })

def newest_cars(request):
    cars = Car.objects.order_by('-rok')
    return render(request, 'cars.html', {
        'cars': cars
    })

def riding_cars(request):
    cars = Car.objects.filter(stan='Jeżdzący')
    return render(request, 'cars.html', {
        'cars': cars
    })

def staying_cars(request):
    cars = Car.objects.filter(stan='Stojący')
    return render(request, 'cars.html', {
        'cars': cars
    })

def driver_cars(request):
    cars = Car.objects.filter(stan='Z kierowcą')
    return render(request, 'cars.html', {
        'cars': cars
    })

def contact(request):
    contacts = Contact.objects.order_by('id')
    return render(request, 'contact.html', {'contacts': contacts})


def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, "car_details.html", {
        'car': car
    })


def cart(request):
    cars = _get_products_in_cart(request)
    return render(request, "cart.html", {"cars": cars})


def _get_products_in_cart(request):
    selected_cars = []
    for item_id in request.session.get('zamawiane', []):
        car = Car.objects.get(pk=item_id)
        selected_cars.append(car)

    return selected_cars


def add_to_cart(request):
    if request.method == "POST":
        if 'zamawiane' not in request.session:
            request.session['zamawiane'] = []
        item_id = request.POST['item_id']
        if item_id not in request.session['zamawiane']:
            request.session['zamawiane'].append(item_id)
            request.session.modified = True

    return HttpResponseRedirect('/zamawiane')


def remove_from_cart(request):
    if 'zamawiane' in request.session:
        item_id = request.POST['item_id']
        # index = request.POST.index(item_id)
        # del request.session['zamawiane'][index]
        request.session['zamawiane'].remove(item_id)
        request.session.modified = True

    return HttpResponseRedirect('/zamawiane')

def clean_card(request):
    request.session['zamawiane'] = []    # Czyscimy koszyk
    return HttpResponseRedirect('/zamawiane')

def order(request):
    cars_to_order = _get_products_in_cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                name=form.cleaned_data['name'],
                lastName=form.cleaned_data['lastName'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
            )
            order.save()
            for car in cars_to_order:
                OrderedCar(
                    car=car, order=order
                ).save()
            request.session['zamawiane'] = []
            return HttpResponseRedirect('/order/'+str(order.id))
        else:
            form = OrderForm()
        return render(request, 'order_form.html', {"form": form, "cars": cars_to_order})


def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    ordered_car = OrderedCar.objects.filter(id=order_id)
    context = {"order": order, "ordered_cars": ordered_car}
    return render(request, "order_details.html", context)




 
