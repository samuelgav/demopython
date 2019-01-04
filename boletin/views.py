# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import RegForm, RegModelForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo = "HOLA"
	if request.user.is_authenticated():
		titulo = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)

	context = {
				"titulo": titulo,
				"el_form": form,
			}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "PERSONA"
		instance.save()
			
		context = {
			"titulo": "Gracias %s!" %(nombre)		
		}

		if not nombre:
			context = {
				"titulo": "Gracias %s!" %(email)
			}

		print instance
		print instance.timestamp
		#form_data = form.cleaned_data
		#abc = form_data.get("email")	
		#abc2 = form_data.get("nombre")
		#obj = Registrado.objects.create(email=abc, nombre=abc2)

	
	return render(request, "inicio.html", context)