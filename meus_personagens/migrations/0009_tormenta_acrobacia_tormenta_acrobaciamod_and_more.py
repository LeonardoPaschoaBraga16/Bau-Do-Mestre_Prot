# Generated by Django 4.2.4 on 2023-09-10 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meus_personagens', '0008_remove_tormenta_acrobacia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tormenta',
            name='acrobacia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='acrobaciaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='acrobaciaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='adestramento',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='adestramentoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Car', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='adestramentoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='alcance1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='alcance2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='alcance3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='alcance4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='alcance5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='armaduraBonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkBonus1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkBonus2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkBonus3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkBonus4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkBonus5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDano1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDano2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDano3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDano4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDano5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDanoExtra1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDanoExtra2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDanoExtra3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDanoExtra4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkDanoExtra5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkNome1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkNome2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkNome3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkNome4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atkNome5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atletismo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atletismoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atletismoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atuacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atuacaoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='atuacaoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='bonusArmaduraItem',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='bonusEscudoItem',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='car',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='cavalgar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='cavalgarMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='cavalgarOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='classe',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tormenta',
            name='conhecimento',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='conhecimentoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='conhecimentoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='const',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='cura',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='curaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='curaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='dadoCrit1',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='dadoCrit2',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='dadoCrit3',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='dadoCrit4',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='dadoCrit5',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='des',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='desBonus',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='diplomacia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='diplomaciaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='diplomaciaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='divindade',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tormenta',
            name='enganacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='enganacaoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='enganacaoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='escudoBonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='forca',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='fortitude',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='fortitudeMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='fortitudeOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='furtividade',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='furtividadeMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='furtividadeOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='guerra',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='guerraMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='guerraOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='iniciativa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='iniciativaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='iniciativaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='inteli',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='intimidacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='intimidacaoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='intimidacaoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='intuicao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='intuicaoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='intuicaoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='investigacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='investigacaoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='investigacaoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='jogatina',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='jogatinaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='jogatinaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='ladinagem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='ladinagemMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='ladinagemOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='luta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='lutaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='lutaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='magiasCirculo1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='magiasCirculo2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='magiasCirculo3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='magiasCirculo4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='magiasCirculo5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='manaAtual',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='manaMax',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='misticismo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='misticismoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='misticismoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='multiplicadorCrit1',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='multiplicadorCrit2',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='multiplicadorCrit3',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='multiplicadorCrit4',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='multiplicadorCrit5',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='nobreza',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='nobrezaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='nobrezaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='nomeArmadura',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='nomeEscudo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio1Mod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio1Nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio1Outros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio2Mod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio2Nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='oficio2Outros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='origem',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='outrosBonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='penalidadeArmadura',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='penalidadeEscudo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='percepcao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='percepcaoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='percepcaoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pilotagem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pilotagemMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pilotagemOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pontaria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pontariaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pontariaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='proficiencias',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pvAtual',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='pvMax',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='reflexos',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='reflexosMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='reflexosOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='religiao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='religiaoMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='religiaoOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='sab',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='sobrevivencia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='sobrevivenciaMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='sobrevivenciaOutros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='vontade',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='vontadeMod',
            field=models.CharField(choices=[('For', 'For'), ('Des', 'Des'), ('Con', 'Con'), ('Int', 'Int'), ('Sab', 'Sab'), ('Car', 'Car')], default='Des', max_length=3),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='vontadeOutros',
            field=models.IntegerField(default=0),
        ),
    ]
