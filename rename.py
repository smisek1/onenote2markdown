import os
import re

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        # Odstranit případný text " NE" před zpracováním
        cleaned_filename = filename.replace(" NE", "")
        
        # Ignorovat soubory, které nemají "."
        if '.' not in cleaned_filename:
            continue
        
        # Upravený regex pro zachycení variant jako 05_5.1.md nebo 05_5.1..md
        match = re.match(r'^\d+_(\d{1,2})\.(\d{1,2})\.?\.?md$', cleaned_filename)
        if match:
            day, month = match.groups()
            # Zajistit dvoumístné formátování dne a měsíce
            day = day.zfill(2)
            month = month.zfill(2)
            new_name = f"2025-{month}-{day}.md"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Přejmenován: {filename} -> {new_name}")

# Použití
directory_path = "/home/smich/Documents/_git/obsidian/denik/2025/"  # Nahraď svou cestou
rename_files_in_directory(directory_path)
