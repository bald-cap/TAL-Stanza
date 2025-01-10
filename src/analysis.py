# %%
import stanza
nlpStanza=stanza.Pipeline("fr")
#%%
"""Segmentation en tokens du fichier textProjet.txt"""
#%%
with open("textProjet.txt","r",encoding="utf-8") as fichier:
    texte = fichier.read()
    st = nlpStanza(texte)
    print ("\n\tSTANZA\n---")
    count = 0
    total_mot = 0
    for sent in st.sentences:
        count += 1
        print(f"------\n\nPHRASE {count} -> {sent.text}", end="\n------\n")
        count_mot = 0
        for x in sent.tokens:
            count_mot += 1
            print(f"{count_mot} - {x.text}", end="\n")
#%%


#%%
def etiquetage_pos_stanza(fichier_texte):
    # Charger le modèle de langue française
    nlp = stanza.Pipeline(lang='fr', processors='tokenize,pos', tokenize_pretokenized=False)
    
    # Lire le contenu du fichier
    with open(fichier_texte, 'r', encoding='utf-8') as file:
        texte = file.read()
    
    # Analyse du texte
    doc = nlp(texte)
    
    # Récupérer les tokens et leurs étiquettes POS
    pos_resultats = []
    for sentence in doc.sentences:
        for word in sentence.words:
            pos_resultats.append((word.text, word.upos))
    
    # Afficher les résultats
    for mot, pos in pos_resultats:
        print(f"{mot:<15} {pos}")
    
    return pos_resultats

# Chemin vers votre fichier
fichier = 'textProjet.txt'

# Appeler la fonction
etiquetage_pos_stanza(fichier)

#%%