# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.defaults import page_not_found, server_error

from lizard_htmlreport.views import index
from lizard_htmlreport.views import generate_rtf
from lizard_htmlreport.views import generate_pdf


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='htmlrapportage-index'),
    url(r'^generate/rtf/$', generate_rtf, name='htmlrapportage-generate-rtf'),
    url(r'^generate/pdf/$', generate_pdf, name='htmlrapportage-generate-pdf'),
    )


if settings.DEBUG:
    # Add this also to the projects that use this application
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )


def handler500(request):
    """
    500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('500.html') # You need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))