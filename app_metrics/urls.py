from django.conf.urls import url

from app_metrics import views

urlpatterns = [
    url(r'^reports/$', views.metric_report_view, name='app_metrics_reports'),
]
