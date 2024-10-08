# Generated by Django 4.0.4 on 2022-05-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_supplier_profilepicture_alter_authuser_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='profilepicture',
            new_name='displaypicture',
        ),
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Product Manager'), (3, 'Customer Manager'), (2, 'Customer'), (4, 'Reviewer')], null=True),
        ),
    ]
