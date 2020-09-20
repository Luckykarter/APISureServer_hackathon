from django.urls import path

import apisure.views as views

urlpatterns = [
    path('guarantee/apply', views.send_guarantee),
    path('guarantee/apply/', views.send_guarantee),
    path('guarantee/', views.get_guarantee),
    path('guarantee/<str:deal_number>', views.get_guarantee),
    path('guarantee/test/', views.test_guarantee),
    path('guarantee/project/', views.post_project),
    path('guarantee/project', views.post_project),
    path('guarantee/project/delete/<str:id>', views.delete_project),
    path('apitest/', views.test_connection)
]
