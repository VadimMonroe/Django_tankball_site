# Generated by Django 4.0.6 on 2022-08-16 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_category_alter_messages_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Сообщениe в Форме', 'verbose_name_plural': 'Сообщения в Форме'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='MessagesForm2',
        ),
    ]
