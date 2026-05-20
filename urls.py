from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/customers/", include("apps.customers.urls")),
    path("api/radios/", include("apps.radios.urls")),
    path("api/rentals/", include("apps.rentals.urls")),
    path("api/payments/", include("apps.payments.urls")),
]