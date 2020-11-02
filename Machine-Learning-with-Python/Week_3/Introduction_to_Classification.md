# **Machine Learning with Python**
## **Week 3: Introduction to Classification**
### **K-Nearest Neighbours**
#### **1. Introduction to Classification**
* Enfoque de supervised learning.
* Medio de categorizar o clasificar algunos elementos desconocidos en un conjunto discreto de clases.
* La clasificación intenta aprender la relación entre un conjunto de variables de características y una variable objetivo.
* El atributo objetivo en la clasificación es una variable categórica con valores discretos.
La clasificación puede ser binaria o múltiple, dependiendo del problema al que nos enfrentemos.
Tipos de clasificación:
* Decision Trees.
* Naïve Bayes.
* Linear Discriminant Analysis.
* K-Nearest Neighbours
* Logistic Regression.
* Neural Networks.
* Support Vector Machines(svm).
**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_1.png)

#### **2. K-Nearest Neighbours**
Es un algoritmo de clasificación que toma un conjunto de puntos etiquetados y los utiliza para aprender como etiquetar otros
puntos.
* Los casos que están más cerca unos de otros se llaman "Neighbours".
* Se basa en los casos similares con la misma etiqueta que están más cerca unos de otros.
* La distancia entre dos casos es una medida de su disimilitud.
A continuación se enumera como funciona el algoritmo de knn:
1. Elegir un valor para K.
2. Calcular la distancia desde el caso desconocido con el resto de K valores.
3. Seleccionar las k-observaciones en los datos de entrenamiento que son más cercanas para el dato desconocido.
4. Predecir el valor del caso desconocido utilizando la respuesta más probable de los k vecinos más cercanos.
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_2.png)
El punto 1 y 2 pueden ser más complicados de entender por lo que se profundiza en ellos a continuación:
* Punto 1: Elegir el valor de K:
* K con un valor muy bajo puede producir overfitting.
* K con un valor demasiado alto, provocaría un modelo generalizado.
* La solución es reservar una parte de los datos para probar la precisión del modelo. Una vez que lo hayas hecho, se
elige k=1 y luego se usa la parte de entrenamiento para modelar y calcular la precisión de la predicción utilizando todas
las muestras en el conjunto de prueba. Se repite el proceso aumentando la k y se ve cual es el mejor valor para el modelo.

* Punto 2: Calcular la distancia en 1 dimension:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_3.png" width="70%">

En el caso de tener más de una característica la fórmula se debe aplicar como sigue, que es el caso en el que se aumentan
las dimensiones.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_4.png" width="70%">
**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_5.png" width="70%">

#### **3. Evaluation Metrics in Classification**
Las métricas de evaluación explican el desempeño de un modelo. Las métricas de evaluación son claves en el desarrollo
de un modelo, ya que dan información a áreas que podrían requerir mejoras. Hay diferentes métricas, pero en este curso
se habla de tres:
* Indice de Jaccard.
* Puntuación F1.
* Pérdida de Registro.

1. Indice de Jaccard
Se puede definir como el tamaño de la intersección dividido por el tamaño de la unión de dos juegos de etiquetas.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_6.png" width="70%">

2. Puntuación F1

Otra forma de ver la precisión de los clasificadores es la matriz de confusión. Cada fila de la matriz muestra las etiquetas Actual/ Verdadero en el conjunto de prueba y las columnas muestran las etiquetas predicas por el clasificador.
Lo bueno de la matriz de confusión es que muestra la capacidad del modelo para predecir o separar clases.

La precisión se calcula como Verdadero Positivo / (Verdadero Positivo + Falso Positivo).

El recall es Verdadero Positivo / (Verdadero Positivo + Falso Negativo)
Es el promedio armónico de precisión y recall, donde una puntuación F1 alcanza su mejor valor en 1 (que representa precisión y recall perfectas) y su peor valor en 0. Es una buena forma de demostrar que un clasificador tiene un buen valor tanto para el recall como para la precisión.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_7.png" width="70%">


Tano el índice de Jaccard como la puntuación F1 se pueden utilizar para clasificaciones múltiples.

3. Pérdida logarítmica

Mide el rendimiento de un clasificador donde la salida prevista es un valor de probabilidad entre 0 y 1. Por ejemplo, predecir una probabilidad de 0.13 cuando la etiqueta real es 1, sería malo y daría lugar a una gran pérdida de registros. Podemos calcular la pérdida logarítmica de cada fila usando la ecuación de pérdida logarítmica, que mide que tan lejos
está cada predicción de la etiqueta real. Y luego calculamos la pérdida de registro promedio en todas las filas del conjunto de prueba.
Es obvio que los clasificadores ideales tienen valores de pérdida logarítmica progresivamente más pequeños. Por tanto, el clasificador con menor pérdida logarítmica tiene mejor precisión.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_8.png" width="70%">

**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_9.png" width="70%">

### **Decision Trees**
#### **1.Introduction to Decision Trees**
Los árboles de decisión se construyen dividiendo el conjunto de entrenamiento en distintos nodos, donde un nodo contiene
todos o la mayor parte de una categoría de datos.
Los árboles de decisión tratan de probar un atributo e ir bifurcando los casos en función del resultado de la prueba.
Cada nodo interno corresponde a una prueba, y cada rama corresponde a un resultado de la prueba, cada nodo de la hoja
asigna un paciente a una clase.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_11.png" width="70%">

**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_10.png" width="70%">

#### **2.Building Decision Trees**
Los árboles de decisión de construyen utilizando particiones recursivas para clasificar los datos. Lo importante a la hora
de hacer un árbol de decisiones es determinar qué atributo es el mejor o más predictivo para dividir datos según la función.

Un nodo en el árbol se cosidera puro si en el 100% de los casos, los nodos caen en una categoría específica del campo
objetivo. De hecho, el método utiliza particiones recursivas para dividir los registros de entrenamiento en segmentos minimizando
la impureza en cada paso. La impureza de los nodos se calcula mediante la entropía de los datos en el nodo.

**La entropía** es la cantidad de desorden de información o la cantidad de aleatoriedad en los datos. La entropía en el
nodo depende de cuántos datos aleatorios hay en ese nodo y se calcula para cada nodo. Se utiliza para calcular la homogeneidad
de las muestras en ese nodo. Si las muestras son completamente homogéneas, la entropía es cero y si las muestras se dividen
por igual, tienen una entropía 1.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_12.png" width="50%">

**La ganancia** de información es la información que puede aumentar el nivel de certeza después de dividir, es decir,
es la entropía del arbol antes de separar.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_13.png" width="50%">

* **A medida que la entropía o la cantidad de aleatoriedad disminuyen, la ganancia de información o la cantidad de certeza aumnenta y viceversa**
* **Construir un árbol de decisión se basa en encontrar los atributos que devuelven la mayor ganancia de información**
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_14.png" width="90%">

Ejemplo de calculo de la ganancia:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_15.png" width="50%">

* **Se elige el atributo que tenga una ganancia mayor, la ganancia tiene más peso que la entropía**

**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_16.png" width="50%">
### **Logistic Regression**
#### **1.Intro to Logistic Regression**
La regresión logística es una técnica estadística y de aprendizaje automático para clasificar registros de un conjunto de datos basado en los valores de los campos de entrada.
* En la regresión logística, utilizamos una o más variables independientes.
* La regresión logística es análoga a la regresión lineal, pero trata de predecir un campo objetivo discreto en lugar de uno numérico.
En la regresión lineal, podríamos intentar predecir un valor continuo de variables como el precio de una casa, presión arterial de un paciente o consumo de combustible de un automóvil. Sin embargo, en la regresión logística, predecimos una variable que es binaria como sí/no, verdadero/falso,todos los cuales se pueden codificar como cero o uno.
* En la regresión logística, las variables independientes deben ser continuas. Si son categóricos, deben estar codificados como indicadores o ficticios. Esto significa que tenemos que transformarlos en algún valor continuo.
* La regresión logística se puede utilizar tanto para clasificación binaria como para clases múltiples clasificación.
Ejemplo: para predecir la probabilidad de que una persona tenga un ataque cardíaco dentro de un período específico de tiempo, basado en nuestro conocimiento de la edad de la persona, sexo e índice de masa corporal. **En los ejemplos no solo predecimos la clase de cada caso, también medimos la probabilidad de que un caso pertenezca a una clase específica**

**Cuando utilizar la regresión logística**
Hay cuatro situaciones en las que la regresión logística es una buena elección:

1. **Cuando el campo de destino en sus datos es categórico o específicamente es binario**
Como cero/uno,sí/no,abandono o no abandono, positivo / negativo, etc.
2. **Necesidad de la probabilidad de su predicción**
Por ejemplo, si desea saber cuál es la probabilidad de que un cliente compre un producto.
La regresión logística devuelve una puntuación de probabilidad entre cero y uno para una muestra determinada de datos.
3. **Si sus datos son linealmente separables**
El límite de decisión de la regresión logística es una línea, un plano o un hiperplano.
Un clasificador clasificará todos los puntos de un lado del límite de decisión como pertenecientes
a una clase y todos los del otro lado como pertenecientes a la otra clase.
4. **Debe comprender el impacto de una función**
Puede seleccionar las mejores características en función de la importancia estadística de la logística
coeficientes o parámetros del modelo de regresión. De hecho, nos permite comprender el impacto que una variable independiente
tiene sobre la variable dependiente mientras controla otras variables independientes.

**El objetivo de la regresión logística es construir un modelo para predecir la clase de cada muestra;así como la probabilidad de que cada muestra pertenezca a una clase**

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_18.png" width="70%">

**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_17.png" width="50%">

#### **2.Logistic regression vs Linear Regression**
Repasamos  por qué la regresión lineal no se puede utilizar correctamente para algunos problemas de clasificación binaria.
* El objetivo de la regresión logística es construir un modelo para predecir la clase de cada cliente y también la probabilidad de que cada muestra pertenezca a una clase.
* y es el vector de la etiqueta,también llamados valores reales, que nos gustaría predecir, y qué es el vector de los valores predichos por nuestro modelo.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_19.png" width="50%">

A continuación, vamos a tratar de explicar con un ejemplo como se aplicaría la regresión lineal frente a la logística. En primer,
lugar vamos a trabajar con esta tabla de datos. Si quieremos conocer que valor "income"(variable dependiente) tendrá un nuevo dato frente a la edad (variable independient),por ejemplo, se representa como se ve en la siguiente figura:

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_21.png" width="50%">
En este caso tiene sentido utilizar una regresión lineal porque buscamos un valor continuo y no uno binario; además, si
representamos los datos vemos que cumplen la ecuación de theta0 + theta1X.

Sin embargo, si ahora intentamos aplicar esta misma situación y ecuación, pero representando como variable dependiente "churn"
frente a la edad:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_22.png" width="50%">

vemos que al buscar que valor de churn obtendríamos frente a una nueva edad, tendremos un valor
float, lo que nos podría llevar a generalizar con:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_23.png" width="50%">
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_24.png" width="50%">
Esto como podemos concluir no nos sirve para este tipo de variable, por lo que la regresión lineal cuando la variable dependiente es una etiqueta y es un binario no puede aplicarse.

Si continuamos analizando el problema de la regresión lineal en este ejemplo, vamos a hablar de la función escalón que se produce
con respecto a lo último que hemos mencionado.
Este umbral de 0.5 funciona como una función escalón que tiene una salida 0 o 1, sin importar cuan grande o pequeño sea el valor
de entrada; es decir, siempre que sea menor a 0.5 obtendremos un 0 y cuando sea mayor un 1.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_25.png" width="50%">

Para evitar estos valores bruscos, una idea es suavizar la función escalón y esto nos da, la función sigmoide.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_26.png" width="50%">

**La función sigmoide**, también llamada función logística,se asemeja a la función de paso y es utilizada por la siguiente expresión en la regresión logística. Cuando Theta transpuesta de x se vuelve muy grande,la potencia e menos Theta transpuesta de x en el denominador de la fracción se vuelve casi 0, y el valor de la función sigmoide se acerca a 1.
**La salida de la funcion sigmoide siempre está entre 0 y 1,lo que hace que sea adecuado interpretar los resultados como probabilidades**
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_27.png" width="50%">

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_28.png" width="50%">

Podemos encontrar a Theta a través del proceso de formación, que se compone de los siguientes pasos:
1. Inicializar el vector Theta con valores aleatorios como ocurre con la mayoría de los algoritmos de aprendizaje automático.
Por ejemplo, menos 1 o 2.
2. Calcular la salida del modelo,que es sigmoide de Theta transpose x.
Por ejemplo, cliente en su conjunto de formación. La salida de esta ecuación es la probabilidad de que el cliente pertenezca a la clase 1.
3. Comparar la salida de nuestro modelo, ŷ, que podría ser un valor de, 0,7, con la etiqueta real del cliente, que es, por ejemplo, 1, para churn.
Después se registra la diferencia como el error de nuestro modelo para este cliente, que sería 1 menos 0,7,qu es igual a 0,3.
Este es el error de un solo cliente de todos los clientes del conjunto de formación.
4. Calcular el error para todos los clientes como hicimos en los pasos anteriores y sumar estos errores.
El error total es el coste del modelo y se calcula mediante la función de coste del modelo.
* **El coste muestra qué tan mal estima el modelo las etiquetas**
* **Cuanto menor sea el coste, mejor sera el modelo para estimar correctamente las etiquetas de los clientes**
* **Intentar minimizar este coste**
5. Cambiar el valor de Theta de tal manera que reduzcamos el costo total.
6. Después de cambiar los valores de Theta, volvemos al paso dos, y luego comenzamos otra iteración y calculamos nuevamente el costo del modelo.
Seguimos haciendo esos pasos una y otra vez, cambiando los valores de Theta cada vez hasta que el costo sea lo suficientemente bajo.
Resumen:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_29.png" width="50%">

**Importante, para encontrar los valores theta que reduzcan el valor del coste, se suele emplear la técnica del descenso de gradientes; para detener el modelo lo único que se puede hacer es calcular la precisión y parar cuando nos parezca satisfactorio**

**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_30.png" width="50%">

#### **3.Logistic Regression Training**
El objetivo principal de la función de coste y de la regresión logística es cambiar los parámetros del modelo, para conseguir
la mejor estimación de las etiquetas de nuestra base de datos.

El primer paso, es ver la relación entre la función de coste y los parámetros theta. La función de coste es la diferencia entre
los valores reales de y y la salida de nuestro modelo ŷ.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_31.png" width="50%">

**¿cómo encontramos los mejores pesos o parámetros que minimizan esta función de coste?**
Debemos calcular el punto mínimo de esta función de coste. Esta es la función de coste de regresión logística.
Como puede ver, penaliza situaciones en las que la clase es cero y la salida del modelo es uno, y viceversa.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_32.png" width="50%">

**Resumen**
* **Objetivo**: encontrar un modelo que mejor estime las etiquetas reales, es decir, encontrar los mejores parámetros theta.
* **¿Cómo encontrar los mejores parámetros para el modelo?** Minimizando la función de coste.
* **¿Cómo minimizamos la función de costes?** Descenso de gradientes.
* **El descenso de gradiente** es un enfoque iterativo para encontrar el mínimo de una función. Es una técnica
para utilizar la derivada de una función de costo para cambiar los valores de los parámetros para minimizar el costo o el error.

**Si calculamos la derivada de J con respecto a theta uno, y obtenemos un número positivo, indica que la función aumenta; por tanto, para disminuir la J debemos cambiar la dirección y obtener un número negativo**
**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_34.png" width="50%">

* **La tasa de aprendizaje** nos da un control adicional sobre la rapidez con la que nos movemos en la superficie.
En resumen, podemos decir, que **el descenso de gradiente** es como dar pasos en la dirección actual de la pendiente,
y la **tasa de aprendizaje** es como la longitud del paso que das.

* **Repaso del algoritmo de este punto**
1. Inicializamos los parámetros con valores aleatorios.
2. Alimentamos la función de coste con el conjunto de capacitación y calculamos el coste. Esperamos una alta tasa de error ya que los parámetros se establecen de forma aleatoria.
3. Calculamos el gradiente de la función de coste teniendo en cuenta que tenemos que usar una derivada parcial.
4. Actualizamos los pesos con nuevos valores de parámetros.
5. Volvemos al paso dos y alimentamos la función de coste nuevamente, que tiene nuevos parámetros.
Como se explicó anteriormente, esperamos menos errores a medida que bajamos por la superficie del error.
Continuamos este bucle hasta llegar a un valor corto de costo o un número limitado de iteraciones.
6. El parámetro debe encontrarse aproximadamente después de algunas iteraciones.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_35.png" width="50%">

**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_36.png" width="50%">

### **Support Vector Machine**
#### **1.Support Vector Machine**
Support Vector Machine es un algoritmo supervisado que puede clasificar los casos encontrando un separador.
Funciona mapeando primero los datos a un espacio de características de alta dimensión para que los datos
se pueden categorizar, incluso cuando no sean linealmente separables.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_37.png" width="50%">

Por ejemplo, si vemos la figura de arriba se muestra la distribución de un pequeño conjunto de puntos que se dividen en dos categorías diferentes; sin embargo no son linealmente separables, pero si a traves de una curva.

Ahora bien, si pasamos estos datos a un espacio de mayor dimensión, por ejemplo a 3 dimensiones, quedando como la figura de abajo.
Vemos que se pueden separar fácilmente a través de un plano.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_38.png" width="50%">

**El algoritmo SVM** genera un hiperplano óptimo que categoriza nuevos ejemplos.
**Kernelling**: mapeo de datos en un espacio de mayor dimensión. La función matemática utilizada para la transformación se conoce como kernel función, y puede ser de diferentes tipos, como lineal, polinomio, función de base radial o RBF y sigmoide.

**¿cómo encontramos el separador correcto u optimizado después de la transformación?**
SVM se basan en la idea de encontrar un hiperplano que mejor divide un conjunto de datos en dos clases.
El objetivo es elegir un **hiperplano** con el **mayor margen** posible.
Los ejemplos más cercanos al hiperplano son los **vectores de soporte**

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_40.png" width="50%">

* **Ventajas SVM**
  * Precisa en espacios de gran dimensión.
  * Eficiente en memoria.
  * Es bueno para tareas de análisis de imágenes (clasificiación y reconocimiento de dígitos escritos a mano)
  * Eficaz en minería de texto.

* **Inconvenientes**
  * Algoritmo propenso a sobreajuste si el número de características es mucho mayor que el número de muestras.
  * No proporcionan directamente estimaciones de probabilidad, que son deseables en la mayoría de los problemas de clasificación.
  * No son muy eficientes computacionalmente si su conjunto de datos es muy grande, como cuando tiene más de 1,000 filas.

* **Aplicaciones**
  * Detección de spam.
  * Asignación de categorías de texto y análisis de opiniones.
  * Clasificación de datos de expresión génica.

**Quiz**
Pregunta 1:
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_3/images/Image_39.png" width="50%">
