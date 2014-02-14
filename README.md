=================
Pax Gallery
=================

Simple, reusable Django gallery app. It can display photos grouped in Galleries. 

Quick start
-----------

1. Add "paxGallery" to your INSTALLED_APPS setting like this::
```
    INSTALLED_APPS = (
        ...
        'paxGallery',
    )
```
2. Include the polls URLconf in your project urls.py like this::
```
    url(r'^gallery/', include('paxGallery.urls')),
```
3. Run `python manage.py syncdb` to create the gallery models.

4. In the Admin page create Gallery and Photos attached to it. While adding or editing a Photo you can set it as a cover for the gallery in which it will be. If no cover is set the "No cover" image will be displayed.

5. Override templates to customize it to your need. There are three templates used by this app - `gallery/base.html` for the page with all galleries displayed, `gallery/gallery.html` for the all photos in given gallery and `gallery/photo.html` for the display of the single photo.


TODO
----
1. Templatetags for displaying photos and others (i.e. Random Photo)
2. Some kind of permissions.

License
-------
MIT License (see LICENSE file for details). 
In brief you can do whatever you want as long as the copyright header is left intact. 
Also I would be glad if you would notice me about usage it on your site ;)
