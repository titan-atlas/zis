from django.contrib import admin
from labMat.models import Center, User_Center, Unit_Of_Measure, Item_Group, Year


class YearAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'locked')

    
class CenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'center_name')

    
class ItemGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_group_name')


admin.site.register(Center, CenterAdmin)
admin.site.register(User_Center)
admin.site.register(Unit_Of_Measure)
admin.site.register(Item_Group, ItemGroupsAdmin)
admin.site.register(Year, YearAdmin)
