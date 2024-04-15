# Fonction pour générer les valeurs de vérité
def generate_truth_values():
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                yield a, b, c

# Fonction logique
def logical_function(a, b, c):
    return (a and not b) or (b and c)

# Table de vérité
def truth_table():
    print("Table de vérité de la fonction logique [(a and not b) or (b and c)] :")
    print("a\tb\tc\tF(a, b, c)")
    print("-----------------------")
    for a, b, c in generate_truth_values():
        result = logical_function(a, b, c)
        print(f"{a}\t{b}\t{c}\t{result}")

# Première forme canonique
def first_canonical_form():
    termes_premiere_forme = []
    for a, b, c in generate_truth_values():
        if logical_function(a, b, c):
            termes_premiere_forme.append(f"({'not ' if not a else ''}a{' not ' if b else ''}b{' ' if not b else ''}c)")
    print("\nPremière forme canonique :")
    print(" + ".join(termes_premiere_forme))

# Seconde forme canonique
def second_canonical_form():
    termes_seconde_forme = []
    for a, b, c in generate_truth_values():
        if not logical_function(a, b, c):
            termes_seconde_forme.append(f"({'not ' if a else ''}a{' ' if b else ''}{'not ' if not b else ''}b{' ' if not b else ''}c")
    print("\nSeconde forme canonique :")
    print(" + ".join(termes_seconde_forme))

# Appel des fonctions
truth_table()
first_canonical_form()
second_canonical_form()