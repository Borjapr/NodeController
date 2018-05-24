from pysnmp.hlapi import * #Importamos la libreria pysnmp para utilizar el protocolo SNMP y RMON
from collections import defaultdict
import re
def getrequest(IP, PORT, MIB, Object):
    print "estamos dentro de getrequest"
    dict1=defaultdict(dict)
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),#Creating SNMP Engine
            CommunityData('public', mpModel=1), #Si ponemos como sengundo argumento mpModel=0 sera SNMPV1 y si mpModel=1 so nada sera SNMPv2c 
            UdpTransportTarget((IP,PORT)), #Usamos UDP y el protocolo IPV4
            ContextData(),
            ObjectType(ObjectIdentity(MIB,Object)))
    )
    print "getr1"
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
    else:
        print "getr2"
        for varBind in varBinds:
            tipo =varBind[0].prettyPrint()
            print tipo
            colnum=re.split('::',tipo)
            columnas= colnum[1].split('.',2)
            print columnas
            try:
                valor = eval(varBind[1].prettyPrint())
            except: 
                valor = varBind[1].prettyPrint()
            print valor
            try:
                key1 = eval(columnas[0])
            except: 
                key1 = columnas[0]
            print "gtr3"
            dict1[key1]=valor
    print dict1
    return(dict1)