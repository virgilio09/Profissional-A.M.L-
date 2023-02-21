# Generated by Django 4.0.6 on 2022-07-22 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('bairro', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('desativado', 'Desativado')], max_length=10)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('telefone01', models.CharField(max_length=15, verbose_name='Telefone 1')),
                ('telefone02', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone 2 (Opcional)')),
                ('descricao', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.categoria')),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicos.endereco')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Adicione images do seu serviço')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servico')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('status', models.CharField(choices=[('Lido', 'Lido'), ('Não Lido', 'Não Lido')], default='Não Lido', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servico')),
            ],
        ),
    ]
