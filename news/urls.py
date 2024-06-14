from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.redir, name='redir'),
    path('site/', views.news, name='news'),
    path('site/<int:n>', views.article, name='article'),
    path('arts/', views.arts, name='arts'),
    path('arts/<int:n>', views.art, name='art'),
    path('arts/new', views.newart, name='newart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()