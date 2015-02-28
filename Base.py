from operator import itemgetter, attrgetter, methodcaller
import ipaddress
def Acl_list_create(NAME,ACTION):
	File=open("ACL.txt","a")
	File.close()
	File=open("ACL.txt")
	for line in File:
		
		line=line.strip()
		line=line.split(",")
		
		if line[0]==NAME:
			File.close()
			return "False"
	File.close()
	File=open("ACL.txt","a")
	File.write(NAME+','+'-1,'+ACTION+','+'*,'+'*,'+'*,'+'*,'+'*,'+"\n")
	File.close()
	return "True"

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
			Temp=open(FILENAME,"a")
			Temp.write(line)
			Temp.close()
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
			
			
			if Temp[1]!=PRIO:
				output.append(line)
										

		else:
			output.append(line)
			
	File.close()
	File=open("ACL.txt","wb")
	File.writelines(output)
	File.writelines(output2)
	File.close()
	return "Done"	

def Acl_add_rule(ACLNAME,PRIORITY,ACTION='ALLOW',SRC_IP_PREFIX='*', DST_IP_PREFIX='*', PROTO='*', SRC_PORT='*', DST_PORT='*'):
	File=open("ACL.txt")
	for line in File:
		Line=line.split(",")
		if Line[0]==ACLNAME:
			if Line[1]==PRIORITY:
				return "Rule Cannot be added"
					
	File.close()
	File=open("ACL.txt","a")
	File.write(ACLNAME+","+PRIORITY+","+ACTION+","+SRC_IP_PREFIX+","+DST_IP_PREFIX+","+PROTO+","+SRC_PORT+","+DST_PORT+","+"\n")
	return "Rule added"

def Acl_check_packet(ACLNAME,SRCIP, DSTIP, PROTO, SRCPORT, DSTPORT):
	comp=[]
	File=open("ACL.txt")
	for line in File:
		Line=line.split(",")
		if Line[0]==ACLNAME:
			comp.append(Line)
			
	comp.sort(key=lambda x: float(x[1]),reverse=True)
	for item in comp:
			count=0
			if item[3]=="*":
				count=count+1
			else:	
				if ipaddress.networkcompare(item[3],SRCIP)==True:
					count=count+1
			if item[4]=="*":
				count=count+1
			else:	
				if ipaddress.networkcompare(item[4],DSTIP)==True:
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
			if count==5:
				print "Packet",item[2]	
				print item
				return item[2]+" Priority of ACL "+item[1]
			
	return "No Match Found"

			

				
			
		
	
	
	
			
	

		

	
	

	
	

		
