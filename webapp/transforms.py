import random
import re


def binarize(s):
    return " ".join(f"{ord(l):08b}" for l in s)


def clapify(s):
    return "๐".join(l for l in s)


def emojify(s):
    mappings = {
        "kiss": "๐",
        "airplane": "โ๏ธ",
        "pizza": "๐",
        "happy": "๐",
        "sad": "๐ญ",
        "star": "โญ๏ธ",
        "sleep": "๐ด",
        "sun": "โ๏ธ",
        "moon": "๐",
        "christmas": "๐",
        "birthday": "๐",
        "ball": "๐",
        "balloon": "๐",
        "cake": "๐",
        "laugh": "๐",
        "sick": "๐ท",
        "cheese": "๐ง",
        "cow": "๐ฎ",
        "horse": "๐ด",
        "bear": "๐ป",
        "monkey": "๐",
        "surprised": "๐ณ",
        "clap": "๐",
        "prayer": "๐๐ฝ",
        "run": "๐๐ป",
        "pencil": "โ๏ธ",
        "fire": "๐ฅ",
        "rocket": "๐",
        "car": "๐",
        "movie": "๐ฅ",
        "lips": "๐",
        "eyes": "๐",
        "tv": "๐บ",
        "soccer": "โฝ๏ธ",
        "football": "๐",
        "hat": "๐ฉ",
        "dog": "๐ถ",
        "cat": "๐ฑ",
        "elephant": "๐",
        "lol": "๐",
        "dancer": "๐๐ฟ",
        "world": "๐",
    }
    return " ".join(
        mappings.get(word, word) for word in re.findall(r"[\w']+|[.,!?;]", s)
    )


def exclamify(s):
    end_marks = ["โฃ๏ธ", "โผ๏ธ", "โ๏ธ", "!", "แฅ", "โฃ", "โผ๏ธ"]
    start = random.choice(["ยก", "ยกยก"] + end_marks)
    end = random.choice(end_marks)
    return f"{start} {s} {end}"


def mystery(s):
    return "".join(l for l in s if l.upper() not in ["A", "E", "I", "O", "U"])
