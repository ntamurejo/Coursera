# **Introduction to Deep Learning & Neural Networks with keras**
## **Week 1**
### **Introduction to Deep Learning**
#### **1. Introduction to Deep Learning**
En este vídeo se hace un video motivacional en el que se explican tres aplicaciones, para que veamos hasta donde puede llegar deep learning.
* Una empresa japonesa realiza una aplicación que permite colorear de forma realista imágenes en blanco en negro a color.
* La universidad de washington realiza una aplicación en la que puede sintetizar un video para que mueva los labios con un audio diferente a lo que está diciendo de forma muy realista.
* Hablar y que se escriba todo de forma correcta.
* Así como otras.

### **Neural Networks - Making Predictions**
#### **1. Neurons and Neural Networks**
En este punto se hace un resumen en el que se explican las partes de las neuronas del cerebro humano, descubiertas por Santiago Ramón y Cajal. Estas partes:
* Soma.
* Axón.
* Dentritas.
Se llevan de forma análoga a las redes neuronales artificiales, que tienen un modo de aprendizaje similar a como lo hace el cerebro.

#### **2. Artificial Neural Networks**
Empecemos por un esquema resumen de que es una red neuronal artificial. Cómo podemos ver en la imagen, está formada por capas. En primer lugar, tenemos la capa de entrada y al final una capa de salida, y todas las capas que están entre ambas se denominan capas ocultas.

![Red Neuronal](/home/ntamurejocolorado/Projects/Coursera/Introduction_to_Deep_Learning_Neural_Networks_with_keras/Week_1/images/Image_1.png)

Los 3 temas con los que se trabaja en redes neuronales son:
1. Forward Propagation.
2. Backpropagation.
3. Activation function.

De momento nos vamos a centrar en **Forward Propagation** que es el proceso a través del cual los datos pasan a través de capas de neuronas en una red neuronal desde la capa de entrada hasta la capa de salida.
![Red Neuronal](/home/ntamurejocolorado/Projects/Coursera/Introduction_to_Deep_Learning_Neural_Networks_with_keras/Week_1/images/Image_2.png)
Según la imagen, tenemos las entradas x1,x2 que serán resueltas por unos pesos (w1, w2) según
su entrada, y finalmente se les agrega una constante (b) conocida como sesgo.

Por lo tanto, un mejor procesamiento de los datos sería asignar la suma ponderada a un espacio no lineal. Una función popular es la función sigmoide, donde si la suma ponderada es un número positivo muy grande, entonces la salida de la neurona es cerca de 1, y si la suma ponderada es un número negativo muy grande, entonces la salida de la neurona está cerca de cero.

Las transformaciones no lineales como la función sigmoide se llaman funciones de activación. Las funciones de activación son otra característica extremadamente importante de las redes neuronales artificiales. Deciden si una neurona se activa o no. La función de activación realiza la transformación no lineal a la entrada permitiendo la red neuronal de aprendizaje y realizando tareas más complejas, como clasificaciones de imágenes y lenguaje traducciones.

![Red Neuronal](/home/ntamurejocolorado/Projects/Coursera/Introduction_to_Deep_Learning_Neural_Networks_with_keras/Week_1/images/Image_3.png)
