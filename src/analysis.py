
# %%
import stanza
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
# %%
with open("message.txt", "r", encoding="UTF-8") as file:
    holding = file.read()
    lemmatization(holding)
# %%
