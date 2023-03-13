from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Reply)
admin.site.register(Review)
admin.site.register(Avatar)