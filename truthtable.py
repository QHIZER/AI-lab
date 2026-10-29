from itertools import product

def entails(kb, query, symbols):
    print("\nTRUTH TABLE ENUMERATION")
    print("-" * 55)
    print(f"{'P':<8}{'Q':<8}{'P -> Q':<12}{'Query Q':<12}{'KB entails Q'}")
    print("-" * 55)

    for p, q in product([True, False], repeat=2):
        model = {'P': p, 'Q': q}
        kb_value = kb(model)
        query_value = query(model)

        print(f"{str(p):<8}{str(q):<8}{str(kb_value):<12}"
              f"{str(query_value):<12}"
              f"{'No' if kb_value and not query_value else '-'}")

        if kb_value and not query_value:
            print("\nResult: KB does not entail Q")
            return False

    print("\nResult: KB entails Q")
    return True


kb = lambda m: (not m['P']) or m['Q']
query = lambda m: m['Q']

entails(kb, query, ['P', 'Q'])