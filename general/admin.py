from django.contrib import admin
from .models import UserProfile, board, checklist, card


admin.site.register(UserProfile)
admin.site.register(board)
admin.site.register(checklist)
admin.site.register(card)