# Generated by Django 5.0.2 on 2024-03-03 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='chat',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_message_set', to='chat.chat'),
        ),
    ]
