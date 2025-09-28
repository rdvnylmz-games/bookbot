def count_characters(text: str) -> dict:
    char_counts = {}
    for char in text.lower():  # tüm karakterleri küçük harf yap
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts