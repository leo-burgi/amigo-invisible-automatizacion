import random
import pywhatkit
import time
import keyboard

# ================= CONFIGURACIÓN DE DATOS =================
# CORRECCIÓN: Se agregó la coma faltante y se revisó la estructura.

participantes = [
    # --- PAREJAS (Indices 0-11) ---
    ["Leonel", "+5493492528528"],
    ["Luisina", "+5493492315618"], 
    
    ["Andrea", "+5493492325406"], 
    ["Andrés", "+5493492648771"],          
    
    ["Patricia", "+5493492617264"], 
    ["Don Diego", "+5493492665697"], 
    
    ["Abuela Norma", "+5493492623528"], 
    ["Dante", "+5493496498312"], 
    
    ["Elena", "+5493492315597"], 
    ["Matias", "+5493492618792"], 
    
    ["Noelia", "+5493492671982"], 
    ["Paloma", "+5493492656792"], 
    
    # --- SOLTEROS / LIBRES (Indices 12-15) ---
    ["Agustín", "+5493492637461"],
    ["Bruno", "+5493492599796"],
    ["Dieguito", "+5493492418639"], # <--- COMA AGREGADA AQUÍ
    ["Rafael", "+5493492619823"] 
]

# ================= LÓGICA DEL SORTEO =================

def realizar_sorteo():
    nombres = [p[0] for p in participantes]
    indices = list(range(len(participantes)))
    
    asignaciones_indices = []
    valido = False
    intentos = 0
    
    print("🔄 Mezclando papeles...")

    while not valido and intentos < 10000:
        random.shuffle(indices)
        valido = True
        asignaciones_indices = indices[:]
        
        for i_giver, i_receiver in enumerate(asignaciones_indices):
            # 1. No regalarse a sí mismo
            if i_giver == i_receiver:
                valido = False
                break
            
            # 2. Regla de Parejas (Indices 0-11)
            if i_giver < 12:
                pareja_index = i_giver + 1 if i_giver % 2 == 0 else i_giver - 1
                if i_receiver == pareja_index:
                    valido = False
                    break
        intentos += 1

    if not valido:
        raise Exception("❌ No se encontró combinación válida.")
        
    print(f"✅ Sorteo exitoso tras {intentos} intentos.")
    
    resultados = []
    for i, p in enumerate(participantes):
        giver_name = p[0]
        giver_phone = p[1]
        receiver_name = nombres[asignaciones_indices[i]]
        resultados.append({
            "telefono": giver_phone,
            "mensaje": construir_mensaje(giver_name, receiver_name)
        })
    
    return resultados

# ================= DISEÑO DEL MENSAJE =================

def construir_mensaje(giver, receiver):
    return f"""*Hola {giver}!* 🎄

Tu amigo invisible asignado es:

🎁 👉 *{receiver}* 👈 🎁

_Recordá que es secreto._
_No des indicios en el grupo familiar ni en el asado del finde._

--------------------------------
*Recordatorios:*
• Dejar alguna pista en el paquete o tarjeta 🏷️
• Monto sugerido: *$20.000* 💰
--------------------------------

_(Este es un mensaje automático, no respondas)_"""

# ================= EJECUCIÓN DE ENVÍO =================

def enviar_mensajes(lista_envios):
    print(f"⚠️ SE ENVIARÁN {len(lista_envios)} MENSAJES.")
    # MEJORA: Input de seguridad
    input("👉 Presiona ENTER para comenzar el envío masivo (Asegúrate de tener WA Web abierto)...")
    
    print("⏳ Tienes 5 segundos para soltar el mouse...")
    time.sleep(5)
    
    for i, envio in enumerate(lista_envios):
        phone = envio["telefono"]
        msg = envio["mensaje"]
        
        print(f"[{i+1}/{len(lista_envios)}] Enviando a {phone}...")
        
        try:
            # MEJORA: Aumentado wait_time a 20s por seguridad
            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone, 
                message=msg, 
                wait_time=20, 
                tab_close=True,
                close_time=4
            )
            
            # MEJORA: Refuerzo de cierre de pestaña
            time.sleep(2) 
            keyboard.press_and_release('ctrl+w') 
            
        except Exception as e:
            print(f"❌ Error enviando a {phone}: {e}")
        
        print("⏳ Esperando 10 segundos para el siguiente...")
        time.sleep(10)

    print("🏁 ¡Proceso terminado!")

if __name__ == "__main__":
    try:
        envios = realizar_sorteo()
        enviar_mensajes(envios)
    except Exception as e:
        print(e)