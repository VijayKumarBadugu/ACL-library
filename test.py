ACLNAME,SRC_IP_PREFIX, DST_IP_PREFIX, PROTO, SRC_PORT, DST_PORT, PRIORITY,ACTION
ACLNAME,SRC_IP_PREFIX, DST_IP_PREFIX, PROTO, SRC_PORT, DST_PORT, PRIORITY,ACTION
ACLL,SRC_IP_PREFIX, DST_IP_PREFIX,100, SRC_PORT, DST_PORT, PRIORITY,ACTION

for i in range(len(output)):
		if output[i]==PRIORITY:
			print "Function cannot be added"
			return "Done"
	print output



File=open("ACL.txt")
	output = []
	output2=[]
	for line in File:
		Line=line.split(",")
		if Line[0]==ACLNAME:
			print "Found Entry"
			output2.append(line)
		else:
			output.append(line)
			
	File.close()
	File=open("ACL.txt","wb")
	File.writelines(output)
	File.close()

	File=open("ACL.txt")
	output=[]
	for line in File:
		line=line.split(",")
		if line[0]!="\n":
			output.append(line[6])
	File.close()
	for i in range(len(output)):
		print output[i]
		print PRIORITY
		if output[i]==PRIORITY:
			print "Function cannot be added"
			File.close()
			File=open("ACL.txt","a")
			File.writelines(output2)
			File.close()
			
			return "Done"
	File=open("ACL.txt","a")
	File.write(ACLNAME+","+SRC_IP_PREFIX+","+DST_IP_PREFIX+","+PROTO+","+SRC_PORT+","+DST_PORT+","+PRIORITY+","+ACTION+"\n")
	return "Done"










****
def Acl_list_create(NAME,ACTION):
	File=open("ACL.txt")
	for line in File:
		
		line=line.strip()
		line=line.split(",")
		
		if line[0]==NAME:
			File.close()
			return "True"
	File.close()
	File=open("ACL.txt","a")
	File.write(NAME+','+'*,'+'*,'+'*,'+'*,'+'*,'+'*,'+ACTION+"\n")
	File.close()
	return "False"

def Acl_list_delete(NAME):
	File=open("ACL.txt")
	output = []
	for line in File:
		Line=line.split(",")
		if Line[0]==NAME:
			print "Found Entry"
		else:
			output.append(line)
			
	File.close()
	File=open("ACL.txt","wb")
	File.writelines(output)
	File.close()
	return "ACL updated"

def Acl_show_rules(ACLNAME,FILENAME):
	File=open("ACL.txt")
	for line in File:
		Line=line.split(",")
		if Line[0]==ACLNAME:
			print "Came here"
			Temp=open(FILENAME,"wb")
			Temp.write(line)
			Temp.close()
			print FILENAME
			return "File created"
	File.close()
	
	return "File created"

def Acl_show_all(FILENAME):
	File=open("ACL.txt")
	Temp=open(FILENAME,"wb")
	for line in File:
		Temp.write(line)
	Temp.close()
	File.close()
	return "File created"

def Acl_del_rule(ACLNAME,PRIO):
	File=open("ACL.txt")
	output=[]
	output2=[]
	
	for line in File:
		Line=line.startswith(ACLNAME)
		Temp=line.split(",")
		if Temp[0]==ACLNAME:
			for i in range(len(Temp)):
				
				if Temp[i]==PRIO:
					
					output2.append("*,")
				else:
					if i==(len(Temp)-1):
						output2.append(Temp[i])
					else:
						output2.append(Temp[i]+",")					

		else:
			output.append(line)
			
	File.close()
	File=open("ACL.txt","wb")
	File.writelines(output)
	File.writelines(output2)
	File.close()

	return "Done"	

def Acl_add_rule(ACLNAME,PRIORITY,SRC_IP_PREFIX='*', DST_IP_PREFIX='*', PROTO='*', SRC_PORT='*', DST_PORT='*',ACTION='Allow'):
	File=open("ACL.txt")
	output = []
	output2=[]
	for line in File:
		Line=line.split(",")
		if Line[0]==ACLNAME:
			print "Found Entry"
			output2.append(line)
		else:
			output.append(line)
			
	File.close()
	File=open("ACL.txt","wb")
	File.writelines(output)
	File.close()

	File=open("ACL.txt")
	output=[]
	for line in File:
		line=line.split(",")
		if line[0]!="\n":
			output.append(line[6])
	File.close()
	for i in range(len(output)):
		print output[i]
		print PRIORITY
		if output[i]==PRIORITY:
			print "Function cannot be added"
			File.close()
			File=open("ACL.txt","a")
			File.writelines(output2)
			File.close()
			
			return "Done"
	File=open("ACL.txt","a")
	File.write(ACLNAME+","+SRC_IP_PREFIX+","+DST_IP_PREFIX+","+PROTO+","+SRC_PORT+","+DST_PORT+","+PRIORITY+","+ACTION+"\n")
	return "Done"

def Acl_check_packet(ACLNAME, SRC IP, DST IP, PROTO, SRC PORT, DST PORT):
	File=open("ACL.txt")
	for line in File:
		Line=line.split(",")
		if Line[0]==ACLNAME:
		

	
	

	
	addr5 = ipaddress.ip_address(DSTIP)
			if item[3]=="*":
				count=count+1
			else:	
				if addr4 in ipaddress.ip_network(item[3])==True:
					count=count+1
			if item[4]=="*":
				count=count+1
			else:	
				if addr5 in ipaddress.ip_network(item[4])==True:
					count=count+1
			if item[5]=="*":
				count=count+1
			else:
				if item[5]==PROTO:
					 count=count+1
			if item[6]=="*":
				count=count+1
			else:
				if item[6]==SRCPORT:
					count=count+1
			if item[7]=="*":
				count=count+1
			else:
				if item[7]==DSTPORT:
					count=count+1
			if count==7:
				print "Packet",item[2]	
				return item

		

