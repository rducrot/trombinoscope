# Generated by Django 4.1.6 on 2023-03-10 08:32

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_service_acronym_service_mail_service_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='service',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='app.service'),
        ),
    ]
