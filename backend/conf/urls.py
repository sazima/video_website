from django_request_mapping import UrlPattern

from web.views import IndexView, VideoView

urlpatterns = UrlPattern()

urlpatterns.register(IndexView)
urlpatterns.register(VideoView)
