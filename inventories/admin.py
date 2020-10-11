from django.contrib import admin
from .models import Inventories, Assigned_Gadget, Department, Email


class InventoriesAdmin(admin.ModelAdmin):
    list_display = ('asset_id', 'asset_name', 'asset_vendor', 'asset_status', 'asset_user', 'asset_desc', 'asset_model', 'asset_image_url',
                    'next_maintenance', 'asset_location', 'asset_sub_location', 'asset_serial_no')


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name', 'department_assets')


class AssignedGadgetsAdmin(admin.ModelAdmin):
    list_display = ('staff', 'gadget')


class StaffEmailsAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'staff_email', 'staff_password', 'staff_email_status')


admin.site.register(Inventories, InventoriesAdmin)

admin.site.register(Department, DepartmentsAdmin)

admin.site.register(Email, StaffEmailsAdmin)

admin.site.register(Assigned_Gadget, AssignedGadgetsAdmin)



