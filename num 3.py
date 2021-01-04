
while True:
   

    MySentence = input("Please enter a sentence : ")
    MySentence_Splited = MySentence.split(" ")


    print("\n tedad kalamat besorat list : ",MySentence_Splited)
    print("Words totall: ",len(MySentence_Splited))


    keyboard.wait('q')
    keyboard.send('ctrl+6')