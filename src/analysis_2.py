def extraire_types_velo(st):
    types_velo_freq = Counter()
    
    for sent in st.sentences:
        for word in sent.words:
            if word.pos == "NOUN" and ("vélo" in word.text.lower() or "bicyclette" in word.text.lower()):
                mot_pos = f"{word.text.lower()} ({word.pos})"
                types_velo_freq[mot_pos] += 1
                for child in sent.words:
                    if child.head == word.id and child.pos in ["NOUN", "ADJ"] and child.deprel in ["amod", "compound"]:
                        type_velo = f"{child.lemma.lower()} ({child.pos})"
                        types_velo_freq[type_velo] += 1

    return types_velo_freq

# Appel
types_velo_freq = extraire_types_velo(st_velo)

# Affichage
print("\nTypes de vélo mentionnés et leur fréquence :")
for type_velo, freq in types_velo_freq.items():
    print(f"{type_velo}: {freq}")