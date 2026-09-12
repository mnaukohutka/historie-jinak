import os
import re

print("Zahajuji převod titulků na čistý text...")

for file in os.listdir('.'):
    if file.endswith('.vtt'):
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        clean_text = []
        for line in lines:
            if 'WEBVTT' in line or '-->' in line or line.strip() == '':
                continue
            clean_line = re.sub(r'<[^>]+>', '', line).strip()
            if clean_line and (not clean_text or clean_text[-1] != clean_line):
                clean_text.append(clean_line)
                
        out_name = file.replace('.cs.vtt', '.txt').replace('.vtt', '.txt')
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(' '.join(clean_text))
        
        print(f'Uloženo: {out_name}')

print("Hotovo! Všechny texty jsou připraveny.")
