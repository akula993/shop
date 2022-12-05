from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from .models import Category, Product


@admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'parent', 'status']
#     list_filter = ['status']

class CategoryAdmin2(DraggableMPTTAdmin):
    # mptt_level_indent = 20
    mptt_indent_field = "some_node_field"  # В каком поле отступ
    list_display = ('tree_actions', 'indented_title', 'uuid', "id", 'parent',
                    'slug', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('indented_title', 'id', 'uuid',)
    prepopulated_fields = {"slug": ("title", 'parent')}
    list_editable = ('is_active', 'parent')
    save_as = True

    # save_as_continue = True
    save_on_top = True
    readonly_fields = ['id', 'uuid', ]
    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ['slug']
    #     else:
    #         return []


# class CategoryAdmin(DjangoMpttAdmin):

#     list_display = ('id', 'title', 'parent', 'is_active',)

#     list_editable = ('is_active', 'parent')
#     # list_filter = ()
#     # list_select_related = False
#     # list_per_page = 100
#     # list_max_show_all = 200
#     # search_fields = ()
#     # search_help_text = 'Выберити активный список'
#     # date_hierarchy = None
#     save_as = True
#     # save_as_continue = True
#     save_on_top = True
#     # preserve_filters = True
#     # inlines = ()
#     #
#     # # Custom templates (designed to be over-ridden in subclasses)
#     # add_form_template = None
#     # change_form_template = None
#     # change_list_template = None
#     # delete_confirmation_template = None
#     # delete_selected_confirmation_template = None
#     # object_history_template = None
#     # popup_response_template = None
#     #
#     # # Actions
#     # actions = ()
#     # action_form = helpers.ActionForm
#     # actions_on_top = True
#     # actions_on_bottom = False
#     # actions_selection_counter = True
#     # checks_class = ModelAdminChecks


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
# https://tretyakov.net/post/drevovidnye-kategorii-v-django/

# admin.site.register(
#     Category,
#     DraggableMPTTAdmin,
#     list_display=(
#         'tree_actions',
#         'indented_title',
#         # ...more fields if you feel like it...
#     ),
#     list_display_links=(
#         'indented_title',
#     ),
# )
