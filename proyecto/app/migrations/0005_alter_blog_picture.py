# Generated by Django 4.0.7 on 2023-05-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_blog_content_type_alter_blog_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.BinaryField(editable=True, null=True),
        ),
    ]
