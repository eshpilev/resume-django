from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class CandidateAdminForm(forms.ModelForm):
    short_info = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Candidate
        fields = '__all__'


class ExperienceAdminForm(forms.ModelForm):
    duties = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Experience
        fields = '__all__'


class CandidateAdmin(admin.ModelAdmin):
    form = CandidateAdminForm
    list_display = ('full_name', 'position', 'views')
    fields = ('full_name', 'position', 'short_info', 'photo', 'get_photo', 'views')
    readonly_fields = ('get_photo', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('type', 'connect')


class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceAdminForm
    list_display = ('from_date', 'company', 'position')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('year_finish', 'title', 'specialty')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('year_finish', 'title')


class HardSkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(HardSkill, HardSkillAdmin)
admin.site.register(SoftSkill)
