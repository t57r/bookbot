#!/usr/bin/env python3

def count_words(contents):
    return len(contents.split())

def count_character_frequencies(contents):
    freq = {}
    for ch in contents.lower():
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    return freq

def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()
        print(f"--- Begin report of books {file_name} ---")
        words_count = count_words(file_contents)
        print(f"{words_count} words found in the document\n")
        char_freq = count_character_frequencies(file_contents)
        sorted_chars = sorted(char_freq, key=char_freq.get, reverse=True)
        sorted_chars = [x for x in sorted_chars if x.isalpha()]
        for fr in sorted_chars:
            print(f"The '{fr}' character was found {char_freq[fr]} times")
        print("--- End report ---")

if __name__ == "__main__":
    main()
