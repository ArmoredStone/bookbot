def count_words(count_string: str) -> int:
    return len(count_string.split())

def count_characters(count_string: str) -> dict:
    counts = {}
    for char in count_string.lower():
        if not char.isalpha():
            continue
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_desc(tosort: dict) -> dict:
    sorted_desc = {k: v for k, v in sorted(tosort.items(), key=lambda item: item[1], reverse=True)}
    return sorted_desc

