from django.contrib import admin
from .models import Discipline


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    """
    Custom Discipline admin.
    """

    list_display = ['code', 'title', 'semester', 'classification']
    list_filter = ['semester', 'classification', 'created_at']
    search_fields = ['title', 'code']
    prepopulated_fields = {'slug': ('code',)}

    def get_object(self, request, object_id, from_field=None):
        """
        Get the object for use in formfield_for_manytomany
        """

        self.obj = super(DisciplineAdmin, self).get_object(request, object_id)
        return self.obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """
        Change ManyToMany to display only required disciplines with semester before the
        discipline semester.
        """

        if getattr(self, 'obj', None):
            kwargs["queryset"] = Discipline.objects.filter(
                semester__lte=self.obj.semester
            ).exclude(id=self.obj.id)

        return super().formfield_for_manytomany(db_field, request, **kwargs)
