# Generated by Django 4.0.5 on 2022-06-16 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacoes', '0003_orgao_relatorio_estado_alter_baseinformacao_tipo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstatisticasAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_acesso', models.DateTimeField(auto_now_add=True)),
                ('informacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacoes.baseinformacao')),
            ],
        ),
    ]