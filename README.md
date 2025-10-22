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
W(EDAD) = 0.0807         
W(RIESGO) = 0.074        
Sesgo o bias = -0.0742 

¿Cuál será la respuesta del perceptrón para los siguientes valores? 
(EDAD, RIESGO)  =  (50, BAJO),  (51, MEDIO),  (54, ALTO)

### Ejercicio 2 
Se busca predecir si el tipo de fármaco que se debe administrar a un paciente afectado de rinitis alérgica es 
el habitual o no. Se dispone de información correspondiente a las historias clínicas de pacientes atendidos 
previamente. Las variables relevadas son las siguientes:
- Age: Edad
- Sex: Sexo
- BP (Blood Pressure): Presión sanguínea.
- Cholesterol: nivel de colesterol.
- Na: Nivel de sodio en la sangre.
- K: Nivel de potasio en la sangre.
- Class: Fármaco suministrado. Cada paciente ha sido medicado con un único fármaco de 5 posibles: DrugA, DrugB, DrugC, DrugX, DrugY

a) Utilice el archivo drugs_train.csv para entrenar un perceptrón que sea capaz de predecir si el tipo de 
fármaco que se debe administrar a un paciente afectado de rinitis alérgica es el habitual (suministro de 
DrugY) o no.  

b) Luego utilice el archivo drugs_test.csv para medir la calidad del modelo. 

c) Resuelva el problema: 
- numerizando los atributos ordinales utilizando dos representaciones diferentes: como entero único y de manera binaria (dummy).
- Normalizando de diferentes formas: Sin normalizar, normalización lineal, normalización con media y desvío
