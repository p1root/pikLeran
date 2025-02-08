# Generated by Django 5.1.6 on 2025-02-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('notification_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('read', 'Read'), ('unread', 'Unread')], default='unread', max_length=10)),
            ],
        ),
    ]
