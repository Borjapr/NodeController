import argparse, re, sys
from Lib.ParameterChecking import _re_IPv4Port
from Lib.VTY import VTY
from Client import Client
#Importamos los distinos comandos
from Commands.VTY import Command_VTY
from Commands.VTY_Connect import Command_VTY_Connect
from Commands.VTY_Traceback import Command_VTY_Traceback

from Commands.Manager import Command_Manager
from Commands.Manager_Version import Command_Manager_Version
from Commands.Manager_Terminate import Command_Manager_Terminate
from Commands.Manager_Start import Command_Manager_Start

from Commands.Agent import Command_Agent
from Commands.Agent_Create import Command_Agent_Create
from Commands.Agent_Start import Command_Agent_Start
from Commands.Agent_Stop import Command_Agent_Stop
from Commands.Agent_Modify import Command_Agent_Modify
from Commands.Agent_Delete import Command_Agent_Delete
from Commands.Agent_List import Command_Agent_List

from Commands.ObservationPoint import Command_ObservationPoint
from Commands.Agent_ObservationPoint_List import Command_Agent_ObservationPoint_List
from Commands.Agent_ObservationPoint_Create import Command_Agent_ObservationPoint_Create
from Commands.Agent_ObservationPoint_Modify import Command_Agent_ObservationPoint_Modify
from Commands.Agent_ObservationPoint_Delete import Command_Agent_ObservationPoint_Delete
from Commands.Agent_ObservationPoint_Enable import Command_Agent_ObservationPoint_Enable
from Commands.Agent_ObservationPoint_Disable import Command_Agent_ObservationPoint_Disable

def IPv4PortType(s):
    if(re.match(_re_IPv4Port, s)): return(str(s))
    raise argparse.ArgumentTypeError

def main():
     # ----- Read Configuration ---------------------------------------------------
    parser = argparse.ArgumentParser(description='NCTerm - Node Controler Terminal')
    parser.add_argument('ipPort',         metavar='ip:Port', type=IPv4PortType,           help='server IPv4:port')
    parser.add_argument('-s', '--script', metavar='script',  type=argparse.FileType('r'), help='script file, interactive when not specified')
    parser.add_argument('-o', '--output', metavar='output',  type=argparse.FileType('w'), help='output file, terminal when not specified')
    args = parser.parse_args()

    serverIP,serverPort = args.ipPort.split(':')
    serverPort = int(serverPort)
    sys.stdout.write('Connecting to %s:%d...\n' % (serverIP, serverPort))
    
    client = Client()
    client.configure({'serverIP': serverIP, 'serverPort': serverPort})

    vty = VTY(client, prompt='NCTerm> ', stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr) #Definimos la entrada y salida de datos (teclado y terminal)
    #Anadimos los comandos creados
    vty.addCommand(Command_VTY)
    vty.addCommand(Command_VTY_Connect)
    vty.addCommand(Command_VTY_Traceback)
    vty.addCommand(Command_Manager)
    vty.addCommand(Command_Manager_Terminate)
    vty.addCommand(Command_Manager_Version)
    vty.addCommand(Command_Manager_Start)
    vty.addCommand(Command_Agent)
    vty.addCommand(Command_Agent_Create)
    vty.addCommand(Command_Agent_Start)
    vty.addCommand(Command_Agent_Stop)
    vty.addCommand(Command_Agent_Modify)
    vty.addCommand(Command_Agent_Delete)
    vty.addCommand(Command_Agent_List)
    vty.addCommand(Command_ObservationPoint)
    vty.addCommand(Command_Agent_ObservationPoint_Create)
    vty.addCommand(Command_Agent_ObservationPoint_List)
    vty.addCommand(Command_Agent_ObservationPoint_Modify)
    vty.addCommand(Command_Agent_ObservationPoint_Delete)
    vty.addCommand(Command_Agent_ObservationPoint_Enable)
    vty.addCommand(Command_Agent_ObservationPoint_Disable)
    
    
    succeeded = vty.runCommand('manager version')
    if(not succeeded): return(1)

    vty.run()

    return(0)

if(__name__ == '__main__'):
    sys.exit(main())
