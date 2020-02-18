from django.contrib import admin
from django.urls import include, path
from crowdsource import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('crowdsource/', include('crowdsource.urls')),
    path('admin/', admin.site.urls),
    path('EmbData/', views.EmbDataList.as_view()),
]