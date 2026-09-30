from django.urls import path
from . import views
urlpatterns=[path('api/health/',views.health),path('api/routes/',views.routes),path('api/pass-types/',views.pass_types),path('api/applications/',views.applications),path('api/applications/create/',views.create_application),path('api/applications/<str:i>/',views.detail),path('api/applications/<str:i>/update/',views.update_application),path('api/applications/<str:i>/feedback/',views.feedback_view),path('api/dashboard/',views.dashboard),path('api/notifications/',views.notifications)]
