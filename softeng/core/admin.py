from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = "SoftEng PCP Creator Admin"
admin.site.site_title = "Site Administration"
admin.site.index_title = "Welcome to SoftEng PCP Creator"
