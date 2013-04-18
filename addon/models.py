from django.db import models
from addon.fields import JSONField
from django.template.defaultfilters import slugify


class Addon(models.Model):
    name = models.CharField(max_length=30, unique=True)
    config_vars = JSONField(default='', blank=True, null=True)
    slug = models.SlugField(max_length=30, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ("addon:detail", (), {"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Addon, self).save(*args, **kwargs)
