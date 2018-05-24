from pysnmp.hlapi import * #Importamos la libreria pysnmp para utilizar el protocolo SNMP y RMON
from collections import defaultdict
import re
def getbulk(IP, PORT, MIB, Object):
    dict1=defaultdict(dict)
    N=0 #indica al comando getbulk que los primeros N objetos pueden ser recuperdados con una simple operacion getnext
    M=23#Indica al comando getbulk que intente hasta M operaciones getnext para recuperar los objetos restantes
    g = bulkCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((IP,PORT)),
                ContextData(),
                N, M,
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsOversizePkts')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsFragments')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsJabbers')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsCollisions')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsPkts64Octets')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsPkts65to127Octets')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsPkts128to255Octets')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsPkts256to511Octets')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsPkts512to1023Octets')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsPkts1024to1518Octets')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsDataSource')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsOwner')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsStatus')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsDropEvents')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsOctets')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsPkts')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsBroadcastPkts')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsMulticastPkts')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsCRCAlignErrors')),
                ObjectType(ObjectIdentity('RMON-MIB','etherStatsUndersizePkts')),
                )
    i=0
    while(i<(M+1)):
        try:
            errorIndication,errorStatus,errorIndex,varBinds = next(g)
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
        except:
            break
            pass
        i+=1
    
    #print dict1
    #print "Devolvemos desde Getnext el diccionario"
    return(dict1)

