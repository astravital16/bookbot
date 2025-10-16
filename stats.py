def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercase_counts = {}
    lower_text = text.lower()
    for ch in lower_text:
        lowercase_counts[ch] = lowercase_counts.get(ch, 0) +1
    return lowercase_counts

def sort_char(lowercase_counts):
    character_list = []
    for character, count in lowercase_counts.items():
        if character.isalpha():
            character_list.append({"char": character, "num": count})
    character_list.sort(reverse=True, key=lambda item: item["num"])
    return character_list