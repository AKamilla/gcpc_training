
def trim_to_last_vowel(s: str) -> str:
    VOWELS = 'aeiou'
    last_vowel = None
    for i, c in enumerate(s):
        if c in VOWELS:
            last_vowel = i

    return s[:last_vowel+1] + "ntry"


if __name__ == "__main__":
    while True:
        print(trim_to_last_vowel(input()))