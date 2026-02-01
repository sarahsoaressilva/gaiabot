from django.db import models

# Create your models here.

# Dados Municipais
class emission_city(models.Model):
    type_emission = [("1", "Emissão"), ("2", "Remoção"), ("3", "Bunker")]

    id = models.AutoField(primary_key=True, null=False, blank=False)
    city = models.CharField(max_length=150, null=True, blank=True)
    emission_type = models.CharField(max_length=100, choices=type_emission)
    setor = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    sub_category = models.CharField(max_length=200, null=True, blank=True)
    obs = models.CharField(max_length=150, null=True, blank=True)
    activity = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    municipio = models.CharField(max_length=150, null=True, blank=True)
    id_municipio = models.IntegerField(null=True, blank=True)
    
    # {1977: 1000, 1975: 2000 ...}
    valores_anuais = models.JSONField(
        default=dict,
        help_text="Dicionario com ano chave e emissão como valor"
    )
