from django.contrib import admin
from app.models import Company, VehicleCharge, VehicleType, WeightTransaction
# Register your models here.

admin.site.register([Company, VehicleType, VehicleCharge, WeightTransaction ])
