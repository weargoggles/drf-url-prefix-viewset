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

````python
from rest_framework import viewsets, routers
from drf_url_prefix_viewset.mixins import PrefixedModelViewSetMixin

class ChildViewSet(viewsets.ModelViewSet, PrefixedModelViewSetMixin):
    class Meta:
        model = Child

router = routers.SimpleRouter()
router.register('parent/(?P<parent__pk>\d+)/child', ChildViewSet)
````

When the PrefixedModelViewSetMixin'd ViewSet is used, its 
queryset filter will be updated with all of the keyword 
arguments to the view function: in other words, a map of 
the capture group names to the text they have captured.

In this case, it means that the Child QuerySet will 
have .filter(parent__pk=123) applied when the url begins parent/123/child/.

The second part of the puzzle is providing references to 
these nested viewsets from their parent viewsets. To that 
end, a subclass of HyperlinkedIdentityField called 
PrefixAwareHyperlinkedRelationship, which takes a map of 
capture group names to attributes of the object being serialized:

````python
from rest_framework import serializers
from drf_url_prefix_viewset.fields import PrefixAwareHyperlinkedRelationship

class ParentSerializer(serializers.ModelSerializer):
    child = PrefixAwareHyperlinkedRelationship(
        view_name='child-list',
        url_kwarg_map={
        'parent__pk': 'pk',
    })
````

For the parent with pk '123' this produces:

````json
{
    "child": "/parent/123/child/"
}
````
