# Generated by Django 5.0.2 on 2024-03-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_messages_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='messages',
            name='created_at',
            field=models.CharField(default='', max_length=30),
        ),
    ]