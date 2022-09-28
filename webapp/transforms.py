import random
import re


def binarize(s):
    return " ".join(f"{ord(l):08b}" for l in s)


def clapify(s):
    return "👏".join(l for l in s)


def emojify(s):
    mappings = {
        "kiss": "😘",
        "airplane": "✈️",
        "pizza": "🍕",
        "happy": "😊",
        "sad": "😭",
        "star": "⭐️",
        "sleep": "😴",
        "sun": "☀️",
        "moon": "🌙",
        "christmas": "🎄",
        "birthday": "🎉",
        "ball": "🏀",
        "balloon": "🎈",
        "cake": "🎂",
        "laugh": "😂",
        "sick": "😷",
        "cheese": "🧀",
        "cow": "🐮",
        "horse": "🐴",
        "bear": "🐻",
        "monkey": "🐒",
        "surprised": "😳",
        "clap": "👏",
        "prayer": "🙏🏽",
        "run": "🏃🏻",
        "pencil": "✏️",
        "fire": "🔥",
        "rocket": "🚀",
        "car": "🚗",
        "movie": "🎥",
        "lips": "👄",
        "eyes": "👀",
        "tv": "📺",
        "soccer": "⚽️",
        "football": "🏈",
        "hat": "🎩",
        "dog": "🐶",
        "cat": "🐱",
        "elephant": "🐘",
        "lol": "😂",
        "dancer": "💃🏿",
        "world": "🌏",
    }
    return " ".join(
        mappings.get(word, word) for word in re.findall(r"[\w']+|[.,!?;]", s)
    )


def exclamify(s):
    end_marks = ["❣️", "‼️", "❗️", "!", "᥄", "❣", "‼︎"]
    start = random.choice(["¡", "¡¡"] + end_marks)
    end = random.choice(end_marks)
    return f"{start} {s} {end}"


def mystery(s):
    return "".join(l for l in s if l.upper() not in ["A", "E", "I", "O", "U"])
