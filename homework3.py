def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                name, salary = line.split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total // count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0


# --- ШЛЯХ ДО ФАЙЛУ ---
file_path = r"C:\Users\olhab\OneDrive\Desktop\projects\repo\first_try\salary_file.txt"

# --- СТВОРЮЄМО ФАЙЛ З ДАНИМИ ---
with open(file_path, "w", encoding="utf-8") as file:
    file.write(
        "Alex Korp,3000\n"
        "Nikita Borisenko,2000\n"
        "Sitarama Raju,1000\n"
    )

# --- ВИКОРИСТАННЯ ФУНКЦІЇ ---
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")