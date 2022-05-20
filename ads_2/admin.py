from django.contrib import admin

from ads_2.models import Category, Ad
from users.models import User, Location

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(User)
admin.site.register(Location)

