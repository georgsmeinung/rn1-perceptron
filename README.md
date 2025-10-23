## Redes Neuronales
### Práctica 1 - Perceptrón

### Objetivos 
El objetivo principal de esta práctica es comprender el funcionamiento del perceptrón como bloque de 
construcción elemental de las redes neuronales. Adicionalmente se realiza un repaso sobre el análisis y 
preprocesamiento de los datos. 

### Temas 
- Perceptrón. Entrenamiento
- Normalización y tratamiento de datos
- Correlación
- Representaciones Gráficas 

### Lectura 
Material de Lectura: Capítulo 13 del Libro Introducción a la Minería de Datos de Hernández Orallo

### Ejercicio 1 
La Tabla 1 muestra información correspondiente de pacientes para determinar si deben realizarse un 
examen médico en función de su edad, altura y riesgo médico.

<img width="334" height="403" alt="image" src="https://github.com/user-attachments/assets/038b6e1e-25c6-4c25-8a51-0777f2043039" />

Donde: 
- EDAD es un atributo numérico que indica la edad del paciente.
- RIESGO es el nivel de riesgo del paciente.
- EXAMEN indica si debe realizarse un examen extra. 
Para obtener transformar el atributo nominal RIESGO en uno 
numérico se lo numerizó de la siguiente forma: BAJO = 1, MEDIO = 2 y 
ALTO = 3.

a) Luego de la numerización se calculó el coeficiente de correlación lineal entre los atributos EDAD y RIESGO 
y se obtuvo como resultado -0.71. ¿Cómo debe interpretarse este valor? 

b) Luego de numerizar el atributo RIESGO y de normalizar los atributos de manera lineal entre 0 y 1, los 
ejemplos fueron utilizados para entrenar un perceptrón capaz de predecir correctamente el atributo 
EXAMEN. Los pesos obtenidos fueron los siguientes:  

**W(EDAD) = 0.0807   W(RIESGO) = 0.074   Sesgo o bias = -0.0742**

¿Cuál será la respuesta del perceptrón para los siguientes valores? 

**(EDAD, RIESGO)  =  (50, BAJO),  (51, MEDIO),  (54, ALTO)**

### Ejercicio 2 
Se busca predecir si el tipo de fármaco que se debe administrar a un paciente afectado de rinitis alérgica es 
el habitual o no. Se dispone de información correspondiente a las historias clínicas de pacientes atendidos 
previamente. Las variables relevadas son las siguientes:
- **Age**: Edad
- **Sex**: Sexo
- **BP (Blood Pressure)**: Presión sanguínea.
- **Cholesterol**: nivel de colesterol.
- **Na**: Nivel de sodio en la sangre.
- **K**: Nivel de potasio en la sangre.
- **Class**: Fármaco suministrado. Cada paciente ha sido medicado con un único fármaco de 5 posibles: DrugA, DrugB, DrugC, DrugX, DrugY

a) Utilice el archivo **drugs_train.csv** para entrenar un perceptrón que sea capaz de predecir si el tipo de 
fármaco que se debe administrar a un paciente afectado de rinitis alérgica es el habitual (suministro de 
DrugY) o no.  

b) Luego utilice el archivo **drugs_test.csv** para medir la calidad del modelo. 

c) Resuelva el problema: 
- numerizando los atributos ordinales utilizando dos representaciones diferentes: como entero único y de manera binaria (dummy).
- Normalizando de diferentes formas: Sin normalizar, normalización lineal, normalización con media y desvío

### Ejercicio 3 
El archivo **semillas.csv** contiene información de granos que pertenecen a tres variedades diferentes de trigo: 
Kama, Rosa y Canadiense. El total es de 210 ejemplos a razón de 70 ejemplos para cada tipo de grano, 
seleccionados al azar para el experimento. La información registrada corresponde al resultado de la 
visualización de alta calidad de la estructura interna del núcleo efectuada utilizando una técnica de rayos X 
blandos. Este tipo de estudio no es destructivo y es considerablemente más económico que otras técnicas 
de imagen más sofisticadas como la microscopía de barrido o la tecnología láser. Las imágenes se grabaron 
en placas KODAK de rayos x de 13x18 cm. Los estudios se realizaron utilizando granos de trigo cosechados 
combinados procedentes de campos experimentales, explorados en el Instituto de Agro física de la Academia 
Polaca de Ciencias en Lublin. Para construir los datos, se midieron siete parámetros geométricos de cada 
grano de trigo:

- i. área A
- ii. perímetro P
- iii. compacidad C = 4 * pi * A / P ^ 2
- iv. longitud del núcleo
- v. ancho del núcleo
- vi. coeficiente de asimetría
- vii. longitud del surco del núcleo

A partir de los 210 ejemplos, luego de normalizarlos utilizando los valores de media y desvío, se logró entrenar 
un perceptrón capaz de identificar, con una precisión del 100%, uno de los tres tipos de semillas. Para realizar 
el entrenamiento se utilizó una velocidad de aprendizaje de 0.05 y un máximo de 200 iteraciones. Indique 
cuál es el tipo de semilla que puede ser reconocido correctamente por un perceptrón.

### Ejercicio 4 
El archivo **zoo.csv** contiene información de 101 animales caracterizados por los siguientes atributos

- A1. Nombre del animal
- A2. Tiene Pelo
- A3. Plumas
- A4. Huevos
- A5. Leche
- A6. Vuela
- A7. Acuático
- A8. Depredador
- A9. Dentado
- A10. Vertebrado
- A11. Branquias
- A12. Venenoso
- A13. Aletas
- A14. Patas
- A15. Cola
- A16. Domestico
- A17. Tamaño gato
- A18. Clase

Salvo los atributos A1 y A18 que contienen texto y el A14 que contiene el número de patas del animal, el resto 
toma el valor 1 si el animal posee la característica y 0 si no. Hay 7 valores de clase posible (atributo A18): 
mamífero, ave, pez, invertebrado, insecto, reptil y anfibio.

a) Realice un gráfico que visualice de la cantidad de ejemplos por cada valor del atributo clase y analice que tipos de problema podrían surgir al entrenar un modelo para clasificación. 

b) Utilice todos los ejemplos para entrenar un perceptrón que sea capaz de reconocer si un animal es un mamífero. Entrene varias veces si es necesario y verifique que funcione correctamente. 

c) Observe los pesos del perceptrón entrenado en a) ¿Puede determinar cuáles son las características más  relevantes para decidir si se trata de un mamífero o no? Realice varias ejecuciones independientes y observe si las características más relevantes siguen siendo las mismas. 
d) Repita b) y c) para las aves. 
e) Repita b) y c) para los reptiles.

### Ejercicio 5 
El archivo **automobile-simple.csv** contiene 11 atributos de automóviles de un total de 205 registros. Es una versión modificada y simplificada del dataset disponible en el repositorio UCI https://archive.ics.uci.edu/ml/datasets/Automobile. La siguiente tabla contiene una breve descripción de los atributos que contiene el archivo y caracterizan a cada vehículo. 

<img width="1058" height="669" alt="image" src="https://github.com/user-attachments/assets/537b20e5-fb45-4472-9cbb-f0ca3d1529c9" />

a) Para cada atributo indique si es Discreto, Continuo, Nominal u Ordinal. 

b) Elimine los registros que presenten valores faltantes. 

c) Calcule la matriz de correlación usando los atributos numéricos. 

d) Realice el entrenamiento de un perceptrón para que aprenda a clasificar si un auto es ecológico. Tenga 
en cuenta los siguientes pasos: 

I. Utilice el atributo eco-rating para generar un nuevo atributo binario que determine si un auto es ecológico o no. Un auto es considerado ecológico si el valor de eco-rating supera la media de dicho atributo. 

II. Genere y compare 3 modelos utilizando diferentes normalizaciones (Sin normalizar, normalización lineal, normalización estándar. 

III. Teniendo en cuenta la matriz de correlación del punto c) repita el punto II) eliminando dos 
atributos fuertemente correlacionados (uno negativo y otro positivo). Compare y reflexione 
sobre los resultados obtenidos.
