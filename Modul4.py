# Task1

from pathlib import Path

def total_salary(path):
    total_sum = 0 
    count = 0
    
    try:
       
        with open(Path(path), 'r', encoding='utf-8') as file: 
            for line in file:
                if line.strip(): 
                    name, salary = line.strip().split(',')
                    total_sum = total_sum + int(salary)
                    count += 1 
                    
        if count > 0: 
            avrg = total_sum / count 
            return total_sum, int(avrg)
        else:
            return 0, 0
            
    except FileNotFoundError: 
        print("Файл не знайдено") 
        return 0, 0 
        
    except (UnicodeDecodeError, ValueError): 
        print("Файл пошкоджений або має некоректний формат даних") 
        return 0, 0
