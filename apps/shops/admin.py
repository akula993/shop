from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    """Encapsulate all admin options and functionality for a given model."""
    mptt_indent_field = "some_node_field"
    list_display = ('id', 'title', 'parent', 'top',)
    list_display_links = ('id', 'title',)
    list_editable = ('top', 'parent')
    # list_filter = ()
    # list_select_related = False
    # list_per_page = 100
    # list_max_show_all = 200
    # search_fields = ()
    # search_help_text = 'Выберити активный список'
    # date_hierarchy = None
    save_as = True
    # save_as_continue = True
    save_on_top = True
    # preserve_filters = True
    # inlines = ()
    #
    # # Custom templates (designed to be over-ridden in subclasses)
    # add_form_template = None
    # change_form_template = None
    # change_list_template = None
    # delete_confirmation_template = None
    # delete_selected_confirmation_template = None
    # object_history_template = None
    # popup_response_template = None
    #
    # # Actions
    # actions = ()
    # action_form = helpers.ActionForm
    # actions_on_top = True
    # actions_on_bottom = False
    # actions_selection_counter = True
    # checks_class = ModelAdminChecks
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
# https://tretyakov.net/post/drevovidnye-kategorii-v-django/



