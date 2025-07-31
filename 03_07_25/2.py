"""
Даны две строки ransom_note и magazine, вернуть , true если ransom_note можно построить, используя буквы из magazine и,
false в противном случае .

Каждая буква в magazine может быть использована только один раз ransom_note.

Пример 1:
Ввод: ransom_note = "a", magazine = "b"
 Вывод: false

Пример 2:
Ввод: ransom_note = "aa", magazine = "ab"
 Вывод: false

Пример 3:
Ввод: ransom_note = "aa", magazine = "aab"
 Вывод: true

Ограничения:
1 <= ransom_note.length, magazine.length <= 105
ransom_note и magazine состоят из строчных английских букв.
"""


def can_construct(ransom_note: str, magazine: str) -> bool:
    from collections import Counter

    d_ransom_note = Counter(ransom_note)
    d_magazine = Counter(magazine)
    return d_ransom_note <= d_magazine


print(can_construct("aaс", "aba"))
