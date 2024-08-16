from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # ADMIN pages
    path("house_rules_admin", views.house_rules_admin, name="house_rules_admin"),
    path("information_admin", views.information_admin, name="information_admin"),
    path("eats_admin", views.eats_admin, name="eats_admin"),

    # API routes
    path("add_new_rule", views.add_new_rule, name="add_new_rule"),
    path("delete_rule/<int:rule_id>", views.delete_rule, name="delete_rule"),
    path("edit_rule/<int:rule_id>", views.edit_rule, name="edit_rule"),
    path("edit_position", views.edit_position, name="edit_position"),
    path("edit_info/<int:info_id>", views.edit_info, name="edit_info"),
    path("add_new_info", views.add_new_info, name="add_new_info"),
    path("upload_image/<int:info_id>", views.upload_image, name="upload_image"),
    path("delete_info/<int:info_id>", views.delete_info, name="delete_info")
]