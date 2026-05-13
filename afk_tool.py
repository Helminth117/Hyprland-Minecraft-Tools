import subprocess
import time
import json

# ⚙️ CONFIGURACIÓN
COOLDOWN = 0.65
EAT_INTERVAL = 30

def run(cmd):
    subprocess.run(cmd, shell=True)

def click_left():
    run("ydotool click 0xC0")

def eat():
    print(f"[{time.strftime('%H:%M:%S')}] Comiendo...")
    run("ydotool key 3:1 3:0")
    time.sleep(0.5)
    run("ydotool mousemove -- 0 -2000")   # mira al cielo
    time.sleep(0.2)
    run("ydotool click 0x41")
    time.sleep(2.1)
    run("ydotool click 0x81")
    time.sleep(0.3)
    run("ydotool mousemove -- 0 2000")    # regresa a mirar al mob
    time.sleep(0.2)
    run("ydotool key 2:1 2:0")

def is_minecraft_focused():
    try:
        result = subprocess.run(
            ["hyprctl", "activewindow", "-j"],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        title = data.get("title", "") + data.get("class", "")
        return "minecraft" in title.lower()
    except:
        return False

print("Iniciando en 3 segundos, pon foco en Minecraft...")
time.sleep(3)
print("Corriendo. Presiona Ctrl+C para detener.")

last_eat = time.time()

try:
    while True:
        if not is_minecraft_focused():
            print(f"[{time.strftime('%H:%M:%S')}] Minecraft no está en foco, pausado...")
            time.sleep(COOLDOWN)
            continue

        if time.time() - last_eat >= EAT_INTERVAL:
            eat()
            last_eat = time.time()
            continue

        click_left()
        time.sleep(COOLDOWN)

except KeyboardInterrupt:
    print("Detenido.")