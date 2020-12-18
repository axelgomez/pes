# PES

Procesamiento Embebido de Señales
Departamento de Electrónica
Facultad Regional Avellaneda
Universidad Tecnológica Nacional

## Objetivos para aprobar la cursada
1. Desarrollar un algoritmo tal que detecte el contorno de hasta 3 imagenes dentro del dataset [BSDS 500](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html#bsds500)
2. El procedimiento de detección será sin supervisión or medio de funciones en OpenCV
   1. Algoritmo K-Means (OpenCV)
   2. Algoritmo SLIC (Simple Linear Iterative Clustering)
       1. RAG con corte por umbral
       2. RAG con corte normalizado
       3. RAG con Merge
   3. Algoritmo Felzenszwalb
       1. RAG con corte por umbral
       2. RAG con corte normalizado
       3. RAG con Merge
   4. Contadores de segmentos únicos segun cada algoritmo con su variante

## Objetivos para aprobar el final
1. Lograr que el algoritmo generalice mejor que el desarrollo anterior para detectar hasta 50 imagenes (y más si es posible) dentro del dataset [BSDS 500](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html#bsds500)
2. Terminar de probar metodologías actuales (estado del arte)
3. Embeber el algoritmo
   1. Compilar el entorno en la BeagleBone Black
   2. Probar el algoritmo
   3. Convertir el notebook a .py

Próximos pasos a futuro:
1. Levantar un webserver que espere por la foto
2. Procesar dicha foto e imprimir los resultados con cada algoritmo de segmentación
