# Generated by Django 4.1.6 on 2023-03-11 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_remove_review_img_alter_movie_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.user'),
        ),
    ]