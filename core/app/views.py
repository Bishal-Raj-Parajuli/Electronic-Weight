from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from app import models
import xlwt
# Create your views here.

def log_in(request):
    if request.method == "GET":
        comp = get_object_or_404(models.Company, id=1)
        if request.user.is_authenticated:
            return redirect('/dashboard/list')
        else:
            return render(request, 'login.html',{'company':comp})

    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/list')
        else:
            message = "Sorry Your Credentials Doesn't Match !!!"
            comp = get_object_or_404(models.Company, id=1)
            return render(request, 'login.html', {'message':message,'company':comp})

@login_required
def log_out(request):
    logout(request)
    return redirect('/')

@login_required
def dashboardList(request):
    objects = models.WeightTransaction.objects.all().order_by('-slip_no')
    paginator = Paginator(objects, 10)
    page_number = request.GET.get('page')
    object = paginator.get_page(page_number)
    return render(request, 'app/weight_transaction_list.html', {'object_list':object})


@login_required
def dashboardCreate(request):
    if request.method == 'GET':
        v_type = models.VehicleCharge.objects.all()
        return render(request, 'app/dashboard.html', {'v_type':v_type})
    elif request.method == 'POST':
        vechicle_type = request.POST['v_type']
        vt_name = get_object_or_404(models.VehicleType, id=vechicle_type)
        tran = models.WeightTransaction(
            chalan_no = str(request.POST['c_no']),
            vehicle_no = str(request.POST['v_number']),
            material = str(request.POST['material']),
            Vehicle_Type = str(vt_name.v_type),
            charge = int(request.POST['charge']),
            gross_weight = int(request.POST['g_weight']),
            tare_weight = int(request.POST['t_weight']),
            net_weight = int(request.POST['n_weight']),
            total_amount = int(request.POST['t_amount']),
        )
        tran.save()
        object = get_object_or_404(models.WeightTransaction, slip_no=tran.slip_no)
        return redirect(f'/invoice/{object.slip_no}')

def vehicleList(request):
    objects = models.VehicleType.objects.all()
    paginator = Paginator(objects, 10)
    page_number = request.GET.get('page')
    object = paginator.get_page(page_number)
    return render(request, 'app/vehicle_type_list.html', {'object_list':object})

def vehicleCreate(request):
    if request.method == 'GET':
        return render(request, 'app/vehicle_type_create.html')
    elif request.method == 'POST':
        obj = models.VehicleType(
            v_type = request.POST['v_name']
        )
        obj.save()
        return redirect('/v-type/list')

def vehicleChargeList(request):
    objects = models.VehicleCharge.objects.all()
    paginator = Paginator(objects, 10)
    page_number = request.GET.get('page')
    object = paginator.get_page(page_number)
    return render(request, 'app/vehicle_charge_list.html', {'object_list':object})

def vehicleChargeCreate(request):
    if request.method == 'GET':
        v_type = models.VehicleType.objects.all()
        return render(request, 'app/vehicle_charge_create.html', {'v_type':v_type})
    elif request.method == 'POST':
        print(request.POST['v_name'])
        obj = models.VehicleCharge(
            v_type = get_object_or_404(models.VehicleType, id=int(request.POST['v_name'])),
            charge = int(request.POST['charge'])
        )
        obj.save()
        return redirect('/v-charge/list')

@login_required
def invoice(request, pk):
    comp = get_object_or_404(models.Company, id=1)
    object = get_object_or_404(models.WeightTransaction, slip_no=pk)
    return render(request, 'app/invoice.html', {'object':object, 'company':comp})



