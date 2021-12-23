def ball():
    redfile=input("Enter Your Name")
    file=open(redfile,"r")
    for line in file:
      word=line.split()
      numberofwords=numberofwords+len(word)
      
    print(numberofwords)

    