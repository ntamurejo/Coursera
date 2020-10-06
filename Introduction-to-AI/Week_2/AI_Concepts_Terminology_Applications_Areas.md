# **AI Concepts, Terminology and Applications Areas**
## **Week 2**
### **AI Introduction**
#### **1. Cognitive Computing (Perception, learning, reasoning)**
La IA está a la vanguardia de una nueva era de la informática. La informática congnitiva difiere en gran medida de los
sistemas programables que se han desarrollado hasta la fecha, los cuales tenían un enfoque muy rígido y su uso a día de
hoy con el gran volumen de datos y la necesidad de tomar decisiones, hace que fallen y no puedan seguir el ritmo de las
nuevas tecnlogías.

La informática cognitiva ayuda a la gente para crear nuevos tipos de valores, encontrar respuestas y conocimiento ence-
rrado en grandes volúmenes de datos.

Cuando las personan buscan entender algo y tomar una decisión, realizan 4 pasos:
1. Observar la situación.
2. Interpretar las posibilidades que se hay delante.
3. Evaluar la hipótesis que se ha creado en el punto 2.
4. Tomar una decisión. Siempre la que parece la mejor y actuar acorde a ella.

Los sistemas cognitivos usan un proceso muy similar para razonar sobre la información que les llega. Además pueden
entender datos no estructurados (son todos aquellos que se asemejan al lenguaje coloquial, contexto...) siendo estos el
80% de los datos actuales. Los sistemas cognitivos se basan en:
* Lenguaje natural.
* Implícito.
* Ambiguo.
* Complejo.
Además comprenden el contexto e intentan entender la intención del usuario.

En resumen, los sistemas cognitivos se diferencian de los convencionales en que pueden:
* Leer e interpretar datos no estructurados, entendiendo no sólo el significado de las palabras sino también la intención
y el contexto.
* Razonar y tomar decisiones sobre problemas de forma similar a los humanos.
* Aprender de sus interacciones con los humanos y hacerse más "inteligentes"

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_1.png)

### **Machine Learning, Deep Learning, Neural Networks**

#### **1. Terminology and Related Concepts**
En primer lugar, se van a definir algunos términos y conceptos de IA, que suelen usarse indistintamente, pero que no se
refieren a lo mismo; como son: inteligencia artificial, machine learning, deep learning y neural networks.

* **La inteligencia artificial** es una rama de la informática que se ocupa de una simulación de comportamiento inteligente, asociados
con inteligencia humana como la planificación, el aprendizaje, el razonamiento, resolución de problemas, representación del conocimiento,percepción...

* **Machine Learning** es un subconjunto de la IA que utiliza algoritmos informáticos para analizar datos y tomar decisiones inteligentes basadas en lo aprendido, sin estar programado explícitamente. Se entrenan con grandes conjuntos de datos y aprenden de los ejemplos. **No siguen algoritmos basados ​​en reglas**

* **Deep learning** es un subconjunto especializado
de Machine Learning que utiliza redes neuronales en capas
para simular la toma de decisiones humana.
Los algoritmos de deep learning pueden etiquetar y categorizar información e identificar patrones; esto es lo que permite que aprendan todo el tiempo y mejoren los resultados de sus decisiones.

* **Neural Networks** son pequeñas unidades informáticas que tienen de entrada datos y aprenden a tomar decisiones. Normalmente las redes neuronales tienen capas y son la base de deep learning, lo cual permite que los algoritmos de aprendizaje sean más eficiente según aumenta la cantidad de datos, ya que tendrán más ejemplos y más experiencias con las que entrenar y tomar mejores decisiones para sacar mejores resultados.

Por último, vamos a diferenciar entre data science e IA.

* Data science es el proceso y método para extraer conocimientos de grandes volúmenes de datos no estructurados. Están involucradas disciplinas como matemáticas, estadística, machine learning, etc.
El data sciencie puede utilizar muchas técnicas de IA para obtener información a partir de los datos.

Cómo vemos, hay relación entre IA y Data Science, pero no es un subconjunto una de la otra, data science es la metodología para el procesamiento de datos mientra que IA es todo aquello que permite que los ordenadores aprendan a resolver problemas y tomar decisiones.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_2.png)

Pregunta 2:
![Question 2](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_3.png)

#### **2. Machine Learning**
Machine Learning es un subconjunto de la inteligencia artificial que utiliza los algoritmos para analizar datos y tomar decisiones inteligentes en base a lo que ha aprendido.

Machine learning lo que hace es ofrecer unos resultados acorde a unas entradas, generando modelos internamente qu ele ayuden a tomar la mejor decisión. Pero esto, ¿en que se diferencia de los actuales modelos estadísticos?

Programación Tradicional
![Tradiotional](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Traditional.png)
En la programación tradicional tenemos una serie de datos y unas reglas que son las entradas al algoritmo, el cual es fijo y se basa en condiciones de if-else-then, según el proyecto en el que se esté trabajando. En conclusión, se obtienen respuestas/salidas según como hayamos programado el algoritmo.

Machine learning
![Machine Learning](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/MachineLearning.png)

Cómo vemos el esquema ha varíado un poco, machine learning utiliza como entradas los datos y las respuestas y con ello genera un algoritmo variable. A partir de este algoritmo se consigue un conjunto de reglas que determinan como será el modelo de machine learning.

Tipos de machine learning:
1. Supervised Learning: es entrenado con datos etiquetados previamente. Cuántas más muestras se le proporcionen, más preciso será.

2. Unsupervised learning: se le proporcionan como entrada datos sin etiquetar y se deja que encuentre patrones por sí mismos. Normalmente se utiliza para clasterizar ejemplo kmeans.

3. Reinforcement learning: se le proporciona un conjunto de reglas y restricciones; dejando que logre por si mismo sus objetivos. Se define el estado, el objetivo, las acciones permitidas y las limitaciones. Se le premia cuanco acierta y se le penaliza cuando falla. Aplicación: enseñarle a jugar al ajedrez.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_4.png)

Pregunta 2:
![Question 2](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_5.png)

#### **3. Machine Learning Techniques and Training**
En este apartado se desarrollan un poco más los tres tipos de machine learning que se nombraron en el apartado anterior.

1. Supervised learning se refiere a cuando tenemos etiquetas en la base de datos y las usamos para construir un modelo de clasificación. Este tipo a su vez tiene 3 formas de aplicarse.
  1. Regresión.
  2. Clasificación.
    2.1 Decision Trees.
    2.2 SVM
    2.3 Logistic Regression.
    2.4 Random forests.
  3. Neural Networks

2. Unsupervised Learning en este caso como ya se explicó antes no tenemos los datos etiquetados, sino que es el propio algoritmo quien clasifica los datos, por ejemplo kmeans. Muy usado para clusterizar.

3. Reinforcement learning: en resumen este tipo de algoritmo trabaja con datos no estructurados y sin etiquetar, pero tiene una función de recompensa donde le "da" puntos o penaliza al algoritmo según vaya acertando o fallando. Recuerda el juego de caliente y frío cuando buscas algo.

En machine learning el conjunto de datos se divide en 3 categorías:

1. Training: es el subconjunto de datos utilizados para entrenar el algoritmo.

2. Validation: es el subconjunto de los datos que se utiliza para validar el algoritmo después de entrenarlo.

3. Test Sets son los datos que no se han utilizado antes ni para entrenar ni para validar, con ellos se puede comprobar si el algoritmo ofrecie buenos resultados o es necesario seguir trabajando en el. Podemos obtener con test sets data, la _accuracy_, _precision_ y _recall_.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_6.png)

#### **4. Deep Learning**
Deep learning es un subconjunto de machine learning. Consiste en varias capas formadas por algoritmos que crean una red neuronal, asemejándose a la estructura y funcionalidad del cerebro, por así decirlo.

Deep learning, permite que los sistemas de inteligencia artificial aprendan continuamente y mejoren la calidad y precisión de los resultados. Esto se puede lograr porque trabajan con datos no estructurados como videos, audios,...
Además corrige uno de los mayores problemas en los algoritmos tradicionales de apredizaje. La eficiencia y el rendimiento de los algoritmos de aprendizaje se estabilizan conforme crecen los datos de entrada, mientras que los algoritmos de deep learning continúan mejorando a medida que reciben más datos. Algunos ejemplos de deep learning son: subtítulos, reconocimiento de voz, traducción, coches autónomos.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_7.png)

#### **5. Neural Networks**
Una red neuronal es un conjunto de pequeñas unidades llamadas neuronas. Estas unidades toman datos de entrada y aprenden de ellos para tomar una decisión. Las redes neuronales aprenden a través de "backpropagation" que utiliza un conjunto de datos de entrenamiento que hace coincidir las entradas conocidas con las salidas deseadas.

Las capas ocultas toman un conjunto de entradas ponderadas y producen una salidad. Si tiene más de una capa oculta se llama "deep neural network".

Los perceptrones son los más simples. Es un nodo de entrada conectado a un nodo de salida.

Las capas de entrada envían los valores de entrada a la siguiente capa multiplicados por un peso y sumando los resultados.

Los nodos ocultos y de salida, tienen un sesgo que es un tipo especial de peso que se aplica a un nodo después de considerar las otras entradas. Por último, la función de activación determina como responde un nodo a sus entradas. Es un elemento muy importante.

* **Redes Neuronales Convolucionales (CNN)** son redes multicapa, útiles en el procesamiento de imágenes, reconocmiento de videos... Son muy buenas para detectar estructuras simples en una imagen y unirlas a otras para formar características más complejas.

* **Redes Neuronales Recurrentes (RNN)** son recurrentes porque realizan la misma tarea para cada elemento de una secuencia. Pueden hacer uso de secuencias largar, cada capa representa la observación en un momento determinado, esto ayuda a "ver o analizar" el contexto.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_8.png)

Pregunta 2:
![Question 2](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_9.png)

Pregunta 3:
![Question 3](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_10.png)

En resumen, en este punto se han analizado las siguientes ideas:

* Machine Learning es un subconjunto de la IA, utiliza algoritmos informáticos para analizar datos y tomar deciones inteligentes en función de lo aprendido. Las tres categorías principales son Supervised learning, Unsupervised learning y Reinforcement learning.
* Deep learning, es un subconjunto especializado de machine learning, que tiene capas de algoritmos para crear una red neuronal que permite a los sistemas de IA aprender de datos no estructurados y continuar aprendiendo.
* Las Neural networks, son una colección de unidades informáticas modeladas en neuronas biológicas, toman los datos entrantes y aprenden a tomar decisiones con el tiempo. Los diferentes tipos son perceptrones, redes neuronales Convolucionales(CNN) y redes neuronales recurrentes (RNN).
* El aprendizaje supervisado es cuando tenemos etiquetas de clase en el conjunto de datos y las usamos para construir el modelo de clasificación.
Se divide en tres categorías, regresión, clasificación y redes neuronales.
* Los algoritmos de machine learning se entrenan utilizando conjuntos de datos divididos en entrenamiento, validación y test-set.

### **AI Applications Areas**

#### **Key Fields of Applications in AI**
En este punto Tanmay Bakshi experto en IA nos habla de los diferentes campos en los que la IA está trabajando.

Para Tanmay subiendo a un alto nivel, habla del lenguaje natural, como el campo en el que más se está trabajando. Esto se debe a que el lenguaje natural son los datos más complejos con los que trabaja machine learning. Porque otros datos como el genoma, audio, imágenes tienen un patrón distinguible o que se puede intuir, sin embargo el lenguaje natural depende del contexto en el que se diga, a veces se acortan palabras,... porque fue inventado por los humanos para que los humanos lo entendieran, las personas no entendemos el lenguaje literalmente sino conceptualmente.

En segundo lugar, se encontraría computer vision. Describe que para los humanos el sentido de la vista es algo primitivo, nacemos con ello y podmeos hacer muchas cosas con ello.

En tercer lugar, estaría los datos de audio, text-to-speech, speech-to-text; esto es algo muy complejo, porque se combinan muchas cosas en una. Es necesario tener en cuenta todos los idiomas que hay, más los acentos, como lo interpreta cada pais o persona... Otro problema es que el audio, es algo que existe de por si en la naturalez, por lo que dificulta separar que es idioma de que es ruido o audio.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/Image_11.png)

#### **Natural Language Processing, Speech, Computer Vision**

Los humanos tenemos el método más avanzado de comunicación, conocido como lenguaje natural.

Las áreas donde la IA tiene mayor implicación son:

* Natural Language processing: es un subconjunto de la IA que permite a los ordenadores entender lo que las personas quieren decir. Utiliza algoritmos de machine learning y de deep learning para diferenciar el significado semántico de una palabra. Además, permiten entender el contexto de la frase. Algunos usos que tiene, es convertir lo que hablamos a texto.

* Speech Synthesis: sintetiza la voz humana tanto como sea posible. Se suele usar redes neuronales. Se suele usar en medicina para ayudar a personas que ha perdido su voz, a que el aparato con el que hablan se parezca lo máximo a su voz natural.

* Computer vision: se centra en replicar partes de la complejidad del sistema visual humano, y permite a los ordenadores identificar y procesar objetos en imágenes y videos, de la misma manera que hacemos las personas. El campo de la visión artificial ha dado grandes saltos en los últimos años y supero a los humanos en tareas relacionadas con la detección y etiquetado de objetos, gracias a deep learning y neural networks. Ejemplos importantes de su uso es el reconocmiento facial, realidad aumentada y mixta.


#### **Self Driving Cars**
En este apartado varios expertos nos hablan de la IA en la automoción.
LLevan trabajando en los coches autónomos durante varios años, explican que es un campo muy explotado desde 2005. En su caso, se han centrado en la detección de objetos 3D, ya que sigue siendo una tarea muy complicada para hacerse de forma automática (detectar vehículos, peatones, señales). Se centran en cómo tomar los datos láser y los datos de visión y radar, para posteriormente fusionarlos y sacar una vista completa del mundo que rodea al coche.

Una de las limitaciones de la visión humana, es la atención visual. Los humanos visualmente sólo podemos prestar atención a una cosa, mientras que las cámaras pueden hacerlo a varias.

-----------------------------------------------------------------
-----------------------------------------------------------------
En resumen, los puntos claves de este apartado son:
* El procesamiento del lenguaje natural (NLP) es un subconjunto de IA que permite a los ordenadores comprender el significado del lenguaje humano, incluida la intención y el contexto de uso.
* Speech-to-text permite a los ordenadores convertir el habla en texto identificando patrones comunes en las diferentes pronunciaciones de una palabra, asignando nuevas muestras de voz a las palabras correspondientes.
* Speech Synthesis permite a los ordenadores crear modelos de voz con un sonido natural.
* Computer Vision permite a los ordenadores identificar y diferenciar objetos en imágenes de la misma manera que lo hacen las personas.
* Los coches autónomos son una aplicación de IA que puede utilizar el procesado del lenguaje natural, el habla y la visión para ayudar a una conducción más eficiente y segura para los conductores.
------------------------------------------------------------------
## Ejemplo de algoritmo no supervisado. Adaptive Resonance Theory (ART).
Adaptive Resonance Theory es un algoritmo que proporciona capacidades de reconocimiento y predicción de patrones. Sirve tanto para supervisado como no supervisado. Explico el no supervisado.

ART es una arquitectura de red neuronal autoorganizada, el enfoque permite aprender nuevas asignaciones mantiendo el conocimiento existente.

Tiene la ventaja respecto a k-means, que puede alterar la cantidad de clústeres en función de los datos.

Características clave:
* Comparison field: utilizado para determinar cómo un nuevo vector de características encaja dentro de las categorías existentes.

* Recognition field: contiene neuronas que representan los grupos activos.

* Reset module.

![ART](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/ART.png)

Cuando se aplica el vector de entrada, el campo de comparación identifica el grupo en el que se ajusta más. Si el vector de entrada coincide en el campo de reconocimiento por encima de un valor, las conexiones a la neurona en el campo de reconocmiento se actualizan para tener en cuenta el nuevo vector. De lo contrario, se crea una nueva neurona para tener en cuenta el nuevo vector. Cuando ocurre esto los pesos de las neuronas existentes no se actualizan, esto hace que se pueda guardar el conocimiento existente. Todos los ejempos del conjunto de datos se aplican de esta forma hasta que ningún vector de entrada de ejempo cambia de grupo, momento en el que el entrenamiento ha terminado.
