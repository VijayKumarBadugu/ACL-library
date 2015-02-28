import Base
	
print "Test Case 1 result is in TextCase1.txt"
File=open("TextCase1.txt","wb")
File.write(Base.Acl_list_create("ACL_A", "ALLOW"))
File.write(Base.Acl_list_create("ACL_B", "ALLOW"))
File.write(Base.Acl_list_create("ACL_C", "DENY"))
File.close()


print "Test Case 2 result is in TextCase2.txt"
File=open("TextCase2.txt","wb")
File.write(Base.Acl_list_create("ACL_A", "Allow"))
File.close()

print "Test Case 3 result is in TextCase3.txt"

Base.Acl_add_rule("ACL_A", "100","DENY", "3.4.5.0/24", "4.5.6.0/24", "TCP", "*", "12456")
Base.Acl_add_rule("ACL_B", "2","ALLOW","7.8.9.0/24", "9.10.11.0/24", "TCP", "8080", "13455")
Base.Acl_add_rule("ACL_C","5","DENY", "11.12.13.0/24", "12.13.14.0/24", "UDP", "8080", "*")
Base.Acl_add_rule("ACL_A" , "2","ALLOW","3.4.5.6/32", "4.5.6.7/32", "TCP", "8080", "12456")
Base.Acl_add_rule("ACL_A", "6","DENY","*", "*", "TCP", "8080", "12456")
Base.Acl_add_rule("ACL_B", "10","ALLOW","*", "9.10.11.0/24", "TCP", "*", "*")
Base.Acl_add_rule("ACL_B", "5","ALLOW","192.168.3.4/32", "4.5.6.7/32", "TCP", "8080", "12456")
Base.Acl_add_rule("ACL_C" , "7","DENY","192.168.0.0/24", "192.168.0.0/24", "TCP", "8080", "12456")
Base.Acl_add_rule("ACL_C", "2","ALLOW", "192.168.0.0/25", "192.168.0.0/25", "TCP", "8080", "12456")
Base.Acl_add_rule("ACL_C", "100","ALLOW","3.4.5.6/32", "4.5.6.7/32", "*", "8080", "12456")
Base.Acl_show_all("TextCase3.txt")


print "Test Case 4 result is in TextCase4.txt"
File=open("TextCase4.txt","wb")
File.write(Base.Acl_add_rule("ACL_B", "5" ,"Allow","192.168.3.4/32", "4.5.6.7/32", "TCP", "8080", "12456"))
File.close()

print "Test Case 5 result is in TextCase5.txt"
File=open("TextCase5.txt","wb")
File.write(Base.Acl_check_packet("ACL_A", "3.4.5.6","4.5.6.7","TCP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_A", "192.168.3.5","1.3.4.6","TCP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_A","192.168.3.5","1.3.4.6","UDP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_A","3.4.5.7","4.5.6.7","TCP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_A","3.4.5.6","4.5.6.8","TCP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_A","3.4.6.7","4.5.6.7","TCP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_B","7.8.9.10","9.10.11.12","TCP","8081","13455")+"\n")
File.write(Base.Acl_check_packet("ACL_B","7.8.9.10","9.10.11.12","TCP","8081","13455")+"\n")
File.write(Base.Acl_check_packet("ACL_C","192.168.0.130","192.168.0.131","TCP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_C","192.168.0.120","192.168.0.121","TCP","8080","12456")+"\n")
File.write(Base.Acl_check_packet("ACL_C","192.168.1.130","192.168.1.131","TCP","8080","12456")+"\n")

print "Test Case 6 result is in TextCase6.txt"
Base.Acl_del_rule("ACL_C", "100")
Base.Acl_show_all("TextCase6.txt")

print "Test Case 7 result is in TextCase6.txt"
Base.Acl_del_rule("ACL_C", "2")
Base.Acl_show_all("TextCase7.txt")


print "Test Case 8 result is in TextCase6.txt"
Base.Acl_add_rule("ACL_C", "100","ALLOW","3.4.5.6/32", "4.5.6.7/32", "*", "8080", "12456")
Base.Acl_show_all("TextCase8.txt")







