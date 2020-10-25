from django_request_mapping import UrlPattern

from web.views import IndexView

urlpatterns = UrlPattern()

urlpatterns.register(IndexView)
