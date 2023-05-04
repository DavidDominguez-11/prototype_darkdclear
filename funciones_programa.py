import os
import datetime
import zipfile


"""
Podemos probar esto, pero no es seguro que funcione
# Obtener la ruta de la carpeta Documentos en Windows
if os.name == 'nt':
    documents_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')

    # Comprobar si la carpeta de Documentos existe en la ruta predeterminada del sistema
    if not os.path.exists(documents_path):
        # Si no existe, buscar la carpeta de Documentos en la ruta del usuario
        for root, dirs, files in os.walk(os.environ['USERPROFILE']):
            if 'Documents' in dirs:
                documents_path = os.path.join(root, 'Documents')
                print(documents_path)
                break

# Obtener la ruta de la carpeta Documentos en Mac
if os.name == 'posix':
    documentos_path = os.path.join(os.path.expanduser('~'), 'Documents')
    print(documentos_path)
"""


def add_backslash(ruta):
    """
    Agrega un carácter de barra diagonal inversa adicional después de cada barra diagonal inversa en una cadena
    """
    new_path = ""
    for char in ruta:
        if char == "\\":
            new_path += "\\"
        else:
            new_path += char
    return new_path
#print(neww_path)

def split_name(name):
    split_name = name.split(" ")
    new_name = split_name[0]
    #print(new_name)
    return new_name


def cosa(ruta):
    lista_archivos = []
    lista_ordenada = []
    neww_path = add_backslash(ruta)

    # Recorre todos los archivos en el directorio
    for filename in os.listdir(neww_path):
        filepath = os.path.join(neww_path, filename)
        if os.path.isfile(filepath):
            # Obtiene la fecha de creación y modificación del archivo
            created = os.path.getctime(filepath)
            modified = os.path.getmtime(filepath)
            # Los convierte a objetos datetime
            created_datetime = datetime.datetime.fromtimestamp(created)
            modified_datetime = datetime.datetime.fromtimestamp(modified)
            # Imprime la información del archivo
            print("Archivo:", filename)
            print("Fecha de creación:", created_datetime)
            print("Fecha de modificación:", modified_datetime)

            # Compara la fecha si han pasado 6 meses
            now = datetime.datetime.now()
            six_months_ago = now - datetime.timedelta(days=180)
            if modified_datetime < six_months_ago:
                temp_disc = {}
                date = str(modified_datetime)
                #print("Temp needed", date)
                temp_disc[filename] = split_name(date)
                lista_archivos.append(temp_disc)
                print("------------------------")
            else:
                print("No han pasado 6 meses")
                print("------------------------")

    #for i in range(len(lista_archivos)):
        #print(lista_archivos[i])
        #print("------------------------")

    lista_ordenada = sorted(lista_archivos, key=lambda x: datetime.datetime.strptime(list(x.values())[0], '%Y-%m-%d'))
    print(lista_ordenada)
    for i in range(len(lista_ordenada)):
        print(lista_ordenada[i])
        print("------------------------")

    return (lista_ordenada, neww_path, True) if len(lista_ordenada)>0 else (lista_ordenada, neww_path, False)

def eliminar(lista_ordenada, neww_path, i):
    try:
        archivo = list(lista_ordenada[i].keys())[0]
        filepath = os.path.join(neww_path, archivo)
        os.remove(filepath)
        print(f"Archivo eliminado: {archivo}")
    except Exception as e:
        print(e)

def comprimir(lista_ordenada, neww_path, i):
        print(i)
        # comprimir archivos
        # Crear zip
        nombre_archivo = list(lista_ordenada[i].keys())[0]
        zip_filename = list(lista_ordenada[i].keys())[0]
        if not zip_filename.endswith(".zip"):
            zip_filename += ".zip"
        zip_filepath = os.path.join(neww_path, zip_filename)
        zip_obj = zipfile.ZipFile(zip_filepath, 'w')
        # agregar al archivo zip
        zip_obj.write(os.path.join(neww_path, nombre_archivo), arcname=nombre_archivo)
        # eliminar el archivo seleccionado
        os.remove(os.path.join(neww_path, nombre_archivo))
    # Cerrar el zip
        zip_obj.close()
    