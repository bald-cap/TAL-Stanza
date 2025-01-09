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
