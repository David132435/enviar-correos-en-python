  ## Como Usar
El Script por defecto no envía ningún mail.  

Antes de usar el script es necesario configurar la cuenta que vamos a usar para mandar los mails. Por eso, hace falta rellenar el valor de las variables username, password, from_email.  
Nota: \(El valor de username y from_email será el mismo\)  

Una vez rellenadas las variables correctamente, el script tiene una función llamada send_email que requiere tres argumentos: email de destino, asunto y mensaje.

Un ejemplo de mail sería send_email(correodedestino@gmail.com, "Este es el asunto del mensaje", "Este es el cuerpo del mensaje")  

También se puede importar desde otro script y hacer uso de la función.

  
