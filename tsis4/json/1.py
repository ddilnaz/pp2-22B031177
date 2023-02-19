#https://github.com/ddilnaz/pp2-22B031177/blob/master/tsis4/json/sampledata.json
import json
x = open(r'C:\Users\ddilnaz\Desktop\git\tsis4\json\sampledata.json')
y = json.load(x)
print('''=======================================================================================
DN                                                 Description           Speed    MTU" 
-------------------------------------------------- --------------------  ------  ------''')
imdata = y["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:51} {1:20} {2:8} {3:6}".format(dn,descr,speed,mtu))