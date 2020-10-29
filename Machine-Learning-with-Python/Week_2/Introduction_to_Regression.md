# **Machine Learning with Python**
## **Week 2: Introduction to Regression**
### **Linear Regression**
#### **1. Introduction to Regression**
La regresión es el proceso de predecir un valor continuo. Está formado por dos tipos de variables:
- variable dependiente: estado objetivo o meta final que se trata de predecir.(se denota con Y)
- una o mas variables independientes: son las causas de esos estados; muestran convencionalmente por X.

Las variables se pueden medir en una escala de medición continua y a partir de esos datos, hacer un modelo de regresión.
Hay dos tipos de modelos:
* Simple: cuando se usa una variable independiente para estimar una variable dependiente que puede ser lineal o no. Por ejemplo predecir la emisión de co2, utilizando sólo el tamaño del motor. La linealidad de la regresión se basa en la naturaleza de la relación entre las variables dependientes e independientes.
* Múltiple: Cuando más de una variable independiente está presente. Por ejemplo, calcular el c02 teniendo en cuenta el número de cilindros y el tamaño del motor.

Dependiendo de la relación entre las variables dependientes e independientes, puede ser lineal o no lineal. Algunos ejemplos de algoritmos que se utilizan para la regresión son: ordinal regression, poisson regression, fast forest quantile regression, linear, polynomial, lasso, stepwise, ridge regression, bayesian linear regression, neural nertwork regression, decision forest regression, decision forest regression, boosted decision tree regression, knn.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_1.png)

#### **2. Simple Linear Regression**
En Simple Linear Regresion hay dos variables, una variable dependiente (Y) y una variable independiente (X). Es importante entender que en la regresión lo que se busca es un valor continuo y no discreto. Las variables independientes se pueden medir en una escala de medición.

##### **¿Cómo funciona la regresión lineal simple?**
Para explicar como funciona lo mejor es que nos apoyemos en el siguiente ejemplo:
En primer lugar, distinguimos en el eje X la variable independiente (Tamaño del motor); y en el eje Y la variable dependiente (emisión c02) que es la que tenemos por objetivo.

En segundo lugar, si se analiza el gráfico, en el que está dispuestos los datos de diferentes motores y cual es su emisión de co2 podemos trazar una linea creciente, en la cual se puede concluir que a mayor tamaño del motor mayo es la emisión de co2.

A través del modelo de regresión podemos estimar que para un motor de 2.4, la emisión de co2 es de 214 aprox.
![Ecuacion](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_2.png)

La ecuación que define esta línea es:
![Ecuacion](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_3.png)
* y: variable dependiente y valor que buscamos.
* x: variable independiente.
* coeficientes de la cuación lineal:(son los valores a ajustar en el model.)
 * theta 0: interceptor.
 * theta 1: pendiente.

Para estimar cual es la mejor linea de regresión que se ajusta a los datos que tenemos, debemos calcular theta 0 y theta 1.
![Error Residual](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_4.png)

El objetivo es encontrar una linea en la que la media de todos estos errores es mínimo. El objetivo de la regresión lineal es minimizar el MSE (Minimal Error Residual) y al minimizarlo deberíamos encontrar los mejores valores para theta 0 y 1.
Ahora bien, como podemos elegir los mejor valores de theta 0 y 1. A continuación, vamos a explicar un enfoque matemático:

#### Estimación de los parámetros
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_5.png)

Sin embargo, no es necesario memorizar la fórmula, ya que la mayoría de las librerías de machine learning en python la tienen implementada.

Una vez calculados los valores theta, es tan sencillo como sustituir el valor de x (variable independiente) en este caso el valor del tamaño del motor, por obtener el valor de y (emisión de c02).

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_6.png)

#### **3. Model Evaluation in Regression Models**
El objetivo de la regresión es construir un modelo para predecir con precisión un caso desconocido. En este punto, se explicarán dos tipos de evaluación que se pueden usar después de construir el modelo de regresión.
* **Enfoque A: Usar los mismos datos para entrenar y testear**
Al considerar los modelos de evaluación, queremos elegir el que nos dará una mayor precisión. Para saber cuanto podemos confiar en el modelo para que la predicción de una muestrada desconocida sea precisa; una de las soluciones es seleccionar una parte de nuestro conjunto de datos para realizar pruebas. Por ejemplo, si tenemos 10 registros, podemos usar todos para entrenamiento y para calcular nuestro modelo, a continuacion elegimos de esos 10, 4 y les quitamos las etiquetas pasándolos por el modelo para obtener los resultados. Las **etiquetas se llaman valores reales** del conjunto de prueba.
Esto indica cuan preciso es el modelo.

La mayoría de las métricas funcionan basandose en la similitud de los valores predichos y reales.
Este enfoque es el mas simple, ya que usa los mismos datos para entrenar y probar. Este enfoque suele tener una alta precisión de entrenamiento y baja precisión fuera de la muestra.
  **La precisión de entrenamiento** es el porcentaje de predicciones correctas que hace el modelo al usar el conjunto de datos de prueba. Sin embargo, una alta precisión en el entrenamiento no siempre es algo bueno. Por ejemplo, tener una alta precisión de entrenamiento puede resultar en un ajuste excesivo de los datos (overfitting). Esto significa que el modelo está demasiado entrenado para el conjunto de datos, que puede capturar ruido y producir un modelo generalizado.
  **La precisión fuera de la muestra** es el porcentaje de predicciones correctas que el modelo obtiene basándose en datos en los que no se ha entrenado el modelo.
**Hacer un entrenamiento y una prueba en el mismo conjunto de datos probablemente tendrá baja precisión fuera de la muestra debido al overfitting**
**Importante alta precisión fuera de la muestra**

* **Enfoque B: Separar los datos para entrenar y testear**
Para mejorar la precisión fuera de la muestra, lo mejor es separar los datos en dos grupos, entrenamiento y test.
Esto proporcionará una evaluación más precisa fuera de la muestra porque el conjunto de datos de test no es parte del entrenamiento.
El problema es que es muy dependiente de como se dividan los datos para entrenar y testear.

En la siguiente imagen se recoge un resumen de los dos enfoques:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_8.png)

Otro modelo de evaluación, es **k-fold o cross-validation**,que resuelve la mayoría de los problemas. Consiste en realizar múltiples divisiones de entrenamiento y test, utilizando el mismo conjunto de datos, dónde cada división es diferente.
El resultado es promedio para producir una precisión fuera de muestra más consistente. Es decir, si tenemos 100 datos los podemos agrupar en 4 conjutos de 25.
Grupo 1: 25
Grupo 2: 25
Grupo 3: 25
Grupo 4: 25
1. Realizamos un primer entrenamiento con los grupos 2,3 y 4; y un test con 1 --> Obtenemos la precisión 1
2. Realizamos un segundo entrenamiento con los grupos 1,3 y 4; y un test con 2 --> Obtenemos la precisión 2
3. Realizamos un tercero entrenamiento con los grupos 1,2 y 4; y un test con 3 --> Obtenemos la precisión 3
4. Realizamos un cuarto entrenamiento con los grupos 1,2 y 3; y un test con 4 --> Obtenemos la precisión 4
Por últimos calculamos la precisión media de los 4 casos, de esta forma se obtiene un valor más real, ya que se ha entrenado con todos los datos y se ha testeado con todos, pero mezclados.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_7.png)
#### **4. Evaluation Metrics in Regression Models**
Las métricas de evaluación se utilizan para explicar el rendimiento de un modelo. Estas métricas son clave en el desarrollo de un modelo, ya que proporcionan información sobre las áreas que requieren mejoras. Algunas métricas de evaluación son:
* Error absoluto medio: es la media del valor absoluto de los errores.
* Error cuadrático medio: eses l amedia del error cuadrático; más orientado a grandes errores.
* Error de la raiz cuadrada del error cuadrático medio: es bastante populas, porque el error cuadrático medio es interpretable en las mismas unidades que el vector de respuesta y facilita la relación de información.
* Error abosluto relativo: suma residual de cuadrados, donde la barra y es un valor medio de y, toma el error abostluto total y lo normaliza dividiendo por el error absoluto total del predictor.
* Error relativo al cuadrado: es una métrica muy popular en la comunidad científica par la precisión de los modelos. Representa la cercania de los datos a la linea de regresión.

**Error** diferencia entre los puntos de datos y la línea de tendencia generada por el algoritmo.
![Ecuaciones](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_10.png)

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_9.png)

#### **5. Multiple Linear Regression**
La regresión lineal multiple es cuando hay varias variables independientes presentes. Básicamente es la extensión del modelo de regresión lineal simple.

Existen dos aplicaciones para la regresión lineal múltiple:
* Para identificar la fuerza del efecto que tienen las variables independientes sobre la dependiente.
* Predecir el impacto de los cambios, es decir, para entender cómo cambia la variable dependiente cuando cambiamos las variables independientes.

En este tipo de regresión, la Y es una combinación lineal de variables independientes X. Es muy útil porque puede examinar qué variables son predictores significativos de la variable de resultado. Y conocer como afecta cada variable al resultado.
![Ecuaciones](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_11.png)
Se puede mostrar como una forma vectorial, es decir, producto escalar de dos vectores (vector de parámetros y vector de conjunto  de características). La idea es encontrar el hiperplano que mejor se ajuste a nuestros datos.

![Forma vectorial](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_12.png)
A diferencia de la regresión simple, en la múltiple los valores de theta0 y theta 1 son vectores.

El objetivo de la regresión lineal múltiple es minimizar la ecuación de MSE. Para ello, hay que encontrar los mejores valores para los coeficientes theta 0 y 1. Los métodos más utilizados para encontrar los valores de theta, son el método de optimización y el de mínimos cuadrados (para valores inferiores a 10000 muestras).
![MSE](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_13.png)

El descenso de gradiente es un buen enfoque cuando se tienen muchos datos.

Ojo, hay que tener cuidado, porque agregar demasiadas variables independientes sin justificación puede desembocar en un sobreajuste del modelo. Un modelo sobreajustado es un problema porque es demasiado complicado para su conjunto de datos y no lo suficientemente general como para ser utilizado para predicción.

En este tipo de modelo, debe haber una relación lineal entre la variable dependiente y cada una de sus variables independientes. Para comprobar eso, se pueden usar diagramas de dispersión y luego verificar visualmente su linealidad.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_14.png)

### **Non-Linear Regression**

#### **1. Non-linear regression**

Si los datos muestran gráficamente una tendencia con curvas, entonces la regresión lineal no produciría resultados muy precisos.

La regresión polinomial ajusta una línea curva a sus datos.
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_16.png)

La regresión no lineal no lineal es un método para modelar una relación no lineal entre la variable dependiente y un conjunto de variables independientes.

Para que un modelo se considere no lineal, Y debe ser una función no lineal de los parámetros theta, no necesariamente de las características X. Las ecuaciones pueden ser de forma exponencial, logarítmica...

**¿Cómo puedo saber si un problema es lineal o no lineal de una manera fácil?**

1. Averiguar visualmente si la relación es lineal o no. Lo mejor es trazar gráficos bivariados de salida con cada entrada.
2. Calcular el coeficiente de correlación entre variables independientes y dependientes, y si para todas es 0.7 o mayor, hay una tendencia lineal.
3. Utilizar regresión no lineal en lugar de regresión lineal cuando no se pueda modelar con precisión de parámetros lineales.

**¿Cómo modelar los datos si no son lineales?**

Usando regresión polinomial, es decir, regresión no lineal.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_2/images/Image_15.png)
