# Generated by Django 4.0.6 on 2022-08-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_messages_id_alter_messages_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('message', models.CharField(max_length=1000, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
        ),
        migrations.AlterField(
            model_name='messages',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
