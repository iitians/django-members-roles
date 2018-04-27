from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', login_required(ManageStaffFullView.as_view()),
        name="manage-staff"),
    url(r'^add_staff/$', login_required(AddStaffView.as_view()),
        name="add-staff"),
    url(r'^staff_list/$', login_required(StaffListView.as_view()),
        name="staff-list"),
    url(r'^add_role/$', login_required(AddRoleView.as_view()), name="add-role"),
    url(r'^role_list/$', login_required(RoleListView.as_view()), name="role-list"),
]
