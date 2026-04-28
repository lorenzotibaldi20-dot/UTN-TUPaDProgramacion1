#Actividad 1
nombre = input("Porfavor ingresa tu nombre: ")
while not nombre.isalpha():
    nombre = input("Ingresa solo tu nombre y sin espacios: ")
print("Nombre valido")

# Pedir cantidad de productos
cantidad = input("Ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Error. Ingrese un número entero positivo: ")

cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

# Recorrer cada producto
for i in range(cantidad):
    print(f"\nProducto {i+1}")
    
    # Pedir precio
    precio = input("Ingrese el precio: ")
    
    while not precio.isdigit():
        precio = input("Error. Ingrese un precio válido (solo números): ")
    
    precio = int(precio)
    
    total_sin_descuento += precio
    
    # Preguntar descuento
    descuento = input("¿Tiene descuento? (S/N): ").lower()
    
    while descuento != "s" and descuento != "n":
        descuento = input("Error. Ingrese S o N: ").lower()
    
    # Aplicar descuento
    if descuento == "s":
        precio_con_descuento = precio * 0.9
    else:
        precio_con_descuento = precio
    
    total_con_descuento += precio_con_descuento

# Cálculos finales
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Total sin descuentos: {total_sin_descuento}")
print(f"Total con descuentos: {total_con_descuento:.2f}")
print(f"Ahorro total: {ahorro:.2f}")
print(f"Promedio por producto: {promedio:.2f}")

#Actividad 2}
# Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

# Login (máx 3 intentos)
while intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        break
    else:
        intentos += 1
        print(f"Datos incorrectos. Intentos restantes: {3 - intentos}")

# Si falla 3 veces
if not acceso:
    print("Cuenta bloqueada")

else:
    # Menú repetitivo
    opcion = ""

    while opcion != "4":
        print("\n--- MENÚ ---")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mensaje motivacional")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        # Validar que sea número
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            opcion = input("Error. Ingrese un número entre 1 y 4: ")

        # Opciones
        if opcion == "1":
            print("Estado: Inscripto")

        elif opcion == "2":
            nueva_clave = input("Ingrese nueva clave: ")
            
            # Validar longitud
            while len(nueva_clave) < 6:
                nueva_clave = input("Error. Mínimo 6 caracteres. Intente de nuevo: ")
            
            confirmar = input("Confirme la nueva clave: ")

            # Validar que coincidan
            while confirmar != nueva_clave:
                print("Las claves no coinciden.")
                confirmar = input("Confirme la nueva clave: ")

            clave_correcta = nueva_clave
            print("Clave cambiada correctamente.")

        elif opcion == "3":
            print("Seguí esforzándote, vas por buen camino.")

        elif opcion == "4":
            print("Saliendo del sistema...")
#Actividad 3
# Operador
operador = input("Ingrese su nombre: ")

while not operador.isalpha():
    operador = input("Error. Solo letras: ")

# Turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != "5":
    print("\n--- MENU ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Salir")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion = input("Error. Ingrese opción válida: ")

    # RESERVAR
    if opcion == "1":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Error. Ingrese 1 o 2: ")

        nombre = input("Nombre del paciente: ")

        while not nombre.isalpha():
            nombre = input("Error. Solo letras: ")

        if dia == "1":
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Paciente ya registrado.")
            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay cupos.")

        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Paciente ya registrado.")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay cupos.")

    # CANCELAR
    elif opcion == "2":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Error. Ingrese 1 o 2: ")

        nombre = input("Nombre del paciente: ")

        while not nombre.isalpha():
            nombre = input("Error. Solo letras: ")

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No encontrado.")

        else:
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No encontrado.")

    # VER AGENDA
    elif opcion == "3":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Error. Ingrese 1 o 2: ")

        if dia == "1":
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    # RESUMEN
    elif opcion == "4":
        ocupados_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        ocupados_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")

        print("Lunes:", ocupados_lunes, "ocupados,", 4 - ocupados_lunes, "libres")
        print("Martes:", ocupados_martes, "ocupados,", 3 - ocupados_martes, "libres")

        if ocupados_lunes > ocupados_martes:
            print("Más ocupado: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Más ocupado: Martes")
        else:
            print("Empate")
#actividad 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

agente = input("Nombre del agente: ")

while not agente.isalpha():
    agente = input("Error. Solo letras: ")

racha_forzar = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("\nEnergía:", energia, "Tiempo:", tiempo, "Cerraduras:", cerraduras_abiertas, "Alarma:", alarma)

    opcion = input("1.Forzar 2.Hackear 3.Descansar: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Error: ")

    # FORZAR
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            alarma = True
            print("Se trabó la cerradura.")
        else:
            if energia < 40:
                riesgo = input("Número 1-3: ")

                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    riesgo = input("Error: ")

                if riesgo == "3":
                    alarma = True

            if not alarma:
                cerraduras_abiertas += 1

    # HACKEAR
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        for i in range(4):
            print("Hackeando...")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1

    # DESCANSAR
    elif opcion == "3":
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado.")
        break

if cerraduras_abiertas == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
#actividad 5
print("=== ARENA DE COMBATE ===")

nombre = input("Ingrese nombre del gladiador: ")

while not nombre.isalpha():
    print("Error: el nombre debe tener solo letras.")
    nombre = input("Ingrese nombre del gladiador: ")

# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
juego_activo = True

print("\nComienza la batalla...\n")

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"{nombre} HP:{vida_jugador} | Enemigo HP:{vida_enemigo} | Pociones:{pociones}")
    print("1) Ataque Pesado")
    print("2) Ráfaga Veloz")
    print("3) Curar")

    opcion = input("Elegí una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Opción inválida.")
        opcion = input("Elegí una opción: ")

    # ATAQUE PESADO
    if opcion == "1":
        danio = danio_base

        if vida_enemigo < 20:
            danio = danio_base * 1.5
            print("¡Golpe crítico!")

        vida_enemigo -= danio
        print(f"Golpeaste al enemigo y causaste {danio} de daño.")

    # RAFAGA
    elif opcion == "2":
        print("Realizás una ráfaga de ataques:")
        for i in range(3):
            vida_enemigo -= 5
            print("- Impacto de 5 de daño")

    # CURAR
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Recuperaste 30 de vida.")
        else:
            print("No te quedan pociones.")

    # TURNO ENEMIGO
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"El enemigo te golpea y te quita {danio_enemigo} de vida.")

    print("-------------------------")

# RESULTADO FINAL
if vida_jugador > 0:
    print(f"{nombre} ganó el combate.")
else:
    print("Fuiste derrotado.")