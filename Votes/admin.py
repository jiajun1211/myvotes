from django.contrib import admin
from models import Vote
# Register your models here

class CustomVoteAdmin(admin.ModelAdmin):

    pass
admin.site.register(Vote, CustomVoteAdmin)