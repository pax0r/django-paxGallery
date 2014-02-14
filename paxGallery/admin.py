from django.contrib import admin

# Register your models here.
from django import forms
from models import Gallery, Photo


class GalleryAdmin(admin.ModelAdmin):
    exclude = ['cover']
    prepopulated_fields = {"slug": ("name",)}


class PhotoAdminForm(forms.ModelForm):
    is_cover = forms.BooleanField(required=False)

    class Meta:
        model = Photo
        exclude = []

    def __init__(self, *args, **kwargs):
        super(PhotoAdminForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            instance = kwargs.get('instance')
            if instance.gallery.cover == instance:
                self.initial['is_cover'] = True

    def save(self, commit=True):
        model = super(PhotoAdminForm, self).save(commit)
        if self.cleaned_data.get('is_cover', False):
            model.gallery.cover = model
            model.gallery.save(commit)
        return model


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)