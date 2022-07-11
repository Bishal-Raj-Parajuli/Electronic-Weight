from django.urls import path
from app import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.log_in, name='login' ),
    path('logout', views.log_out, name='logout' ),
    path('dashboard/list', views.dashboardList, name='dashboard_list'),
    path('dashboard/create', views.dashboardCreate, name='dashboard_create'),
    path('v-type/list', views.vehicleList, name='v_type_list'),
    path('v-type/create', views.vehicleCreate, name='v_type_create'),
    path('v-charge/list', views.vehicleChargeList, name='v_charge_list'),
    path('v-charge/create', views.vehicleChargeCreate, name='v_charge_create'),
    path('invoice/<int:pk>', views.invoice, name='invoice'),

]