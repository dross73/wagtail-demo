# Generated by Django 5.1.8 on 2025-04-20 02:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_aboutpage_body'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='button_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='button_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
