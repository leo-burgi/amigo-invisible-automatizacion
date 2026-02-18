# 🎄 Amigo Invisible Automation

Proyecto de automatización desarrollado en **Python** para realizar el sorteo de *Amigo Invisible* y **notificar automáticamente a cada participante**, sin intervención manual.

El sistema fue utilizado en un entorno **real y familiar**, resolviendo un problema concreto: evitar errores humanos, filtraciones y desorden al momento del sorteo.

---

## 🎯 Qué hace este proyecto

- Realiza un **sorteo aleatorio válido** de Amigo Invisible
- Aplica **reglas de negocio**:
  - Nadie se regala a sí mismo
  - Las parejas no pueden regalarse entre sí
- Notifica automáticamente a cada participante mediante:
  - 📲 **WhatsApp Web** (usando un número activo en desuso)
  - 📧 **Email** (usando una cuenta Gmail exclusiva)

---

## 🧩 Versiones incluidas

### WhatsApp
- Envío automático de mensajes individuales
- Uso de WhatsApp Web
- Control de tiempos para evitar bloqueos
- Mensajes personalizados y formateados

### Email
- Envío automático vía SMTP
- Cuenta dedicada para el evento
- Mensajes individuales y privados

---

## 🛠️ Tecnologías utilizadas

- Python 3
- `random` (lógica del sorteo)
- `pywhatkit` (automatización WhatsApp Web)
- `keyboard` (cierre automático de pestañas)
- SMTP (versión email)

---

## 🧠 Lógica del sorteo

El algoritmo:
1. Mezcla aleatoriamente los participantes
2. Valida reglas:
   - No auto-asignación
   - No asignación a la pareja
3. Reintenta hasta obtener una combinación válida
4. Genera mensajes personalizados
5. Ejecuta el envío automático

Incluye control de errores y límite de intentos.

---

## ⚠️ Consideraciones importantes

- El envío por WhatsApp depende de:
  - WhatsApp Web abierto
  - Navegador activo
- Se agregan pausas deliberadas para:
  - Evitar bloqueos
  - Simular comportamiento humano
- Proyecto pensado para **eventos pequeños** (familia, grupos cerrados)

---

## 🚀 Ejecución

```bash
pip install -r requirements.txt
python whatsapp/sorteo_whatsapp.py
