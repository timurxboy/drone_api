from django.urls import path, include

API = [
    path('',
         include(
             (
                 'src.apps.API.urls',
                 'src.apps.API',
             ),
             namespace='API'
         ),
         ),
]

urlpatterns = API
