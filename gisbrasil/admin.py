from django.contrib.gis import admin
from models import *

class MunicipioAdmin(admin.GeoModelAdmin):
    list_filter = ['sigla', 'regiao', 'nome_mesorregiao',
        'nome_microrregiao']
    list_display = ['nome_municipio', 'sigla', 'regiao',
        'nome_mesorregiao', 'nome_microrregiao']
    search_fields = ['nome_municipio']

class PortoAlegreBairroAdmin(admin.GeoModelAdmin):
    list_filter = ['oficial']
    list_display = ['codigo_bairro', 'nome_bairro', 'oficial']
    search_fields = ['nome_bairro']

class PortoAlegreAcidenteTransitoAdmin(admin.GeoModelAdmin):
    list_display = ['dataset_id', 'data_hora', 'logradouro1',
        'logradouro2', 'local', 'tipo_acidente', 'noite_dia', 'tempo']
    list_filter = ['tipo_acidente', 'noite_dia', 'fonte', 'local',
        'data_hora', 'tempo']
    search_fields = ['logradouro1', 'logradouro2', 'dataset_id']

class PortoAlegreTaxiAdmin(admin.GeoModelAdmin):
    list_display = ['idtaxi', 'endereco', 'telefone']
    search_fields = ['idtaxi', 'endereco', 'telefone']

class PortoAlegreEstacaoBikePoaAdmin(admin.GeoModelAdmin):
    list_display = ['dataset_id', 'numero', 'nome']
    search_fields = ['dataset_id', 'numero', 'nome']

class PortoAlegreErbAdmin(admin.GeoModelAdmin):
    list_display = ['dataset_id', 'empresa_01', 'empresa_02',
        'empresa_03', 'empresa_04', 'site_01', 'site_02',
         'site_03', 'site_04', 'nome_da_er', 'n13',
         'bairro', 'tipo']
    search_fields = ['dataset_id', 'nome_da_er', 'tipo', 'bairro',
        'empresa_01', 'empresa_02', 'empresa_03', 'empresa_04', 
        'site_01', 'site_02', 'site_03', 'site_04',]   
    list_filter = ['tipo', 'empresa_01', 'empresa_02', 'empresa_03',
        'empresa_04', 'tipo', 'bairro']

class PortoAlegreConteineresLixoAdmin(admin.GeoModelAdmin):
    list_display = ['nro', 'logradouro', 'referencia', 'lote']
    search_fields = ['lote', 'passeio', 'area_azul', 'av_status',
        'av_side', 'av_status', 'referencia']
    list_filter = ['passeio', 'cat', 'area_azul', 'av_status',
        'av_side']

class PortoAlegreLixeirasAdmin(admin.GeoModelAdmin):
    list_display = ['cod_lograd', 'nome', 'referencia', 'lote', 'data_insta']
    list_filter = ['categoria', 'data_insta', 'secao']

class PortoAlegreEspacoCulturalAdmin(admin.GeoModelAdmin):
    list_display = ['_id', 'name', 'endereco_formatado', 'tipo', 'bairro']
    list_filter = ['bairro', 'tipo', 'categoria']    

class PortoAlegreParadaAdmin(admin.GeoModelAdmin):
    list_display = ['idparada', 'codigo', 'terminal']
    search_fields = ['idparada', 'codigo']

class PortoAlegreEixoAdmin(admin.GeoModelAdmin):
    list_display = ['nome', 'abreviatura', 'cep', 'grupo_cep',
        'preposicao', 'categoria', 'smf_i_i', 'smf_i_f', 'smf_p_i',
        'smf_p_f']
    search_fields = ['nome', 'abreviatura', 'cep']
    list_filter = ['categoria']

admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(PortoAlegreBairro, PortoAlegreBairroAdmin)
admin.site.register(PortoAlegreAcidenteTransito, PortoAlegreAcidenteTransitoAdmin)
admin.site.register(PortoAlegreTaxi, PortoAlegreTaxiAdmin)
admin.site.register(PortoAlegreEstacaoBikePoa, PortoAlegreEstacaoBikePoaAdmin)
admin.site.register(PortoAlegreParada, PortoAlegreParadaAdmin)
admin.site.register(PortoAlegreEixo, PortoAlegreEixoAdmin)
admin.site.register(PortoAlegreErb, PortoAlegreErbAdmin)
admin.site.register(PortoAlegreConteinerLixo, PortoAlegreConteineresLixoAdmin)
admin.site.register(PortoAlegreLixeiras, PortoAlegreLixeirasAdmin)
admin.site.register(PortoAlegreEspacoCultural, PortoAlegreEspacoCulturalAdmin)


