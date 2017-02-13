from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from AppBackend import views
from django.conf.urls import include,url
from rest_framework.authtoken import views as authViews
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'locationList/upload', views.LocationAdd.as_view()),
    url(r'locationGetAll/', views.LocationGetAll.as_view()),
    url(r'^locationGetSpecific/(?P<pk>[0-9]+)/$', views.LocationGetSpecific.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'pathList/upload', views.PathAdd.as_view()),
    url(r'pathGetAll/', views.PathGetAll.as_view()),
    url(r'^pathGetSpecific/(?P<pk>[0-9]+)/$', views.PathGetSpecific.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns += [ url(r'api-token-auth/', authViews.obtain_auth_token)]
