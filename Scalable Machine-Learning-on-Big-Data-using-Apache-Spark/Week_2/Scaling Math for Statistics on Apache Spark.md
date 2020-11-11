# **Scalable Machine Learning on Big Data using Apache Spark**
## **Week 2:Scaling Math for Statistics on Apache Spark**
### **Experience parallel programming on Apache Spark**
#### **1. Averages**
**Primer momento**
En este punto se trata la distribución estadística de tendencia central, es decir, la media y la mediana.
La **media** es muy fácil de calcular:
<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_1.png" width="70%">

La **mediana** consiste en dado un conjunto de valores numéricos, ordenarlos de menor a mayor y elegir en elemento central. Si ocurre que la lista de valores es par, se eligen los dos valores centrales y se dividen entre dos, lo que nos daría el valor medio.

**La mediana es una versión más resistente de la media, porque los valores extremadamente inusuales tienen menos efecto en ella.**

**La media se tira en la dirección de los valores atípicos, mientras que la mediana es mucho más resistente a los valores atípicos.**

**El primer momento da una idea sobre la tendencia central de un valor de sensor.**

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_2.png" width="100%">


#### **2. Standard deviation**
**Segundo momento**
La desviación estándar indica la amplitud de los datos en torno a la media.
* Si es baja,entonces todos los valores están muy cerca del valor medio.
* Si es alta, los valores de la lista están mucho más extendidos alrededor de la media,

Para visualizar mejor la desviación estandar, podemos utilizar el histograma, que nos indica cuántos valores de una lista están dentro de un rango determinado.

Para calcular la desviación estándar podemos seguir la siguiente fórmula:
<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_3.png" width="100%">
Cómo podemos ver, el valor es independiente del tamaño de la lista.

La **desviación estándar** explica como se extienden los datos a lo largo de la media.

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_4.png" width="100%">

#### **3. Skewness**
**Tercer momento estadístico: Asimetría**
La **asimetría** explica como se distribuyen los datos alrededor de la media. Si el histograma tiene cola, hablamos de sesgo.
* Si la cola está a la derecha, sesgo positivo, de lo contrario sesgo negativo.

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_5.png" width="100%">

Cuánto más cerca esté el resultado del valor cero nos indica que existe menor sesgo.

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_6.png" width="100%">

#### **4. Kurtosis**
**Cuarto momento estadístico: Kurtosis**

**Kurtosis** da información sobre la forma de los datos cuando se grafican en un histograma. Cuánto mayor es la medida de Kurtosis, más valores atípicos están presentes y más largas son las colas de la distribución en el histograma.

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_7.png" width="100%">

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_8.png" width="100%">

#### **5. Covariance, Covariance Matrices, Correlation**
La covarianza y la correlación nos dicen cómo dos columnas están interactuando entre sí.
Para calcular la covarianza seguimos la siguiente ecuación:
<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_9.png" width="100%">

Correlación es un parámetro numérico adimensional que cuantifica el grado de relación lineal entre dos variables continuas X e Y, y se define a partir de la covarianza.
<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_10.png" width="100%">

**La covarianza y la correlación describen la dependencia entre pares de datos**
Si el resultado de la correlación es:
* +1 existe una relación lineal fuerte, en sentido creciente.
* 0 Las columnas muestran que no hay dependencia entre ellas.
* -1 existe una relación lineal fuerte, en sentido decreciente.

**Si el signo de la covarianza es positivo, existe una relación lineal directa entre las variables, es decir, a mayor valor observado de X, mayor valor de Y**

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_11.png" width="100%">
### **Data Visualization of Big Data**
#### **1.Plotting with Apache Spark and python's matplotlib**
Cuando el conjunto de datos con el que trabajamos es muy grande, debemos utilizar el muestreo (sampling). Los motivos son:
* Es un subconjunto de los datos originales.
* El subconjunto conserva la mayoría de las propiedades de los datos originales, debido a la aleatoriedad.
* Reduce el coste computacional.
A continuación vamos a analizar diferentes tipos de gráficos que nos ayudaran a sacar conclusiones respecto a los datos:

1. **Box plots**
Muestran muchas propiedades estadísticas al mismo tiempo: media, desviación estándar, sesgo y contenido atípico.
<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_12.png" width="100%">

2. **Run charts**
Son muy utilizados en las gráficas de mercados y se usan para sacar resultados de series de datos.

<img src="/home/ntamurejocolorado/Projects/Coursera/Scalable Machine-Learning-on-Big-Data-using-Apache-Spark/Week_2/images/Image_13.png" width="100%">

3. **Scatter plots**
Consiste en trazar puntos de datos indivicuales en un espacio vectorial de dos o tres dimensiones. Cada punto refleja una fila en el conjunto de datos y en cada dimensión o columna. Se puede utilizar para clasificación, agrupación de clúster de datos similares o detectar valores atípicos del comportamiento normal.

4. **Histograma**
Sirven para tener una idea de la distribución de valoes dentro de una sola dimensión.
