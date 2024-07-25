# Laboratorio 1 Filling any Polygon

Este proyecto dibuja y rellena múltiples polígonos en una ventana utilizando la biblioteca Pygame en Python. Los polígonos se renderizan con diferentes colores y uno de ellos crea un espacio en blanco dentro de otro polígono.

## Requisitos Previos

Necesitarás tener Python y Pygame instalados en tu sistema para ejecutar este proyecto.

## Instalación

Clona este repositorio y navega al directorio del proyecto:

```sh
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO>
```

### Instalar Pygame

Instala Pygame si no lo tienes instalado:

```sh
pip install pygame
```

## Uso

Para ejecutar el script y ver los polígonos en la ventana de Pygame:

```sh
python poligonos.py
```

## Detalles del Código

1. **Inicialización de Pygame:** Se inicializa la biblioteca Pygame y se configura la pantalla.
2. **Definición de Polígonos:** Se definen las coordenadas de los vértices para cada uno de los cinco polígonos.
3. **Inversión de Coordenadas Y:** Se ajustan las coordenadas Y de los puntos para que los polígonos se dibujen correctamente en Pygame.
4. **Dibujo y Relleno de Polígonos:** Se utilizan funciones de Pygame para dibujar y rellenar los polígonos en la pantalla.
5. **Bucle Principal:** Un bucle que mantiene la ventana abierta y maneja los eventos de Pygame.

## Documentación

El script principal (`poligonos.py`) contiene el código necesario para inicializar Pygame, definir los polígonos y manejarlos adecuadamente para su visualización.

## Estructura del Proyecto

- `poligonos.py`: Contiene el código fuente principal para dibujar y rellenar los polígonos.
- `README.md`: Este archivo, que proporciona información sobre el proyecto.

## Licencia

Este proyecto está bajo la licencia de MIT.
```
