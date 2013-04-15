from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Addon
from .update import updateAddons
import os
import json


# cred_file = open(os.environ["CRED_FILE"])
# data = json.load(cred_file)
# addons = Addon.objects.all()

# for addon in addons:
# 	name = addon.name
# 	if addon.config_vars != data[addon.name.upper()]:
# 		addon.config_vars = data[addon.name.upper()]
# 	addon.save()

def Update(request):
	updateAddons()
	return redirect('/addons/')


class AddonListView(ListView):
	model = Addon


class AddonDetailView(DetailView):
	model = Addon

