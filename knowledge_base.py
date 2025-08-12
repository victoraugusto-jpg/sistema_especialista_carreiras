# Definindo as regras da base de conhecimento (pelo menos 10 regras, como solicitado)
regras = [
    {
        "se": ["gosta_de_programacao", "gosta_de_resolver_problemas_complexos"],
        "entao": "Tecnologia"
    },
    {
        "se": ["gosta_de_ajudar_pessoas", "gosta_de_biologia_ou_quimica"],
        "entao": "Saúde"
    },
    {
        "se": ["e_criativo", "gosta_de_trabalhar_sozinho"],
        "entao": "Artes e Design"
    },
    {
        "se": ["gosta_de_liderar", "gosta_de_trabalhar_com_numeros"],
        "entao": "Finanças e Negócios"
    },
    {
        "se": ["gosta_de_aprender_constantemente", "gosta_de_ajudar_pessoas"],
        "entao": "Educação e Pesquisa"
    },
    {
        "se": ["gosta_de_trabalhar_em_equipe", "gosta_de_trabalhar_com_numeros", "e_analitico"],
        "entao": "Finanças e Negócios"
    },
    {
        "se": ["gosta_de_programacao", "e_criativo"],
        "entao": "Tecnologia" # Pode ser Desenvolvimento Web, Design de Jogos, etc.
    },
    {
        "se": ["gosta_de_biologia_ou_quimica", "gosta_de_resolver_problemas_complexos"],
        "entao": "Saúde" # Pesquisa Médica, por exemplo.
    },
    {
        "se": ["gosta_de_liderar", "gosta_de_trabalhar_em_equipe"],
        "entao": "Finanças e Negócios" # Gerente, CEO, etc.
    },
    {
        "se": ["gosta_de_aprender_constantemente", "gosta_de_resolver_problemas_complexos"],
        "entao": "Educação e Pesquisa"
    }
]

# Definindo as perguntas iniciais (pelo menos 5 perguntas, como solicitado)
perguntas = {
    "gosta_de_programacao": "Você gosta de programar ou tem interesse em tecnologia?",
    "gosta_de_ajudar_pessoas": "Você se sente confortável em ajudar e cuidar de outras pessoas?",
    "e_criativo": "Você se considera uma pessoa criativa e gosta de expressar suas ideias?",
    "gosta_de_trabalhar_com_numeros": "Você tem facilidade em matemática e raciocínio lógico?",
    "gosta_de_resolver_problemas_complexos": "Você gosta de resolver problemas complexos e encontrar soluções lógicas?",
    "gosta_de_biologia_ou_quimica": "Você tem interesse por biologia ou química?",
    "gosta_de_liderar": "Você gosta de liderar equipes e tomar decisões?",
    "gosta_de_trabalhar_em_equipe": "Você prefere trabalhar em equipe?",
    "gosta_de_trabalhar_sozinho": "Você prefere trabalhar sozinho?",
    "gosta_de_aprender_constantemente": "Você gosta de estar sempre aprendendo e se atualizando?"
}