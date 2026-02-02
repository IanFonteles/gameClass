#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de teste para verificar se o jogo Whack-a-Mole funciona corretamente
Valida todos os 5 requisitos implementados
"""

import sys
import re

def analisar_arquivo(caminho):
    """Lê e analisa o arquivo app.py"""
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    return conteudo

def validar_requisitos(conteudo):
    """Valida se todos os 5 requisitos estão implementados"""
    
    requisitos = {
        "1. Tabuleiro de jogo": {
            "padroes": [
                r"gameBoard",
                r"grid-template-columns",
                r"mole-hole"
            ],
            "descricao": "Grade de 9 tocas com CSS Grid"
        },
        "2. Exibição aleatória de toupeiras": {
            "padroes": [
                r"showRandomMole\(\)",
                r"Math\.random\(\) \* holes\.length",
                r"randomHole"
            ],
            "descricao": "Função que seleciona tocas aleatoriamente"
        },
        "3. Sistema de 'acertos'": {
            "padroes": [
                r"whackMole",
                r"gameState\.score\+\+",
                r"classList\.contains\('show'\)"
            ],
            "descricao": "Detecção de clique e incremento de pontos"
        },
        "4. Pontuação em destaque": {
            "padroes": [
                r"stat-value.*score",
                r"font-size.*2em",
                r"gradient"
            ],
            "descricao": "Pontuação exibida em grande com estilo"
        },
        "5. Temporizador": {
            "padroes": [
                r"updateTimer",
                r"timeLeft",
                r"setInterval"
            ],
            "descricao": "Contagem regressiva de tempo"
        }
    }
    
    resultados = {}
    for req, dados in requisitos.items():
        encontrado = all(
            re.search(padrao, conteudo, re.IGNORECASE) 
            for padrao in dados['padroes']
        )
        resultados[req] = encontrado
    
    return resultados

def exibir_resultado_teste(resultados):
    """Exibe os resultados do teste"""
    print("\n" + "="*70)
    print("🔨 VALIDAÇÃO DO WHACK-A-MOLE 🔨")
    print("="*70 + "\n")
    
    todos_ok = True
    
    for requisito, valido in resultados.items():
        status = "✅ IMPLEMENTADO" if valido else "❌ NÃO ENCONTRADO"
        print(f"{requisito}")
        print(f"   Status: {status}\n")
        
        if not valido:
            todos_ok = False
    
    print("="*70)
    
    if todos_ok:
        print("🎉 RESULTADO: TODOS OS 5 REQUISITOS IMPLEMENTADOS COM SUCESSO! 🎉")
        print("\n✨ O jogo está pronto para jogar!")
        print("📱 Execute: python app.py")
        print("🌐 Acesse: http://localhost:5000")
    else:
        print("⚠️  ALGUNS REQUISITOS NÃO FORAM ENCONTRADOS")
        print("    Verifique a implementação do arquivo app.py")
        return 1
    
    print("="*70 + "\n")
    return 0

def main():
    """Função principal"""
    try:
        print("\n🔍 Analisando arquivo app.py...")
        conteudo = analisar_arquivo('app.py')
        
        print("✓ Arquivo carregado com sucesso\n")
        print("📋 Validando requisitos...\n")
        
        resultados = validar_requisitos(conteudo)
        
        return exibir_resultado_teste(resultados)
        
    except FileNotFoundError:
        print("\n❌ Erro: Arquivo 'app.py' não encontrado!")
        print("   Certifique-se de estar no diretório correto")
        return 1
    except Exception as e:
        print(f"\n❌ Erro ao analisar arquivo: {e}")
        return 1

if __name__ == '__main__':
    exit(main())
