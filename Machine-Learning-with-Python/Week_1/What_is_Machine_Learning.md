# **Machine Learning with Python**
## **Week 1**
### **What is Machine Learning?**
#### **1. Introduction to Machine Learning**
Machine Learning es un subcampo de computer science que da a los ordenadores la capacidad para aprender **sin necesidad de estar programado**. Esto último lo que indica es que no es necesario tener una regla que le diga cómo tiene actuar para dar un resultado, sino que a través de todos los inputs y respuestas, consigue generar un aprendizaje. Por ejemplo: tenemos un conjunto de animales y queremos saber cuales son perros y cuales gatos. Con la programación tradicional tendríamos que colocar reglas (if, else, for...) que hicieran preguntas (numero de patas, tiene alas, tamaño de ojos, etc) y según por donde fuera acabaría dando un resultado u otro. Sin embargo, para una mayor precisión deberíamos crear miles de preguntas y de reglas, y es aquí donde entra en juego el machine learning,que nos permite construir un modelo que analiza todo el conjunto de características y su correspondiente animal, aprendiendo el patrón de cada animal. Es decir, aprende como lo haría una persona, diferenciando entre cada animal y aprendiendo como son por separado, sin necesidad de saber si tiene dos ojos, o no.

Algunos ejemplos del uso de machine learning en la industria son:
* Netflix, amazon o cualquiera de estas plataformas.
* A los bancos para conocer si pueden conceder un préstamo y como varían las cuentas.
* En telecomunicaciones.
* Chatbots, face-recognizition.
* etc...

### Técnicas
* Regression / Estimation: consiste en la predicción de valores continuos. Por ejemplo: predecir el precio de una casa basándose en sus características.
* Classification: consiste en predecir que algo pertenece a una clase o tipo. Por ejemplo: para conocer si un lunar es maligno o benigno.
* Clustering: consiste en encontrar la estructura de unos datos. Por ejemplo, para segmentar los tipos de clientes que hay en la banca.
* Associations: es usado para encontrar puntos o eventos que coocurren con frencuencia por ejemplo comestibles que suelen ser comprados juntos por un cliente en particular.
* Anomaly detection: es usado para descubrir casos raros, por ejemlo para fraudes bancarios.
* Sequence mining es usado para predecir el próximo evento. Por ejemplo: se utiliza en el ámbito web.
* Dimension Reduction se utiliza para reducir el tamaño de los datos
* Recommendation systems asocia las preferencias de unas personas con otras que tienen gustos similares y les recomienda artículos nuevos, como libros o películas.

### Diferencia entre inteligencia artificial, machine learning y deep Learning
* **Inteligencia artificial** es un campo muy amplio que persigue el objetivo de hacer cualquier cosa para que las máquinas actúen de forma inteligente. Es un campo muy amplico que incluye: computer vision, language processing, creativity...
* **Machine Learning** es una rama de IA que cubre la parte matemática y estadística de la IA. Enseña a los ordenadores a resolver problemas analizando muchos ejemplos, aprendiendo de ellos y usando la experiencia para resolver el mismo problema en nuevas situaciones.

* **Deep Learning** es un subconjunto de machine learning, que surge por el hecho de usar redes neuronales que intentan imitar el comportamiento del cerebro humano.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_1/images/Image_1.png)

#### **2. Python for Machine Learning**
Python es un lenguaje de programación de propósito general que surgió hace unos años como lenguaje preferido entre los científicos de datos. Se puede utilizar para escribir algoritmos que se utilicen en machine learning, pero hay que tener en cuenta que ya existen muchos módulo y librerías que están implementados. A continuación, trataremos algunos de los paquetes más importantes de Python para machine learning:
* ***NumPy***: es una librería matemática para trabajar con arrays de N dimensiones.
* ***SciPy***: es una colección de algoritmos numéricos y toolbox específicas, que incluyen procesamiento de señales, optimización, estadísticas y más.
* ***Matplotlib***: es un paquete para dibujar 2D y 3D.
Eston son tres paquetes muy importantes, aunque existen más.
* ***Pandas***: es una biblioteca de Python de muy alto nivel que proporciona estructuras de datos fáciles de usar. Tiene funciones de importación, manipulación y análisis de datos.
* ***Scikit Learn***: es una colección de algoritmos y herramientas para el aprendizaje automático. Tiene la mayoría de algoritmos de clasificación, regresión y agrupación, y está diseñada para trabajar con NumPy y SciPy.

La mayoría de tareas que se realizan en un primer algoritmo de aprendizaje automático, ya están implementadas en Scikit Learn, incluído el preprocesamiento de datos, selección de características, extracción de características, modelos, parámetros...

Los algoritmos de machine learning se benefician de la estandarización del conjunto de datos. ***Scikit Learn*** proporciona funciones de utilidad y clases para cambiar los vectores de características sin procesar en una forma adecuada para el modelo.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_1/images/Image_2.png)

#### **3. Supervised vs Unsupervised**

* **Supervisado** es entrenado con datos etiquetados previamente. Cuántas más muestras se le proporcionen, más preciso será.
En la imagen de abajo se puede ver como son un conjunto de datos etiquetados:
![Datos etiquetados](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_1/images/Image_3.png)
Desglose de la tabla:
* Los nombres que componen las columnas son los **atributos**.
* Las columnas son las **características** las cuales están incluíadas en los datos.
* Si se observa el valor de los datos hay dos tipos:
  * Numérico.
  * Categórico.
  En este ejemplo, es categórico porque este conjunto de datos está hecho para clasificación.
Hay dos tipos de aprendizaje supervisado:
1. Clasificación: proceso para predecir una etiqueta de clase o categoría discreta.
2. Regresión: proceso para predecir un valor continuo en lugar de un valor categórico.

* **No supervisado** se le proporcionan como entrada datos sin etiquetar y se deja que encuentre patrones por sí mismos. Normalmente se utiliza para clasterizar ejemplo kmeans. Estos algoritmos son más complejos ya que apenas se conoce información de los datos.

Técnicas de algoritmos no supervisado.
1. La reducción de dimensiones: consiste en reducir características rendundantes para facilitar la clasificacion.
2. Market basket analysis es una técnica de modelado basada en la teoría de que si compras un grupo de alimentos es más probable que compres otros.
3. La estimación de densidad es un concpeto que se usa para explorar los datos y encontrar alguna estructura entre ellos.
4. Agrupación es una de las técnicas más famosas utilizada para agrupar puntos de datos u objetos que tienen algo en común. Normalmente se usa para encontrar estructuras y detección de anomalías.

En comparación comparación con el aprendizaje supervisado, el aprendizaje no supervisado tiene menos modelos y menos métodos de evaluación que se puedan utilizar para garantizar que el resultado del modelo sea exacto.
**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_1/images/Image_4.png)
