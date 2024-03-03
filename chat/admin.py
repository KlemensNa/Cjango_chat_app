from django.contrib import admin
from chat.models import Chat, Messages

# hier kann man selber einstellen welche Felder auf der AdminPage angezeigt werden
# lösche Tupelfelder um weniger Inforamtionen anzuzeigen
# list_display für die Übersicht (default steht nur MessageObject da)
# fields für Felder wenn man Message anklickt (default werden alle angezeigt)
# weitere Sachen können eingefügt werden, z.B. search_filter o.Ä.
class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text', 'author', 'receiver', 'created_at')
    list_display = ('created_at', 'chat', 'author', 'text')

admin.site.register(Messages, MessageAdmin)
admin.site.register(Chat)

