# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'webshop.catalog.views',
    url(r'^$', 'index_view',
        {'template_name': 'catalog/index.html'},
        name='catalog_home'),

    url(r'^category/(?P<category_slug>[-\w]+)/$', 'category_view',
        {'template_name': 'catalog/category.html'},
        name='catalog_category'),

    url(r'^product/(?P<product_slug>[-\w]+)/$', 'product_view',
        {'template_name': 'catalog/product.html'},
        name='catalog_product'),

    url(r'^sale/', 'sale_view',
        {'template_name': 'catalog/sale.html', 'type': 'sale'},
        name='catalog_product'),

    url(r'^novelty/', 'sale_view',
        {'template_name': 'catalog/sale.html', 'type': 'novelty'},
        name='catalog_product'),
)

urlpatterns += patterns(
    'webshop.ajaxcore.views',
    url(r'^ajax-cart/', 'ajaxCart',
        name='ajaxCart'),
    url(r'^ajax-delivery/', 'ajaxDelivery',
        name='ajaxDelivery'),
)
