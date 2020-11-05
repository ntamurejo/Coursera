# **Machine Learning with Python**
## **Week 5: Intro to Recommender Systems**
### **Content-based Recommendation Engines**
#### **1. Intro to Recommender Systems**
Las personas suelen tener gustos que siguen unos patrones, así como pueden tener gustos similares personas conocidas,
o del entorno. En este punto, surgen los sistemas de recomendación, para ayudar a tener contenido que le interese a la persona.

**Los sistemas de recomendación** intentan capturar estos patrones y comportamientos similares, para ayudar a predecir qué más podría gustarle.Tienen muchas aplicaciones en muchos sitios web. Por ejemplo, sugiriendo libros en Amazon y
películas en Netflix.

Una de las principales ventajas de utilizar sistemas de recomendación es que los usuarios obtienen una exposición más amplia
a muchos productos diferentes en los que podrían estar interesados.
En general, existen 2 tipos principales de sistemas de recomendación: filtrado basado en contenido y colaborativo.
La principal diferencia entre cada uno, se puede resumir por el tipo de declaración que un consumidor podría hacer. Por ejemplo, el paradigma principal de un contenido.
El sistema de recomendación se basa en la afirmación: "Muéstrame más de lo mismo de lo que me gustó antes".
* Los sistemas basados ​​en contenido intentan averiguar cuales son los favoritos de un usuario, y luego hacer recomendaciones.
* El filtrado colaborativo se basa en un usuario que dice: "Dime qué es popular entre mis vecinos porque a mí también me puede gustar ".  
Las técnicas de filtrado colaborativo encuentran similares grupos de usuarios y proporcionan recomendaciones basadas en gustos similares dentro de ese grupo.

En cuanto a la **implementación** de sistemas de recomendación, existen 2 tipos: basados en memoria y basados en modelos.
* En los enfoques basados en memoria, usamos todo el conjunto de datos de elementos de usuario para generar una recomendación
sistema. Utiliza técnicas estadísticas por ejemplo: Pearson Similitud de coseno y Distancia euclidiana, entre otros.
* En los enfoques basados en modelos, se desarrolla un modelo de usuarios en un intento de aprender sus preferencias. Los modelos se pueden crear usando Machine Learning técnicas como regresión, agrupamiento, clasificación, etc.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_5/images/Image_1.png)

#### **2. Content-based Recommender Systemns**
Un sistema de recomendación basado en contenido intenta recomendar elementos a los usuarios según su perfil.
El perfil del usuario gira en torno a las preferencias y gustos de ese usuario y tiene una forma basada en las calificaciones de los usuarios,incluyendo el número de veces que el usuario ha hecho clic en artículos diferentes ... El proceso de recomendación se basa en la similitud entre esos elementos.
La similitud o cercanía de elementos es medido sobre la base de la similitud en el contenido de esos elementos (categoría de artículos,
etiqueta, género, etc.)
Por ejemplo, si tenemos cuatro películas,y al usuario le gustan los dos primeros elementos, y si el elemento 3 es similar al elemento 1 en términos de su género, el motor también recomendará el elemento 3 al usuario.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_5/images/Image_2.png)


#### **3. Collaborative Filtering**
El filtrado colaborativo se basa en el hecho de que existen relaciones entre los productos y los intereses de las personas.
Muchos sistemas de recomendación utilizan filtros colaborativos para encontrar estas relaciones y dar una recomendación precisa de un producto que le puede gustar o interesar al usuario.
**Enfoques**
* Basado en el usuario se basa en la similitud o vecindario del usuario.
* Basado en elementos se basa en la similitud entre elementos.

**Basado en usuario**
En el filtrado colaborativo basado en usuarios, tenemos un usuario activo al que va dirigida la recomendación.
El motor de filtrado colaborativo primero busca usuarios que sean similares. Luego usa las calificaciones de estos usuarios similares para predecir las posibles calificaciones del usuario activo para una película que no había visto anteriormente.

En el enfoque basado en el usuario, la recomendación se basa en usuarios del mismo barrio con el que comparte preferencias comunes.
En el enfoque basado en artículos, artículos similares construyen vecindarios sobre el comportamiento de los usuarios.

El filtrado colaborativo es un sistema de recomendación muy eficaz. Sin embargo, también presenta algunos desafíos.
* Escasez de datos.
* El arranque en frío se refiere a la dificultad del sistema de recomendación tiene cuando hay un nuevo usuario,
y como tal aún no existe un perfil para ellos.
* La escalabilidad.
Hay algunas soluciones para cada uno de estos desafíos, como el uso de sistemas de recomendación basados en híbridos,
pero están fuera del alcance de este curso.

**Quiz**
Pregunta 1:
![Question 1](/home/ntamurejocolorado/Projects/Coursera/Machine-Learning-with-Python/Week_5/images/Image_3.png)
