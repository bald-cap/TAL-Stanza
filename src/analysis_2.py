# %%
import stanza
from collections import Counter

nlpStanza=stanza.Pipeline("fr")

# %%
def compareSyntaxe(text):
    st = nlpStanza(text)

    count = 0
    print("\n\tSTANZA\n---")
    for sent in st.sentences:
        count += 1
        print(f"SENTENCE {count} - {sent.text}\n----")
        print("ANALYSE \n----")

        # Define column widths
        id_width = 5
        text_width = 20
        lemma_width = 20
        pos_width = 20
        head_width = 20
        deprel_width = 15

        # Print headers with fixed widths
        print(
            "ID".ljust(id_width),
            "TEXT".ljust(text_width),
            "LEMMA".ljust(lemma_width),
            "PART OF SPEECH".ljust(pos_width),
            "HEAD".ljust(head_width),
            "DEP REL".ljust(deprel_width),
            sep=""
        )

        # Print rows with fixed widths
        for x in sent.words:
            head_word = sent.words[x.head - 1].text if x.head > 0 else "ROOT"
            print(
                str(x.id).ljust(id_width),
                x.text.ljust(text_width),
                x.lemma.ljust(lemma_width),
                x.pos.ljust(pos_width),
                (str(x.head) + f"({head_word})").ljust(head_width),
                x.deprel.ljust(deprel_width),
                sep=""
            )

        print("\n-----------------------------------\n")


# %%
with open("message.txt", "r", encoding="UTF-8") as file:
    holding = file.read()
    compareSyntaxe(holding)

# * LEMMATISATIONS
# %%
def lemmatization(text):
    st = nlpStanza(text)

    count = 0
    print("\n\tSTANZA\n---")
    for sent in st.sentences:
        count += 1
        print(f"SENTENCE {count} - {sent.text}\n----")
        print("ANALYSE \n----")

        # Define column widths
        id_width = 5
        text_width = 20
        lemma_width = 20

        # Print headers with fixed widths
        print(
            "ID".ljust(id_width),
            "TEXT".ljust(text_width),
            "LEMMA".ljust(lemma_width),
            sep=""
        )

        # Print rows with fixed widths
        for x in sent.words:
            head_word = sent.words[x.head - 1].text if x.head > 0 else "ROOT"
            print(
                str(x.id).ljust(id_width),
                x.text.ljust(text_width),
                x.lemma.ljust(lemma_width),
                sep=""
            )

        print("\n-----------------------------------\n")

# * EXTRACTION DU FICHIER CORPUS
# %%

with open("cocorep-velo.txt", "r", encoding="UTF-8") as file:
    text_velo = file.read()
    st_velo = nlpStanza(text_velo)
    for phrase in st_velo.sentences:
        print(phrase)


# %%
# Fonction pour extraire les informations sur les vélos
def extraire_infos_velo(st):
    mots_velo_freq = {}
    types_velo_freq = {}
    
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == "NOUN" and ("vélo" in word.text.lower() or "bicyclette" in word.text.lower()):
                mot_pos = f"{word.text.lower()} ({word.pos})"
                mots_velo_freq[mot_pos] = mots_velo_freq.get(mot_pos, 0) + 1
                head_id = word.head
                deprel = word.deprel
                if head_id > 0 and deprel in ["amod", "compound"]:
                    head_word = sent.words[head_id - 1]
                    if head_word.pos in ["NOUN", "ADJ"]:
                        type_velo = f"{head_word.lemma.lower()} ({head_word.pos})"
                        types_velo_freq[type_velo] = types_velo_freq.get(type_velo, 0) + 1
    return mots_velo_freq, types_velo_freq

# Appeler la fonction pour extraire les informations sur les vélos
mots_velo_freq, types_velo_freq = extraire_infos_velo(st_velo)

# Afficher les résultats
print("Mots utilisés pour désigner un vélo et leur fréquence :")
for mot_pos, freq in mots_velo_freq.items():
    print(f"{mot_pos}: {freq}")

print("\nTypes de vélo mentionnés et leur fréquence :")
for type_velo, freq in types_velo_freq.items():
    print(f"{type_velo}: {freq}")


# %%
def analyser_couples_noun_verb(st):

    couples_noun_verb =[]

    for sent in st.sentences:
        for word in sent.words:
            if (
                word.pos == 'NOUN' 
                and word.head > 0 
                and sent.words[word.head - 1].pos == 'VERB'
            ):
                couples_noun_verb.append((word.text, sent.words[word.head - 1].text))
    return couples_noun_verb

# Lire le texte depuis le fichier

# Appeler la fonction d'analyse et obtenir les couples NOUN-VERB
couples_noun_verb = analyser_couples_noun_verb(st_velo)

# Calculer la fréquence des couples NOUN-VERB
frequence_couples = Counter(couples_noun_verb)

# Afficher les 5 couples NOUN-VERB les plus fréquents
nombre_affichage = 5
print(f"Les {nombre_affichage} couples NOUN-VERB les plus fréquents :")
for couple, frequence in frequence_couples.most_common(nombre_affichage):
    print(f"{couple}: {frequence} fois")



# %%
def compter_lemmes_verbes(st):

    lemmes_verbes = Counter()
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == 'VERB':
                lemmes_verbes[word.lemma] += 1

    return lemmes_verbes.most_common(5)

resultat_verbes = compter_lemmes_verbes(st_velo)

# Afficher les 5 lemmes des verbes les plus fréquents
print("Les 5 lemmes des verbes les plus fréquents sont :")
for lemme, count in resultat_verbes:
    print(f"{lemme}: {count} fois")


# %%
# Fonction pour compter les lemmes des adjectifs
def compter_lemmes_adjectifs(st):

    lemmes_adjectifs = Counter()
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == 'ADJ':
                lemmes_adjectifs[word.lemma] += 1
    
    return lemmes_adjectifs.most_common(5)

# Appeler la fonction d'analyse et de comptage des lemmes des adjectifs
resultat_adjectifs = compter_lemmes_adjectifs(st_velo)


# Afficher les 5 lemmes des adjectifs les plus fréquents
print("Les 5 lemmes des adjectifs les plus fréquents sont :")
for lemme, count in resultat_adjectifs:
    print(f"{lemme}: {count} fois")

# %%
# Fonction pour compter les lemmes des noms communs
def compter_lemmes_noms_communs(st):

    lemmes_noms_communs = Counter()
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == 'NOUN':
                lemmes_noms_communs[word.lemma] += 1

    return lemmes_noms_communs.most_common(5)

# Appeler la fonction d'analyse et de comptage des lemmes des noms communs
resultat_noms_communs = compter_lemmes_noms_communs(st_velo)

# Afficher les 5 lemmes des noms communs les plus fréquents
print("Les 5 lemmes des noms communs les plus fréquents sont :")
for lemme, count in resultat_noms_communs:
    print(f"{lemme}: {count} fois")

# %%
# Fonction pour analyser le texte et compter les noms communs
def compter_noms_communs(st):
    return sum(1 for sent in st.sentences for word in sent.words if word.pos == 'NOUN')

# Appeler la fonction pour compter les noms communs
nombre_noms_communs = compter_noms_communs(st_velo)

# Afficher le résultat
print(f"Le nombre de mots avec POS 'NOUN' dans l'analyse syntaxique est : {nombre_noms_communs}")
#%%
#!! compter le nombre d'adjectifs
def compter_adjectifs(st):
    return sum(1 for sent in st.sentences for word in sent.words if word.pos == 'ADJ')

nbAdj = compter_adjectifs(st_velo)
print (f"le nombre total des adjectifs est:{nbAdj}")


#%%
#!! compter nombre de verbes
def compter_verbes(st):
    return sum(1 for sent in st.sentences for word in sent.words if word.pos == 'VERB' or word.pos = 'AUX')

nbVerb = compter_verbes(st_velo)
print (f"le nombre total de verbes est égal à:{nbVerb}")


#%%
# nombre de mots 


#%%moyenne de nombre de mots par phrase

