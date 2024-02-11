from django.contrib import admin
from .models import PostProject, PostJobs 
 
class PostProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'nom_projet', 'epic_coder', 'location', 'prix_premiere', 'prix_derniere', 'cacher')
    readonly_fields = ('created_project', 'updated_project')

class PostJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name_jobs', 'epic_coder', 'type_work_job', 'location', 'prix', 'cacher')
    readonly_fields = ('created_job', 'updated_job')
 