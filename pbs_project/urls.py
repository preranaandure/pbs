from django.conf.urls import include
from django.urls import re_path, path
from django.contrib import admin

"""
some import statmement will load some module (directly or indirectly)
and that module maybe include some statement "reverse('djdt:render_panel')" which will access the urlpattern of this module,
but urlpatterns are populated after import statement, so this cause famous exception "ImproperlyConfigured: The included urlconf pbs_project.urls doesn't have any patterns in it"

Solution is using two steps to populate urlpatterns
1. just populate the very basic url patterns, that will make property 'urlpatterns' always avaiable
2. populate others.

"""
# urlpatterns = ['',
#     (r'^docs/', include('django.contrib.admindocs.urls')),
#     (r'^', include('django.contrib.auth.urls'))
# ]
urlpatterns = [
    re_path(r'^docs/', include('django.contrib.admindocs.urls')),
    re_path(r'^', include('django.contrib.auth.urls')),
]

from django.views.generic.base import RedirectView
from django_downloadview import ObjectDownloadView
from pbs.document.models import Document
from pbs.sites import site
from pbs.forms import PbsPasswordResetForm

from tastypie.api import Api
from pbs.review.api import PrescribedBurnResource
from django.contrib.auth.views import PasswordResetView

handler500 = 'pbs.views.handler500'
# Define the simplest possible view for Document uploads.
document_download = ObjectDownloadView.as_view(model=Document, file_field='document')
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

v1_api = Api(api_name='v1')
v1_api.register(PrescribedBurnResource())

urlpatterns = urlpatterns + [
    # '',
    #path('admin/', admin.site.urls),
    #re_path(r'^', include(site.urls)),
    # re_path("", site.urls),
    # (r'^', include('pbs.registration.urls')),
    re_path(r'^', include('pbs.registration.urls')),

    # the password reset must come before site.urls, site.urls match all
    #re_path(r'^', include((site.urls, 'site'), namespace='site')),
    #re_path(r'^',include((site.urls, 'site'), namespace='admin')),
    #re_path(r'^', include(site.urls)),
    #re_path(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
    #     {'password_reset_form': PbsPasswordResetForm}, name='password_reset'),
    re_path(r'^password_reset/$', PasswordResetView.as_view(form_class=PbsPasswordResetForm), name='password_reset'),
    re_path(r'^chaining/', include('smart_selects.urls')),
    re_path(r'^select2/', include("django_select2.urls")),
    re_path('^documents/(?P<pk>\d+)/download$', document_download, name='document_download'),
    re_path(r'^favicon\.ico$', favicon_view, name='favicon_view'),
    re_path(r'^api/', include(v1_api.urls)),
    #path('', site.urls),
    re_path(r'^', site.urls),
]
