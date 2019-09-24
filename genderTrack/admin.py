from django.contrib import admin

from genderTrack.models import Activity

# admin.site.register(Activity)

# Define the admin class

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity', 'sub_activity', 'cost', 'description')


# Register the Admin classes for Book using the decorator
# @admin.register(Outcome)
# class OutcomeAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# Register the Admin classes for BookInstance using the decorator
# @admin.register(OutcomeInstance)
# class OutcomeInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#     fieldsets = (
#         (None, {
#             'fields': ('Activity', 'imprint', 'id')
#         }),
#         ('Target status', {
#             'fields': ('status', 'due_back')
#         }),
#     )
