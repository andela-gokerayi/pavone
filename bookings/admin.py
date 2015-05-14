from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from bookings.models import Booking

# Register your models here.
AdminSite.site_header = "Pavone Events"

admin.site.register(Booking)

# Register your models here.
