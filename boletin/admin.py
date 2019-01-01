# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp"]
	form = RegModelForm
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	list_fields = ["email", "nombre"]
	#class Meta:
	#	model = Registrado
		

admin.site.register(Registrado, AdminRegistrado)