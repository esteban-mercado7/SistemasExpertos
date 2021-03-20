# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import random
from os import system
import sys
from random import randint

background =  ( ' En la reunión de los fines de semana, cinco amigos se reúnen. \n' 
                ' Norma Bates y su hijo Norman, Laurel Castillo estudiante de derecho y alumna de la \n' 
                ' abogada Annalise Keating quien se especializa en derecho penal y, finalmente, \n' 
                ' su asistente Frank Delfino. \n \n'
                ' Ellos se conocieron ya que fueron abogados defensores de Norma Bates y \n'
                ' Norman después de que fueran acusados de asesinato de primer grado, pero \n'
                ' salieron impunes gracias a un excelente manejo por parte de sus representantes. \n \n'
                ' En una de esas reuniones Blaire Watson, una invitada para esa ocasión, \n'
                ' hacía acto de presencia. Blaire, una profesora y amiga de Norma, fue invitada  \n'
                ' particularmente por Norman quien, a pesar de ser mucho menor que ella, parecía \n'
                ' muy interesado por conocerla. Su madre, a pesar de no estar de acuerdo con la \n'
                ' invitación, accedió ya que hacía mucho tiempo no la veía. \n \n'
                ' Por otro lado, Annalise se debatía entre promover a Laurel por su gran  \n'
                ' ayuda en los casos o por ratificar a Frank en su puesto ya que era una persona de  \n'
                ' su confianza, además de tener un manejo admirable de situaciones complicadas,  \n'
                ' ya sea con clientes u otras situaciones con personas ajenas a su círculo que  \n'
                ' pudieran amenazar su tranquilidad.  \n'
                ) 

reglas = ("Bienvenido al juego. ¿Estás listo para comenzar? \n \n"
          "A continuación mostraremos las 'reglas del juego' \n"
          " - Se mostrará el background del juego al iniciar. \n"
          " - Aleatoriamente se seleccionará la historia a resolver. \n"
          " - También aleatoriamente se sortearán los personajes entre culpable y no culpables. \n"
          " - Se mostrarán las opciones en consola y deberás presionar solamente las teclas que \n"
          "   representan las opciones, de lo contrario el juego finalizará automáticamente. \n"
          "   Tendrás tres oportunidades para encontrar al culpable, el arma utilizada y \n "
          "   el lugar del homicidio. Esas tres oportunidades contarán desde el momento en que \n"
          "   termines de leer la historia principal, después de la primer pista es la segunda \n"
          "   oportunidad y después de la segunda posta será la tercer y última oportunidad de \n"
          "   señalar al culpable. Al finalizar se mostrarán las respuestas correctas y una tabla \n"
          "   para que compares tus resultados con las calificaciones. \n"
          " - Si fallas en tus inferencias irás perdiendo vidas, así como si no aciertas en la tercer \n"
          "   oportunidad que tienes. \n"
          )

armas = ['la soga', 'el cuchillo', 'la pistola', 'el martillo', 'la bolsa']
randArmas = armas

personajes = ['Blaire Watson', 'Norman Bates', 'Norma Bates', 'Laurel Castillo', 'Frank Delfino', 'Annalise Keating']
randPersonajes = personajes

locaciones = ['la sala de estar', 'el cuarto de lavado', 'el baño', 'la cocina', 'el balcón']
randLocaciones = locaciones

def Aleatorio():
    random.shuffle(randArmas)
    random.shuffle(randPersonajes)
    random.shuffle(randLocaciones)
    
    homicida = randPersonajes[randint(0, len(randPersonajes)-1)]
    fallecido = randPersonajes[randint(0, len(randPersonajes)-1)]

    while fallecido == homicida:
        fallecido = randPersonajes[randint(0, len(randPersonajes)-1)]
    
    armaUtilizada = randArmas[randint(0, len(randArmas)-1)]
    lugarMuerte = randLocaciones[randint(0, len(randLocaciones)-1)]
    
    randPersonajes.pop(randPersonajes.index(fallecido))
    randPersonajes.pop(randPersonajes.index(homicida))
    randLocaciones.pop(randLocaciones.index(lugarMuerte))
    randArmas.pop(randArmas.index(armaUtilizada))
    
    return homicida, fallecido, armaUtilizada, lugarMuerte, randPersonajes, randLocaciones, randArmas

def Historia1(homicida, fallecido, armaUtilizada, lugarMuerte) :

    resultado = (   f"El homicida fue {homicida}. \n "
                    f"El fallecido fue {fallecido}. \n "
                    f"El lugar del homicidio fue {lugarMuerte}. \n "
                    f"El arma homicida fue {armaUtilizada}. \n \n"
                    )

    h = ( f" {randPersonajes[0]} fue visto por última vez en la sala de estar platicando con {randPersonajes[1]}.  \n"
                  f" Mientras {randPersonajes[2]} fue al baño, {fallecido} y {randPersonajes[3]} estuvieron fumando un cigarro en el balcón. \n \n"
                  f" Después de un tiempo de no ver a {fallecido}, {randPersonajes[2]} se encuentra con su cadáver en {randLocaciones[randint(0, len(randLocaciones)-1)]}.\n"
                  f" También se encontró con el presunto arma homicida siendo {randArmas[randint(0, len(randArmas)-1)]}\n"
                  f" la causa de su muerte. Ya que {randPersonajes[2]} fue quien encontró el cadáver, es \n"
                  f" el principal sospechoso, y a su vez crece la sospecha por {homicida} a quien no se le ha visto. \n \n"
                  f" {randPersonajes[2]} trata de defenderse diciendo que solamente estuvo en el baño y que {randPersonajes[3]} fue \n"
                  f" el último que vio a {fallecido}. En la cocina falta {armaUtilizada} que no se encuentra en \n"
                  f" su lugar. Ya que {randPersonajes[0]} es quien vive ahí fue quien notó su ausencia. \n"
                  )
    
    pista1 = (f" {randPersonajes[2]} vio a alguien entrar justo después de que él salió de {lugarMuerte}.\n"
               f" Lo único que cree recordar es haber visto que entrara con lo que parecía\n"
               f" {armaUtilizada} y, al no tenía idea de qué sucedía, prefirió irse del\n"
               f" lugar. Comparando historias con {homicida}, se dio cuenta que pudo haber visto\n"
               f" {randArmas[randint(0, len(randArmas)-1)]} en lugar de {armaUtilizada}.\n"       
               )
    
    pista2 = (f" Después de tratar de investigar entre {randPersonajes[1]} y {randPersonajes[0]}\n"
               f" y confrontar sus versiones de la historia, pudieron descartar a {randPersonajes[2]}\n"
               f" por su forma de reaccionar y se dieron cuenta que {randPersonajes[3]} y {homicida}\n"
               f" ocultan algo. A {homicida} se le vio por última vez en {lugarMuerte} y a {randPersonajes[3]} \n"
               f" en {randLocaciones[randint(0, len(randLocaciones)-1)]}.\n"
               )

    return resultado, h, pista1, pista2
             
           # f" \n"
           # f" \n"
           # f" \n"
           # f" \n"
           # f" \n"
           # f" \n"
           # f" \n"        

def Historia2(homicida, fallecido, armaUtilizada, lugarMuerte):
    h = (f"Los cinco amigos y la invitada pasaron una velada maravillosa, después de \n"
         f"muchos temas de conversación, muchas copas y juegos de cartas. Cada uno se \n"
         f"fue a su habitación para ir a dormir. A la mañana siguiente encontraron a {fallecido} \n"
         f"en {lugarMuerte}, con una aparente sobredosis, ya que encontraron pastillas a su alrededor. \n"
         f"Se dividió la “unión” que existía entre las personas ya que cada uno comenzó a \n"
         f"especular sobre qué fue lo que pasó. La primera impresión fue un suicidio, pero la \n" 
         f"escena del crimen era demasiado perfecta para eso. {randPersonajes[0]} y {randPersonajes[1]} \n" 
         f"comenzaron el rumor de que pudo haber sido {randPersonajes[2]}, aunque nadie estaba seguro.\n"
         )
    
    resultado = (   f"El homicida fue {homicida}. \n "
                    f"El fallecido fue {fallecido}. \n "
                    f"El lugar del homicidio fue {lugarMuerte}. \n "
                    f"El arma homicida fue {armaUtilizada}. \n \n"
                    )
    
    pista1 = ( "Pista 1:  \n"
               f"{randPersonajes[2]} busca la forma de recuperar la confianza de {randPersonajes[0]} y {randPersonajes[1]}, \n"
               f"aunque por lo visto tratan de boicotearlo a él junto con {randPersonajes[3]} y {homicida}. \n"
               f"{homicida} sembró la luda por {randPersonajes[2]} cuando dijo que escuchó que salió de \n"
               f"su habitación durante la noche cuando {homicida} fue inexplicablemente a {lugarMuerte}. \n"
               )
    
    pista2 = ( "Pista 2: \n"
              f"A pesar de que los principales sospechosos son {homicida} y {randPersonajes[2]}, la última \n"
              f"palabra la tienen los demás ya que no saben si {randPersonajes[2]} quiso sembrar la \n"
              f"duda sobre {homicida}, o si verdaderamente fue {randPersonajes[2]}. Lo cierto es que \n"
              f"encontraron rastros de {armaUtilizada} o {randArmas[1]}. \n"
              )
               
    return resultado, h, pista1, pista2


def Historia3(homicida, fallecido, armaUtilizada, lugarMuerte):
    h = ( f" Era bien sabido que existía tensión entre {fallecido} y {randPersonajes[1]}, y que \n"
          f"{randPersonajes[2]} era el tercero en discordia. Por lo que comenzó cierto descontento \n" 
          f"con los demás integrantes del grupo y fue algo que {homicida} no toleraba \n" 
          f"porque quería que el grupo siguiera conviviendo como siempre. \n"
          f"A la mañana siguiente de la reunión {randPersonajes[0]} encontró el cuerpo sin vida \n"
          f"de {fallecido} sin muchas respuestas y un mundo de preguntas. Lo que sabe es que\n"
          f"su cuerpo tiene rastros de haber sido asesinado por lo que pudo haber sido {randArmas[1]},\n"
          f"sin embargo, no está seguro. \n"
          f"De lo que todos pueden llegar a estar seguros es que, a pesar de que encontraron \n"
          f"a {fallecido} en {lugarMuerte}, {randPersonajes[3]} dice que sí vio que fue a dormir a su habitación. \n"
          )
    
    resultado = (   f"El homicida fue {homicida}. \n "
                    f"El fallecido fue {fallecido}. \n "
                    f"El lugar del homicidio fue {lugarMuerte}. \n "
                    f"El arma homicida fue {armaUtilizada}. \n \n"
                    )
    
    pista1 = ( "Pista 1: \n"
              f"Durante la noche {homicida} vio que {fallecido} salió de su habitación para ir con \n"
              f"{randPersonajes[2]} y pasó eso por alto, ya que sabía que {randPersonajes[1]} tenía sentimientos \n"
              f"de por medio. Lo que sí no pasó por alto fue la presencia de lo que, en vez de \n"
              f"{randArmas[1]} podía ser {armaUtilizada} con lo que parecían rastros de la prenda de \n"
              f"{fallecido}, lo que hacía más probable su fallecimiento por esa causa.\n"
              )
    
    pista2 = ( "Pista 2:\n"
              f"Otro detalle para considerar fue que en su tristeza {randPersonajes[1]} se puso a indagar \n"
              f"y encontró que {homicida} tampoco estaba en su habitación durante la noche, \n"
              f"aunque presuntamente fue a {randLocaciones[3]}, y las historias difícilmente encajan. Lo que \n"
              f"se sabe con certeza es que ni  {homicida}  ni {randPersonajes[3]} estaban en sus habitaciones.\n"
              )
               
    return resultado, h, pista1, pista2


def Historia4(homicida, fallecido, armaUtilizada, lugarMuerte):
    h = ( f"{homicida} fue la última en llegar a la reunión de esa noche en la que se celebrara \n"
          f"el gran logro de {fallecido}. Al entrar, encuentra en la sala a {randPersonajes[0]}, {randPersonajes[1]},\n"
          f"{randPersonajes[2]} y {randPersonajes[3]}, quiénes están platicando sobre las nuevas noticias. \n"
          f"{randPersonajes[1]} menciona que {fallecido} fue por bebidas pero no ha vuelto, va a buscarla y encuentra su \n"
          f"cadáver en{randLocaciones[2]} y a un costado {armaUtilizada}. Asustado corre y avisa a los demás, pero al volver \n"
          f"a la sala sólo están {randPersonajes[3]} y {randPersonajes[0]}. Nadie sabe a dónde fue {randPersonajes[3]}.\n" 
          f"{randPersonajes[3]} y {randPersonajes[0]} argumentan que han estado platicando juntos todo el tiempo, y {randPersonajes[1]} se \n"
          f"defiende diciendo que él fue quien notó la ausencia.\n"
          )
    
    resultado = (   f"El homicida fue {homicida}. \n "
                    f"El fallecido fue {fallecido}. \n "
                    f"El lugar del homicidio fue {lugarMuerte}. \n "
                    f"El arma homicida fue {armaUtilizada}. \n \n"
                    )
    
    pista1 = ( "Pista 1: \n"
              f"{randPersonajes[1]} vuelve del baño, diciendo que ella no sabe nada acerca de lo sucedido y platica que vio una \n"
              f"huella de sangre de zapato en el camino de vuelta. Y no recuerda si pudiera pertenecer al zapato de \n"  
              f"{homicida} o {randPersonajes[0]}. "
              )
    
    pista2 = ( "Pista 2: \n"
              f"{homicida} actúa extraño y se defiende diciendo que ella llegó después de todos. {randPersonajes[0]} no sabe qué \n"
              f"decir y se acusa a {homicida}, diciendo que llegó justo antes de que se enteraran lo que había pasado\n"
              f"lo que le hace pensar que antes de llegar, cometió el asesinato. "
              )
               
    return resultado, h, pista1, pista2

def Historia5(homicida, fallecido, armaUtilizada, lugarMuerte):
    h = ( f"{fallecido} aparece muerto en el {lugarMuerte},  mientras todos disfrutan de la fiesta. \n" 
          f"{homicida} y {randPersonajes[0]} se encuentran platicando en {randLocaciones[2]} cuando {randPersonajes[1]}\n"
          f"entra gritando lo que acaba de suceder. {randPersonajes[3]} y {randPersonajes[2]} se miran fijamente \n"
          f"sorprendidos y sonríen. {homicida} comenta que vio entrar a {randPersonajes[3]} con lo que parecía ser\n" 
          f"{randArmas[1]} en el arreglo de vinos que trajo. {randPersonajes[3]} comenta que \n"
          f"{randArmas[1]} está intacta en la cocina. \n"
          f"{randPersonajes[1]} comenta que {fallecido} estaba tirado con {armaUtilizada} y que había un reloj tirado \n"
          f"en el camino. {randPersonajes[2]} comenta de inmediato que ni el ni {randPersonajes[3]} traían reloj. \n"
          )
    
    resultado = (   f"El homicida fue {homicida}. \n "
                    f"El fallecido fue {fallecido}. \n "
                    f"El lugar del homicidio fue {lugarMuerte}. \n "
                    f"El arma homicida fue {armaUtilizada}. \n \n"
                    )
    
    pista1 = ( "Pista 1: \n"
              f"{randPersonajes[2]} comenta que {randPersonajes[1]} fue quien encontró y anunció lo cometido y \n"
              f"por tanto es el principal sospechoso de lo ocurrido; éste se defiende diciendo que antes de lo ocurrido \n"
              "estuvo todo el tiempo con {randPersonajes[0]}."
              )
    
    pista2 = ( "Pista 2: \n"
              f"{randPersonajes[3]} afirma que {homicida} y {fallecido} estaban molestos antes de la reunión \n"
              f"de ese día y que el reloj era justo de la medida y estilo de {homicida}.\n" 
              )
               
    return resultado, h, pista1, pista2

historias = [Historia1, Historia2, Historia3, Historia4, Historia5]

def Pulsa():
    print( " Pulsa la tecla con la que deseas continuar ")
    input()
    system("cls")

def Pista(pista, resultado):
    print("¿Deseas leer la siguiente pista? O prefieres señalar al culpable")
    print(" a) Pista \n b) Señalar al culpable \n \n")
    s = input()
    
    if s == "a":
        print (pista)
        return s
    
    elif s == "b":
        print("¿Quién es el culpable? ¿Cuál es el arma homicida? ¿Dónde murió?")
        return s
    
    else: 
        print(resultado)
        sys.exit()
        
def Comparacion(armas, arma, asesino, sospechosos, lugares, lugar):
    sospechosos.append(asesino)
    lugares.append(lugar)
    armas.append(arma)
    random.shuffle(sospechosos)
    random.shuffle(lugares)
    random.shuffle(armas)
    
    indice = ['a', 'b', 'c', 'd', 'e']
    contador = 0
    
    print("El asesino fue: \n")
    print(f" a) {sospechosos[0]} \n b) {sospechosos[1]} \n c) {sospechosos[2]} \n d) {sospechosos[3]} \n e) {sospechosos[4]}\n \n")
    
    x = input()
    
    if sospechosos[indice.index(x)] == asesino:
        contador += 1
    
    print("El lugar fue: \n")
    print(f" a) {lugares[0]} \n b) {lugares[1]} \n c) {lugares[2]} \n d) {lugares[3]} \n e) {lugares[4]}\n \n")
    
    y = input()
    
    if lugares[indice.index(y)] == lugar:
        contador += 1
    
    
    print("El arma fue: \n")
    print(f" a) {armas[0]} \n b) {armas[1]} \n c) {armas[2]} \n d) {armas[3]} \n e) {armas[4]}\n \n")
    
    z = input()
    
    if armas[indice.index(z)] == arma:
        contador += 1
        
    return contador
    

def Juego():
    sel = randint(0, len(historias)-1)
    
    asesino, muerto, arma, lugar, sospechosos, lugares, armas = Aleatorio()
    
    resultado, h, pista1, pista2 = historias[sel](asesino, muerto, arma, lugar)
    
    print(reglas)
    Pulsa()
    print(background)
    Pulsa()
    print(h)
    
    x = Pista(pista1, resultado)
    
    if x == 'a':
        y = Pista(pista2, resultado)
        
        if y == 'a':
            res = Comparacion(armas, arma, asesino, sospechosos, lugares, lugar)
            print(resultado)
        
        elif y == 'b':
            res = Comparacion(armas, arma, asesino, sospechosos, lugares, lugar)
            print(resultado)
        
    elif x == 'b':
        res = Comparacion(armas, arma, asesino, sospechosos, lugares, lugar)
        print(resultado)
        
    else :
        print(resultado)
        sys.exit()
    
    return res

# x = Juego()
print(f"Sacaste {Juego()} de 3 bien")
        
# asesino, muerto, arma, lugar, sospechosos, lugares, armas = Aleatorio()    

# res = Comparacion(armas, arma, asesino, sospechosos, lugares, lugar)

# print(res)

# print(resultado)

# print(background)



# print(historia1)

# while vidas != 0:
#     if sel == 1:
#         vidas -= 1


