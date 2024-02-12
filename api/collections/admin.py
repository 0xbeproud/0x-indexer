from django.contrib import admin

from api.collections.models import Collection, CollectionStat, CollectionToken

admin.site.register(Collection)
admin.site.register(CollectionStat)
admin.site.register(CollectionToken)


# Register your models here.
class CollectionAdmin(admin.ModelAdmin):
    model = Collection


class CollectionStatAdmin(admin.ModelAdmin):
    model = CollectionStat


class CollectionTokenAdmin(admin.ModelAdmin):
    model = CollectionToken
