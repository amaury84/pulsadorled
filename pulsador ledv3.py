import pyfirmata                              # Librería para comunicarse con Arduino

# IDENTIFICACIÓN DEL PUERTO USB 
puertoUSB = "COM4"                            # Define el puerto USB donde conecta Arduino
                                              
# CONFIGURACIÓN DEL PUERTO USB
print('Configuracion de las comunicaciones usando FIRMATA a Arduino..')    
controlArdu = pyfirmata.Arduino(puertoUSB)    # Habilita la comunicación con Arduino
print("Conexión Exitosa...")
pyfirmata.util.Iterator(controlArdu).start()  # Prepara la transmisión de datos

# DEFINIR PINES Y VARIABLES
S2 = controlArdu.get_pin('d:2:i')             # Configura el pin de entrada                                              
actuador = controlArdu.get_pin('d:13:o')      # Configura el pin de salida
                                              
# INICIO DEL PROGRAMA
while True:                                   
    # RECIBE Y TRANSMITE A ARDUINO POR EL USB
    if S2.read() == False:                     # Evalua S2 (Pulsador)
       print("No Pulsado...")                                    
       actuador.write(0)                       # Transmite APAGADO
       controlArdu.pass_time(0.5)              
    elif S2.read() == True:                                      
        print("Pulsado...")                
        actuador.write(1)                      # Transmite PARPADEO                                          
        controlArdu.pass_time(0.5)             
        actuador.write(0)                                            
        controlArdu.pass_time(0.5)
        
        

