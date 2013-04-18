# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
# from django.template.defaultfilters import slugify
# from django.test import TestCase
# from addon.models import Addon


# class AddonApiTests(TestCase):

#     def setUp(self):
#         self.user = User.objects.create(username='test')

#     def create_addon(self, name='ELEPHANTSQL'):
#         return Addon.objects.create(
#             name=name,
#             config_vars=''
#         )

#     def test_model_url(self):
#         addon = self.create_addon()
#         self.assertEqual(
#             reverse('addon:detail', kwargs={'name': addon.name}))

#     def test_custom_slug(self):
#         addon = Addon.objects.create(
#             name='specialaddon',
#             slug='randomaddon'
#         )
#         self.assertNotEqual(addon.slug, slugify(addon.name))
#         self.assertEqual(addon.slug, 'randomaddon')
