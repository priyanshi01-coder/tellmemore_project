
from django.contrib import admin
from django.urls import path , include
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('sessions/', views.my_sessions, name='my_sessions'),
    path('uploads/', views.uploaded_items, name='uploaded_items'),
    path('analytics/', views.analytics, name='analytics'),
    path("category/",views.category_view , name="category"),
    
    path("interview_requirements/",views.interview_requirements_view , name="interview_requirements"),
    path("presentation_requirements/",views.presentation_requirements_view , name="presentation_requirements"),
    path("communication_requirements/",views.communication_requirements_view , name="communication_requirements"),
    path("question_requirements/",views.question_requirements_view , name="question_requirements"),

    path("profile/",views.profile_view, name="profile"),
    path("profile_edit/",views.profile_edit_view, name="profile_edit"), 

    path('ai_session/', views.ai_page_view, name='ai_page'),
    path('simple_interview/', views.simple_interview_view, name='simple_interview'),
    path('start_session/', views.start_interview_session, name='start_session'),
    path('generate_question/', views.generate_question, name='generate_question'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('evaluate_answer/', views.evaluate_answer, name='evaluate_answer'),  # Legacy support
    path('end_session/', views.end_interview_session, name='end_session'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


