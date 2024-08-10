from PyDictionary import PyDictionary

dictionary = PyDictionary()

# functions
def meaning(word):
    meaning = dictionary.meaning(word)
    if meaning:
        print(f"Definition of '{word}':")
        for part_of_speech, definitions in meaning.items():
            print(f"{part_of_speech}:")
            for definition in definitions:
                print(f"  - {definition}")
    else:
        print(f"Sorry, {word} is not a word")

# loop
try:
    while True:
        x = input("Enter a word (Ctrl+C to quit): ").strip()
        meaning(x)
        
except KeyboardInterrupt:
    print("\nExiting the program.")
