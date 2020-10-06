# Hands On Lab: COMPUTER VISION

## 1. Introducción

Gracias a IBM Research, en este laboratorio se aprenderá acerca de la IBM'S Adversarial Robustness Toolbox, y se utilizará para mitigar los ataques simulados de los piratas informático.

## 2. Desarrollo

Se siguen los pasos que se marca en la práctica. En primer lugar, se selecciona una imagen de las 5 que hay y podemos visualizar la precisión y confianza con la que Watson identifica lo que es, como podemos ver en la imagen adjunta.

![queso][1]![cat][2]![bombilla][3]

[1]:/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/queso.png
[2]:/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/cat.png
[3]:/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/bombilla.png

En estas imágenes todos los slider de atacantes están desactivados.

En la siguiente imagen, hemos elegido un tipo de ataque y lo hemos dejado en nivel bajo, como vemos en el caso del gato el porcentaje de precisión baja considerablemente. Igual que en otro casos.

![atque1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/ataque_1.png)

El siguiente paso es activar la defensa. Cuando se hace esto se puede observar que a mayor ruido o suavizado mayor es el porcentaje de acierto. Esto es debido a que los detalles de la foto disminuyen generando figuras más suavizadas, lo que ayuda a distinguir las partes más importantes de la image.

![solucion1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/porcentaje_1.png)

![solucion2](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/porcentaje_2.png)

Contesta a las preguntas:
1. Mueva el control deslizante de Ruido Gaussiano a medio y luego a alto. Para cada nivel, observe con qué identifica Watson la imagen y en qué nivel de confianza. ¿Mejoró el reconocimiento de imágenes?

![solucion1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/bajo.png)

![solucion2](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/alto.png)

En ninguno de los casos mejorar el reconocmiento del gato siames, lo confunde con un gato egipcio.

2. Mueva el control deslizante de Ruido gaussiano a Ninguno.
Esta pregunta relacionándola con al anterior, se puede ver que la confianza del resultado está ligada al grado de ataque. A mayor ataque y mayor ruido gaussiano menor probabilidad de acierto.

3. En la sección Defender ataque, mueva el control deslizante Suavizado espacial a bajo. ¿Cómo identifica Watson la imagen como ahora y con qué nivel de confianza? ¿Mejoró el reconocimiento de imágenes?
![solucion1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/suavizado_bajo.png)

Se aprecia claramente que sube el porcentaje, pero sigue indicando que es un gato egipcion; cuando elevamos el suavizado a medio y alto es cuando lo clasifica correctamente como siames.

4. En la sección Defend attack, mueva el control deslizante Feature Squeezing a bajo. ¿Cómo identifica Watson la imagen como ahora y con qué nivel de confianza? ¿Mejoró el reconocimiento de imágenes?

![solucion1](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/squeezing_bajo.png)

![solucion2](/home/ntamurejocolorado/Projects/Coursera/Introduction-to-AI/Week_2/images/squeezing_alto.png)

En este caso, si lo ponemos en un nivel bajo, no hace nada ni mejora el porcentaj ni lo clasifica correctamente. Mientras que si lo elevamos sí que lo clasifica correctamente.

En conclusión, se puede decir que "defend attack" es mejor cuanto mayor es el valor, pero hay que tener cuidado ya que dependiendo del tipo que se escoja puede que el resultado no sea el esperado.

## 3. Preguntas
a. ¿Puedes colocar una puerta en el cielo?

No, he intentado colocar objetos en lugares no apropiados y donde no es lógico que puedan estar, como es el caso de una puerta en el cielo o cesped en el cielo, y no hace nada, no lo dibuja.

b. ¿Se puede añadir cesped encima del cesped ya existente?
Esto tampoco se puede hacer, y no hace nada.

Para más información revisar el documento de Interesting_Links.md
