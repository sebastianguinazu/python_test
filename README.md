# Test de Python 

Esta es una breve prueba para chequear su conocimiento de Python. La prueba consta de levantar un dataset, realizar un análisis exploratorio, manipulación básica de variables, entrenar un modelo lineal e interpretar los resultados. Desde ya, está permitido (e incluso se recomienda) que busquen toda la información que necesiten en la web. Es decir, no se espera que sepan hacer todo, pero si que puedan hacer el ejercicio de buscar en internet y resolver lo que se pide. 

La forma de entrega es a través de una Notebook de Colab. Pueden ingresar directamente la [Pagina de Colab](https://colab.research.google.com/) o desde Google Drive. Para entregar, una opción es descargarla y enviarla por email o directamente dar acceso a sebastianguinazu@gmail.com. 

A continuación se detalla brevemente qué se espera en cada paso.

### 1. Levantar el dataset
Idealmente deberían clonar este repositorio de GitHub en su Notebook de Colab e importar la función `load_data` que se encuentra en el script `data_prueba.py` como un modulo. Una vez que hacen eso, puede crear el dataframe como `df = load_data()`. Si se les complica de esta forma, pueden copiar el contenido de `data_prueba.py` en una celda de la Notebook. Una tercera opción es levantarlo con `pd.read_csv(url)`, donde `url` debería ser igual a este [link](https://raw.githubusercontent.com/sebastianguinazu/python_test/main/wine.csv). El dataset es wine, un dataset de juguete de sklearn, pero en este caso con algunas adaptaciones menores para el ejercicio.

### 2. Análisis Exploratorio
En esta sección se busca que usen distintas funcionalidades de Python para explorar un dataset. No es necesario que se extiendan tanto, sino que hagan los chequeos principales que se suelen hacer para entender el dataset con el que se está trabajando y que demuestren el uso de las principales funciones y librerias de Python para ello (pandas, matplotlib, etc.).

### 3. Manipulación de variables
Acá se espera que hagan un tratamiento muy báscio de las variables para poder usar todas en el modelo sin perder observaciones. Algunas cuestiones importantes que se esperan son: no perder observaciones en el análisis, no utilizar información repetida, crear alguna variable como transformación de las existentes.

### 4. Modelo para Clasificar
En esta última sección se busca que entrenen un modelo para predecir y evaluén su capacidad predictiva. La variable que deben predecir es `target`. Pueden usar un Modelo Lineal o una Regresión Logística. No se extiendan mucho, la idea es que muestren conocimiento de los principales conceptos y librerías. Si pueden probar distintas alternativas y comentarlas brevemente, suma.
