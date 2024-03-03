from datetime import date
from django.conf import settings
from django.db import models




# models.Model heißt, dass Chat von models.Model erbt bzw. diese erweitert
class Chat(models.Model):
    created_at = models.DateField(default=date.today)



# ForeignKey auf anderes Object referenzieren
# settings.AUTH_USER_MODEL, zeigt das author und receiver jeweils user sind, die in dem Project gespeichert sind
# Cascade --> wenn User gelöscht wird, löschen sich die Daten
# related_name --> author Object1_Object2_set --> set immer dahinter, auch wenn nur ein Object
# default gibt Wert an der gegeben wird, wenn nciht vorhandne
# blank sagt, dass leere Werte angegeben werden können
# null sagt der Datenbank, dass leere Werte genommen werden dürfen
    
class Messages(models.Model):
    text = models.CharField(max_length=256)
    created_at = models.DateField(default=date.today)
    # chat = verknüpfe mit chatklasse
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')



    