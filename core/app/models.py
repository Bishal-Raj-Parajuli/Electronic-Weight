from turtle import update
from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class VehicleType(models.Model):
    v_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.v_type

class VehicleCharge(models.Model):
    v_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    charge  = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.v_type)

class WeightTransaction(models.Model):
    slip_no = models.BigAutoField(primary_key=True)
    chalan_no = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=100)
    material = models.CharField(max_length=255)
    Vehicle_Type = models.CharField(max_length=100)
    charge = models.PositiveIntegerField()
    gross_weight = models.PositiveIntegerField()
    tare_weight = models.PositiveIntegerField()
    net_weight = models.PositiveIntegerField()
    total_amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.chalan_no)

    
