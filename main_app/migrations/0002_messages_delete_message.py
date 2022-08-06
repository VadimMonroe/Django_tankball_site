# Generated by Django 4.0.6 on 2022-08-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('message', models.CharField(max_length=1000, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Сообщениe в Форме',
                'verbose_name_plural': 'Сообщения в Форме',
            },
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
