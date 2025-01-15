
# %%
import stanza
import re
from collections import Counter
nlpStanza=stanza.Pipeline("fr")


# %%
# * 3.1.1. Nombre de phrases
# ? EXTRACTION ET AFFICHAGE DE CHAQUE PHRASE DU FICHIER CORCOREP-VELO.TXT
with open("src\cocorep-velo.txt", "r", encoding="UTF-8") as file:
    text_velo = file.read()
    st_velo = nlpStanza(text_velo)
    num_phrase = 0
    for phrase in st_velo.sentences:
        num_phrase += len(phrase.text)

# Total
print(f"Le texte a {num_phrase} phrases en total")


# %%
# * 3.1.2. Nombre moyen de phrases par message
# ? CALCUL ET AFFICHAGE DE LA MOYENNE NOMBRE DE PHRASES PAR MESSAGES SEPARES PAR DES LIENS HTTPS.
def segmenter_messages(texte):
    return re.split(r"<.*?>", texte)

with open("src/cocorep-velo.txt", "r", encoding="UTF-8") as file:
    raw_text = file.read()
    messages = segmenter_messages(raw_text)
    messages = [msg.strip() for msg in messages if msg.strip()]

def compter_phrases_par_message(messages):
    phrase_counts = []
    for msg in messages:
        st = nlpStanza(msg)
        phrase_counts.append(len(st.sentences))
    return phrase_counts

nombre_phrases_par_message = compter_phrases_par_message(messages)

# Calcul
def calculer_moyenne(liste):

    if not liste:
        return 0
    return sum(liste) / len(liste)

moyenne_phrases_par_message = calculer_moyenne(nombre_phrases_par_message)

# Affichage
print(f"Nombre moyen de phrases par message : {moyenne_phrases_par_message:.2f}")

# %%
# * 3.2.a. Types de vélo mentionnés
# ? CALCUL DE LA FREQUENCE DES MOTS/ SYNONYMES DE "VELO"
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

# Appel
mots_velo_freq, types_velo_freq = extraire_infos_velo(st_velo)

# Affichage
print("Mots utilisés pour désigner un vélo et leur fréquence :")
for mot_pos, freq in mots_velo_freq.items():
    print(f"{mot_pos}: {freq}")

print("\nTypes de vélo mentionnés et leur fréquence :")
for type_velo, freq in types_velo_freq.items():
    print(f"\t{type_velo}: {freq}")


# %%
# * 3.1.11 Couple NOUN-VERB le plus fréquent tel que :
# ? CALCUL ET AFFICHAGE DU "NOUN-VERB" LE PLUS FREQUENT
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

# Appel
couples_noun_verb = analyser_couples_noun_verb(st_velo)

# Calcul
frequence_couples = Counter(couples_noun_verb)

# Affichage
nombre_affichage = 1
print(f"Les {nombre_affichage} couples NOUN-VERB les plus fréquents :")
for couple, frequence in frequence_couples.most_common(nombre_affichage):
    print(f"{couple}: {frequence} fois")



# %%
# * 3.1.10. Lemmes des 5 verbes les plus fréquents
# ? CALCUL ET AFFICHAGE DES LEMMES DES 5 VERBES VERBES LE PLUS FREQUENTS
def compter_lemmes_verbes(st):

    lemmes_verbes = Counter()
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == 'VERB':
                lemmes_verbes[word.lemma] += 1

    return lemmes_verbes.most_common(5)

resultat_verbes = compter_lemmes_verbes(st_velo)

# Affichage
print("Les 5 lemmes des verbes les plus fréquents sont :")
for lemme, count in resultat_verbes:
    print(f"{lemme}: {count} fois")


# %%
# * 3.1.8. Lemmes des 5 adjectifs les plus fréquents
# ? CALCUL ET AFFICHAGE DES 5 ADJECTIFS LE PLUS FREQUENT DANS LE TEXTE
def compter_lemmes_adjectifs(st):

    lemmes_adjectifs = Counter()
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == 'ADJ':
                lemmes_adjectifs[word.lemma] += 1

    return lemmes_adjectifs.most_common(5)

# Appel
resultat_adjectifs = compter_lemmes_adjectifs(st_velo)

# Affichage
print("Les 5 lemmes des adjectifs les plus fréquents sont :")
for lemme, count in resultat_adjectifs:
    print(f"{lemme}: {count} fois")

# %%
# * 3.1.6. Lemmes des 5 noms communs les plus fréquents
# ? CALCUL ET AFFICHAGE DES LEMMES DES 5 NOMS COMMUNS LE PLUS FREQUENTS
def compter_lemmes_noms_communs(st):

    lemmes_noms_communs = Counter()
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == 'NOUN':
                lemmes_noms_communs[word.lemma] += 1

    return lemmes_noms_communs.most_common(5)

# Appel
resultat_noms_communs = compter_lemmes_noms_communs(st_velo)

# Affichage
print("Les 5 lemmes des noms communs les plus fréquents sont :")
for lemme, count in resultat_noms_communs:
    print(f"{lemme}: {count} fois")

# %%
# * 3.1.4. Nombre de noms communs (pos = NOUN) 
# ? CALCUL ET AFFICHAGE DU NOMBRE TOTAL DE NOMS COMMUNS 
def compter_noms_communs(st):
    return sum(1 for sent in st.sentences for word in sent.words if word.pos == 'NOUN')

# Appel
nombre_noms_communs = compter_noms_communs(st_velo)

# Affichage
print(f"Le nombre de mots avec POS 'NOUN' dans l'analyse syntaxique est : {nombre_noms_communs}")