from django.contrib import admin
from .models import Worker, Store, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', ]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', ]


@admin.register(Visit)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'store',)
    search_fields = ('store__name', 'store__worker__name')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
