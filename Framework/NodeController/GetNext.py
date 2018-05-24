from pysnmp.hlapi import * #Importamos la libreria pysnmp para utilizar el protocolo SNMP y RMON
from collections import defaultdict
import re
def getnext(IP, PORT, MIB, Object):
    dict1=defaultdict(dict)
    for (errorIndication,
        errorStatus,
        errorIndex,
        varBinds) in nextCmd(SnmpEngine(),
                            CommunityData('public', mpModel=1),
                            UdpTransportTarget((IP,PORT)),
                            ContextData(),
                            ObjectType(ObjectIdentity(MIB,Object)),
                            lexicographicMode=False):

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                #print(' = '.join([x.prettyPrint() for x in varBind]))
                tipo =varBind[0].prettyPrint()
                #tipo[len(tipo)-1:len(tipo)]-> Obtener indices tipo.split('.',2)[1]
                #tipo[8:len(tipo)-2] -> para obtener el nombre de la columna bonito 
                colnum=re.split('::',tipo)
                columnas= colnum[1].split('.',2)
                #print columnas
                try:
                    valor = eval(varBind[1].prettyPrint())
                except: 
                    valor = varBind[1].prettyPrint()
                try:
                    key1 = eval(columnas[0])
                except: 
                    key1 = columnas[0]
                try:
                    key2 = eval(columnas[1])
                except:
                    key2 = columnas[1]
                dict1[key1][key2]=valor
                #print dict1
    #print "Devolvemos desde Getnext el diccionario"
    return(dict1)
