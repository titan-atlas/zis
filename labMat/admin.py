from django.contrib import admin
from labMat.models import Center, User_Center, Unit_Of_Measure, Item_Group, Year, Item, Plan, Center_Item_Group, Note


class CenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'center_name')

    
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'measure')


class ItemGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_group_name')

    
class YearAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'locked')

    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'unit_of_measure', 'item_group')
    list_display_links = ('id', 'item_name')
    list_filter = ('item_group',)


admin.site.register(Center, CenterAdmin)
admin.site.register(User_Center)
admin.site.register(Unit_Of_Measure, UnitOfMeasureAdmin)
admin.site.register(Item_Group, ItemGroupsAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Plan)
admin.site.register(Center_Item_Group)
admin.site.register(Note)
