"""
Inform the admin site of objects that have an admin interface.  This is where we
can set up objects to be managed through the admin interface.
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from stickymessages import models

class SystemMessageAdmin(admin.ModelAdmin):
    """
    Admin class for the SystemMessage model.
    """
    fieldsets = [
        ('System message to display', {'fields': ['message']}),
        ('Setup', {'fields': ['active_datetime', 'inactive_datetime']})
    ]
    list_display = ('message', 'active_datetime', 'inactive_datetime', 'modified', 'modified_by', 'created', 'created_by' )
    
    def save_model(self, request, message, form, change): 
        if not change:
            ##Only going to add the created by field on a new entry
            message.created_by = request.user
        
        message.modified_by = request.user
        message.save()

admin.site.register(models.Message, SystemMessageAdmin)
