def reverse_string():
    """ input: string
    output: reversed string
    """
    # noe som skjer
    text = "neger"
    text_2 = "regen"

    "Skriv ordet baklengs: "
    "ta ordet og separer bokstavene slik at de står for seg selv"
    "deretter sorterer du bokstavene i motsatt rekkefølge enn det de var tidligere"

    text = text.replace("n", "r")
    print(text)
    text = text.replace("neger"[4], "neger"[0])
    print(text)

reverse_string()


