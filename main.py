# Arquivo: main.py
# Motor de Inferência e Interface do Usuário para o Sistema Especialista

# Importa a base de conhecimento do arquivo knowledge_base.py
from knowledge_base import regras, perguntas

def coletar_fatos_do_usuario():
    """
    Coleta as respostas do usuário para as perguntas iniciais.
    Inclui validação para garantir que a resposta seja 'sim' ou 'nao'.
    """
    fatos = {}
    print("Olá! Vamos descobrir qual área de carreira mais se encaixa com você.")
    
    # Itera sobre as perguntas para coletar as respostas
    for chave, pergunta in perguntas.items():
        resposta_valida = False
        while not resposta_valida:
            resposta = input(f"\n{pergunta} (sim/nao): ").lower()
            if resposta in ["sim", "nao"]:
                fatos[chave] = resposta == 'sim'
                resposta_valida = True
            else:
                print("Resposta inválida. Por favor, digite 'sim' ou 'nao'.")
    return fatos

def motor_de_inferencia(fatos):
    """
    Aplica as regras para encontrar as áreas de carreira, somando os pesos
    das regras ativadas para calcular a pontuação de cada profissão.
    """
    # Dicionário para armazenar a pontuação de cada profissão
    pontuacoes = {}

    # Itera sobre todas as regras na base de conhecimento
    for regra in regras:
        # Verifica se todas as condições da regra são verdadeiras com base nos fatos do usuário
        condicoes_atendidas = all(fatos.get(condicao, False) for condicao in regra["se"])
        if condicoes_atendidas:
            profissao = regra["entao"]
            peso = regra["peso"]
            
            # Adiciona o peso da regra à pontuação da profissão
            pontuacoes[profissao] = pontuacoes.get(profissao, 0) + peso
    
    return pontuacoes

def main():
    """
    Função principal que executa o sistema especialista.
    Coleta os fatos, executa o motor de inferência e exibe as 3 principais recomendações.
    """
    # Coleta as respostas do usuário
    fatos_iniciais = coletar_fatos_do_usuario()
    
    # Executa o motor de inferência para obter as pontuações
    pontuacoes = motor_de_inferencia(fatos_iniciais)

    # Ordena as profissões pela pontuação em ordem decrescente
    ranking = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)

    print("\n--- Resultado ---")
    if ranking:
        print("As 3 principais áreas de carreira que se encaixam com seu perfil são:")
        # Exibe as 3 primeiras profissões do ranking
        for i, (profissao, pontuacao) in enumerate(ranking[:3]):
            # Transforma a pontuação em porcentagem (ex: 0.6 -> 60%)
            porcentagem = round(pontuacao * 100)
            print(f"{i+1}. {profissao}: {porcentagem}% de confiança")
    else:
        print("Não foi possível encontrar uma área de carreira que se encaixe com seu perfil. Tente responder 'sim' para mais perguntas!")

if __name__ == "__main__":
    main()