import re
from collections import Counter

def parse_log(file_path, keywords):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except (FileNotFoundError, IOError) as e:
        raise RuntimeError(f"No se pudo abrir el archivo: {e}")

    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b', re.IGNORECASE)
    matches = pattern.findall(content)
    return Counter(map(str.upper, matches))
