from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact', views.contact),
    path('about', views.about),
    path('login', views.login),
    path('addbranch', views.add_branch),
    path('editbranch/<int:id>', views.getBranch),
    path('deletebranch/<int:id>', views.deleteBranch),
    path('updatebranch/<int:id>', views.updateBranch),
    path('addcourse', views.addcourse),
    path('getcourse/<int:id>', views.getCourse),
    path('deletecourse/<int:id>', views.deleteCourse),
    path('addAccount_master', views.addAccount_master),
    path('viewallaccount', views.viewallaccount),
    path('deleteaccount_master/<int:id>', views.deleteaccount_master),
    path('updateaccount/<int:id>', views.updateaccount),
    path('getaccount/<int:id>', views.getaccount),
    path('allBranch', views.allBranches),
    path('allcourse', views.allcourses),
    path('admin_home', views.admin_home),
    path('accountant_home', views.accountant_home),
    path('add_student', views.addstudent),
    path('viewallstudent', views.viewallstudent),
    path('user_logout', views.user_logout),
    path('adminlogout', views.admin_logout),
    path('pay_fees/<int:id>', views.pay_fees12),
    path('payed_fees/<int:id>', views.payed_fees),
    path('student_by_admin', views.student_by_admin),
    path('student_by_branch/<int:id>', views.student_by_branch),

]
