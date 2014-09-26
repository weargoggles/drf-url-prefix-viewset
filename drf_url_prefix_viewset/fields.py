from rest_framework import serializers
from django.core.urlresolvers import reverse

class PrefixAwareHyperlinkedRelationship(serializers.HyperlinkedIdentityField):
    """Allows a mapping of url capture group names (queryset filter keys)
    to be sourced from the serialized object and included in the call to
    reverse()."""

    def __init__(self, *args, **kwargs):
        self.url_kwarg_map = kwargs.pop('url_kwarg_map', None)
        super(PrefixAwareHyperlinkedRelationship, self).__init__(*args, **kwargs)

    def get_url(self, obj, view_name, request, format):
        """ 
        Replaces lookup_field with arbitrary capture-group:attribute map
        """
        kwargs = {}

        for group_name, attr in self.url_kwarg_map.items():
            val = getattr(obj, attr)
            if val:
                kwargs[group_name] = val 

        # We also short-circuit all the deprecated functionality of
        # HyperlinkedIdentityField
        return reverse(view_name, kwargs=kwargs, request=request, format=format)

