None
meme_dict={"CRING": "qualcosa che ti fa mettere in imbarazzo,è imbarazzante",
           "NABBO": "una persona scarsa,per esempio nei giochi di combattimento",
           "LAGGARE": "quando la rete non ti prende bene",
            "PARA": "preoccuparsi per qualcosa"}
parola = input("Scrivi una parola di cui nn conosci il significato (preferibilmente in maiuscolo")

if parola in meme_dict.keys():
    print(meme_dict[parola])
else:
    print("Mi dispiace la parola non è stata trovata ")
