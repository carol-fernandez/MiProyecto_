#inicio
define p = Character("Protagonista", color="#8c1239")

label start:
    "esta empezando a dejar de llover"
    "estoy sentada, buscando de manera de forma un poco desesperada trabajo. "  
    "termine encontrando un anuncio muy reciente de trabajo en un bar claro la idea es mala: borrrachos, alcohol y ese tipo de hambientes no se si son para mi"
    "¡pero es el sueldo cubre las facturas atrasadas! Odio tener pagos atrasados"
    "¡¡¡y no necesito experiencia!!!" 
    "¡espero que no sea muy bueno como para ser cierto. ojala que no sea una estafa para quitarme los organos!" 
    p "Hola, esto es un ejemplo de {b}negrita{/b}, {i}cursiva{/i} y {u}subrayado{/u}."
    "También puedo poner palabras en {color=#FF6347}rojo{/color}."
    ##ejemplo de como cambiar la fuente de alcunas palabras!!

    menu:
        "mandar mi CV":
            jump CV

        "NO HACER NADA":
            jump nada

label CV:
    "casi al instante despues de manda mi CV me llego a mi correo electronico un mensaje de aceptacion de solicitud de empleo."
    
    menu:
        "te parece que elegiste bien??":
            jump dudar

        "quieres regresar??":
            jump regresar1

label dudar:
    "si estoy seguro"
    "bien es el fin"
    jump marry

label regresar1:
    "si! quiero regresar!"
    jump marry


label nada:
    "te ahogaste en deudas y te moriste de hambre"
    "fin"
    jump marry

return

#actualizar 
#control + s para actualizar el codigo!!!!