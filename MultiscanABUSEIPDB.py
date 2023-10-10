import requests
import subprocess

# Tu clave de API de AbuseIPDB
api_key = 'TUAPI'

# Nombre del archivo que contiene las direcciones IP (cada IP en una línea)
file_name = 'lista_de_ips.txt'

# Nombre del archivo de resultados
output_file_name = 'resultado.txt'

# URL base de la API de AbuseIPDB
api_url = 'https://api.abuseipdb.com/api/v2/check'

# Abrir el archivo y leer las direcciones IP
with open(file_name, 'r') as file:
    ips = file.read().splitlines()

# Inicializar una lista para almacenar los resultados
results = []

# Realizar solicitudes a la API para cada IP en el archivo
for ip in ips:
    headers = {
        'Key': api_key,
    }
    
    params = {
        'ipAddress': ip,
    }

    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()
    
    # Agregar los resultados a la lista
    results.append(data)

# Abrir el archivo de resultados en modo escritura
with open(output_file_name, 'w') as output_file:
    # Escribir los resultados en el archivo
    for result in results:
        output_file.write(f'Dirección IP: {result["data"]["ipAddress"]}\n')
        output_file.write(f'Reputación: {result["data"]["abuseConfidenceScore"]}\n')
        output_file.write(f'Informes totales: {result["data"]["totalReports"]}\n')
        output_file.write(f'Último informe: {result["data"]["lastReportedAt"]}\n')
        output_file.write('---\n')

# Imprimir un mensaje de confirmación
print(f'Los resultados se han guardado en el archivo {output_file_name}')
# Comando que deseas ejecutar
comando = "cat resultado.txt | grep -B 1 -A 1 'Reputación: [1-9][0-9]*'"

# Ejecutar el comando y capturar la salida
resultado = subprocess.run(comando, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Verificar si la ejecución fue exitosa
if resultado.returncode == 0:
    # Imprimir la salida del comando
    print(resultado.stdout)
else:
    # En caso de error, imprimir el mensaje de error
    print("Error al ejecutar el comando:")
    print(resultado.stderr)
