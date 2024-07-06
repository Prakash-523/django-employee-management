from django.contrib import admin
from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['eno','ename']
    list_display = ['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)

