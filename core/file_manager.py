from json import load, dump
import os

# path = ruta del archivo
def load_file(path):
    if not os.path.exists(path):
        # dir = folder
        # makedirs = make folders
        # os.path.dirname = extrae el nombre del folder de un path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as file:
            file.write('[]')
        return []
    else:
        with open(path, 'r') as file:
            return load(file)
    
def save_data(path, content):
    with open(path, 'w') as file:
        # dumb convierte de lista/objeto/etc a un texto y guarda en el archivo
        dump(content, file)

'''Formato JSON
{
    "key": "value"
}
o
["xd", "dwafaewf", 12213, "dasfadsgase", ["esfafaewfd"]]
'''