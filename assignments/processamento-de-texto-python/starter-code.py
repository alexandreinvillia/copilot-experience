from collections import Counter
import re


def clean_text(text: str) -> str:
    """Normalize text: lowercase, remove punctuation, and collapse spaces."""
    # TODO: implemente a limpeza conforme os requisitos da tarefa.
    return text


def word_frequencies(text: str) -> list[tuple[str, int]]:
    """Return the top 5 most common words from a cleaned text."""
    words = text.split()
    return Counter(words).most_common(5)


def process_file(file_path: str) -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
    except FileNotFoundError:
        print("Arquivo nao encontrado. Verifique o caminho e tente novamente.")
        return

    lines_count = raw_text.count("\n") + (1 if raw_text else 0)
    cleaned = clean_text(raw_text)

    print(f"Linhas: {lines_count}")
    print(f"Palavras: {len(cleaned.split())}")
    print(f"Caracteres: {len(cleaned)}")

    print("\nTop 5 palavras mais frequentes:")
    for word, count in word_frequencies(cleaned):
        print(f"- {word}: {count}")


if __name__ == "__main__":
    path = input("Digite o caminho do arquivo de texto: ").strip()
    process_file(path)
