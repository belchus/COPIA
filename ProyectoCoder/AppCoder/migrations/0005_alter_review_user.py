# Generated by Django 4.1.6 on 2023-03-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
