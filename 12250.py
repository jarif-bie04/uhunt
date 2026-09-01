i=1
while True:
    try:
        lan = input()
        
        if lan == "HELLO":
            print(f"Case {i}: ENGLISH")
            i+= 1
        elif lan == "HOLA":
            print(f"Case {i}: SPANISH")
            i+= 1
        elif lan == "HALLO":
            print(f"Case {i}: GERMAN")
            i+= 1
        elif lan == "BONJOUR":
            print(f"Case {i}: FRENCH")
            i+= 1
        elif lan == "CIAO":
            print(f"Case {i}: ITALIAN")
            i+= 1
        elif lan == "ZDRAVSTVUJTE":
            print(f"Case {i}: RUSSIAN")
            i+= 1
        elif lan == "#":
            break
        else:
            print(f"Case {i}: UNKNOWN")
            i+= 1
        
    except EOFError:
        break