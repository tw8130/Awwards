from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='index'),
    path('ajax/newsletter/', views.newsletter, name='newsletter'),
    path('search/',views.search_project, name='search_results'),
    path('profile/',views.profile,name='profile'),
    path('project/review/(\d+)',views.project_review,name='project_review'),
    path('new/project', views.new_project, name='new_project'),
    path('new_profile/',views.new_profile,name = 'new_profile'),
    path('edit/profile/',views.profile_edit,name = 'edit_profile'),
    path('api/project/', views.ProjectList.as_view()),
    path('api/project<int:/project-id>/',
        views.ProjectDescription.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/profile/<int:profile-id>/',
        views.ProfileDescription.as_view()),
    # path('', views.review_list, name='review_list'),
    # # ex: /review/5/
    # path('review/<int:review_id>[0-9]/',
    #     views.review_detail, name='review_detail'),
    # # ex: /project/
    # path('project/', views.project_list, name='project_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password_reset/',
          auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
          name='password_reset'),
    path('password_reset/done/',
          auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
          name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
          name='password_reset_confirm'),
    path('password_reset_complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
          name='password_reset_complete'),
      
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)