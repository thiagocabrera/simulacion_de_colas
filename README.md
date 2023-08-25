
![Logo](https://www.frba.utn.edu.ar/wp-content/uploads/2017/10/Logos-UTN.BA-cs6-fondo-blanco.png)


# Simulación: Modelos de colas

Este repositorio contiene modelos de colas para realizar simulaciones de avance del tiempo. A medida que vaya viendo más modelos en la cursada los voy a ir subiendo por acá.

## Como correr

El código no requiere la instalación de ningún paquete extra. Para correr simulaciones sobre los diferentes modelos, simplemente debemos utilizar las diferentes clases que tenemos disponibles.
## Documentación

**¿Cómo obtenemos los resultados de las simulaciones?**

Para obtener los resultados, primero debemos instanciar el modelo y correrlo de la siguiente manera:
``` python
s = Simulador(tf)
s.simular()
print(s.pps, s.pto)
```

**¿Cómo cambiamos las fdp de los datos?**

Estas funciones de probabilidad están guardadas en variables, por lo que para definirlas basta con establecer dicha fdp como valor al dato que se quiere cambiar:
``` python
s = Simulador(tf)
s.ta = fdp1
s.ia = fdp2
```

A continuación dejamos la clase correspondiente a cada modelo presente en los ejercicios de la guía de la materia Simulación de la UTN FRBA:
* **Prueba de escritorio**: Sistema de una cola con vaciamiento y sin arrepentimiento:
``` python
s = SimuladorPruebaDeEscritorio(tf)
```
tf es un valor numérico.
Resultados:
``` python
s.pps # Promedio de permanencia en el sistema
s.pto # Porcentaje de tiempo ocioso
```
Datos:
``` python
s.ta # tiempo de atención
s.ia # intervalo entre arrivos
```
* **Ejercicio 1**: Sistema de una cola con vaciamiento y arrepentimiento:
``` python
Próximamente
```
## Créditos

Todo crédito va para panfleto, el rey sin corona del Kahoot.

![Logo](https://i.ytimg.com/vi/PLtNuyH_uxI/maxresdefault.jpg)