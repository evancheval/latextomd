import re

def latextomd(text):

    # Replace $...$ with \(...\)
    regex = r'(^|[^\$\\])\$(.*?[^\$\\])\$([^\$]|$)'
    while re.search(regex, text):
        text = re.sub(regex, r'\1\(\2\)\3', text)
    
    # # Replace $ ...$ with $...$ but not $$ ...$$
    # while re.search(r'([^\$])\$ (.*?)\$([^\$])',text):
    #     text = re.sub(r'([^\$])\$ (.*?)\$([^\$])', r'\1$\2$\3', text)

    # # Replace $... $ with $...$ but not $$... $$
    # while re.search(r'([^\$])\$(.*?) \$([^\$])',text):
    #     text = re.sub(r'([^\$])\$(.*?) \$([^\$])', r'\1$\2$\3', text)

    # # Replace $$       ...$$ with $$...$$
    # while re.search(r'\$\$\s+(.*)\$\$', text, flags=re.DOTALL):
    #     text = re.sub(r'\$\$\s+(.*)\$\$', r'$$\1$$', text, flags=re.DOTALL)

    # # Replace $$...       $$ with $$...$$
    # while re.search(r'\$\$(.*)\s+\$\$', text, flags=re.DOTALL):
    #     text = re.sub(r'\$\$(.*)\s+\$\$', r'$$\1$$', text, flags=re.DOTALL)

    # # Replace $$...\\        with $$...\\ 
    # while re.search(r"\$\$(.*)\\\\\s*\n", text):
    #     text = re.sub(r"\$\$(.*)\\\\\s*\n", r"$$\1\\\\ ", text)

    # # Replace :     $$      with : $$
    # while re.search(r'([^\.\s])\s+\$\$\s*', text):
    #     text = re.sub(r'([^\.\s])\s+\$\$\s*', r'\1$$', text)
    # while re.search(r'([^\.\s])\$\$', text):
    #     text = re.sub(r'([^\.\s])\$\$', r'\1 $$', text)

    # # Passe une ligne après une display mode si une nouvelle phrase commence après
    # while re.search(r'\$\$ ?[A-Z[0-9]*]',text):
    #     text = re.sub(r'\$\$ ?([A-Z[0-9]*])', r'$$\n\1', text)

    # # Passe une ligne avant une display mode qui suit une phrase
    # while re.search(r'\.\$\$',text):
    #     text = re.sub(r'\.\$\$', r'.\n$$', text)    
    
    # Replace \( ... \) with $...$
    while re.search(r'\\\( ?(.*?) ?\\\)',text):
        text = re.sub(r'\\\( ?(.*?) ?\\\)', r'$\1$', text)

    return text


input_text = r"""$18 = 20-2$ et $27 = 32 - 5$
Mon coca m'a coûté 10\$

3. Soient $f$ et $g$ deux fonctions $R$-intégrables sur $I$ vérifiant $|f(x)| \leq g(x)$ pour tout $x \in I$. Alors on a :
   $$
   \left| \int_{I} f(x) dx \right| \leq \int_{I} g(x) dx
   $$

4. Soit $f$ une fonction $R$-intégrable sur $I$ telle que $|f|$ est $R$-intégrable sur $I$. Alors on a :
   $$
   \left| \int_{I} f(x) dx \right| \leq \int_{I} |f(x)| dx
   $$

5. Soit $f$ une fonction $R$-intégrable sur $I$ vérifiant $f(x) \geq 0$ pour tout $x \in I$. Alors on a :
   $$
   \int_{I} f(x) dx \geq 0
   $$

6. Soient $f : I \to \mathbb{R}$ et $\mathcal{P} = \{I^j : 1 \leq j \leq m\}$ une partition de $I$. Si $f$ est $R$-intégrable sur $I^j$ pour tout $j = 1, \dots, m$, alors $f$ est $R$-intégrable sur $I$ et on a :
   $$
   \int_{I} f(x) dx = \sum_{j=1}^{m} \int_{I^j} f(x) dx
   $$
"""

# print(input_text)
# print("--------------------")
output_text = latextomd(input_text)
# print(output_text)

# Sauvegarder dans un fichier texte
with open("output.md", "w", encoding="utf-8") as f:
    f.write(output_text)
    print("Sauvegardé dans output.md")
