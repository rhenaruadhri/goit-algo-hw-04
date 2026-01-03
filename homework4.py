def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                    cat = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat)
                except ValueError:
                    print(f"Неправильний формат рядка: {line}")

        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except IOError:
        print("Помилка при читанні файлу.")
        return []


# --- ШЛЯХ ДО ФАЙЛУ ---
file_path = r"C:\Users\olhab\OneDrive\Desktop\projects\repo\first_try\cats_file.txt"

# --- СТВОРЮЄМО ФАЙЛ З ДАНИМИ ---
with open(file_path, "w", encoding="utf-8") as file:
    file.write(
        "60b90c1c13067a15887e1ae1,Tayson,3\n"
        "60b90c2413067a15887e1ae2,Vika,1\n"
        "60b90c2e13067a15887e1ae3,Barsik,2\n"
        "60b90c3b13067a15887e1ae4,Simon,12\n"
        "60b90c4613067a15887e1ae5,Tessi,5\n"
    )

# --- ВИКОРИСТАННЯ ФУНКЦІЇ ---
cats_info = get_cats_info(file_path)
print(cats_info)