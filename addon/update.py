from .models import Addon
import os
import json


def updateAddonCredentials(data=None):
    addons = Addon.objects.all()

    for addon in addons:
        name = addon.name
        if addon.config_vars != data[addon.name.upper()]:
            addon.config_vars = data[addon.name.upper()]
        addon.save()


def updateAddons():
    cred_file = open(os.environ["CRED_FILE"])
    data = json.load(cred_file)
    for addon in data:
        if not Addon.objects.filter(name=addon):
            Addon.objects.create(name=addon)
    for addon in Addon.objects.all():
        notexisting = True
        for a in data:
            if addon.name == a:
                notexisting = False
        if notexisting:
            addon.delete()
    updateAddonCredentials(data)

updateAddons()
