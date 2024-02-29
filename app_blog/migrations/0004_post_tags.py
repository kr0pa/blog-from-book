# Generated by Django 5.0.1 on 2024-02-29 05:22

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_comment_comment_app_blog_co_created_15b33d_idx'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]