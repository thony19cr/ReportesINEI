# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ccpp',
            fields=[
                ('id', models.CharField(db_column='ID', db_index=True, primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=254)),
                ('ccdd', models.CharField(db_column='CCDD', max_length=254)),
                ('ccpp', models.IntegerField(db_column='CCPP')),
                ('ccdi', models.IntegerField(db_column='CCDI')),
                ('codccpp', models.CharField(db_column='CODCCPP', max_length=254)),
                ('nomccpp', models.IntegerField(db_column='NOMCCPP')),
                ('area', models.IntegerField(db_column='AREA')),
                ('viv_ccpp', models.IntegerField(db_column='VIV_CCPP')),
                ('categoria', models.CharField(db_column='CATEGORIA', max_length=254)),
                ('categoria_o', models.IntegerField(db_column='CATEGORIA_O')),
                ('idccpp', models.CharField(db_column='IDCCPP', max_length=40)),
            ],
            options={
                'db_table': 'TB_CCPP',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manzanas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=255)),
                ('codccpp', models.CharField(db_column='CODCCPP', max_length=255)),
                ('zona', models.CharField(db_column='ZONA', max_length=255)),
                ('manzana', models.CharField(db_column='MANZANA', max_length=255)),
                ('viv_mz', models.CharField(db_column='VIV_MZ', max_length=255)),
                ('cant_aeus', models.CharField(db_column='CANT_AEUS', max_length=255)),
                ('aeus', models.CharField(db_column='AEUS', max_length=255)),
                ('llave_mzs', models.CharField(db_column='LLAVE_MZS', max_length=255)),
            ],
            options={
                'db_table': 'TB_MZN',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('objectid', models.IntegerField(db_column='OBJECTID', db_index=True, primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=6)),
                ('zona', models.CharField(db_column='ZONA', max_length=5)),
                ('manzana', models.CharField(db_column='MANZANA', max_length=4)),
                ('aeu', models.IntegerField(db_column='AEU')),
                ('id_ruta', models.CharField(db_column='ID_RUTA', max_length=254)),
                ('viv_aeu', models.IntegerField(db_column='VIV_AEU')),
                ('flag', models.IntegerField(db_column='FLAG')),
                ('aeu_final', models.IntegerField(db_column='AEU_FINAL')),
                ('seccion', models.IntegerField(db_column='SECCION')),
                ('est_seg', models.CharField(db_column='EST_SEG', max_length=1)),
                ('est_croquis', models.CharField(db_column='EST_CROQUIS', max_length=1)),
                ('llave_mzs', models.CharField(db_column='LLAVE_MZS', max_length=1)),
                ('llave_aeu', models.CharField(db_column='LLAVE_AEU', max_length=1)),
            ],
            options={
                'db_table': 'TB_RUTAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Secciones',
            fields=[
                ('objectid', models.CharField(db_column='OBJECTID', db_index=True, max_length=254, primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=254)),
                ('zona', models.CharField(db_column='ZONA', max_length=254)),
                ('seccion', models.IntegerField(db_column='SECCION')),
                ('cant_viv', models.IntegerField(db_column='CANT_VIV')),
                ('llave_seccion', models.CharField(db_column='ZONA', max_length=40)),
            ],
            options={
                'db_table': 'TB_SECCIONES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ViviendaU',
            fields=[
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=6, primary_key=True, serialize=False)),
                ('ccdd', models.CharField(db_column='CCDD', max_length=2)),
                ('ccdi', models.CharField(db_column='CCDI', max_length=2)),
                ('codccpp', models.CharField(db_column='CODCCPP')),
                ('zona', models.CharField(db_column='ZONA', max_length=5)),
                ('manzana', models.CharField(db_column='MANZANA', max_length=4)),
                ('nomccpp', models.CharField(db_column='NOMCCPP', max_length=60)),
                ('departamento', models.CharField(db_column='DEPARTAMENTO', max_length=60)),
                ('provincia', models.CharField(db_column='PROVINCIA', max_length=50)),
                ('distrito', models.CharField(db_column='DISTRITO', max_length=50)),
                ('area', models.IntegerField(db_column='AREA')),
                ('frente_ord', models.IntegerField(db_column='FRENTE_ORD')),
                ('id_reg_or', models.IntegerField(db_column='ID_REG_OR')),
                ('aer_ini', models.CharField(db_column='AER_INI', max_length=3)),
                ('aer_fin', models.CharField(db_column='AER_FIN', max_length=3)),
                ('p19a', models.IntegerField(db_column='P19A')),
                ('p20', models.IntegerField(db_column='P20')),
                ('p20_o', models.CharField(db_column='P20_O', max_length=50)),
                ('p21', models.CharField(db_column='P21', max_length=60)),
                ('p21_a', models.CharField(db_column='P21_A', max_length=100)),
                ('p22_a', models.CharField(db_column='P22_A', max_length=4)),
                ('p22_b', models.CharField(db_column='P22_B', max_length=4)),
                ('p23', models.CharField(db_column='P23', max_length=3)),
                ('id_p23', models.IntegerField(db_column='ID_P23')),
                ('p23_nombre', models.CharField(db_column='P23_NOMBRE', max_length=50)),
                ('p23_vivpiso', models.IntegerField(db_column='P23_VIVPISO')),
                ('p23_viviendas', models.IntegerField(db_column='P23_VIVIENDAS')),
                ('p23_registros', models.IntegerField(db_column='P23_REGISTROS')),
                ('p24', models.CharField(db_column='P24', max_length=4)),
                ('p25', models.CharField(db_column='P25', max_length=4)),
                ('p26', models.CharField(db_column='P26', max_length=2)),
                ('p27_a', models.CharField(db_column='P27_A', max_length=4)),
                ('p27_b', models.CharField(db_column='P27_B', max_length=4)),
                ('p28', models.CharField(db_column='P28', max_length=4)),
                ('p29', models.IntegerField(db_column='P29')),
                ('p29_a', models.IntegerField(db_column='P29_A')),
                ('p29_1', models.IntegerField(db_column='P29_1')),
                ('p29_1_nombre', models.CharField(db_column='P29_1_NOMBRE', max_length=50)),
                ('p29m', models.IntegerField(db_column='P29M')),
                ('p29_o', models.CharField(db_column='P29_O', max_length=50)),
                ('p29_8_o', models.CharField(db_column='P29_8_O', max_length=100)),
                ('p29_p', models.CharField(db_column='P29_P', max_length=100)),
                ('p30', models.IntegerField(db_column='P30')),
                ('p31', models.IntegerField(db_column='P31')),
                ('p32', models.CharField(db_column='P32', max_length=100)),
                ('p35', models.CharField(db_column='P35', max_length=100)),
                ('or_viv_aeu', models.IntegerField(db_column='OR_VIV_AEU')),
            ],
            options={
                'db_table': 'TB_CPV0301_VIVIENDA_U',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ViviendaUrbana',
            fields=[
                ('id', models.IntegerField(db_column='ID', max_length=6, primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=6, primary_key=True)),
                ('ccdd', models.CharField(db_column='CCDD', max_length=2)),
                ('ccdi', models.CharField(db_column='CCDI', max_length=2)),
                ('codccpp', models.CharField(db_column='CODCCPP', max_length=4)),
                ('zona', models.CharField(db_column='ZONA', max_length=5)),
                ('manzana', models.CharField(db_column='MANZANA', max_length=4)),
                ('nomccpp', models.CharField(db_column='NOMCCPP', max_length=60)),
                ('departamento', models.CharField(db_column='DEPARTAMEN', max_length=60)),
                ('provincia', models.CharField(db_column='PROVINCIA', max_length=50)),
                ('distrito', models.CharField(db_column='DISTRITO', max_length=50)),
                ('area', models.IntegerField(db_column='AREA')),
                ('frente_ord', models.IntegerField(db_column='FRENTE_ORD')),
                ('id_reg_or', models.IntegerField(db_column='ID_REG_OR')),
                ('usolocal', models.IntegerField(db_column='USOLOCAL')),
                ('aeu', models.IntegerField(db_column='AEU')),
                ('or_viv_aeu', models.IntegerField(db_column='OR_VIV_AEU')),
                ('corte', models.IntegerField(db_column='CORTE')),
                ('llave_mzs', models.CharField(db_column='LLAVE_MZS', max_length=40)),
            ],
            options={
                'db_table': 'TB_VIVIENDAS_URBANO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zonacensal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubigeo', models.CharField(db_column='UBIGEO', max_length=255)),
                ('ccdd', models.CharField(db_column='CCDD', max_length=255)),
                ('ccpp', models.CharField(db_column='CCPP', max_length=255)),
                ('ccdi', models.CharField(db_column='CCDI', max_length=255)),
                ('codccpp', models.CharField(db_column='CODCCPP', max_length=255)),
                ('zona', models.CharField(db_column='ZONA', max_length=255)),
                ('idccpp', models.CharField(db_column='IDCCPP', max_length=40)),
                ('idzona', models.CharField(db_column='IDZONA', max_length=40)),
            ],
            options={
                'db_table': 'TB_ZONA_CENSAL',
                'managed': False,
            },
        ),
    ]
