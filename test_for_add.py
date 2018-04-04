from login import ldapTool2
import pdb
import threading
while(True):
	t = ldapTool2.LDAPTool()
	name = raw_input('username? :')
	print('adding %s'%name)
	t.ldap_add_user(name,name+'@qq.com',name,name)
	next = raw_input('add next?')
	if(next != ''):
		break
