from django.conf.urls.defaults import *
from plotnya_app.views import admin
from plotnya_app.views import add_photo
from plotnya_app.views import del_photo

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/delphoto/(\d+)', del_photo),
    (r'^admin/addphoto/', add_photo),
    (r'^admin/$', admin),
    
    # Example:
    # (r'^plotnya/', include('plotnya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
