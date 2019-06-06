# MDP: Markov Decision Process

## Resumo
O projeto visa ilustrar dois métodos de implementação de aprendizado por reforço baseado em MDP,
 Policy Evaluation e Value Iteraction.

O problema proposto é um mundo de grade clássico em que o ator nasce em uma posição aleatória 
do mundo de grades e deve tomar a melhor ação para chegar em seu objetivo.

![Alt text](image/small-gridworld.png? "Small Grid World")

Cada ação tomada pelo ator tem uma recompensa negativa de -1. Quando o ator chegar no 
quadriculado cinza ele recebe uma recompensa de 0. Ou seja, o sistema foi modelado com reforço 
negativo e o ator deve otimizar a tomada de decisão para que tenha a maior recompensa possível 
dado o estado inicial dele.

Chamamos de política ótima a melhor ação para uma dada posição (x,y) do sistema de 
coordenadas do problema ou da posição estatica de cada região.

## Formalização

> **Policy Evaluation**

![Alt text](image/policy-evaluation.png? "Policy Evaluation")

> **Value Iteraction**

![Alt text](image/value-iteration.png? "Value Iteration")

## Resultados

Após o desenvolvimento do algorítimo temos a politica ótima do nosso mundo, ou seja, as 
melhores decisões a serem tomadas dada uma posição no mundo de grades.

Para o "Policy Evaluation" temos:

![Alt text](image/result-pe.png? "Result - Policy Evaluation")

Cada politica é modelada numericamente, porém tem significados semânticos mostrados em
"Translation of Policy States"

Para o "Value Iteration" temos:

![Alt text](image/result-vi.png? "Result - Value Iteration")

Temos pequenas variações em função do algorítimo aplicado, pode-se notar politicas diferentes.

A modelagem possibilita implementações/testes com mundos de tamanhos diferentes e matriz de
recompensa diferente alterando os valores das dimensões e da classe de reward.

![Alt text](image/other.png? "Others Possibilities")

## Development Requirements

### Versions
 - Python [3.7.3](https://www.python.org/downloads/release/python-373/)

### Instalação
```bash
$ pip install -r requirements.txt
```
### Execução do Projeto
Lembrar que existe uma linha que ilustra um método de resolução comentada, caso queira comparar deve-se descomenta-la
```bash
$ python main.py
```

## License
MIT
_______________________________________________________
