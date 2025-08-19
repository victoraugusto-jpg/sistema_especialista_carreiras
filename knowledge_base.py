# Definindo as regras da base de conhecimento (25 regras)
regras = [
    # 1. Tecnologia
    {"se": ["gosta_de_programar", "gosta_de_resolver_problemas_complexos"], "entao": "Desenvolvimento de Software"},
    {"se": ["gosta_de_liderar", "gosta_de_programar", "gosta_de_trabalhar_em_equipe"], "entao": "Gerência de TI"},
    {"se": ["e_criativo", "gosta_de_design"], "entao": "UX/UI Design"},
    {"se": ["gosta_de_trabalhar_com_numeros", "gosta_de_seguranca"], "entao": "Cibersegurança"},
    {"se": ["gosta_de_aprender_constantemente", "gosta_de_trabalhar_em_equipe"], "entao": "Analista de Dados"},

    # 2. Saúde
    {"se": ["gosta_de_ajudar_pessoas", "gosta_de_biologia_ou_quimica"], "entao": "Medicina"},
    {"se": ["gosta_de_cuidar_de_pessoas", "e_paciente"], "entao": "Enfermagem"},
    {"se": ["gosta_de_trabalhar_com_numeros", "gosta_de_biologia_ou_quimica"], "entao": "Pesquisa Médica"},

    # 3. Artes e Comunicação
    {"se": ["e_criativo", "gosta_de_escrever"], "entao": "Jornalismo"},
    {"se": ["e_criativo", "gosta_de_design"], "entao": "Design Gráfico"},
    {"se": ["e_criativo", "gosta_de_interagir_com_pessoas"], "entao": "Publicidade e Marketing"},
    {"se": ["gosta_de_trabalhar_sozinho", "e_criativo"], "entao": "Artista Plástico"},

    # 4. Finanças e Negócios
    {"se": ["gosta_de_liderar", "gosta_de_trabalhar_com_numeros"], "entao": "Administração de Empresas"},
    {"se": ["gosta_de_trabalhar_com_numeros", "e_analitico"], "entao": "Contabilidade"},
    {"se": ["gosta_de_liderar", "gosta_de_interagir_com_pessoas"], "entao": "Gestão de Recursos Humanos"},

    # 5. Educação e Pesquisa
    {"se": ["gosta_de_aprender_constantemente", "gosta_de_ajudar_pessoas"], "entao": "Professor"},
    {"se": ["gosta_de_aprender_constantemente", "e_analitico", "gosta_de_resolver_problemas_complexos"], "entao": "Pesquisador"},

    # 6. Setor Público e Jurídico
    {"se": ["gosta_de_escrever", "e_analitico"], "entao": "Advocacia"},
    {"se": ["gosta_de_ajudar_pessoas", "gosta_de_liderar", "gosta_de_trabalhar_em_equipe"], "entao": "Servidor Público"},

    # 7. Engenharia
    {"se": ["gosta_de_resolver_problemas_complexos", "gosta_de_trabalhar_com_numeros"], "entao": "Engenharia Civil"},
    {"se": ["gosta_de_liderar", "gosta_de_trabalhar_em_equipe", "gosta_de_resolver_problemas_complexos"], "entao": "Gerência de Projetos"},

    # 8. Outras Áreas
    {"se": ["gosta_de_cuidar_de_pessoas", "e_paciente"], "entao": "Psicologia"},
    {"se": ["gosta_de_interagir_com_pessoas", "e_analitico"], "entao": "Vendas"},
    {"se": ["gosta_de_trabalhar_com_numeros", "e_analitico"], "entao": "Economista"},
    {"se": ["gosta_de_trabalhar_sozinho", "gosta_de_escrever"], "entao": "Escritor"}
]

# Definindo as 10 perguntas iniciais
perguntas = {
    "gosta_de_programar": "Você gosta de programar ou tem interesse em tecnologia?",
    "gosta_de_ajudar_pessoas": "Você se sente confortável em ajudar e cuidar de outras pessoas?",
    "e_criativo": "Você se considera uma pessoa criativa e gosta de expressar suas ideias?",
    "gosta_de_trabalhar_com_numeros": "Você tem facilidade em matemática e raciocínio lógico?",
    "gosta_de_resolver_problemas_complexos": "Você gosta de resolver problemas complexos e encontrar soluções lógicas?",
    "gosta_de_trabalhar_em_equipe": "Você prefere trabalhar em equipe a trabalhar sozinho?",
    "gosta_de_liderar": "Você gosta de liderar equipes e tomar decisões?",
    "gosta_de_aprender_constantemente": "Você gosta de estar sempre aprendendo e se atualizando?",
    "gosta_de_interagir_com_pessoas": "Você se sente à vontade interagindo e se comunicando com muitas pessoas?",
    "e_analitico": "Você é uma pessoa analítica e gosta de examinar dados e fatos?",
    "gosta_de_design": "Você gosta de criar e trabalhar com elementos visuais?",
    "gosta_de_biologia_ou_quimica": "Você tem interesse em biologia ou química?",
    "gosta_de_escrever": "Você gosta de escrever e se comunicar através de textos?",
    "gosta_de_seguranca": "Você se interessa por segurança e proteção de dados?",
    "gosta_de_trabalhar_sozinho": "Você prefere trabalhar sozinho?"
}