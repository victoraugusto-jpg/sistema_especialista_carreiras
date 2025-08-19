# Arquivo: knowledge_base.py
# Base de Conhecimento para o Sistema Especialista de Carreira

# As regras são dicionários que contêm os fatos (SE), a conclusão (ENTÃO) e um peso de confiança.
# O peso reflete a força da relação entre os fatos e a conclusão.
regras = [
    # 1. Tecnologia (Peso de 0.2 a 0.3)
    {"se": ["gosta_de_programar", "gosta_de_resolver_problemas_complexos", "gosta_de_criacao_de_sistemas"], "entao": "Desenvolvimento de Software", "peso": 0.3},
    {"se": ["gosta_de_liderar", "gosta_de_programar", "gosta_de_trabalhar_em_equipe", "gosta_de_estrategia"], "entao": "Gerência de TI", "peso": 0.25},
    {"se": ["e_criativo", "gosta_de_design", "gosta_de_interacao_usuario"], "entao": "UX/UI Design", "peso": 0.2},
    {"se": ["gosta_de_trabalhar_com_numeros", "gosta_de_seguranca", "e_analitico"], "entao": "Cibersegurança", "peso": 0.25},
    {"se": ["gosta_de_aprender_constantemente", "gosta_de_trabalhar_em_equipe", "gosta_de_analise_dados"], "entao": "Analista de Dados", "peso": 0.2},

    # 2. Saúde (Peso de 0.2 a 0.3)
    {"se": ["gosta_de_ajudar_pessoas", "gosta_de_biologia_ou_quimica", "gosta_de_diagnostico_tratamento"], "entao": "Medicina", "peso": 0.3},
    {"se": ["gosta_de_cuidar_de_pessoas", "e_paciente", "gosta_de_rotinas_cuidados"], "entao": "Enfermagem", "peso": 0.2},
    {"se": ["gosta_de_trabalhar_com_numeros", "gosta_de_biologia_ou_quimica", "gosta_de_laboratorio"], "entao": "Pesquisa Médica", "peso": 0.25},

    # 3. Artes e Comunicação (Peso de 0.2 a 0.25)
    {"se": ["e_criativo", "gosta_de_escrever", "gosta_de_pesquisa_noticias"], "entao": "Jornalismo", "peso": 0.25},
    {"se": ["e_criativo", "gosta_de_design", "gosta_de_comunicacao_visual"], "entao": "Design Gráfico", "peso": 0.2},
    {"se": ["e_criativo", "gosta_de_interagir_com_pessoas", "gosta_de_persuasao"], "entao": "Publicidade e Marketing", "peso": 0.25},
    {"se": ["gosta_de_trabalhar_sozinho", "e_criativo", "gosta_de_expressao_artistica"], "entao": "Artista Plástico", "peso": 0.2},

    # 4. Finanças e Negócios (Peso de 0.2 a 0.3)
    {"se": ["gosta_de_liderar", "gosta_de_trabalhar_com_numeros", "gosta_de_planejamento_financeiro"], "entao": "Administração de Empresas", "peso": 0.3},
    {"se": ["gosta_de_trabalhar_com_numeros", "e_analitico", "gosta_de_organizacao_financeira"], "entao": "Contabilidade", "peso": 0.25},
    {"se": ["gosta_de_liderar", "gosta_de_interagir_com_pessoas", "gosta_de_gestao_pessoal"], "entao": "Gestão de Recursos Humanos", "peso": 0.2},

    # 5. Educação e Pesquisa (Peso de 0.2 a 0.25)
    {"se": ["gosta_de_aprender_constantemente", "gosta_de_ajudar_pessoas", "gosta_de_ensinar"], "entao": "Professor", "peso": 0.25},
    {"se": ["gosta_de_aprender_constantemente", "e_analitico", "gosta_de_resolver_problemas_complexos", "gosta_de_laboratorio"], "entao": "Pesquisador", "peso": 0.2},

    # 6. Setor Público e Jurídico (Peso de 0.25 a 0.3)
    {"se": ["gosta_de_escrever", "e_analitico", "gosta_de_leis_regulamentos"], "entao": "Advocacia", "peso": 0.3},
    {"se": ["gosta_de_ajudar_pessoas", "gosta_de_liderar", "gosta_de_trabalhar_em_equipe", "gosta_de_normas_publicas"], "entao": "Servidor Público", "peso": 0.25},

    # 7. Engenharia (Peso de 0.2 a 0.25)
    {"se": ["gosta_de_resolver_problemas_complexos", "gosta_de_trabalhar_com_numeros", "gosta_de_projetos_fisicos"], "entao": "Engenharia Civil", "peso": 0.25},
    {"se": ["gosta_de_liderar", "gosta_de_trabalhar_em_equipe", "gosta_de_resolver_problemas_complexos", "gosta_de_cronogramas"], "entao": "Gerência de Projetos", "peso": 0.2},

    # 8. Outras Áreas (Peso de 0.2 a 0.3)
    {"se": ["gosta_de_cuidar_de_pessoas", "e_paciente", "gosta_de_analisar_comportamento"], "entao": "Psicologia", "peso": 0.3},
    {"se": ["gosta_de_interagir_com_pessoas", "e_analitico", "gosta_de_negociacao"], "entao": "Vendas", "peso": 0.2},
    {"se": ["gosta_de_trabalhar_com_numeros", "e_analitico", "gosta_de_mercado_economia"], "entao": "Economista", "peso": 0.25},
    {"se": ["gosta_de_trabalhar_sozinho", "gosta_de_escrever", "gosta_de_narrativa"], "entao": "Escritor", "peso": 0.25}
]

# Definindo as 15 perguntas iniciais para coletar os fatores
perguntas = {
    "gosta_de_programar": "Você gosta de programar ou tem interesse em tecnologia?",
    "gosta_de_resolver_problemas_complexos": "Você gosta de resolver problemas complexos?",
    "gosta_de_criacao_de_sistemas": "Você se interessa em criar sistemas e aplicativos?",
    "gosta_de_liderar": "Você gosta de liderar equipes e tomar decisões?",
    "gosta_de_trabalhar_em_equipe": "Você prefere trabalhar em equipe?",
    "gosta_de_estrategia": "Você se interessa por estratégia e planejamento de longo prazo?",
    "e_criativo": "Você se considera uma pessoa criativa?",
    "gosta_de_design": "Você gosta de trabalhar com elementos visuais?",
    "gosta_de_interacao_usuario": "Você se interessa em entender como as pessoas interagem com produtos?",
    "gosta_de_trabalhar_com_numeros": "Você tem facilidade com matemática e números?",
    "gosta_de_seguranca": "Você se interessa por segurança de dados e informações?",
    "e_analitico": "Você é uma pessoa analítica?",
    "gosta_de_aprender_constantemente": "Você gosta de estar sempre aprendendo?",
    "gosta_de_analise_dados": "Você se interessa por analisar grandes volumes de dados?",
    "gosta_de_ajudar_pessoas": "Você se sente confortável em ajudar outras pessoas?",
    "gosta_de_biologia_ou_quimica": "Você tem interesse por biologia ou química?",
    "gosta_de_diagnostico_tratamento": "Você se interessa por diagnóstico e tratamento de doenças?",
    "gosta_de_cuidar_de_pessoas": "Você gosta de cuidar e dar suporte a outras pessoas?",
    "e_paciente": "Você se considera uma pessoa paciente?",
    "gosta_de_rotinas_cuidados": "Você se sente confortável com rotinas de cuidado?",
    "gosta_de_laboratorio": "Você se interessa por trabalho em laboratório?",
    "gosta_de_escrever": "Você gosta de escrever e se comunicar por texto?",
    "gosta_de_pesquisa_noticias": "Você se interessa por pesquisar e investigar notícias?",
    "gosta_de_comunicacao_visual": "Você gosta de se expressar através de elementos visuais?",
    "gosta_de_interagir_com_pessoas": "Você gosta de interagir com muitas pessoas?",
    "gosta_de_persuasao": "Você tem facilidade em persuadir e convencer pessoas?",
    "gosta_de_trabalhar_sozinho": "Você prefere trabalhar sozinho?",
    "gosta_de_expressao_artistica": "Você gosta de se expressar artisticamente?",
    "gosta_de_planejamento_financeiro": "Você se interessa por planejamento e organização financeira?",
    "gosta_de_organizacao_financeira": "Você gosta de organizar e controlar finanças?",
    "gosta_de_gestao_pessoal": "Você se interessa por gestão e desenvolvimento de pessoas?",
    "gosta_de_ensinar": "Você gosta de ensinar e compartilhar conhecimento?",
    "gosta_de_leis_regulamentos": "Você se interessa por leis e regulamentos?",
    "gosta_de_normas_publicas": "Você se interessa por normas e funcionamento do setor público?",
    "gosta_de_projetos_fisicos": "Você se interessa por projetos de construção ou infraestrutura?",
    "gosta_de_cronogramas": "Você gosta de planejar e gerenciar cronogramas?",
    "gosta_de_analisar_comportamento": "Você se interessa por analisar o comportamento humano?",
    "gosta_de_negociacao": "Você tem facilidade em negociar?",
    "gosta_de_mercado_economia": "Você se interessa por mercado e economia?",
    "gosta_de_narrativa": "Você gosta de criar histórias e narrativas?"
}