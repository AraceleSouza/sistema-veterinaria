#  Cadastro de Animais - Veterinária 🐾

## **:computer:** Sobre o Projeto

Este projeto é um **sistema simples de cadastro de animais** desenvolvido em **Python**, voltado para o uso em clínicas veterinárias ou abrigos.  
O objetivo é registrar informações básicas sobre cada animal atendido, garantindo que os dados fiquem organizados e padronizados durante o atendimento.
O programa é executado no terminal e permite **cadastrar vários animais**, registrando dados como nome, tipo, sexo, vacinação e uma breve descrição da situação do animal.

## 🛠️ Tecnologias Utilizadas

-  Python 3  
- Módulo `datetime` 

## ⚙️ Funcionalidades

- Cadastro de múltiplos animais. 
-  Validação de entrada (aceita apenas opções válidas). 
-  Registro automático da data atual do cadastro.
-  Impressão de um relatório final com todos os animais cadastrados.


## 🧠 Conceitos utilizados

-   Estruturas de repetição
-   Estruturas condicionais
-   Dicionários e listas
-   Métodos de formatação e validação de entrada
-   Módulo `datetime` para obter a data atual

## 📦 Campos do Cadastro

-   **Nome:** nome do animal
-   **Tipo:** escolha entre Peixes, Mamíferos, Anfíbios, Aves ou Répteis
-   **Sexo:** Masculino (M) ou Feminino (F)
-   **Vacinado:** Sim (S) ou Não (N)
-   **Descrição:** breve relato sobre a condição ou observação do animal (mínimo de 10 caracteres)


## 💻 Exemplo de Saída

-=-= CADASTRO VETERINÁRIA =-=-
Digite o nome do animal: LUNA
Tipos de animais:
[1]Peixes
[2]Mamíferos
[3]Anfíbios
[4]Aves
[5]Repteis
Digite o tipo do animal: [1 a 5]2
Digite o sexo do animal: [M/F]F
Vacinado? [S/N]S
Descreva a situação do animal: ANIMAL EM BOAS CONDIÇÕES
Realizar outro cadastro? [S/N]N


Animais cadastrados dia: 12 / 10 / 2025

NOME         |TIPO            |SEXO            |VACINADO         |DESCRIÇÃO     

LUNA            |2               |F                |S                |ANIMAL EM BOAS CONDIÇÕES

## 🎯 Objetivo

Criar uma aplicação prática de registro de animais, para reforçar o aprendizado em **lógica de programação**, uso de **estruturas de repetição**, **validação de dados** e **manipulação de dicionários e listas** em Python.