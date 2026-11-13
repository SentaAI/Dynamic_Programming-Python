# Dynamic_Programming-Python

Sistema de lotação de ônibus em tempo real usando programação dinâmica.

🔗 **Site explicativo da solução:** https://senta-ai-sigma.vercel.app/

## Integrantes

- Arthur Berlofa Bosi - RM564438
- Levi de Jesus - RM563279
- Luigi Borghi - RM563096
- Ulisses Ribeiro - RM562230

## A ideia

Sensores IoT na porta do ônibus contam quantas pessoas entram e saem em cada parada. Com isso:

- **O passageiro** vê numa tela quantas pessoas estão a bordo e quantos lugares estão livres antes de embarcar.
- **Os donos dos ônibus** recebem no fim do dia um relatório com as paradas e os horários mais cheios, para saber onde colocar mais ônibus.

## Programação dinâmica

A lotação de uma parada depende só da parada anterior:

```
lotação(n) = lotação(n-1) + entradas(n) - saídas(n)
```

Cada parada é um subproblema. O resultado fica salvo num dicionário (memoização), então a próxima parada só reaproveita o valor guardado em vez de recalcular a viagem inteira.

## Funções

| Função | O que faz |
|---|---|
| `registrar_fluxo` | Calcula e salva a lotação da parada, com o horário |
| `obter_status_painel` | Mostra ao passageiro a lotação atual |
| `gerar_relatorio` | Mostra a parada e o horário de maior lotação |

## Como rodar

```
python app.py
```
