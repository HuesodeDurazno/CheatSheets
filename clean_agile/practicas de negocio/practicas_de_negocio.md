## Planear

descomponer en pequeñas partes , sacar un estimado exacto y preciso , el periodo de tiempo tiene que ser lo mas corto posible.

Usar trivariate analysis , el mejor caso , el caso promedio y el peor caso

Usar historias de usuario y Puntos 

### Estimar historias 

![historias de usuario](../img/historias%20de%20usuario.PNG)

Definir un puntaje ej: 1-6 para definir el esfuerzo en cada tarjeta 

Para estimar tomar una historia de usuario promedio , por ejemplo login 

### Planear iteracion 1

1. Definir una reunion de una vigesima parte de un sprint ej: 2sem -> 1/2 dia

2. Debe de estar todo el equipo

3. los clientes deben de leer previamente las historias de usuario
 
4. asignar que valor tienen esas historias para el negocio

5. elegir las historias que se van a hacer en el primer sprint 

6.determinar cuanto se puede hacer en un sprint , ha esto se llama velocity , empezar con una suposicion 

### retorno de inversion

![retorno de inversion](../img/retorno%20de%20inversion.PNG)

1.colocamos las tarjetas en el diagrama hasta llegar al velocity que supusimos y elegir cuales hacer

### punto medio de revision

a mitad del sprint revisar la cantidad de puntos cumplidos y no llegamos a la meta , ajustamos las historias de usuario a realizar

### yesterday weather 

realizar el siguiente sprint con las nuevas medidas , si a la siguiente iteracion a media semana hay mas o menos de la media de puntos hecha , se vuelve a ajustar

### final del proyecto
cada iteracion se realiza el mismo proceso, las historias nuevas se van agregando y las hechas se van desechando.

El proyecto acaba cuando no hay tarjetas en el mazo

### Historias

#### INVEST

1. I :independientes de otras historias
2. N:negociable.
3. V:valuable: la historia debe de tener valor claro y cuantificable para el negocio
4. E:stimable: debe ser concreta para poder estimarse
5. S:mall: no debe de ser tan larga para que uno o dos desarolladores puedan cumplicarla en max 1 iteracion
6. T:estable: el negocio tiene que ser capas de testearla

#### Estimacion de historias

1. Discucion entre developers , y cliente si es necesario, individualmente asignamos puntajes a las historias , revelamos resultados y si son iguales o no hay variaciones se deja ese puntaje , si no se discute y se vuelve a hacer el proceso
2. Los puntajes pueden ser puntos o tamaños o cartas (revisar libro)

#### Spliting,Mergin and Spiking 

1.Si una historia no es estimable , se junta.
2. Si no puedes estimar una historia , puedes hacer una spyke , es una historia que estima otra historia.

### Gestionar la iteracion

los programadores escojen que historias realizar.

### QA and Acceptance Tests

los test deben de estar escritos antes de la primera mitad de la iteracion, si no estan los programadores deben de dejar de hacer historias y hacer test.

se debe de terminar historias , vale mas 1 al 100% que dos al 50%.

### la demo

se hace una reunion de 1 hr maximo para mostrar test y funcionalidad

### velocity

actualizar grafico de velocity

### rising velocity

si la velocidad aumenta quiere decir que se esta trabajando bajo presion , las estimaciones se haran mal por parte de los programadores si se trabaja bajo presion

### Falling iteration

si la velocidad baja , lo mas probable es que la calidad del codigo no es la adecuada. Tambien causara malas estimaciones

### The golden story

para saber si las estimaciones estan mal puedes compararlas con la historia promedio inicial


## Small releases

Hacer releases lo mas rapido que se pueda, si es posible tener integracion continua.

los releases no son deployds

## Puebas de aceptacion

los requerimientos deben ser espisificados por el negocio

Describir funcionalidad y generar un test automatizado para eso.

### herramienas y metodologias
los test deben de ser escritos en lenguaje humano por el negocio y los programadores lo traducen a un test automatizado

El QA determina cuando un sistema puede llevarse a produccion.

EL QA solo testea las nuevas funcionalidades

los programadores corren los test

## Whole Team

El cliente tiene que estar cerca de los programadores , en scrum se llama Product Owner
, el sabe las necesidades de el usuario.

Ademas todo el equipo de desarollo tambien debe de estar muy cerca.

El trabajo remoto no generara la misma eficacia que el trabajo co localizado de todo el equipo.


