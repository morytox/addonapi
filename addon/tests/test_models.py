from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.test import TestCase
from ..models import Addon


class AddonTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')

    def create_addon(self, name='ELEPHANTSQL'):
        return Addon.objects.create(
            name=name,
            config_vars=''
        )

    def test_model_creation(self):
        addon = self.create_addon()
        self.assertTrue(isinstance(addon, Addon))
        self.assertEqual(addon.__unicode__(), addon.name)

    def test_model_url(self):
        addon = self.create_addon()
        self.assertEqual(
            addon.get_absolute_url(),
            reverse('addon:detail', kwargs={'slug': addon.slug}))

    def test_custom_slug(self):
        addon = Addon.objects.create(
            name='specialaddon',
            slug='randomaddon'
        )
        self.assertNotEqual(addon.slug, slugify(addon.name))
        self.assertEqual(addon.slug, 'randomaddon')
