# Bot de Clips
Este es un bot que recopila clips que se han puesto previamente pasador por un canal de discord  
En el caso de que el mensaje con los links se envié con más de 2000 caraceres (el limite de discord por mensaje) se mandara como fichero de texto   
## Instrucciones
### Descargar python  
La version con la que se ha hecho es con la version 3.11  
Para **Windows** se puede descargar desde la pagina de [python](https://www.python.org/)  
Para **Linux** usando el administrador de paquetes de la distribución, por ejemplo en arch seria:
```bash
sudo pacman -S python
```
### Descargar la api de discord para python, para ello:
Para ello, hay que ir abrir una consola tanto en windows como en linux
```bash
pip install discord
```
### Crear bot de discord  
Dejo aqui un link de la documentacion de discord porque use uno que habia hecho hace tiempo y no me acuerdo como ajusté los permisos
https://discord.com/developers/docs/getting-started  

### Establecer el Token
Introducir el token en la variable "my_token" del archivo "my_token.py"
El token solo se debe de compartir con aquellos en los que confies, piensa que ese token se podria usar para que ejecute otros programas

### Ejecutar el archivo bot.py 
Ya sea con doble click o usando en la ruta del directorio el comando
```bash
python bot.py
```
### Escribir el comando "!clip" para probarlo  
Si se quiere cambiar el limite de mensajes, hay que ajustar la constante "LIMIT" en la funcion "clips()"  
Si se quiere cambiar el comando, cambiar clips de "name = clips" por la palabra que se quiera  
Si lo que se quiere es cambiar el prefijo, en "command_prefix"