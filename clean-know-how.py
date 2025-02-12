import os
import re

# Funkce pro smazání úvodní části souboru
def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Regulární výrazy pro časové formáty
    time_pattern_12hr = r'^[0-9]{1,2}:[0-9]{2} [AP]M$'  # 12hodinový formát
    time_pattern_24hr = r'^[0-9]{1,2}:[0-9]{2}$'  # 24hodinový formát

    # Hledání první řádky, která odpovídá času
    start_line = None
    for i, line in enumerate(lines):
        if re.match(time_pattern_12hr, line.strip()) or re.match(time_pattern_24hr, line.strip()):
            start_line = i
            break
    
    # Pokud je nalezen čas, smažeme všechny řádky až po něj (včetně)
    if start_line is not None:
        lines = lines[start_line + 1:]  # Zachováme vše za časem (ne i čas)

    # Uložení souboru po odstranění úvodních řádků
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Funkce pro procházení složek a souborů
def process_files(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                clean_file(file_path)
                print(f"Processed: {file_path}")

# Cesta k adresáři, kde jsou soubory .md
root_dir = 'C:\_git\obsidian\knowhow'  # Změň podle potřeby na konkrétní složku
process_files(root_dir)
