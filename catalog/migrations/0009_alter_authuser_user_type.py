# Generated by Django 4.0.4 on 2022-05-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_authuser_user_type_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Product Manager'), (3, 'Customer Manager'), (4, 'Reviewer'), (2, 'Customer')], null=True),
        ),
    ]
