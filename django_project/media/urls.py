from django.urls import path

from . import views

app_name = "media"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("broadcast/", views.broadcast_view, name="broadcast"),
    path("highlights/", views.highlights_view, name="highlights"),
    path("press/", views.press_view, name="press"),
    # data exports
    path("export/press/", views.export_press_csv, name="export_press"),
    path("export/broadcasts/", views.export_broadcast_csv, name="export_broadcasts"),
    path("export/highlights/", views.export_highlights_csv, name="export_highlights"),
]
