# Generated by Django 5.0.8 on 2024-12-16 08:00

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='archive_successful',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='approval',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='approval',
            name='initial_valid_to',
            field=models.DateField(default=datetime.datetime(2025, 12, 16, 8, 0, 51, 449100, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Valid To (Initial)'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='briefingchecklist',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='briefingchecklist',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='endorsement',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='endorsement',
            name='endorsed',
            field=models.BooleanField(blank=True, choices=[(None, ''), (False, 'Reviewed and not endorsed'), (True, 'Endorsed')], default=None),
        ),
        migrations.AlterField(
            model_name='endorsement',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='objective',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='objective',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='contentious',
            field=models.BooleanField(choices=[(None, '-----'), (False, 'No'), (True, 'Yes')], default=None, help_text='Is this burn contentious?', null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='non_calm_tenure',
            field=models.BooleanField(null=True, verbose_name='Non-CALM Act Tenure'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='non_calm_tenure_approved',
            field=models.BooleanField(null=True, verbose_name='Cross Tenure Approved?'),
        ),
        migrations.AlterField(
            model_name='priorityjustification',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='priorityjustification',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='regionalobjective',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='regionalobjective',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='season',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='season',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='successcriteria',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='successcriteria',
            name='modifier',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL),
        ),
    ]