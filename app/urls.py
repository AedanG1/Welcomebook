from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # ADMIN pages
    path("house_rules_admin", views.house_rules_admin, name="house_rules_admin"),
    path("information_admin", views.information_admin, name="information_admin"),
    path("eats_admin", views.eats_admin, name="eats_admin"),
    path("activity_admin", views.activity_admin, name="activity_admin"),
    path("contacts_admin", views.contacts_admin, name="contacts_admin"),

    # API routes
    path("edit_item/<int:item_id>", views.edit_item, name="edit_item"),
    path("add_new_item", views.add_new_item, name="add_new_item"),
    path("delete_item/<int:item_id>", views.delete_item, name="delete_item"),
    path("edit_position", views.edit_position, name="edit_position"),
    path("upload_image/<int:item_id>", views.upload_image, name="upload_image"),
    path("remove_image/<int:item_id>", views.remove_image, name="remove_image")
]