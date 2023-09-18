from django.urls import path

from .views.check_uploaded_medications import CheckUploadedMedications
from .views.drone import DroneView
from .views.drone_register import DroneRegisterView
from .views.medication_register import MedicationRegisterView
from .views.loaded_medications_on_drone import LoadedMedicationsOnDroneView
from .views.check_battery import CheckBatteryView
from .views.checking_stats import CheckingStateView
from .views.clean_card_items import CleanCardItemsView
from .views.upload_medications import UploadMedicationsView

app_name = 'API'

urlpatterns = [
    path('drone/list/', DroneView.as_view(), name='drone list'),
    path('drone/register/', DroneRegisterView.as_view(), name='drone register'),
    path('medication/register/', MedicationRegisterView.as_view(), name='medication register'),
    path('drone/loaded_medications/<str:serial_number>/', LoadedMedicationsOnDroneView.as_view(),
         name='medication register'),
    path('drone/check_battery/<str:serial_number>/', CheckBatteryView.as_view(), name='battery capacity'),
    path('drone/check_stats/', CheckingStateView.as_view(), name='checking state'),
    path('drone/clean_card_items/<str:serial_number>/', CleanCardItemsView.as_view(), name='clean card items'),
    path('drone/upload_medications/', UploadMedicationsView.as_view(), name='upload medication'),
    path('drone/check_uploaded_medications/<str:serial_number>/<int:medication_id>/', CheckUploadedMedications.as_view(), name='check uploaded medications')
]
