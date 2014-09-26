drf-url-prefix-viewset
======================

When creating Django REST Framework routers, I wished
for a straightforward way to express viewsets that 
were logically contained within other viewsets.

That eventually led me to this solution, in which a 
ModelViewSet mixin consumes capture groups from the 
prefix specified by the router.


Example
=======

    from rest_framework import viewsets, routers

    class ChildViewSet(viewsets.ModelViewSet, PrefixedModelViewSetMixin):
        class Meta:
            model = Child

    router = routers.SimpleRouter()
    router.register('parent/(?P<parent__pk>\d+)/child', ChildViewSet)


When the PrefixedModelViewSetMixin'd ViewSet is used, its 
queryset filter will be updated with all of the keyword 
arguments to the view function: in other words, a map of 
the capture group names to the text they have captured.

In this case, it means that the Child QuerySet will 
have .filter(parent__pk=123) applied when the url begins parent/123/child/.

