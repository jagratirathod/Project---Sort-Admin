from django.contrib import admin
from .models import *


# Register your models here.
    

class PostAdmin(admin.ModelAdmin):
    list_display = ['id',"title", "body","get_view_count"]
    
    def get_view_count(self, obj):
        try :
            if obj.post_stats :
                return obj.post_stats.first().view_count
        except:
            return None
    get_view_count.admin_order_field = "-post_stats__view_count"
    get_view_count.short_description = "View count"              # change name of field
admin.site.register(Post, PostAdmin)



class PostStatsAdmin(admin.ModelAdmin):
    list_display = ['id',"post","view_count"]
admin.site.register(PostStats, PostStatsAdmin)  




