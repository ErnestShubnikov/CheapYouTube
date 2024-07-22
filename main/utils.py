import os
import random
import string

def generate_random_filename(instance, filename):
    ext = filename.split('.')[-1].lower()  
    valid_extensions = ['mp4', 'avi', 'mov']  
    
    if ext not in valid_extensions:
        return ValueError('Недопустимое расширение файла. Допустимые расширения: mp4, avi, mov')
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    new_filename = f"{random_name}.{ext}"  
    return os.path.join('main/video/', new_filename)


def generate_random_photo(instance, filename):
    ext = filename.split('.')[-1].lower()
    valid_extensions = ['jpg', 'png', 'jpeg','ico', 'raw']  
    if ext not in valid_extensions:
        return ValueError('Недопустимое расширение файла. Допустимые расширения: jpg, png, jpeg, ico, raw')
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    new_filename = f"{random_name}.{ext}"  
    return os.path.join('main/photo/', new_filename)