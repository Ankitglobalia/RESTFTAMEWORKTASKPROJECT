from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Editor
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class EditorAdminForm(forms.ModelForm):
    Description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Editor
        fields = '__all__'

# Register form
class EditorAdmin(admin.ModelAdmin):
    form = EditorAdminForm

admin.site.register(Editor, EditorAdmin)