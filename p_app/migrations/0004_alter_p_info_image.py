# Generated by Django 4.2.1 on 2023-05-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0003_rename_personal_info_p_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_info',
            name='image',
            field=models.ImageField(max_length=50, upload_to='p_info/'),
        ),
    ]
