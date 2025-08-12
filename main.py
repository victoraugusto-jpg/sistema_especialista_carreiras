# Importa a base de conhecimento do arquivo knowledge_base.py
from knowledge_base import regras, perguntas

def coletar_fatos_do_usuario():
    """Coleta as respostas do usuário para as perguntas iniciais."""
    fatos = {}
    print("Olá! Vamos descobrir qual área de carreira mais se encaixa com você.")
    for chave, pergunta in perguntas.items():
        resposta = input(f"{pergunta} (sim/nao): ").lower()
        fatos[chave] = resposta == 'sim'
    return fatos

def motor_de_inferencia(fatos):
    """Aplica as regras para encontrar as áreas de carreira."""
    conclusoes = []
    for regra in regras:
        # Verifica se todas as condições da regra são verdadeiras
        condicoes_atendidas = all(fatos.get(condicao, False) for condicao in regra["se"])
        if condicoes_atendidas:
            conclusoes.append(regra["entao"])
    return conclusoes

def main():
    """Função principal que executa o sistema especialista."""
    fatos_iniciais = coletar_fatos_do_usuario()
    recomendacoes = motor_de_inferencia(fatos_iniciais)

    print("\n--- Resultado ---")
    if recomendacoes:
        print("As áreas de carreira que mais se encaixam com o seu perfil são:")
        for recomendacao in set(recomendacoes): # Usamos set para evitar duplicações
            print(f"- {recomendacao}")
    else:
        print("Não foi possível encontrar uma área de carreira que se encaixe com seu perfil.")

if __name__ == "__main__":
    main()