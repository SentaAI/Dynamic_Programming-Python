"""
Arthur Berlofa Bosi - RM564438
Levi de Jesus - RM563279
Luigi Borghi - RM563096
Ulisses Ribeiro - RM562230
"""
from datetime import datetime

# Variáveis globais
capacidade_maxima = 40
parada_atual = -1

# Dicionario que vai armazenar cada parada
memoria_paradas = {}

# Dicionario que agrupa o movimento por hora
registro_horas = {}

# Funções
def registrar_fluxo(numero_parada, entradas, saidas, horario=None):
    """
    Essa função calcula a lotação do onibus na parada atual
    e armazena esses resultados na memória pra usar futuramente
    (como por exemplo um dash pra gerencia do sistema)
    """
    global parada_atual  # Permite alterar a variável global

    # Se o sensor não mandar o horario usamos o atual do sistema
    if horario is None:
        horario = datetime.now().strftime("%H:%M")

    # Se for a primeira parada, (nesse caso o terminal) a lotação anterior tem que ser 0
    if numero_parada == 0 or not memoria_paradas:
        lotacao_anterior = 0
    else:
        # Busca o subproblema que ja foi resolvido na memória
        lotacao_anterior = memoria_paradas[numero_parada - 1]['lotacao_atual']

    # Calcula a lotação atual, somando a anterior com as entradas e tirando as saídas
    nova_lotacao = lotacao_anterior + entradas - saidas
    
    # Usamos o max pra impedir que a lotação fique negativa
    nova_lotacao = max(0, nova_lotacao)

    # Salva o resultado no dicionário
    memoria_paradas[numero_parada] = {
        'horario': horario,
        'entradas': entradas,
        'saidas': saidas,
        'lotacao_atual': nova_lotacao,
        'assentos_livres': max(0, capacidade_maxima - nova_lotacao)
    }

    # Soma os embarques e guarda a maior lotação vista naquela hora
    hora = horario.split(":")[0] + "h"
    if hora not in registro_horas:
        registro_horas[hora] = {'embarques': 0, 'lotacao_maxima': 0}
    registro_horas[hora]['embarques'] += entradas
    registro_horas[hora]['lotacao_maxima'] = max(registro_horas[hora]['lotacao_maxima'], nova_lotacao)

    parada_atual = numero_parada
    return memoria_paradas[numero_parada]

# -----

def obter_status_painel():
    """
    Essa função retorna os status do onibus para nosso painel de controle,
    ela não calcula nada, só puxa os dados que ja temos
    """
    if parada_atual == -1:
        return {"Status": "Seu ônibus está no terminal e vai sair em breve."}

    estado = memoria_paradas[parada_atual]
    return {
        "Passageiros a bordo": f"{estado['lotacao_atual']} de {capacidade_maxima}",
        "Lugares livres pra você": estado['assentos_livres']
    }

# -----

def gerar_relatorio():
    """Usa o histórico memoizado para gerar insights pra gestão no fim do dia."""
    print("\n--- CONTROLE DE LOTAÇÃO DO ONIBUS ---")
    pico_entradas = 0
    parada_pico = 0
    
    for parada, dados in memoria_paradas.items():
        print(f"{dados['horario']} | Parada {parada:02d} | Embarcaram: {dados['entradas']:02d} | Desembarcaram: {dados['saidas']:02d} | Passageiros a bordo: {dados['lotacao_atual']:02d}/{capacidade_maxima}")

        # Definição do pico de parada
        if dados['entradas'] > pico_entradas:
            pico_entradas = dados['entradas']
            parada_pico = parada

    print(f"\nNa Parada {parada_pico} embarcou mais gente de uma vez ({pico_entradas} pessoas).")
    print("Reforçar a frota nesse ponto diminui a espera e o aperto pra quem embarca ali.")

    # Relatório por hora
    print("\n--- CONFORTO DOS PASSAGEIROS POR HORA ---")
    for hora, dados in sorted(registro_horas.items()):
        print(f"{hora} | Passageiros que embarcaram: {dados['embarques']:02d} | Ônibus mais cheio: {dados['lotacao_maxima']:02d}/{capacidade_maxima}")

    # Horario que o onibus ficou mais cheio (olhando a lotação, não só quem entrou)
    hora_pico = max(registro_horas, key=lambda h: registro_horas[h]['lotacao_maxima'])
    lotacao_pico = registro_horas[hora_pico]['lotacao_maxima']

    print(f"\nO horário mais apertado pros passageiros foi às {hora_pico}, com {lotacao_pico} pessoas a bordo "
          f"({lotacao_pico * 100 // capacidade_maxima}% da capacidade).")
    print("Se isso se repetir todo dia, vale colocar mais ônibus nesse horário pra ninguém viajar espremido.")

# -----

# 1. Os sensores IoT enviam dados a cada parada
registrar_fluxo(numero_parada=0, entradas=15, saidas=0, horario="06:40") # Terminal
registrar_fluxo(numero_parada=1, entradas=5, saidas=2, horario="06:55") 
registrar_fluxo(numero_parada=2, entradas=22, saidas=4, horario="07:15") 
registrar_fluxo(numero_parada=3, entradas=2, saidas=18, horario="07:40") 

# 2. O passageiro observa o ônibus chegar e olha para a telinha
print("--- Ônibus Agora ---")

# Vizualização formatadinha do status do painel
for i in obter_status_painel().items():
    print(f"{i[0]}: {i[1]}")

# 3. No fim do dia geramos o relatório
gerar_relatorio()