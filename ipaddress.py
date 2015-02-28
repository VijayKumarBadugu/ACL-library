import socket, struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

def networkcompare(Network,IP):
	IP=ip2long(IP)
	Network=Network.split("/")
	NetworkID=ip2long(Network[0])
	Networkmask=2**(32-(int(Network[1])))
	if (IP>NetworkID)&(IP<NetworkID+Networkmask-1):
		return True
	else:
		return False

	
