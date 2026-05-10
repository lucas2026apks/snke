[app]

# (sección 1) Información básica
title = Viborita Lucas
package.name = viborita_game
package.domain = org.lucas
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1

# (sección 2) Requerimientos - Solo lo necesario
# Quitamos pyjinius para que sea más rápido
requirements = python3,kivy

# (sección 3) Configuración de pantalla
orientation = landscape
fullscreen = 1

# (sección 4) Android específico
# Estas versiones son las más estables para evitar que se trabe
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a

# No necesitamos permisos de Bluetooth para un juego offline
# Esto evita errores de licencias
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
