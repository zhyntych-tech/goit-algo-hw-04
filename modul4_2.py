#Task2

from pathlib import Path

def get_cats_info(path):
    cat_list = []
        
    try:
        
        with open(path, 'r', encoding='utf-8') as file: 
            for line in file:
                if line.strip(): 
                    id, name, age = line.strip().split(',')
                    cat_dict = {
                        "id": id,
                        "name": name,
                        "age": age
                    }
                    cat_list.append(cat_dict)
        return cat_list
            
    except FileNotFoundError: 
        print("Файл не знайдено") 
        return [] 
        
    except (UnicodeDecodeError, ValueError): 
        print("Файл пошкоджений або має некоректний формат даних") 
        return []
