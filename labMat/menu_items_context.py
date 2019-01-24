from .models import Item_Group


def show_menu_items(request):
    menu_items = Item_Group.objects.filter(center_item_group__center__user_center__user_id=request.user.id)
    return {'menu_items': menu_items}
