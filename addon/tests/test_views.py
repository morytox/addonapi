from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.encoding import smart_unicode
import os
import json
from ..models import Addon


class AddonViewTests(TestCase):
    cred_file = open(os.environ["CRED_FILE"])
    data = json.load(cred_file)

    def setUp(self):
        self.user = User.objects.create(username='test')
        self.empty_addon = self.create_post(name='INDEXDEPOT')
        self.filled_addon = self.create_post(
            name='ELEPHANTSQL',
            config_vars=self.data['ELEPHANTSQL']
        )

    def create_post(self, name='NEW ADDON', config_vars=None):
        return Addon.objects.create(
            name=name,
            config_vars=config_vars
        )

    def test_list_view(self):
        url = reverse('addon:list')
        req = self.client.get(url)
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'addon/addon_list.html')
        self.assertIn(self.empty_addon.name, req.rendered_content)
        self.assertIn(self.filled_addon.name, req.rendered_content)
        self.assertIn(self.empty_addon.get_absolute_url(),
                      req.rendered_content)
        self.assertIn(self.filled_addon.get_absolute_url(),
                      req.rendered_content)

    def test_detail_view(self):
        url = reverse('addon:detail',
                      kwargs={'slug': self.empty_addon.slug})
        req = self.client.get(url)
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'addon/addon_detail.html')
        self.assertIn(self.empty_addon.name, req.rendered_content)
        self.assertIn(reverse('addon:list'), req.rendered_content)
        url = reverse('addon:detail',
                      kwargs={'slug': self.filled_addon.slug})
        req = self.client.get(url)
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'addon/addon_detail.html')
        self.assertIn(self.filled_addon.name, req.rendered_content)
        self.assertIn(
            self.filled_addon.config_vars['ELEPHANTSQL_URL'],
            req.rendered_content
        )
        self.assertIn(reverse('addon:list'), req.rendered_content)
