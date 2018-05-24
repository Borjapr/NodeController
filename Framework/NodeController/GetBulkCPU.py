from pysnmp.hlapi import * #Importamos la libreria pysnmp para utilizar el protocolo SNMP y RMON
from collections import defaultdict
import re
def getbulkcpu(IP, PORT):
    dict1=defaultdict(dict)
    N=0 #indica al comando getbulk que los primeros N objetos pueden ser recuperdados con una simple operacion getnext
    M=1#Indica al comando getbulk que intente hasta M operaciones getnext para recuperar los objetos restantes
    g = bulkCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((IP,PORT)),
                ContextData(),
                N, M,
                ObjectType(ObjectIdentity('AGENT-GENERAL-MIB','agentCPUutilizationIn5sec')),
                ObjectType(ObjectIdentity('AGENT-GENERAL-MIB','agentCPUutilizationIn1min')),
                ObjectType(ObjectIdentity('AGENT-GENERAL-MIB','agentCPUutilizationIn5min')),
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