from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from models import Gallery, Photo


class GalleryHomeView(TemplateView):
    template_name = 'gallery/home.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryHomeView, self).get_context_data(**kwargs)
        context['all_galleries'] = Gallery.objects.all()
        return context


class GalleryView(GalleryHomeView):
    template_name = 'gallery/gallery.html'

    def get(self, request, *args, **kwargs):
        gallery = get_object_or_404(Gallery, pk=kwargs.get('id'))
        if kwargs.get('galleryslug') != gallery.slug:  #keep our slugs clean
            return redirect('gallery-view', id=gallery.id, galleryslug=gallery.slug)
        context = self.get_context_data(kwargs=kwargs)
        context['gallery'] = gallery
        context['photos'] = gallery.photo_set.all()
        return render(request, self.template_name, context)


class GalleryPhotoView(GalleryHomeView):
    template_name = 'gallery/photo.html'

    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('id'))
        if kwargs.get('galleryslug') != photo.gallery.slug or kwargs.get(
                'photoslug') != photo.slug:  #keep our slugs clean
            return redirect('photo-view', id=photo.id, galleryslug=photo.gallery.slug, photoslug=photo.slug)
        context = self.get_context_data(kwargs=kwargs)
        context['photo'] = photo
        return render(request, self.template_name, context)
