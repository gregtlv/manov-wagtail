from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page

from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class HomePage(Page):
    text = models.CharField(max_length=250, default='Inro text')

    description = models.TextField()

    btn_name = models.CharField(max_length=250, default='')

    Center_Message_header = models.CharField(max_length=250, default='')

    Center_Message_description = models.TextField()

    Footer_header = models.CharField(max_length=250, default='')

    contact_us = models.CharField(max_length=250, default='')

    contact_us_text = models.TextField()

    more_information = models.CharField(max_length=250, default='')

    more_information_text = models.TextField()

    footer_text = models.CharField(max_length=250, default='')

    search_fields = Page.search_fields + [
        index.SearchField('text'),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('text'),
        FieldPanel('description'),
        FieldPanel('btn_name'),
        FieldPanel('Center_Message_header'),
        FieldPanel('Center_Message_description'),
        FieldPanel('Footer_header'),
        FieldPanel('contact_us'),
        FieldPanel('contact_us_text'),
        FieldPanel('more_information'),
        FieldPanel('more_information_text'),
        FieldPanel('footer_text'),

    ]
