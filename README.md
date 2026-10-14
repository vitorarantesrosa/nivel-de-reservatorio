# Controle de Níveis de Água

Sistema simples de monitoramento de um reservatório de água, executado no terminal. O programa recebe o nível atual de água e exibe uma mensagem de alerta colorida de acordo com a situação do reservatório.

## Objetivo

Auxiliar no monitoramento de um reservatório, destacando visualmente cada situação de risco com uma cor específica, usando a biblioteca **Colorama**.

## Como funciona

1. O programa pergunta ao usuário qual o nível de água no reservatório (número inteiro).
2. O valor informado é comparado com os limites de cada nível.
3. O programa exibe no terminal a mensagem correspondente, na cor associada ao nível.

## Níveis do reservatório

Cada nível é representado por uma lista com três valores:

| Posição | Conteúdo                                   |
|---------|--------------------------------------------|
| `[0]`   | Limite máximo de água daquele nível        |
| `[1]`   | Cor do texto exibido (Colorama)            |
| `[2]`   | Mensagem de alerta exibida                 |

| Nível   | Faixa de valores | Situação              | Cor      |
|---------|------------------|-----------------------|----------|
| Nível 1 | até 2            | Muito baixo (crítico) | Vermelho |
| Nível 2 | de 3 a 4         | Baixo                 | Amarelo  |
| Nível 3 | de 5 a 6         | Médio                 | Verde    |
| Nível 4 | de 7 a 8         | Alto                  | Ciano    |
| Nível 5 | de 9 a 10        | Muito alto (alerta)   | Azul     |

### Casos especiais

- **Valor negativo:** exibe `Inválido` em vermelho.
- **Valor acima de 10:** exibe `O reservatório transbordou!` em vermelho.

## Requisitos

- Python 3
- Biblioteca [Colorama](https://pypi.org/project/colorama/)

Instalação da dependência:

```bash
pip install colorama
```

## Como executar

No terminal, dentro da pasta do arquivo:

```bash
python nome_do_arquivo.py
```

## Exemplo de uso

```
Qual o nível no reservatório? 5
Nível 3 - Médio
```

(a mensagem aparece em verde no terminal)

```
Qual o nível no reservatório? 12
O reservatório transbordou!
```

(a mensagem aparece em vermelho no terminal)

## Estrutura do código

- **Importação e inicialização do Colorama:** `from colorama import *` e `init()`, que habilitam as cores no terminal.
- **Entrada de dados:** `input()` convertido para inteiro com `int()`.
- **Definição dos níveis:** cinco listas (`NIVEL_1` a `NIVEL_5`) com limite, cor e mensagem.
- **Verificação:** uma sequência `if / elif` que compara o valor informado com o limite de cada nível, do menor para o maior.
