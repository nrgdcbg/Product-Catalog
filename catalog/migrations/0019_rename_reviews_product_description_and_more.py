# Generated by Django 4.0.4 on 2022-05-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_alter_authuser_user_type_alter_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='reviews',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='review',
            name='media',
        ),
        migrations.RemoveField(
            model_name='review',
            name='photo',
        ),
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Reviewer'), (1, 'Product Manager'), (2, 'Customer'), (3, 'Customer Manager')], null=True),
        ),
    ]
