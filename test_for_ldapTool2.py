from login import ldapTool2
import pdb
t = ldapTool2.LDAPTool()
print("add user test")
t.ldap_add_user('test','test@qq.com','test','test')
print("add user test passed")
print("search test")
r = t.ldap_search_dn(value='test')
print('dn result:%s'%str(r))
#pdb.set_trace()
print("get user test")
r=t.ldap_get_user(uid='test')
print('get user result: %s' %r)

for i in range(2):
        name = 'test'+str(i)
        t.ldap_add_user(name,name+'@qq.com',name,name)
