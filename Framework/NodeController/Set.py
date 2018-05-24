from pysnmp.hlapi import *

def setnext(IP, PORT, MIB, Object,value):
  errorIndication, errorStatus, errorIndex, varBinds = next(
            setCmd(SnmpEngine(),#Creating SNMP Engine
            CommunityData('public',mpModel=1),#Si ponemos como sengundo argumento mpModel=0 sera SNMPV1 y si mpModel=1 so nada sera SNMPv2c 
            UdpTransportTarget((IP, PORT)), #Usamos UDP y el protocolo IPV4
            ContextData(),
            ObjectType(ObjectIdentity(MIB,Object), #Tupla de (OID,value) en este caso seria tupla (OID,valorNuevo)
                    value)
  ))

  if errorIndication:
    print(errorIndication)
  elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
  else:
    for varBind in varBinds:
      print(' = '.join([x.prettyPrint() for x in varBind]))
