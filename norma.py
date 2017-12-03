# Programa para localizar um curso superior e as universidades que o lecionam.

campos_local_oferta = ["CO_LOCAL_OFERTA", "NO_LOCAL_OFERTA", "CO_IES", "CO_UF_LOCAL_OFERTA", "CO_MUNICIPIO_LOCAL_OFERTA", "IN_SEDE", "CO_CURSO_POLO", "CO_CURSO", "IN_LOCAL_OFERTA_NEAD", "IN_LOCAL_OFERTA_UAB", "IN_LOCAL_OFERTA_REITORIA", "IN_LOCAL_OFERTA_POLO", "IN_LOCAL_OFERTA_UNID_ACADEMICA", "DT_INICIO_FUNCIONAMENTO\n"]
campos_uf = ["CO_UF_LOCAL_OFERTA", "SGL_UF_LOCAL_OFERTA"]
campos_municipio = ["CO_MUNICIPIO_LOCAL_OFERTA", "NO_MUNICIPIO_LOCAL_OFERTA"]


######################################
#########ARQUIVO LOCAL OFERTA#########
######################################

local_oferta = open("DM_LOCAL_OFERTA.CSV", "r", encoding='ISO-8859-1')
linhas_totais = local_oferta.readlines()
local_oferta.close()

nomes = linhas_totais[0]
linhas = linhas_totais[1:]

campos = nomes.split("|")

local_oferta = open("LOCAL_OFERTA.CSV", "w", encoding='ISO-8859-1')
uf = open("UF.CSV", "w", encoding='ISO-8859-1')
municipio = open("MUNICIPIO.CSV", "w", encoding='ISO-8859-1')

lista_local_oferta = []
lista_uf = []
lista_municipio = []

local_oferta.write("|".join(campos_local_oferta))
uf.write("|".join(campos_uf)+"\n")
municipio.write("|".join(campos_municipio)+"\n")


######################################
########VERIFICACAO DOS CAMPOS########
######################################

for i in range(len(campos)):
	if (campos[i] in campos_local_oferta):
		lista_local_oferta.append(i)
	if (campos[i] in campos_uf):
		lista_uf.append(i)
	if (campos[i] in campos_municipio):
		lista_municipio.append(i)


linha_local_oferta = []
tabela_local_oferta = []
linha_uf = []
tabela_uf = []
linha_municipio = []
tabela_municipio = []

######################################
###############SEPARACAO##############
######################################

for linha in linhas:
	valor = linha.split("|")
	for i in range(len(valor)):

		####LOCAL OFERTA####
		if (i in lista_local_oferta):
			if i != lista_local_oferta[-1]:
				linha_local_oferta.append(valor[i])
			else:
				linha_local_oferta.append(valor[i])
				#if list(linha_local_oferta) not in tabela_local_oferta:
				tabela_local_oferta.append(list(linha_local_oferta))
				linha_local_oferta[:] = []
		if (i in lista_uf):
			if i != lista_uf[-1]:
				linha_uf.append(valor[i])
			else:
				linha_uf.append(valor[i])
				if list(linha_uf) not in tabela_uf:
					tabela_uf.append(list(linha_uf))
				linha_uf[:] = []
		if (i in lista_municipio):
			if i != lista_municipio[-1]:
				linha_municipio.append(valor[i])
			else:
				linha_municipio.append(valor[i])
				if list(linha_municipio) not in tabela_municipio:
					tabela_municipio.append(list(linha_municipio))
				linha_municipio[:] = []



######################################
###############IMPRIMIR###############
######################################

####LOCAL OFERTA####
for linha in tabela_local_oferta:
	local_oferta.write("|".join(linha))

lista_local_oferta.clear()
linha_local_oferta.clear()
tabela_local_oferta.clear()

lista_uf.clear()
lista_municipio.clear()

local_oferta.close()

######################################
#############ARQUIVO CURSO############
######################################

curso = open("DM_CURSO.CSV", "r", encoding='ISO-8859-1')
linhas_totais = curso.readlines()
curso.close()

nomes = linhas_totais[0]
linhas = linhas_totais[1:]

campos = nomes.split("|")

campos_curso =["CO_IES","CO_MUNICIPIO_CURSO","CO_UF_CURSO","NO_REGIAO_CURSO","IN_CAPITAL_CURSO","CO_CURSO","NO_CURSO","CO_SITUACAO_CURSO","DS_SITUACAO_CURSO","CO_OCDE","NO_OCDE","CO_OCDE_AREA_GERAL","NO_OCDE_AREA_GERAL","CO_OCDE_AREA_ESPECIFICA","NO_OCDE_AREA_ESPECIFICA","CO_OCDE_AREA_DETALHADA","NO_OCDE_AREA_DETALHADA","CO_GRAU_ACADEMICO","DS_GRAU_ACADEMICO","CO_MODALIDADE_ENSINO","DS_MODALIDADE_ENSINO","CO_NIVEL_ACADEMICO","DS_NIVEL_ACADEMICO","IN_GRATUITO","TP_ATRIBUTO_INGRESSO","NU_CARGA_HORARIA","DT_INICIO_FUNCIONAMENTO","DT_AUTORIZACAO_CURSO", "IN_AJUDA_DEFICIENTE", "IN_MATERIAL_DIGITAL", "IN_MATERIAL_AMPLIADO", "IN_MATERIAL_TATIL", "IN_MATERIAL_IMPRESSO", "IN_MATERIAL_AUDIO", "IN_MATERIAL_BRAILLE", "IN_MATERIAL_LIBRAS", "IN_DISCIPLINA_LIBRAS", "IN_TRADUTOR_LIBRAS", "IN_GUIA_INTERPRETE", "IN_RECURSOS_COMUNICACAO", "IN_RECURSOS_INFORMATICA", "IN_INTEGRAL_CURSO", "IN_MATUTINO_CURSO", "IN_VESPERTINO_CURSO", "IN_NOTURNO_CURSO", "NU_INTEGRALIZACAO_INTEGRAL", "NU_INTEGRALIZACAO_MATUTINO", "NU_INTEGRALIZACAO_VESPERTINO", "NU_INTEGRALIZACAO_NOTURNO", "NU_INTEGRALIZACAO_EAD", "IN_OFERECE_DISC_SEMI_PRES", "NU_PERC_CAR_HOR_SEMI_PRES", "IN_POSSUI_LABORATORIO", "QT_INSC_VAGAS_NOVAS_INT", "QT_INSC_VAGAS_NOVAS_MAT", "QT_INSC_VAGAS_NOVAS_VESP", "QT_INSC_VAGAS_NOVAS_NOT", "QT_INSC_VAGAS_NOVAS_EAD", "QT_INSC_VAGAS_REMAN_INT", "QT_INSC_VAGAS_REMAN_MAT", "QT_INSC_VAGAS_REMAN_VESP", "QT_INSC_VAGAS_REMAN_NOT", "QT_INSC_VAGAS_REMAN_EAD", "QT_INSC_VAGAS_PROG_ESP_INT", "QT_INSC_VAGAS_PROG_ESP_MAT", "QT_INSC_VAGAS_PROG_ESP_VESP", "QT_INSC_VAGAS_PROG_ESP_NOT", "QT_INSC_VAGAS_PROG_ESP_EAD", "QT_VAGAS_NOVAS_INTEGRAL", "QT_VAGAS_NOVAS_MATUTINO", "QT_VAGAS_NOVAS_VESPERTINO", "QT_VAGAS_NOVAS_NOTURNO", "QT_VAGAS_NOVAS_EAD", "QT_VAGAS_REMANESC_INTEGRAL", "QT_VAGAS_REMANESC_MATUTINO", "QT_VAGAS_REMANESC_VESPERTINO", "QT_VAGAS_REMANESC_NOTURNO", "QT_VAGAS_REMANESC_EAD", "QT_VAGAS_PROG_ESP_INTEGRAL", "QT_VAGAS_PROG_ESP_MATUTINO", "QT_VAGAS_PROG_ESP_VESPERTINO", "QT_VAGAS_PROG_ESP_NOTURNO", "QT_VAGAS_PROG_ESP_EAD", "QT_MATRICULA_CURSO", "QT_CONCLUINTE_CURSO", "QT_INGRESSO_CURSO", "QT_INGRESSO_VAGAS_NOVAS", "QT_VAGAS_TOTAIS\n"]

curso = open("CURSO.CSV", "w", encoding='ISO-8859-1')
curso.write("|".join(campos_curso))

lista_curso = []


######################################
########VERIFICACAO DOS CAMPOS########
######################################

for i in range(len(campos)):
	if (campos[i] in campos_curso):
		lista_curso.append(i)
	if (campos[i] in campos_uf):
		lista_uf.append(i)
	if (campos[i] in campos_municipio):
		lista_municipio.append(i)


linha_curso = []
tabela_curso = []


######################################
###############SEPARACAO##############
######################################

for linha in linhas:
	valor = linha.split("|")
	for i in range(len(valor)):

		if (i in lista_curso):
			if i != lista_curso[-1]:
				linha_curso.append(valor[i])
			else:
				linha_curso.append(valor[i])
				#if list(linha_local_oferta) not in tabela_local_oferta:
				tabela_curso.append(list(linha_curso))
				linha_curso[:] = []
		if (i in lista_uf):
			if i != lista_uf[-1]:
				linha_uf.append(valor[i])
			else:
				linha_uf.append(valor[i])
				if list(linha_uf) not in tabela_uf:
					tabela_uf.append(list(linha_uf))
				linha_uf[:] = []
		if (i in lista_municipio):
			if i != lista_municipio[-1]:
				linha_municipio.append(valor[i])
			else:
				linha_municipio.append(valor[i])
				if list(linha_municipio) not in tabela_municipio:
					tabela_municipio.append(list(linha_municipio))
				linha_municipio[:] = []


######################################
###############IMPRIMIR###############
######################################

for linha in tabela_curso:
	curso.write("|".join(linha))


lista_uf.clear()
lista_municipio.clear()
lista_curso.clear()

linha_curso.clear()
tabela_curso.clear()

curso.close()



######################################
#############ARQUIVO IES############
######################################

ies = open("DM_IES.CSV", "r", encoding='ISO-8859-1')
linhas_totais = ies.readlines()
ies.close()

nomes = linhas_totais[0]
linhas = linhas_totais[1:]

campos = nomes.split("|")

campos_ies = ["CO_IES", "NO_IES", "SGL_IES", "CO_MANTENEDORA", "CO_CATEGORIA_ADMINISTRATIVA", "CO_ORGANIZACAO_ACADEMICA", "CO_MUNICIPIO_IES", "CO_UF_IES", "NO_REGIAO_IES", "IN_CAPITAL_IES", "IN_ACESSO_PORTAL_CAPES", "IN_ACESSO_OUTRAS_BASES", "IN_REPOSITORIO_INSTITUCIONAL", "IN_BUSCA_INTEGRADA", "IN_SERVICO_INTERNET", "IN_PARTICIPA_REDE_SOCIAL", "IN_CATALOGO_ONLINE", "QT_PERIODICO_ELETRONICO", "QT_LIVRO_ELETRONICO", "IN_REFERENTE"]
campos_valores = ["CO_IES", "VL_RECEITA_PROPRIA", "VL_TRANSFERENCIA", "VL_OUTRA_RECEITA", "VL_DES_PESSOAL_REM_DOCENTE", "VL_DES_PESSOAL_REM_TECNICO", "VL_DES_PESSOAL_ENCARGO", "VL_DES_CUSTEIO", "VL_DES_INVESTIMENTO", "VL_DES_PESQUISA", "VL_DES_OUTRAS\n"]
campos_categoria_administrativa = ["CO_CATEGORIA_ADMINISTRATIVA", "DS_CATEGORIA_ADMINISTRATIVA"]
campos_organizacao_academica = ["CO_ORGANIZACAO_ACADEMICA", "DS_ORGANIZACAO_ACADEMICA"]
campos_tecnico = ["CO_IES", "QT_TEC_TOTAL", "QT_TEC_FUND_INCOMP_FEM", "QT_TEC_FUND_INCOMP_MASC", "QT_TEC_FUND_COMP_FEM", "QT_TEC_FUND_COMP_MASC", "QT_TEC_MEDIO_FEM", "QT_TEC_MEDIO_MASC", "QT_TEC_SUPERIOR_FEM", "QT_TEC_SUPERIOR_MASC", "QT_TEC_ESPECIALIZACAO_FEM", "QT_TEC_ESPECIALIZACAO_MASC", "QT_TEC_MESTRADO_FEM", "QT_TEC_MESTRADO_MASC", "QT_TEC_DOUTORADO_FEM", "QT_TEC_DOUTORADO_MASC"]
campos_mantenedora = ["CO_MANTENEDORA", "NO_MANTENEDORA"]

ies = open("IES.CSV", "w", encoding='ISO-8859-1')
ies.write("|".join(campos_ies)+"\n")
valores = open("VALORES.CSV", "w", encoding='ISO-8859-1')
valores.write("|".join(campos_valores))
categoria_administrativa = open("CATEGORIA_ADMINISTRATIVA.CSV", "w", encoding='ISO-8859-1')
categoria_administrativa.write("|".join(campos_categoria_administrativa)+"\n")
organizacao_academica = open("ORGANIZACAO_ACADEMICA.CSV", "w", encoding='ISO-8859-1')
organizacao_academica.write("|".join(campos_organizacao_academica)+"\n")
tecnico = open("TECNICO.CSV", "w", encoding='ISO-8859-1')
tecnico.write("|".join(campos_tecnico)+"\n")
mantenedora = open("MANTENEDORA.CSV", "w", encoding='ISO-8859-1')
mantenedora.write("|".join(campos_mantenedora)+"\n")

lista_ies = []
lista_mantenedora = []
lista_categoria_administrativa = []
lista_organizacao_academica = []
lista_tecnico = []
lista_valores = []


######################################
########VERIFICACAO DOS CAMPOS########
######################################

for i in range(len(campos)):
	if (campos[i] in campos_ies):
		lista_ies.append(i)
	if (campos[i] in campos_uf):
		lista_uf.append(i)
	if (campos[i] in campos_municipio):
		lista_municipio.append(i)
	if (campos[i] in campos_mantenedora):
		lista_mantenedora.append(i)
	if (campos[i] in campos_categoria_administrativa):
		lista_categoria_administrativa.append(i)
	if (campos[i] in campos_organizacao_academica):
		lista_organizacao_academica.append(i)
	if (campos[i] in campos_tecnico):
		lista_tecnico.append(i)
	if (campos[i] in campos_valores):
		lista_valores.append(i)


linha_ies = []
tabela_ies = []
linha_mantenedora = []
tabela_mantenedora = []
linha_categoria_administrativa = []
tabela_categoria_administrativa = []
linha_organizacao_academica = []
tabela_organizacao_academica = []
linha_tecnico = []
tabela_tecnico = []
linha_valores = []
tabela_valores = []


######################################
###############SEPARACAO##############
######################################

for linha in linhas:
	valor = linha.split("|")
	for i in range(len(valor)):
		if (i in lista_ies):
			if i != lista_ies[-1]:
				linha_ies.append(valor[i])
			else:
				linha_ies.append(valor[i])
				#if list(linha_local_oferta) not in tabela_local_oferta:
				tabela_ies.append(list(linha_ies))
				linha_ies[:] = []
		if (i in lista_uf):
			if i != lista_uf[-1]:
				linha_uf.append(valor[i])
			else:
				linha_uf.append(valor[i])
				if list(linha_uf) not in tabela_uf:
					tabela_uf.append(list(linha_uf))
				linha_uf[:] = []
		if (i in lista_municipio):
			if i != lista_municipio[-1]:
				linha_municipio.append(valor[i])
			else:
				linha_municipio.append(valor[i])
				if list(linha_municipio) not in tabela_municipio:
					tabela_municipio.append(list(linha_municipio))
				linha_municipio[:] = []
		if (i in lista_mantenedora):
			if i != lista_mantenedora[-1]:
				linha_mantenedora.append(valor[i])
			else:
				linha_mantenedora.append(valor[i])
				if list(linha_mantenedora) not in tabela_mantenedora:
					tabela_mantenedora.append(list(linha_mantenedora))
				linha_mantenedora[:] = []
		if (i in lista_categoria_administrativa):
			if i != lista_categoria_administrativa[-1]:
				linha_categoria_administrativa.append(valor[i])
			else:
				linha_categoria_administrativa.append(valor[i])
				if list(linha_categoria_administrativa) not in tabela_categoria_administrativa:
					tabela_categoria_administrativa.append(list(linha_categoria_administrativa))
				linha_categoria_administrativa[:] = []
		if (i in lista_organizacao_academica):
			if i != lista_organizacao_academica[-1]:
				linha_organizacao_academica.append(valor[i])
			else:
				linha_organizacao_academica.append(valor[i])
				if list(linha_organizacao_academica) not in tabela_organizacao_academica:
					tabela_organizacao_academica.append(list(linha_organizacao_academica))
				linha_organizacao_academica[:] = []
		if (i in lista_tecnico):
			if i != lista_tecnico[-1]:
				linha_tecnico.append(valor[i])
			else:
				linha_tecnico.append(valor[i])
				#if list(linha_local_oferta) not in tabela_local_oferta:
				tabela_tecnico.append(list(linha_tecnico))
				linha_tecnico[:] = []
		if (i in lista_valores):
			if i != lista_valores[-1]:
				linha_valores.append(valor[i])
			else:
				linha_valores.append(valor[i])
				#if list(linha_local_oferta) not in tabela_local_oferta:
				tabela_valores.append(list(linha_valores))
				linha_valores[:] = []



######################################
###############IMPRIMIR###############
######################################

for linha in tabela_ies:
	ies.write("|".join(linha)+"\n")
for linha in tabela_uf:
	uf.write("|".join(linha)+"\n")
for linha in tabela_municipio:
	municipio.write("|".join(linha)+"\n")
for linha in tabela_valores:
	valores.write("|".join(linha))
for linha in tabela_categoria_administrativa:
	categoria_administrativa.write("|".join(linha)+"\n")
for linha in tabela_organizacao_academica:
	organizacao_academica.write("|".join(linha)+"\n")
for linha in tabela_tecnico:
	tecnico.write("|".join(linha)+"\n")
for linha in tabela_mantenedora:
	mantenedora.write("|".join(linha)+"\n")


lista_uf.clear()
lista_municipio.clear()
lista_ies.clear()
lista_mantenedora.clear()
lista_categoria_administrativa.clear()
lista_organizacao_academica.clear()
lista_tecnico.clear()
lista_valores.clear()

linha_tecnico.clear()
tabela_tecnico.clear()

linha_valores.clear()
tabela_valores.clear()

linha_ies.clear()
tabela_ies.clear()

linha_mantenedora.clear()
tabela_mantenedora.clear()

linha_categoria_administrativa.clear()
tabela_categoria_administrativa.clear()

linha_organizacao_academica.clear()
tabela_organizacao_academica.clear()

mantenedora.close()
valores.close()
tecnico.close()
ies.close()
categoria_administrativa.close()
organizacao_academica.close()
municipio.close()
uf.close()

linha_uf.clear()
linha_municipio.clear()

tabela_uf.clear()
tabela_municipio.clear()


######################################
############ARQUIVO DOCENTE###########
######################################

docente = open("DM_DOCENTE.CSV", "r", encoding='ISO-8859-1')
linhas_totais = docente.readlines()
docente.close()

nomes = linhas_totais[0]
linhas = linhas_totais[1:]

campos = nomes.split("|")

campos_docente = ["CO_DOCENTE", "CO_SITUACAO_DOCENTE", "CO_ESCOLARIDADE_DOCENTE", "CO_REGIME_TRABALHO", "IN_SEXO_DOCENTE", "NU_ANO_DOCENTE_NASC", "NU_MES_DOCENTE_NASC", "NU_DIA_DOCENTE_NASC", "NU_IDADE_DOCENTE", "CO_COR_RACA_DOCENTE", "CO_PAIS_DOCENTE", "CO_NACIONALIDADE_DOCENTE", "CO_UF_NASCIMENTO", "CO_MUNICIPIO_NASCIMENTO", "IN_DOCENTE_DEFICIENCIA", "IN_DEF_CEGUEIRA", "IN_DEF_BAIXA_VISAO", "IN_DEF_SURDEZ", "IN_DEF_AUDITIVA", "IN_DEF_FISICA", "IN_DEF_SURDOCEGUEIRA", "IN_DEF_MULTIPLA", "IN_DEF_INTELECTUAL", "IN_ATU_EAD", "IN_ATU_EXTENSAO", "IN_ATU_GESTAO", "IN_ATU_GRAD_PRESENCIAL", "IN_ATU_POS_EAD", "IN_ATU_POS_PRESENCIAL", "IN_ATU_SEQUENCIAL", "IN_ATU_PESQUISA", "IN_BOLSA_PESQUISA", "IN_SUBSTITUTO", "IN_EXERCICIO_DT_REF", "IN_VISITANTE", "IN_VISITANTE_IFES_VINCULO\n"]
campos_regime_trabalho = ["CO_REGIME_TRABALHO", "DS_REGIME_TRABALHO"]
campos_ies_docente = ["CO_IES", "CO_DOCENTE_IES", "CO_DOCENTE"]
campos_cor_raca = ["CO_COR_RACA_DOCENTE", "DS_COR_RACA_DOCENTE"]
campos_nacionalidade = ["CO_NACIONALIDADE_DOCENTE", "DS_NACIONALIDADE_DOCENTE"]
campos_sexo = ["IN_SEXO_DOCENTE", "DS_SEXO_DOCENTE"]
campos_escolaridade_docente = ["CO_ESCOLARIDADE_DOCENTE", "DS_ESCOLARIDADE_DOCENTE"]
campos_situacao_docente = ["CO_SITUACAO_DOCENTE", "DS_SITUACAO_DOCENTE"]

campos_cor_raca_padrao = ["CO_COR_RACA", "DS_COR_RACA"]
campos_nacionalidade_padrao = ["CO_NACIONALIDADE", "DS_NACIONALIDADE"]
campos_sexo_padrao = ["IN_SEXO", "DS_SEXO"]


docente = open("DOCENTE.CSV", "w", encoding='ISO-8859-1')
docente.write("|".join(campos_docente))
regime_trabalho = open("REGIME_TRABALHO.CSV", "w", encoding='ISO-8859-1')
regime_trabalho.write("|".join(campos_regime_trabalho)+"\n")
ies_docente = open("IES_DOCENTE.CSV", "w", encoding='ISO-8859-1')
ies_docente.write("|".join(campos_ies_docente)+"\n")
cor_raca = open("COR_RACA.CSV", "w", encoding='ISO-8859-1')
cor_raca.write("|".join(campos_cor_raca_padrao)+"\n")
nacionalidade = open("NACIONALIDADE.CSV", "w", encoding='ISO-8859-1')
nacionalidade.write("|".join(campos_nacionalidade_padrao)+"\n")
sexo = open("SEXO.CSV", "w", encoding='ISO-8859-1')
sexo.write("|".join(campos_sexo_padrao)+"\n")
escolaridade_docente = open("ESCOLARIDADE_DOCENTE.CSV", "w", encoding='ISO-8859-1')
escolaridade_docente.write("|".join(campos_escolaridade_docente)+"\n")
situacao_docente = open("SITUACAO_DOCENTE.CSV", "w", encoding='ISO-8859-1')
situacao_docente.write("|".join(campos_situacao_docente)+"\n")

lista_docente = []
lista_regime_trabalho = []
lista_ies_docente = []
lista_cor_raca = []
lista_nacionalidade = []
lista_sexo = []
lista_escolaridade_docente = []
lista_situacao_docente = []

######################################
########VERIFICACAO DOS CAMPOS########
######################################

for i in range(len(campos)):
	if (campos[i] in campos_docente):
		lista_docente.append(i)
	if (campos[i] in campos_regime_trabalho):
		lista_regime_trabalho.append(i)
	if (campos[i] in campos_ies_docente):
		lista_ies_docente.append(i)
	if (campos[i] in campos_cor_raca):
		lista_cor_raca.append(i)
	if (campos[i] in campos_nacionalidade):
		lista_nacionalidade.append(i)
	if (campos[i] in campos_sexo):
		lista_sexo.append(i)
	if (campos[i] in campos_escolaridade_docente):
		lista_escolaridade_docente.append(i)
	if (campos[i] in campos_situacao_docente):
		lista_situacao_docente.append(i)

linha_docente = []
tabela_docente = []
linha_regime_trabalho = []
tabela_regime_trabalho = []
linha_ies_docente = []
tabela_ies_docente = []
linha_cor_raca = []
tabela_cor_raca = []
linha_nacionalidade = []
tabela_nacionalidade = []
linha_sexo = []
tabela_sexo = []
linha_escolaridade_docente = []
tabela_escolaridade_docente = []
linha_situacao_docente = []
tabela_situacao_docente = []


######################################
###############SEPARACAO##############
######################################

for linha in linhas:
	valor = linha.split("|")
	for i in range(len(valor)):
		if (i in lista_docente):
			if i != lista_docente[-1]:
				linha_docente.append(valor[i])
			else:
				linha_docente.append(valor[i])
				#if list(linha_local_oferta) not in tabela_local_oferta:
				tabela_docente.append(list(linha_docente))
				linha_docente[:] = []
		if (i in lista_regime_trabalho):
			if i != lista_regime_trabalho[-1]:
				linha_regime_trabalho.append(valor[i])
			else:
				linha_regime_trabalho.append(valor[i])
				if list(linha_regime_trabalho) not in tabela_regime_trabalho:
					tabela_regime_trabalho.append(list(linha_regime_trabalho))
				linha_regime_trabalho[:] = []
		if (i in lista_ies_docente):
			if i != lista_ies_docente[-1]:
				linha_ies_docente.append(valor[i])
			else:
				linha_ies_docente.append(valor[i])
				#if list(linha_ies_docente) not in tabela_ies_docente:
				tabela_ies_docente.append(list(linha_ies_docente))
				linha_ies_docente[:] = []
		if (i in lista_cor_raca):
			if i != lista_cor_raca[-1]:
				linha_cor_raca.append(valor[i])
			else:
				linha_cor_raca.append(valor[i])
				if list(linha_cor_raca) not in tabela_cor_raca:
					tabela_cor_raca.append(list(linha_cor_raca))
				linha_cor_raca[:] = []
		if (i in lista_nacionalidade):
			if i != lista_nacionalidade[-1]:
				linha_nacionalidade.append(valor[i])
			else:
				linha_nacionalidade.append(valor[i])
				if list(linha_nacionalidade) not in tabela_nacionalidade:
					tabela_nacionalidade.append(list(linha_nacionalidade))
				linha_nacionalidade[:] = []
		if (i in lista_sexo):
			if i != lista_sexo[-1]:
				linha_sexo.append(valor[i])
			else:
				linha_sexo.append(valor[i])
				if list(linha_sexo) not in tabela_sexo:
					tabela_sexo.append(list(linha_sexo))
				linha_sexo[:] = []
		if (i in lista_escolaridade_docente):
			if i != lista_escolaridade_docente[-1]:
				linha_escolaridade_docente.append(valor[i])
			else:
				linha_escolaridade_docente.append(valor[i])
				if list(linha_escolaridade_docente) not in tabela_escolaridade_docente:
					tabela_escolaridade_docente.append(list(linha_escolaridade_docente))
				linha_escolaridade_docente[:] = []
		if (i in lista_situacao_docente):
			if i != lista_situacao_docente[-1]:
				linha_situacao_docente.append(valor[i])
			else:
				linha_situacao_docente.append(valor[i])
				if list(linha_situacao_docente) not in tabela_situacao_docente:
					tabela_situacao_docente.append(list(linha_situacao_docente))
				linha_situacao_docente[:] = []




######################################
###############IMPRIMIR###############
######################################

for linha in tabela_docente:
	docente.write("|".join(linha))
for linha in tabela_regime_trabalho:
	regime_trabalho.write("|".join(linha)+"\n")
for linha in tabela_ies_docente:
	ies_docente.write("|".join(linha)+"\n")
for linha in tabela_escolaridade_docente:
	escolaridade_docente.write("|".join(linha)+"\n")
for linha in tabela_situacao_docente:
	situacao_docente.write("|".join(linha)+"\n")



lista_docente.clear()
lista_regime_trabalho.clear()
lista_ies_docente.clear()
lista_cor_raca.clear()
lista_nacionalidade.clear()
lista_sexo.clear()
lista_escolaridade_docente.clear()
lista_situacao_docente.clear()

linha_docente.clear()
tabela_docente.clear()

linha_regime_trabalho.clear()
tabela_regime_trabalho.clear()

linha_ies_docente.clear()
tabela_ies_docente.clear()

linha_escolaridade_docente.clear()
tabela_escolaridade_docente.clear()

linha_situacao_docente.clear()
tabela_situacao_docente.clear()

docente.close()
regime_trabalho.close()
ies_docente.close()
escolaridade_docente.close()
situacao_docente.close()


######################################
#############ARQUIVO ALUNO############
######################################

aluno = open("DM_ALUNO.CSV", "r", encoding='ISO-8859-1')
linhas_totais = aluno.readlines()
aluno.close()

nomes = linhas_totais[0]
linhas = linhas_totais[1:]

campos = nomes.split("|")

campos_aluno = ["CO_IES", "CO_ALUNO", "CO_COR_RACA_ALUNO", "IN_SEXO_ALUNO", "NU_ANO_ALUNO_NASC", "NU_MES_ALUNO_NASC", "NU_DIA_ALUNO_NASC", "NU_IDADE_ALUNO", "CO_NACIONALIDADE_ALUNO", "CO_PAIS_ORIGEM_ALUNO", "CO_UF_NASCIMENTO", "CO_MUNICIPIO_NASCIMENTO", "IN_ALUNO_DEF_TGD_SUPER", "IN_DEF_AUDITIVA", "IN_DEF_FISICA", "IN_DEF_INTELECTUAL", "IN_DEF_MULTIPLA", "IN_DEF_SURDEZ", "IN_DEF_SURDOCEGUEIRA", "IN_DEF_BAIXA_VISAO", "IN_DEF_CEGUEIRA", "IN_DEF_SUPERDOTACAO", "IN_TGD_AUTISMO_INFANTIL", "IN_TGD_SINDROME_ASPERGER", "IN_TGD_SINDROME_RETT", "IN_TGD_TRANSTOR_DESINTEGRATIVO"]
campos_cor_raca = ["CO_COR_RACA_ALUNO", "DS_COR_RACA_ALUNO"]
campos_nacionalidade = ["CO_NACIONALIDADE_ALUNO", "DS_NACIONALIDADE_ALUNO"]
campos_sexo = ["IN_SEXO_ALUNO", "DS_SEXO_ALUNO"]
campos_situacao_aluno = ["CO_ALUNO_SITUACAO", "DS_ALUNO_SITUACAO"]
campos_turno = ["CO_TURNO_ALUNO", "DS_TURNO_ALUNO"]
campos_curso_aluno = ["CO_CURSO", "NO_CURSO", "CO_TURNO_ALUNO", "CO_ALUNO_CURSO", "CO_ALUNO_CURSO_ORIGEM", "CO_ALUNO", "CO_ALUNO_SITUACAO", "QT_CARGA_HORARIA_TOTAL", "QT_CARGA_HORARIA_INTEG", "DT_INGRESSO_CURSO", "IN_ING_VESTIBULAR", "IN_ING_ENEM", "IN_ING_AVALIACAO_SERIADA", "IN_ING_SELECAO_SIMPLIFICADA", "IN_ING_SELECAO_VAGA_REMANESC", "IN_ING_SELECAO_VAGA_PROG_ESPEC", "IN_ING_TRANSF_EXOFFICIO", "IN_ING_DECISAO_JUDICIAL", "IN_ING_CONVENIO_PECG", "IN_RESERVA_VAGAS", "IN_RESERVA_ETNICO", "IN_RESERVA_DEFICIENCIA", "IN_RESERVA_ENSINO_PUBLICO", "IN_RESERVA_RENDA_FAMILIAR", "IN_RESERVA_OUTRA", "IN_FINANC_ESTUDANTIL", "IN_FIN_REEMB_FIES", "IN_FIN_REEMB_ESTADUAL", "IN_FIN_REEMB_MUNICIPAL", "IN_FIN_REEMB_PROG_IES", "IN_FIN_REEMB_ENT_EXTERNA", "IN_FIN_REEMB_OUTRA", "IN_FIN_NAOREEMB_PROUNI_INTEGR", "IN_FIN_NAOREEMB_PROUNI_PARCIAL", "IN_FIN_NAOREEMB_ESTADUAL", "IN_FIN_NAOREEMB_MUNICIPAL", "IN_FIN_NAOREEMB_PROG_IES", "IN_FIN_NAOREEMB_ENT_EXTERNA", "IN_FIN_NAOREEMB_OUTRA", "IN_APOIO_SOCIAL", "IN_APOIO_ALIMENTACAO", "IN_APOIO_BOLSA_PERMANENCIA", "IN_APOIO_BOLSA_TRABALHO", "IN_APOIO_MATERIAL_DIDATICO", "IN_APOIO_MORADIA", "IN_APOIO_TRANSPORTE", "IN_ATIVIDADE_EXTRACURRICULAR", "IN_COMPL_ESTAGIO", "IN_COMPL_EXTENSAO", "IN_COMPL_MONITORIA", "IN_COMPL_PESQUISA", "IN_BOLSA_ESTAGIO", "IN_BOLSA_EXTENSAO", "IN_BOLSA_MONITORIA", "IN_BOLSA_PESQUISA", "CO_TIPO_ESCOLA_ENS_MEDIO", "IN_ALUNO_PARFOR", "CO_SEMESTRE_CONCLUSAO", "CO_SEMESTRE_REFERENCIA", "IN_MOBILIDADE_ACADEMICA", "CO_MOBILIDADE_ACADEMICA", "CO_MOBILIDADE_ACADEMICA_INTERN", "CO_IES_DESTINO", "CO_PAIS_DESTINO", "IN_MATRICULA", "IN_CONCLUINTE", "IN_INGRESSO_TOTAL", "IN_INGRESSO_VAGA_NOVA", "ANO_INGRESSO\n"]

aluno = open("ALUNO.CSV", "w", encoding='ISO-8859-1')
aluno.write("|".join(campos_aluno)+"\n")
situacao_aluno = open("SITUACAO_ALUNO.CSV", "w", encoding='ISO-8859-1')
situacao_aluno.write("|".join(campos_situacao_aluno)+"\n")
turno = open("TURNO.CSV", "w", encoding='ISO-8859-1')
turno.write("|".join(campos_turno)+"\n")
curso_aluno = open("CURSO_ALUNO.CSV", "w", encoding='ISO-8859-1')
curso_aluno.write("|".join(campos_curso_aluno))

lista_aluno = []
lista_situacao_aluno = []
lista_turno = []
lista_curso_aluno = []

######################################
########VERIFICACAO DOS CAMPOS########
######################################

for i in range(len(campos)):
	if (campos[i] in campos_aluno):
		lista_aluno.append(i)
	if (campos[i] in campos_situacao_aluno):
		lista_situacao_aluno.append(i)
	if (campos[i] in campos_turno):
		lista_turno.append(i)
	if (campos[i] in campos_cor_raca):
		lista_cor_raca.append(i)
	if (campos[i] in campos_nacionalidade):
		lista_nacionalidade.append(i)
	if (campos[i] in campos_sexo):
		lista_sexo.append(i)
	if (campos[i] in campos_curso_aluno):
		lista_curso_aluno.append(i)

linha_aluno = []
tabela_aluno = []
linha_situacao_aluno = []
tabela_situacao_aluno = []
linha_turno = []
tabela_turno = []
linha_curso_aluno = []
tabela_curso_aluno = []


######################################
###############SEPARACAO##############
######################################

for linha in linhas:
	valor = linha.split("|")
	for i in range(len(valor)):
		if (i in lista_aluno):
			if i != lista_aluno[-1]:
				linha_aluno.append(valor[i])
			else:
				linha_aluno.append(valor[i])
				#if list(linha_aluno) not in tabela_aluno:
				tabela_aluno.append(list(linha_aluno))
				linha_aluno[:] = []
		if (i in lista_situacao_aluno):
			if i != lista_situacao_aluno[-1]:
				linha_situacao_aluno.append(valor[i])
			else:
				linha_situacao_aluno.append(valor[i])
				if list(linha_situacao_aluno) not in tabela_situacao_aluno:
					tabela_situacao_aluno.append(list(linha_situacao_aluno))
				linha_situacao_aluno[:] = []
		if (i in lista_turno):
			if i != lista_turno[-1]:
				linha_turno.append(valor[i])
			else:
				linha_turno.append(valor[i])
				if list(linha_turno) not in tabela_turno:
					tabela_turno.append(list(linha_turno))
				linha_turno[:] = []
		if (i in lista_cor_raca):
			if i != lista_cor_raca[-1]:
				linha_cor_raca.append(valor[i])
			else:
				linha_cor_raca.append(valor[i])
				if list(linha_cor_raca) not in tabela_cor_raca:
					tabela_cor_raca.append(list(linha_cor_raca))
				linha_cor_raca[:] = []
		if (i in lista_nacionalidade):
			if i != lista_nacionalidade[-1]:
				linha_nacionalidade.append(valor[i])
			else:
				linha_nacionalidade.append(valor[i])
				if list(linha_nacionalidade) not in tabela_nacionalidade:
					tabela_nacionalidade.append(list(linha_nacionalidade))
				linha_nacionalidade[:] = []
		if (i in lista_sexo):
			if i != lista_sexo[-1]:
				linha_sexo.append(valor[i])
			else:
				linha_sexo.append(valor[i])
				if list(linha_sexo) not in tabela_sexo:
					tabela_sexo.append(list(linha_sexo))
				linha_sexo[:] = []
		if (i in lista_curso_aluno):
			if i != lista_curso_aluno[-1]:
				linha_curso_aluno.append(valor[i])
			else:
				linha_curso_aluno.append(valor[i])
				#if list(linha_escolaridade_docente) not in tabela_escolaridade_docente:
				tabela_curso_aluno.append(list(linha_curso_aluno))
				linha_curso_aluno[:] = []


######################################
###############IMPRIMIR###############
######################################

for linha in tabela_aluno:
	aluno.write("|".join(linha)+"\n")
for linha in tabela_nacionalidade:
	nacionalidade.write("|".join(linha)+"\n")
for linha in tabela_sexo:
	sexo.write("|".join(linha)+"\n")
for linha in tabela_cor_raca:
	cor_raca.write("|".join(linha)+"\n")
for linha in tabela_situacao_aluno:
	situacao_aluno.write("|".join(linha)+"\n")
for linha in tabela_curso_aluno:
	curso_aluno.write("|".join(linha))
for linha in tabela_turno:
	turno.write("|".join(linha)+"\n")

lista_aluno.clear()
lista_nacionalidade.clear()
lista_sexo.clear()
lista_cor_raca.clear()
lista_situacao_aluno.clear()
lista_curso_aluno.clear()
lista_turno.clear()

linha_aluno.clear()
tabela_aluno.clear()

linha_cor_raca.clear()
tabela_cor_raca.clear()

linha_nacionalidade.clear()
tabela_nacionalidade.clear()

linha_sexo.clear()
tabela_sexo.clear()

linha_situacao_aluno.clear()
tabela_situacao_aluno.clear()

linha_curso_aluno.clear()
tabela_curso_aluno.clear()

linha_turno.clear()
tabela_turno.clear()

aluno.close()
turno.close()
curso_aluno.close()
situacao_aluno.close()
cor_raca.close()
sexo.close()
nacionalidade.close()
