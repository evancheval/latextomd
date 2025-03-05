import re

def latextomd(text):

    # Retire les sauts de ligne inutiles après un :
    regex = r':\s*\n\n( *[\$\-])'
    while re.search(regex, text):
        text = re.sub(regex, r':\n\1', text)

    # Replace $...$ with \(...\)
    regex = r'(^|[^\$\\])\$(.*?[^\$\\])\$([^\$]|$)'
    while re.search(regex, text):
        text = re.sub(regex, r'\1\(\2\)\3', text)
    
    # Replace $ ...$ with $...$ but not $$ ...$$
    regex = r'\\\(\s+(.*?)\\\)'
    while re.search(regex,text):
        text = re.sub(regex, r'\(\1\)', text)

    # Replace $... $ with $...$ but not $$... $$
    regex = r'\\\((.*?)\s+\\\)'
    while re.search(regex,text):
        text = re.sub(regex, r'\(\1\)', text)

    # Replace $$...$$ with \(\(...\)\)
    regex = r'\$\$(.*?)\$\$'
    while re.search(regex, text, flags=re.DOTALL):
        text = re.sub(regex, r'\(\(\1\)\)', text, flags=re.DOTALL)

    # Replace $$       ...$$ with $$...$$
    regex = r'\s*\\\(\\\(\s+(.*)\\\)\\\)'
    while re.search(regex, text, flags=re.DOTALL):
        text = re.sub(regex, r'\(\(\1\)\)', text, flags=re.DOTALL)

    # Replace $$...       $$ with $$...$$
    regex = r'\\\(\\\((.*)\s+\\\)\\\)\s*'
    while re.search(regex, text, flags=re.DOTALL):
        text = re.sub(regex, r'\(\(\1\)\)', text, flags=re.DOTALL)

    # Replace $$...\\        with $$...\\ 
    regex = r'\\\(\\\((.*)\\\\\s*\n'
    while re.search(regex, text):
        text = re.sub(regex, r"\(\(\1\\\\ ", text)

    # Replace :     $$      with : $$
    regex = r'([:,;a-z])\s+\\\(\\\(\s*'
    while re.search(regex, text):
        text = re.sub(regex, r'\1\(\(', text)
    regex = r'([:,;a-z])\\\(\\\('
    while re.search(regex, text):
        text = re.sub(regex, r'\1 \(\(', text)

    # Passe une ligne après une display mode si une nouvelle phrase commence après, sinon on mets un espace parce que la phrase continue
    regex = r'\\\)\\\)+ ?([A-Z0-9])'
    while re.search(regex, text):
        text = re.sub(regex, r'\)\)\n\1', text)
    regex = r'\\\)\\\)([a-z])'
    while re.search(regex, text):
        text = re.sub(regex, r'\)\) \1', text)

    # Passe une ligne avant une display mode qui suit une phrase terminée
    regex = r'([\.!\?])\\\(\\\('
    while re.search(regex,text):
        text = re.sub(regex, r'\1\n\(\(', text)
    

    # Replace \( and \) with $
    regex = r'\\\('
    while re.search(regex,text):
        text = re.sub(regex, r'$', text)
    regex = r'[\.,]?\\\)'
    while re.search(regex,text):
        text = re.sub(regex, r'$', text)

    return text


input_text = r"""
"""

# print(input_text)
# print("--------------------")
output_text = latextomd(input_text)
# print(output_text)

# Sauvegarder dans un fichier texte
with open("output.md", "w", encoding="utf-8") as f:
    f.write(output_text)
    print("Sauvegardé dans output.md")
