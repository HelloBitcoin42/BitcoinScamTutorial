from bitcoin import *
priv = random_key()
pub = privtopub(priv)
addr = pubtoaddr(pub)
#print("priv = " + priv)
#print("pub = " + pub)
#print("addr = " + addr)
#print("History of " + addr + ": ")
#print(history(addr))
#print("History of 1G77U1jrd1YigSWwfRr6dT3yQqAuG6xDpL: ")
#print(history("1G77U1jrd1YigSWwfRr6dT3yQqAuG6xDpL"))

print("This is a Bitcoin Tutorial.  It will teach you something about Bitcoin! \nDeposit Bitcoin here to continue: \n" + addr)

while history(addr) == []:
    if history(addr) != []:
        print(history())
        print("Congradulations!!\nYou have just been scammed!\nWelcome to Bitcoin\nSorry for your loss")
