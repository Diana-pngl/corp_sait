from django.contrib import admin 
from corp_sait import models
admin.site.register([models.Event,models.Team,models.User,models.Employee])