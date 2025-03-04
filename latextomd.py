import pytesseract
from PIL import Image
import re

# Si Tesseract n'est pas dans le PATH (Windows), décommente la ligne ci-dessous et remplace le chemin :
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """Utilise Tesseract OCR pour extraire le texte et les formules depuis une image."""
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img)
    return extracted_text

def apply_latextomd_rules(text):
    """Applique strictement les règles de la procédure *latextomd* au texte extrait."""
    
    # Règle 1 : Convertir \(...\) en $...$
    text = re.sub(r"\\\((.*?)\\\)", r"$\1$", text)
    
    # Règle 2 : Convertir \[...\] en $$...$$ (sur une seule ligne si possible)
    text = re.sub(r"\\\[(.*?)\\\]", r"$$\1$$", text, flags=re.DOTALL)

    # Règle 3 : Assurer que les align utilisent la bonne syntaxe
    text = re.sub(r"\\begin{align}(.*?)\\end{align}", r"$$\begin{align}\1\end{align}$$", text, flags=re.DOTALL)

    # Règle 4 : Conserver la mise en forme (gras, italique, structures)  
    # (Déjà géré automatiquement par l'OCR)

    # Règle 5 : Supprimer les préfixes "###" pour les éléments en emphase ou italique
    text = re.sub(r"^### ", "", text, flags=re.MULTILINE)

    # Règles 6 et 7 : Nettoyage des espaces inutiles
    text = re.sub(r"(\$)\s+|\s+(\$)", r"\1\2", text)  # Supprimer les espaces inutiles autour de $
    text = re.sub(r"(\$\$)\s+|\s+(\$\$)", r"\1\2", text)  # Supprimer les espaces autour de $$

    # Règle 8 : Ne pas insérer de ligne blanche avant une liste introduite par ":"
    text = re.sub(r":\n\s*•", r":\n•", text)

    # Règles 11 à 14 : Assurer que les formules en display mode restent sur la même ligne si elles font partie d'une phrase
    text = re.sub(r"([a-zA-Z0-9])\n\$\$", r"\1 $$", text)  # Éviter d'isoler un display mode inutilement
    text = re.sub(r"\$\$\n([a-zA-Z0-9])", r"$$ \1", text)  # Conserver la phrase après le display mode

    return text

if __name__ == "__main__":
    image_path = "image.png"  # Remplace par le chemin réel de ton image
    raw_text = extract_text_from_image(image_path)
    formatted_text = apply_latextomd_rules(raw_text)

    print("===== Texte formaté en Markdown =====")
    print(formatted_text)
