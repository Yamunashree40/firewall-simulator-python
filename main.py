
from core import main



def main1():
    try:
        f = open('packets/tcp.txt','r')
        g = open('packets/udp.txt','r')  
        choice = int(input("Enter your filters:\n1)TCP\n2)UDP\n"))
        if choice==1:
            main(f)
        else:
            main(g)
    except:
        print()

main1()