Ejercicio 4 ubicado en ./coap-client/ejercicio4.py

Ejercicio 5 ubicado en ./mosquitto-publisher/ejercicio5.py

Ambos simulan la lectura desde un sensor de temperatura y lo escriben en una base de datos influxdb

# Trabajo hecho
- Parado en el root del proyecto, ejecutar docker compose up. Esto levantara todo el ecosistema definido en el archivo de docker compose. Mediante telegraf creo una base de datos con mi nombre: matias_cicchitti al comenzar la ejecucion
- Cree un CLI para poder interactuar con el servidor de coap. En el archivo del ejercicio 4 hay un ejemplo de como usarla. Si se ejecuta el archivo, se insertaran cada 10 segundos las medidas en la bd "matias_cicchitti", en la measure "climate"
- Cree la imagen correspondiente al servidor coap usando la libreria CoAPthon
- Al iniciar, se crea un broker de mosquitto. Con telegraf se crea una suscripcion automatica al topic "temperatura". Ver telegraf.conf
- En el archivo del ejercicio 5, usando una liberia de mosquitto se realizan las publicaciones al topico previamente citado. Las publicaciones realizadas en ese topico se terminan guardando en la measure "climate" de la base de datos "matias_cicchitti". Es decir, tanto las requests de coap como las publicaciones de mosquitto se guardan en el mismo lugar.
- Hay algunos archivos de pruebas con cURL que quizas haya que modificar para que funcionen
- Modificar el archivo de docker compose para usar una network, agregando la inicializacion de los containers y configuraciones necesarias y ademas actualice la version de telegraf para que soporte json_v2

# Todo
- Hacer que los clientes y servers de coap se intercambien json en lugar del payload que es compliant con influxdb
- Seguir mejorando el resto de las cosas
- Poner mas ejemplos
