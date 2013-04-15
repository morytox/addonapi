#!/usr/bin/env python
# −*− coding: UTF−8 −*−
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^addon\.fields\.JSONField"])

class JSONField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        """Convert our string value to JSON after we load it from the DB"""

        if value == "":
            return None

        try:
            if isinstance(value, basestring):
                return json.loads(value)
        except ValueError:
            pass

        return value

    def get_db_prep_save(self, value, **kwargs):
        """Convert our JSON object to a string before we save"""

        if value == "":
            return None

        if isinstance(value, (dict, list)):
            value = json.dumps(value, cls=DjangoJSONEncoder)

        return super(JSONField, self).get_db_prep_save(value, **kwargs)
