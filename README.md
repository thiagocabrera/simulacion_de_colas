
![Logo](https://www.frba.utn.edu.ar/wp-content/uploads/2017/10/Logos-UTN.BA-cs6-fondo-blanco.png)


# Simulación: Modelos de colas

Este repositorio contiene modelos de colas para realizar simulaciones de avance del tiempo. A medida que vaya viendo más modelos en la cursada los voy a ir subiendo por acá.

## Como correr

El código no requiere la instalación de ningún paquete extra. Para correr simulaciones sobre los diferentes modelos, simplemente debemos utilizar las diferentes clases que tenemos disponibles.
## Documentación

A continuación dejamos la clase correspondiente a cada modelo visto en la materia:
* Sistema de una cola con vaciamiento y sin arrepentimiento (TPLL y TPS randoms entre 1 y 120):
``` python
SimuladorDeUnaCola(tf).start()
```
tf es un valor numérico.
* Sistema de una cola con vaciamiento y sin arrepentimiento (TPLL y TPS definidos):
``` python
MockSimuladorDeUnaCola(tplls, tplss, tf).start()
```
tplls y tplss son listas numéricas, tf es un valor numérico.
## Créditos

Todo crédito va para panfleto, el rey sin corona del Kahoot.

![Logo](https://i.ytimg.com/vi/PLtNuyH_uxI/maxresdefault.jpg)