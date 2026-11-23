# Identificadores y comandos de despliegue

## 1. Identificadores de los recursos

Los recursos utilizados para desplegar el servicio Flask en Amazon EC2 fueron los siguientes:

| Recurso | Identificador o valor |
|---|---|
| Instancia EC2 | `i-0cf01fbe645400cdd` |
| Dirección IP pública utilizada para SSH | `54.224.215.150` |
| Imagen AMI | `ami-0d27e0fb3bac4d724` |
| Tipo de instancia | `t2.micro` |
| Clave SSH | `claveayoze-ec2` |
| Grupo de seguridad | `sg-0f60b80757b277e03` |
| Perfil IAM de instancia | `LabInstanceProfile` |
| Bucket S3 | `ayoze-p3-cloud` |
| Archivo descargado desde S3 | `artifacts/webservice.zip` |

## 2. Creación del grupo de seguridad

El grupo de seguridad utilizado fue `sg-0f60b80757b277e03`. La creación de un grupo de seguridad se realiza brevemente con el siguiente comando:

```bash
aws ec2 create-security-group \
  --group-name <nombre-del-grupo> \
  --description "Grupo de seguridad para la instancia Flask"
```

## 2. Creación de la instancia EC2

La instancia se creó con la AMI, el tipo de instancia, la clave, el grupo de seguridad y el perfil IAM indicados anteriormente:

```bash
aws ec2 run-instances \
  --image-id ami-0d27e0fb3bac4d724 \
  --instance-type t2.micro \
  --key-name claveayoze-ec2 \
  --security-group-ids sg-0f60b80757b277e03 \
  --iam-instance-profile Name=LabInstanceProfile
```

El identificador obtenido para la instancia fue `i-0cf01fbe645400cdd`.

## 4. Acceso a la instancia

El acceso remoto a la instancia se realizó mediante SSH utilizando su dirección IP pública:

```bash
ssh -i claveayoze-ec2.pem ec2-user@54.224.215.150
```

> La ejecución se realizó sobre la instancia identificada como `i-0cf01fbe645400cdd`. El nombre exacto del archivo local de la clave puede depender de cómo estuviera guardada en el entorno de trabajo.

## 5. Descarga del código desde Amazon S3

Una vez dentro de la instancia, se descargó el paquete de la aplicación desde el bucket S3:

```bash
aws s3 cp s3://ayoze-p3-cloud/artifacts/webservice.zip .
```

Después se descomprimió el paquete:

```bash
unzip webservice.zip
```

## 6. Configuración y arranque del servicio Flask

Se utilizaron las operaciones de `systemctl` para habilitar el arranque automático, iniciar el servicio y comprobar su estado:

```bash
sudo systemctl enable webservice
sudo systemctl start webservice
sudo systemctl status sebservice
```

## 7. Finalización y limpieza de recursos

Al finalizar las pruebas se terminó la instancia EC2 utilizando su identificador:

```bash
aws ec2 terminate-instances --instance-ids i-0cf01fbe645400cdd
```

Esta acción dejó la instancia marcada para terminación y evitó mantener activo el recurso una vez finalizada la práctica.

## 8. Resumen de la secuencia

1. Creación de la instancia EC2 con la AMI `ami-0d27e0fb3bac4d724`.
2. Acceso mediante SSH a `54.224.215.150`.
3. Descarga de `s3://ayoze-p3-cloud/artifacts/webservice.zip`.
4. Descompresión de `webservice.zip`.
5. Habilitación, arranque y comprobación del servicio Flask mediante `systemctl`.
6. Terminación de la instancia `i-0cf01fbe645400cdd` al finalizar.

