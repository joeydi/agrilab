import json
from django.contrib import admin
from .models import Source, Reading

admin.site.register(Source)


class ReadingAdmin(admin.ModelAdmin):
    list_display = [
        "source",
        "date",
        "T_IN",
        "T_OUT",
        "TW_I",
        "TW_O",
        "DCFM",
        "O2",
    ]
    list_display_links = [
        "source",
        "date",
    ]
    list_filter = ["source"]
    date_hierarchy = "date"

    def T_IN(self, instance):
        # data = json.loads(instance.data)
        return instance.data["T_IN"]

    def T_OUT(self, instance):
        # data = json.loads(instance.data)
        return instance.data["T_OUT"]

    def TW_I(self, instance):
        # data = json.loads(instance.data)
        return instance.data["TW_I"]

    def TW_O(self, instance):
        # data = json.loads(instance.data)
        return instance.data["TW_O"]

    def DCFM(self, instance):
        # data = json.loads(instance.data)
        return instance.data["DCFM"]

    def O2(self, instance):
        # data = json.loads(instance.data)
        return instance.data["O2"]


admin.site.register(Reading, ReadingAdmin)
