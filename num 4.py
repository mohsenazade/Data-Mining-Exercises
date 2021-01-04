
while True:
    
    MySentence = "bani,adam,azaie,yek,digarand,ke,dar,afarinesh,ze,yek,goharand"
    print("Our words are: ",MySentence)
    input("enter for Spliting: ")

    MySentence_Splited = MySentence.split(",")
    print("Word after packaging : ", MySentence_Splited)

    keyboard.wait('q')
    keyboard.send('ctrl+6')