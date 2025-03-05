import re

def latextomd(text):

    # Retire les titres
    regex = r'^#+\s*'
    while re.search(regex, text, flags=re.MULTILINE):
        text = re.sub(regex, r'', text, flags=re.MULTILINE)

    # Retire les sauts de ligne inutiles après un :
    regex = r':\s*\n\n( *[\$\-])'
    while re.search(regex, text):
        text = re.sub(regex, r':\n\1', text)

    # Remplace les || par des \|
    regex = r'\|\|'
    while re.search(regex, text):
        text = re.sub(regex, r'\|', text)

    regex = r'(^|[^\$\\])\$([^\$\\]|$)'
    text = re.sub(regex, r'\1  $  \2', text)

    regex = r'(^|[^\$\\])\$([^\$]|[^\$].*?[^\$\\])\$([^\$]|$)'
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

    # Replace \[...\] with \(\(...\)\)
    regex = r'\\\['
    while re.search(regex, text):
        text = re.sub(regex, r'\(\(', text)
    regex = r'\\\]'
    while re.search(regex, text):
        text = re.sub(regex, r'\)\)', text)

    # Replace $$       ...$$ with $$...$$
    regex = r'\s*\\\(\\\(\s+(.*)\\\)\\\)'
    while re.search(regex, text, flags=re.DOTALL):
        text = re.sub(regex, r'\(\(\1\)\)', text, flags=re.DOTALL)

    # Replace $$...       $$ with $$...$$
    regex = r'\\\(\\\((.*)\s+\\\)\\\)\s*'
    while re.search(regex, text, flags=re.DOTALL):
        text = re.sub(regex, r'\(\(\1\)\)', text, flags=re.DOTALL)

    # Supprime les retour à la ligne après un \begin{align} et avant un \end{align}
    regex = r'\\begin{align\*?}\s*\n'
    while re.search(regex, text):
        text = re.sub(regex, r'\\begin{align*} ', text)
    regex = r'\n\s*\\end{align\*?}'
    while re.search(regex, text):
        text = re.sub(regex, r' \\end{align*}', text)

    # Replace $$...\\        with $$...\\ 
    regex = r'\\\(\\\((.*?),?\s*\\\\\s*\n'
    while re.search(regex, text):
        text = re.sub(regex, r"\(\(\1 \\\\ ", text)

    # Fusionne deux display mode qui se suivent
    regex = r'\\\(\\\((?:\\begin{align\*?})?(.*?)(?:\\end{align\*?})?\\\)\\\)\s*\\\(\\\((?:\\begin{align\*?})?(.*?)(?:\\end{align\*?})?\\\)\\\)'
    while re.search(regex, text):
        text = re.sub(regex, r'\(\(\\begin{align*} \1 \\\\ \2 \\end{align*}\)\)', text)

    # Replace :     $$      with : $$
    regex = r'([:,;a-zéèàù\**])\s+\\\(\\\(\s*'
    while re.search(regex, text):
        text = re.sub(regex, r'\1\(\(', text)
    regex = r'([:,;a-zéèàù\**])\\\(\\\('
    while re.search(regex, text):
        text = re.sub(regex, r'\1 \(\(', text)

    # Passe une ligne après une display mode si une nouvelle phrase commence après, sinon on mets un espace parce que la phrase continue
    regex = r'\\\)\\\)+ ?([A-Z0-9-])'
    while re.search(regex, text):
        text = re.sub(regex, r'\)\)\n\1', text)
    regex = r'\\\)\\\)\s+([a-zéèàù\**])'
    while re.search(regex, text):
        text = re.sub(regex, r'\)\)\1', text)
    regex = r'\\\)\\\)([a-zéèàù\**])'
    while re.search(regex, text):
        text = re.sub(regex, r'\)\) \1', text)

    # Passe une ligne avant une display mode qui suit une phrase terminée
    regex = r'([\.!\?])\\\(\\\('
    while re.search(regex,text):
        text = re.sub(regex, r'\1\n\(\(', text)

    # Supprime les espaces dans $...$ . et $...$ , et $...$ ) et ( $...$
    regex = r'\\\) +([,\.)])'
    while re.search(regex,text):
        text = re.sub(regex, r'\)\1', text)
    regex = r'\( +\\\('
    while re.search(regex,text):
        text = re.sub(regex, r'(\(', text)
    
    
    # Replace \( and \) with $
    regex = r'\\\('
    while re.search(regex,text):
        text = re.sub(regex, r'$', text)

    regex = r'[\.,]?\\\)'
    while re.search(regex,text):
        text = re.sub(regex, r'$', text)

    # Replace             with  
    regex = r'  +'
    text = re.sub(regex, r' ', text)

    return text


# input_text = r"""
# """

# # print(input_text)
# # print("--------------------")
# output_text = latextomd(input_text)
# # print(output_text)

# # Sauvegarder dans un fichier texte
# with open("output.md", "w", encoding="utf-8") as f:
#     f.write(output_text)
#     print("Sauvegardé dans output.md")
