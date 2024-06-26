# Generated by Django 5.0.1 on 2024-04-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('colony', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=6, null=True)),
                ('external_number', models.CharField(blank=True, max_length=5, null=True)),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('type', models.CharField(blank=True, choices=[('house', 'Casa'), ('deparment', 'Departamento'), ('land', 'Terreno')], max_length=100, null=True)),
                ('wide', models.FloatField(default=0)),
                ('long', models.FloatField(default=0)),
                ('ranking', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
