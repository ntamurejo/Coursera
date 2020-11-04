# **Machine Learning with Python**
## **Week 4: Introduction to Clustering**
### **K-Means Clustering**
#### **1. Intro to Clustering**
La segmentación de clientes es la partición de una base de clientes en grupos de individuos que tienen características similares. Es una estrategia significativa,ya que permite a la empresa dirigirse a grupos específicos de clientes,
para asignar más eficazmente los recursos de marketing.

**Un proceso de segmentación general no suele ser factible para grandes volúmenes de datos**

Los clientes se pueden agrupar en función de varios factores, incluidos edad, género, intereses, hábitos de gasto, etc.
El requisito importante es utilizar los datos disponibles para comprender e identificar en qué se parecen los clientes entre sí.

**La agrupación en clústeres** puede agrupar datos solo sin supervisión, basado en la similitud de los clientes entre sí. Partirá a sus clientes en grupos mutuamente excluyentes. Por ejemplo, en tres grupos. Los clientes de cada grupo son similares demográficamente entre sí. Ahora podemos crear un perfil para cada grupo, considerando las características comunes de cada clúster.
Por ejemplo, el primer grupo estaba formado por clientes adinerados y de mediana edad. El segundo está formado por jóvenes, Clientes educados y de ingresos medios,y el tercer grupo incluye clientes jóvenes y de bajos ingresos.
Finalmente, podemos asignar a cada individuo en nuestro conjunto de datos a uno de estos grupos o segmentos de clientes.

**La segmentación de clientes es uno de los usos populares de la agrupación en clústeres**
**Definición**:
Agrupar significa encontrar grupos en un conjunto de datos, sin supervisión.
**Un clúster** es un grupo de puntos de datos u objetos en un conjunto de datos que es similar a otros objetos del grupo,y diferente a los puntos de datos en otros clústeres.

**¿Qué es diferente entre agrupamiento y clasificación?**
Veamos nuevamente nuestro conjunto de datos de clientes.
Los algoritmos de clasificación predicen etiquetas clasificadas categóricas.
Esto significa asignar instancias a clases predefinidas, como predeterminadas o no predeterminadas.
Por ejemplo, si un analista quiere analizar datos del cliente para saber qué clientes pueden incumplir sus pagos,
ella usa un conjunto de datos etiquetado como datos de entrenamiento y utiliza enfoques de clasificación como un árbol de decisiones o SVM.

En general, la clasificación es un aprendizaje supervisado, donde cada instancia de datos de entrenamiento pertenece a una clase particular. Sin embargo, en la **agrupación en clústeres, los datos no están etiquetados y el proceso no está supervisado**
Por ejemplo, podemos usar un algoritmo de agrupamiento como k-medias para agrupar clientes similares en función de si comparten atributos similares, como edad, educación, etc.

En medicina, se puede utilizar para caracterizar el comportamiento del paciente, basado en sus características similares. Para identificar terapias médicas exitosas para diferentes enfermedades o en biología,
la agrupación se utiliza para agrupar genes con patrones de expresión similares
o agrupar marcadores genéticos para identificar los lazos familiares.
La agrupación en clústeres se puede utilizar para uno de los siguientes propósitos:
* La agrupación en clústeres basada en particiones es un grupo de algoritmos de agrupamiento como: K-medias, K-medianas o medias c difusas. Estos algoritmos son relativamente eficientes y son utilizado para bases de datos de tamaño mediano y grande.
* Los algoritmos de agrupación jerárquica producen árboles de agrupaciones, como algoritmos aglomerativos y divisivos.
Este grupo de algoritmos son muy intuitivos y generalmente son buenos para usar con conjuntos de datos de tamaño pequeño.
* Los algoritmos de agrupación basados en densidad producen agrupaciones de formas arbitrarias. Son especialmente buenos cuando se trata de clústeres espaciales o cuando hay ruido en su conjunto de datos.
Por ejemplo, el algoritmo de exploración de la base de datos.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_1.png)

#### **2. Intro to k-Means**
Hay diferentes tipos de Clustering, uno de ellos es el algoritmo de k-means que pertenece al grupo de particionamiento de cluster.

K-means divide los datos en subconjuntos no superpuestos sin ninguna estructura interna del clúster. Por tanto, es un algoritmo que trabaja con datos no supervisados. Los datos dentro de un cluster son muy similares, y los datos entre clusters son muy distintos.

El algoritmo de k-means trata de minimizar la distancia entre los datos de un cluster y de maximizarla entre los datos entre cluster.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_2.png" width="70%">
Para calcular la distancia entre clusters podemos utilizar la distancia euclidea entre dos características o más dependiendo del número que tengamos.

**Funcionamiento de K-Means**
1. Elegir el valor de K que es el número de cluster (más adelante se explica como elegir dicho valor.)
2. Calcular la distancia entre cada centroide y todos los puntos del conjunto de datos, creando la matriz de distancias.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_4.png" width="30%">

3. Asignar a cada punto el centroide más cercado usando la matriz de distancias.
Sin embargo, esto no es una buena clusterización porque los centroides la primera vez han sido elegidos en puntos aleatoriamente, por tanto la clusterización puede ser erronea. El objetivo es minimizar este error, para ello:
4. Se mueven los centroides colocados de forma aleatoria al punto medio de todos los puntos de ese conjunto de datos.
5. Se vuelven a calcular la matriz de distancias y se repiten los pasos 2 al 5 hasta que el movimiento de los centroídes sea mínimo, es decir, el error sea mínimo y los cluster sean densos.

Sin embargo, como es un algoritmo heurístico no hay tiempo para que converge a la global óptimo y el resultado puede depender de los clústeres iniciales, lo que implica que este algoritmo convergerá en un resultado pero el resultado puede ser un óptimo local, es decir no necesariamente el mejor  resultado para resolver el problema sobre el que se aplica. Como el algoritmo es muy rápido no habría problema es probar con diferentes valores de K para ver los resultados y elegir el que mejor se adapte al conjunto.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_3.png)
#### **3. More on K-Means**
A continuación se hace un breve resumen del algoritmo:

1. Un algoritmo de k-means funciona colocando k centroides al azar, uno para cada grupo. Cuanto más separados estén los grupos, mejor.
2. Calcular la distancia de cada punto de datos a los centroides.
**La distancia euclidia** se usa para medir la distancia del objeto al centroide. Se utiliza porque es la más popular.
3. Asignar a cada punto de los datos a su centroide más cercano creando un grupo.
4. Una vez que cada punto de datos se ha clasificado en un grupo, recalcular la posición de los k centroides.
La nueva posición del centroide está determinada por la **media de todos los puntos del grupo**
5. Esto continúa hasta que los centroides ya no se mueven.

**¿Cómo podemos evaluar la precisión de los clusters formados por k-Means?**
Hay una forma de decir qué tan malo es cada clúster, basado en el objetivo de las k-means.
Este valor es la **distancia promedio** entre puntos de datos dentro de un grupo.

La elección correcta de K suele ser ambigua porque depende mucho de la forma y escala de la distribución de puntos en un conjunto de datos. Una de las técnicas que se utiliza comúnmente es ejecutar el agrupamiento en
los diferentes valores de K y mirando una métrica de precisión para la agrupación.
Esta métrica puede ser la media, la distancia entre los puntos de datos y el centroide de su grupo,
que indican qué tan densos son nuestros clústeres o, en qué medida minimizamos el error de agrupación.
Luego, al observar el cambio de esta métrica, podemos encontrar el mejor valor para K.

**Problema** al aumentar la cantidad de clústeres, la distancia de los centroides a los puntos de datos siempre se reducirá.Esto significa que aumentar K siempre disminuirá el error.
Entonces, el valor de la métrica en función de K se traza con el método del codo que determinará donde la tasa de disminución cambia bruscamente, siendo la K más adecuada.
el punto del codo se determina donde la tasa de disminución cambia bruscamente.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_6.png" width="70%">

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_5.png)

### **Hierarchical Clustering**
#### **1.Intro to Hierarchical Clustering**
Hierarchical clustering construyen una jerarquía de
clústeres donde cada nodo es un clúster que consta de los clústeres de sus nodos secundarios.
Las estrategias para la agrupación jerárquica generalmente caen en
dos tipos, divisivo y aglomerativo.
Divisive es de arriba hacia abajo,
por lo que comienza con todas las observaciones en un grupo grande y lo divide
en trozos más pequeños. Piense en divisivo como dividir el grupo.
Aglomerativo es lo opuesto a divisivo. Entonces es de abajo hacia arriba
donde cada observación comienza en su propio grupo y
los pares de grupos se fusionan a medida que ascienden en la jerarquía.
El enfoque aglomerativo es más popular entre
científicos de datos, por lo que es el tema principal de este video.
Este método construye la jerarquía a partir de
los elementos individuales mediante la fusión progresiva de grupos.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_8.png" width="70%">

Esencialmente, las filas y columnas se fusionan
a medida que se fusionan los grupos y se actualiza la distancia.
Esta es una forma común de implementar este tipo de
agrupamiento y tiene la ventaja de almacenar en caché distancias entre clústeres.
Del mismo modo,
El algoritmo aglomerativo procede mediante la fusión de grupos,
y lo repetimos hasta que todos los grupos se fusionan y el árbol se completa.
**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_7.png)


#### **2.More on Hierarchical Clustering**

En este apartado hablaremos de la agrupación aglomerativa. Se trata de un enfoque de abajo hacia arriba.
Digamos que nuestro conjunto de datos tiene n puntos de datos.

1. Queremos crear n grupos, uno para cada punto de datos.
2. Cada punto se asigna como un grupo.
3. Queremos calcular la matriz de proximidad de distancia que será una tabla de n por n.
4. Ejecutar iterativamente los siguientes pasos hasta que se especifique y se alcanza el número de grupo, o hasta que solo queda un grupo.

Entonces, la **operación clave es el cálculo de la proximidad entre los grupos con un punto y también los grupos con múltiples puntos de datos**

**¿Cómo medimos las distancias entre estos grupos?**
Supongamos que tenemos un conjunto de datos de pacientes y queremos agruparlos mediante agrupación jerárquica.
Entonces, nuestros puntos de datos son pacientes con un conjunto destacado de tres dimensiones(edad, índice de masa corporal o IMC y presión arterial.)
Podemos utilizar diferentes medidas de distancia para calcular la matriz de proximidad. Por ejemplo, distancia euclidiana.

**¿cómo podemos calcular la distancia entre grupos cuando hay varios pacientes en cada grupo?**
Podemos utilizar diferentes criterios para encontrar los grupos más cercanos y fusionarlos.
En general, depende completamente del tipo de datos, la dimensionalidad de los datos y lo más importante, el conocimiento de dominio del conjunto de datos.

1. Agrupamiento de enlace único: distancia más corta entre dos puntos en cada grupo, como los puntos a y b.
2. Agrupamiento de enlaces completo: distancia más larga entre los puntos en cada grupo, como la distancia entre los puntos a y b.
3. Agrupamiento de vínculos promedio o la distancia media: distancia promedio de cada punto a un grupo.
4. Agrupamiento de vínculos centroides: Centroide es el promedio de los conjuntos de puntos de características en un grupo.
Este enlace tiene en cuenta el centroide de cada grupo. Existen tres **ventajas** principales al utilizar la agrupación en clústeres jerárquica.
Primero, no necesitamos especificar el número de clústeres necesarios para el algoritmo. En segundo lugar, la agrupación jerárquica es fácil de implementar. Y tercero, el dendrograma producido es muy útil para comprender los datos.
También hay algunas **desventajas**
* El algoritmo nunca puede deshacer ningún paso anterior.Por ejemplo, el algoritmo agrupa dos puntos y más adelante, vemos que la conexión no fue buena. El programa no puede deshacer ese paso.
* La complejidad del tiempo para la agrupación.
* Si tenemos un gran conjunto de datos, puede resultar difícil determinar el número correcto de grupos por el dendrograma.
**Comparativa con K-Means**

| **K-Means** | Hierarchical Clustering |
|-------------|-------------------------|
| Más eficiciente | Lento para grandes conjuntos de datos|
| Requiere el número de cluster en el que se desea dividir | No requiere el número de cluster |
| Proporciona sólo una partición de lo datos | Proporciona más de una partición dependiendo de la resolución de los datos |
| Devuelve diferentes clústeres cada vez que se ejecuta, debido a la inicialización aleatoria de los centroides | Siempre genera los mismos clusters|

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_9.png)

### **Density-based Clustering**
#### **1.DBSCAN**
En este apartado nos centraremos en el escaneo de bases de datos. Un algoritmo de agrupamiento basado en densidad que es apropiado para usar al examinar datos espaciales.

La mayoría de las técnicas de agrupamiento tradicionales como K-Means, jerárquicas,y el agrupamiento difuso se puede utilizar para agrupar datos de forma **no supervisada**.

Sin embargo, cuando se aplica a tareas con grupos de formas arbitrarias o grupos dentro de grupos,es posible que las técnicas tradicionales no logren buenos resultados, es decir, que los elementos del mismo clúster no compartan suficiente similitud.

Los algoritmos basados ​​en K-Means pueden ser fáciles de entender e implementar en la práctica, pero no detecta valores atípicos. Es decir, todos los puntos se asignan a un grupo incluso si no pertenecen a ninguno.

Por el contrario, el **agrupamiento basado en densidad** ubica regiones de alta densidad que están separadas entre sí por regiones de baja densidad. La densidad en este contexto se define como el número de puntos dentro de un radio específico.
Un tipo específico y muy popular de agrupamiento basado en densidad es DBSCAN.
DBSCAN es particularmente eficaz para tareas como la identificación de clases en un contexto espacial.

**IMPORTANTE:el algoritmo DBSCAN puede descubrir cualquier cúmulo de forma arbitraria sin verse afectado por el ruido**

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_10.png" width="70%">

DBSCAN se puede utilizar aquí para encontrar el grupo de estaciones que muestran las mismas condiciones meteorológicas.

**Funcionamiento**
DBSCAN son las siglas en inglés de Density-Based Spatial Clustering of Applications with Noise.

DBSCAN trabaja con la idea de que si un punto en particular pertenece a un grupo debería estar cerca de muchos otros puntos en ese grupo.

Funciona en base a dos parámetros:
* Radio(R): determina un radio específico que si incluye suficientes puntos dentro de él, lo llamamos un área densa.
* Puntos Mínimos(M): determina el número mínimo de puntos de datos que quiere en un vecindario para definir un clúster.

Un punto de datos es un** punto central** si dentro nuestra vecindad del punto hay al menos M puntos.
Por ejemplo, como hay seis puntos en el vecino de dos centímetros del punto rojo, marcamos este punto como un punto central.
<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_12.png" width="50%">

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_14.png" width="50%">


Un punto de datos es un **punto fronterizo** si:
* Su vecindad contiene menos de M puntos de datos.
* Es accesible desde algún punto central. Aquí, accesibilidad significa que está a nuestra distancia de un punto central.

<img src="/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_13.png" width="50%">


**Un valor atípico** es un punto que no es un punto central y tampoco está lo suficientemente cerca como para ser accesible desde un punto central.

El siguiente paso es conectar los puntos centrales que son
vecinos y ponerlos en el mismo grupo. Entonces, un grupo se forma con al menos un punto central más todos los puntos centrales alcanzables más todas sus puntos fronterizos.

Resumen:
* DBSCAN puede encontrar grupos de formas arbitrarias. Incluso puede encontrar un grupo completamente rodeado por un grupo diferente.
* DBSCAN tiene una noción de ruido y es resistente a valores atípicos.
* DBSCAN es muy práctico en muchos problemas del mundo real porque no es necesario que se especifique el número de grupos, como K en K-medias.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_4/images/Image_11.png)
