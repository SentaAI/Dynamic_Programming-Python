# Dynamic_Programming-Python

Sistema de lotação de ônibus em tempo real usando programação dinâmica.

🔗 **Site explicativo da solução:** https://senta-ai-sigma.vercel.app/

## Integrantes

- Arthur Berlofa Bosi - RM564438
- Levi de Jesus - RM563279
- Luigi Borghi - RM563096
- Ulisses Ribeiro - RM562230

## A ideia

Sensores IoT instalados na porta do ônibus, integrados à catraca, poderiam registrar as entradas e saídas de passageiros em cada parada. Esses registros seriam enviados ao sistema para atualizar a lotação do ônibus.

- **O passageiro** poderia ver numa tela quantas pessoas estão a bordo e quantos lugares estão livres antes de embarcar.
- **Os responsáveis pela operação dos ônibus** receberiam no fim do dia um relatório com as paradas e os horários mais cheios, para ajudar a decidir onde colocar mais ônibus.

> **Importante:** o projeto ainda não está integrado a uma catraca ou a sensores reais. Os dados usados são apenas exemplos, representando como as informações de entradas e saídas poderiam chegar ao sistema. No exemplo, o sistema recebe a quantidade de passageiros que entrou e saiu em cada parada; não identifica individualmente os passageiros.

## Programação dinâmica

A lotação de uma parada depende da lotação anterior, da quantidade de passageiros que entrou e da quantidade que saiu:

```
lotação(n) = lotação(n-1) + entradas(n) - saídas(n)
```

Cada parada é um subproblema. O resultado fica salvo num dicionário (memoização), então a próxima parada pode reaproveitar o valor guardado em vez de recalcular a viagem inteira.

## Funcionalidades

| Função | O que faz |
|---|---|
| `registrar_fluxo` | Recebe os dados de entradas e saídas de uma parada, calcula e salva a lotação, junto com o horário. No projeto atual, esses dados são de exemplo. |
| `obter_status_painel` | Mostra ao passageiro a lotação atual. |
| `gerar_relatorio` | Mostra a parada e o horário de maior lotação. |

## Como rodar

```
python app.py
```
