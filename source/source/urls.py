from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'techarena.views.home', name='home'),
    url(r'^contact/$','techarena.views.contact', name='contact'),
    url(r'^mobiles/$','techarena.views.mobiles', name='mobiles'),
    url(r'^laptops/$','techarena.views.laptops', name='laptops'),
    url(r'^/games$','techarena.views.gaming', name='gaming'),
    url(r'^about/$','source.views.about', name='about'),
    url(r'^/apple$','techarena.views.apple', name='apple'),
    url(r'^tomclansy/$','techarena.views.tomclansy', name='tomclansy'),
    url(r'^witcher/$','techarena.views.witcher', name='witcher'),
    url(r'^sniper/$','techarena.views.sniper', name='sniper'),
    url(r'^forhonor/$','techarena.views.forhonor', name='forhonor'),
    url(r'^zero/$','techarena.views.zero', name='zero'),
    url(r'^mirror/$','techarena.views.mirror', name='mirror'),
    url(r'^dead/$','techarena.views.dead', name='dead'),
    url(r'^king/$','techarena.views.king', name='king'),
    url(r'^mafia/$','techarena.views.mafia', name='mafia'),






    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)