# -*- coding: utf-8 -*-
import funcoes


def main():
    while True:
        print("\n" + "=" * 73)
        print("                      MENU DE TABELAS DO PIB (IBGE)")
        print("=" * 73)
        print("1 - Tabela por Trimestre (tabela_pib)")
        print("2 - Tabela Soma por Ano (soma_ano)")
        print("3 - Tabela Soma de 4 em 4 Trimestres (soma_4t)")
        print("4 - Tabela Diferença 1º Semestre 2026 vs Anteriores (diferenca_semestres)")
        print("0 - Sair")
        print("=" * 73)

        escolha = input("Digite o número da tabela que deseja ver: ").strip()

        if escolha == '1':
            print("\n--- TABELA POR TRIMESTRE ---")
            print(funcoes.tabela_pib())
        elif escolha == '2':
            print("\n--- TABELA SOMA POR ANO ---")
            print(funcoes.soma_ano())
        elif escolha == '3':
            print("\n--- TABELA SOMA DE 4 EM 4 TRIMESTRES ---")
            print(funcoes.soma_4t())
        elif escolha == '4':
            print("\n--- TABELA DIFERENÇA DE SEMESTRES ---")
            print(funcoes.diferenca_semestres())
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha de 0 a 4.")


if __name__ == '__main__':
    main()
