<p align="center">
  <a href="https://github.com/Helminth117">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Helminth117/Helminth117/main/assets/icono-blanco-transparente.png">
      <img src="https://raw.githubusercontent.com/Helminth117/Helminth117/main/assets/icono-negro-transparente.png" alt="helminth117" width="64">
    </picture>
  </a>
</p>

<h1 align="center">Hyprland Minecraft Tools</h1>

<p align="center">Herramienta AFK para Minecraft en Wayland, con las utilidades nativas de Hyprland.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3-2B2B2B?style=flat-square&labelColor=0D0D0D&logoColor=F5F5F5&logo=python" alt="Python 3">
  <img src="https://img.shields.io/badge/Hyprland-0D0D0D?style=flat-square&labelColor=0D0D0D&logoColor=F5F5F5&logo=hyprland" alt="Hyprland">
  <img src="https://img.shields.io/badge/Wayland-0D0D0D?style=flat-square&labelColor=0D0D0D&logoColor=F5F5F5&logo=wayland" alt="Wayland">
</p>

`afk_tool.py` ataca con el ritmo de recarga del combate moderno y come cada cierto tiempo, y se
pausa solo cuando Minecraft no es la ventana activa.

- **Detección de foco** con `hyprctl`: si cambias de ventana, deja de hacer clic.
- **Ataque** con un intervalo ajustable (`COOLDOWN`, 0,65 s por defecto).
- **Comer** cada `EAT_INTERVAL` segundos: mira al cielo, come y vuelve a la posición original.
- **Entrada nativa de Wayland** con `ydotool`.

## Requisitos

- Hyprland
- `ydotool` con el demonio `ydotoold` en marcha
- Python 3

```bash
ydotoold --socket-path=$HOME/.ydotool_socket --socket-own=$(id -u):$(id -g) &
python afk_tool.py
```

---

<p align="center">
  <a href="https://github.com/Helminth117">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Helminth117/Helminth117/main/assets/logotipo-blanco-transparente.png">
      <img src="https://raw.githubusercontent.com/Helminth117/Helminth117/main/assets/logotipo-negro-transparente.png" alt="helminth117" width="180">
    </picture>
  </a>
</p>
