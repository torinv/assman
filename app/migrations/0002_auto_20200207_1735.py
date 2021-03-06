# Generated by Django 2.2.9 on 2020-02-07 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='bin_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bin_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bin',
            name='bin_created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bin',
            name='bin_last_edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bin',
            name='bin_last_edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bin_last_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='card_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='card_created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='card_last_edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='card',
            name='card_last_edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_last_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='item_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='item_created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_last_edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_last_edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_last_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='key',
            name='key_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='key_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='key',
            name='key_created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='key',
            name='key_last_edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='key',
            name='key_last_edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='key_last_editor', to=settings.AUTH_USER_MODEL),
        ),
    ]
