# Hyprland Minecraft Tools ⛏️

Script de automatización en Python diseñado para optimizar sesiones AFK en Minecraft dentro de entornos **Wayland**, utilizando las herramientas nativas de **Hyprland**.

## 🚀 Características
- **Detección de Foco:** Utiliza `hyprctl` para pausar el script automáticamente si Minecraft no es la ventana activa.
- **Auto-Clicker:** Optimizado con tiempos de espera (cooldown) para mecánicas de combate modernas.
- **Auto-Eat:** Mecánica inteligente que mira al cielo para alimentarse y regresa a la posición original.
- **Wayland Native:** Emulación de periféricos mediante `ydotool`.

## 🛠️ Requisitos
- **Hyprland** (Compositor)
- **ydotool** (Debe estar corriendo el demonio `ydotoold`)
- **Python 3.x**

## 📋 Configuración de ydotool
Para que el script tenga permisos de ejecución sobre los dispositivos de entrada, asegúrate de iniciar el demonio:
```bash
ydotoold --socket-path=$HOME/.ydotool_socket --socket-own=$(id -u):$(id -g) &
