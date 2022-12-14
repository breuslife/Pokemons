# Generated by Django 3.2.15 on 2022-08-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('weight', models.IntegerField(verbose_name='Weight')),
                ('order', models.IntegerField(verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemons',
                'db_table': 'pokemons',
            },
        ),
    ]
