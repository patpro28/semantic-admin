from semantic_admin.filters import SemanticFilterSet, SemanticModelMultipleChoiceFilter

from .models import Person, Picture

try:
    from django.utils.translation import gettext_lazy as _  # Django >= 4
except ImportError:
    from django.utils.translation import ugettext_lazy as _


class PersonFilter(SemanticFilterSet):
    favorite_pictures = SemanticModelMultipleChoiceFilter(
        label=_("favorite pictures"),
        queryset=Picture.objects.exclude(favorites=None),
        method="filter_favorite_pictures",
    )

    def filter_favorite_pictures(self, queryset, name, value):
        if not value:
            return queryset
        else:
            queryset = queryset.filter(favorites__picture__in=value)
            return queryset.distinct()

    class Meta:
        model = Person
        fields = ("friends", "favorite_pictures")
