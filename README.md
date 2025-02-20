“Algoritmos de búsqueda y modularización “
Este proyecto compara dos métodos de búsqueda en una lista grande de usuarios: 
Búsqueda lineal  (Recorre uno por uno)
Búsqueda binaria (más eficiente en listas ordenadas)

El código mide el rendimiento de cada método al buscar un usuario en 100,000 registros

¿Cómo funciona el codigo?
•	El programa genera 1000000 usuarios aleatorios asignándoles un ID, nombre y edad.
•	Selecciona un ID aleatorio para buscar
•	Ejecuta ambos métodos de búsqueda 
•	Mide el tiempo de ejecución de ambos métodos y compara los resultados 

Características 
•	Genera 1000000 usuarios aleatorios con nombre, edad e ID
•	Implementa los dos tipos de búsqueda que son lineal y binaria
•	Se hace uso de timeit para medir el rendimiento de cada método.
•	Utiliza el bisect para optimizar la búsqueda binaria
