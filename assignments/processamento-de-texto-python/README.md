# 📘 Assignment: Processamento de Texto com Python

## 🎯 Objective

Praticar manipulação de strings e I/O de arquivos em Python para limpar, transformar e analisar textos de forma automatizada.

## 📝 Tasks

### 🛠️ Limpeza e Normalização de Texto

#### Description
Crie uma função `clean_text(text: str) -> str` que receba um texto bruto e devolva uma versão normalizada para análise.

#### Requirements
Completed program should:

- Converter todo o texto para minúsculas.
- Remover pontuação comum (`. , ; : ! ? " ' ( ) [ ] { }`).
- Substituir múltiplos espaços por um único espaço.
- Retornar o texto final sem espaços no início/fim.

### 🛠️ Leitura de Arquivo e Estatísticas

#### Description
Complete o programa para ler um arquivo de texto, aplicar a limpeza e exibir estatísticas básicas sobre o conteúdo processado.

#### Requirements
Completed program should:

- Ler o conteúdo de um arquivo `.txt` usando `open(..., encoding="utf-8")`.
- Exibir o total de linhas, palavras e caracteres após a limpeza.
- Mostrar as 5 palavras mais frequentes com suas contagens.
- Tratar erro de arquivo inexistente com uma mensagem amigável, sem encerrar com traceback.
