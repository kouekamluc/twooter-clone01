# Generated by Django 4.2.4 on 2023-08-21 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_created_at_post_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dislike',
            new_name='dislikes',
        ),
    ]
