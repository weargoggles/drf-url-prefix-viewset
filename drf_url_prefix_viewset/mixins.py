from django.db.models import Q
from rest_framework import viewsets

class PrefixedModelViewSetMixin(viewsets.ModelViewSet):
    """This mixin allows ModelViewSets to use named capture
    groups in their url to filter their queryset. The capture group
    names should be appropriate keys for use in a Q object.


    Example:
    router = SimpleRouter()
    router.register('parent/(?P<parent__pk>\d+)/child')

    This results in the queryset for the viewset being filtered with
    Q(parent__pk=123) when the url 'parent/123/child' is requested.
    """
    def __init__(self, *args, **kwargs):
        super(PrefixedModelViewSetMixin, self).__init__(*args, **kwargs)
        self.queryset_filter = None

    def get_queryset(self):
        queryset = super(PrefixedModelViewSetMixin, self).get_queryset()
        return queryset.filter(self.queryset_filter)

    def initial(self, request, *args, **kwargs):
        self.queryset_filter = Q(**kwargs)
        return super(PrefixedModelViewSetMixin, self).initial(request, *args,
                                                              **kwargs)

