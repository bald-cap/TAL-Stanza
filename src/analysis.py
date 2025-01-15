
# %%
import stanza
from collections import Counter

nlpStanza=stanza.Pipeline("fr")


# * EXTRACTION DU FICHIER CORPUS
# %%
with open("src\cocorep-velo.txt", "r", encoding="UTF-8") as file:
    text_velo = file.read()
    st_velo = nlpStanza(text_velo)
    for phrase in st_velo.sentences:
        print(phrase.text)


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