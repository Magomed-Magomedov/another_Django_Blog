# Generated by Django 3.1.7 on 2021-02-24 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210224_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Статья(ю)', 'verbose_name_plural': 'Статьи'},
        ),
    ]
