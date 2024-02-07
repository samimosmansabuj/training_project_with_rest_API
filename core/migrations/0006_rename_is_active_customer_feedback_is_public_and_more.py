# Generated by Django 5.0.2 on 2024-02-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_blog_is_active_customer_feedback_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_feedback',
            old_name='is_active',
            new_name='is_public',
        ),
        migrations.AlterField(
            model_name='customer_feedback',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='customer_feedback/'),
        ),
    ]
