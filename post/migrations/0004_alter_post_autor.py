# Generated by Django 3.2.8 on 2024-03-10 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_autor_id_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.autor'),
            preserve_default=False,
        ),
    ]
