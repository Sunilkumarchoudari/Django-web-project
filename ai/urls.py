from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>',views.get_project,name='project_page'),
    # path('<int:id>/backup',views.backup,name='backup_project'),
    # path('livedata/<str:datatype>',views.livedata,name='livedata'),
    # path('backup',views.backup_page,name='backup_page'),
    # path('restore',views.restore_page,name='restore_page'),
    # path('<int:id>/restore',views.restore,name='restore_project'),
    # path('clear',views.clear,name='clear_page'),
    # path('check_junk',views.check_junk,name='check_junk'),
    # path('master_clean',views.master_clean,name='master_clean'),
]
