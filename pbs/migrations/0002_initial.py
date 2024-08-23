# Generated by Django 3.2.25 on 2024-08-23 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prescription', '0001_initial'),
        ('pbs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='district',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prescription.district'),
        ),
        migrations.AddField(
            model_name='profile',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prescription.region'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]