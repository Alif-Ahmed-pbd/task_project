
from django.contrib import admin
from django.urls import path
from task_app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signup, name='signup'),
    path('sign-in/', signin, name='signin'),
    path('sign-out/', signout, name='signout'),
    path('home/', home, name='home'),
    path('update_profile/', update_profile, name='update_profile'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('user_delete/<str:id>/', user_delete, name='user_delete'),
    path('addtask/', addtask, name='addtask'),
    path('tasklist/', tasklist, name='tasklist'),
    path('edittask/<str:id>', edittask, name='edittask'),
    path('deletetask/<str:id>', deletetask, name='deletetask'),
    path('task_completed/<str:id>/', task_completed, name='task_completed'),
    path('proggraming/', proggraming, name='proggraming'),
    path('practice/', practice, name='practice'),
    path('contest/', contest, name='contest'),
    path('search_query/', search_query, name="search_query"),


]
