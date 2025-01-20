import tkinter as tk
from tkinter import messagebox


dictionaries = {
    "Spanish": {
    "buen día":"good morning",
    "hola":"hello",
    "adiós":"goodbye",
    "gracias":"thank you",
    "sí":"yes",
    "no":"no",
    "alimento":"food",
    "dormir":"sleep",
    "familia":"family",
    "casa":"house",
    "hablar":"speak",
    "cocina":"kitchen",
    "pan":"bread",
    "huevos":"eggs",
    "amigo":"friend",
    "agua":"water",
    "sol":"sun",
    "luna":"moon",
    "madre":"mother",
    "padre":"father",
},



   "Idoma": {
    "ev": "house",
    "kitap": "book",
    "araba": "car",
    "cicek": "flower",
    "elma": "apple",
    "su": "water",
    "kopek": "dog",
    "okul": "school",
    "kalem": "pen",
    "kapi": "door",
    "bahce": "garden",
    "deniz": "sea",
    "ayakkabi": "shoe",
    "bilgisayar": "computer",
    "telefon": "phone",
    "Kedi": "cat",
    "Sevgi": "love",
    "Hosca kal": "Goodbye",
    "Aile": "Family",
},





   "Italian": {
   "ciao":"hello/goodbye",
   "grazie":"thank you",
   "per favore":"please",
   "si":"yes",
   "no":"no",
   "amore":"love",
   "famiglia":"family",
   "amico":"friend",
   "casa":"home",
   "cibo":"food",
   "aqua":"water",
   "buoanasera":"goodevening",
   "scusa":"sorry",
   "lavoro":"work",
   "tempo":"time",
   "libro":"book",
   "musica":"music",
   "arrivederci":"goodbye",
   "luna":"moon",
   "sole":"sun",
},


   "German": {
    "liebe":"love",
    "freundin":"friend",
    "haus":"house",
    "familie":"family",
    "bindung":"bonding",
    "schule":"school",
    "frieden":"peace",
    "schiff":"ship",
    "morgen":"morning",
    "zeit":"time",
    "strand":"beach",
    "buch":"book",
    "stern":"star",
    "wald":"forest",
    "geld":"money",
    "stadt":"city",
    "wasser":"water",
    "essen":"food",
    "mond":"moon",
    "wirtschaft":"economy",
},



    "Portugese": {
    "floresta":"forest",
    "montanha":"mountain",
    "praia":"beach",
    "cidade":"city",
    "carro":"car",
    "amor":"love",
    "amigo":"friend",
    "casa":"house",
    "familia":"family",
    "comida":"food",
    "agua":"water",
    "sol":"sun",
    "lua":"moon",
    "livro":"book",
    "escola":"school",
    "amizade":"friendship",
    "estela":"star",
    "dinheiro":"money",
    "tempo":"time",
    "paz":"peace",
}
}



# Function to search the selected dictionary
def search_word():
    selected_dictionary = dictionary_var.get()
    word = entry.get().strip().lower()  # Get user input, trim spaces, and convert to lowercase
    meaning = dictionaries.get(selected_dictionary, {}).get(word)

    if meaning:
        result_label.config(text=f"Meaning: {meaning}")
    else:
        result_label.config(text="")
        messagebox.showinfo(
            "Not Found",
            f"The word '{word}' is not in the {selected_dictionary} dictionary.",
        )


root = tk.Tk()
root.title("Nigerian Dictionary")
welcome_label = tk.Label(root, text="Welcome", padx=200, pady=80, bg='blue', fg="maroon",
                         font='Arial 16')
welcome_label.pack()
root.geometry("600x600")

# Title
title_label = tk.Label(root, text="Please select a Language")
title_label.pack(pady=10)

# Selection menu
dictionary_var = tk.StringVar(value="language")
dictionary_menu = tk.OptionMenu(root, dictionary_var, *dictionaries.keys())
dictionary_menu.pack()

# Word Entry
word_label = tk.Label(root, text="Enter a word:")
word_label.pack()

entry = tk.Entry(root)
entry.pack()

# Search Button
search_button = tk.Button(root, text="Search", command=search_word, pady=10, padx=10)
search_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Meaning will appear here.")
result_label.pack(pady=20)

# Run the application
root.mainloop()































