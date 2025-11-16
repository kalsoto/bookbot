def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_occurence(text: str):
    char_count: dict[str, int] = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def get_sorted_char_list(char_dict: dict[str, int]):
    sorted = []
    for key, value in char_dict.items():
        sorted.append({"char": key, "num": value})
    sorted.sort(reverse=True, key=lambda d: d["num"])
    return sorted
