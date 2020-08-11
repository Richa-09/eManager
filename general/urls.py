from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home_page'),
    path('login/', views.loginUser, name="login_page"),
    path('signup/', views.signup, name="signup_page"),
    path('logout/', views.logoutUser, name="logout_page"),
    path('newboard/',views.newboard, name="new_board"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('del_board/<int:z>',views.del_board,name="del_board"),
    path('create_board/',views.create_board,name="create_board"),
    path('listpage/<int:k>',views.listpage,name="listpage"),
    path('create_list/<int:k>',views.create_list,name="create_list"),
    path('create_card/<int:k>/<int:p>',views.create_card,name="create_card"),
    path('del_list/<int:k>/<int:p>',views.del_list,name="del_list"),
    path('del_card/<int:k>/<int:p>/<int:z>',views.del_card,name="del_card"),
]
