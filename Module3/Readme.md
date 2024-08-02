
3.1. Section 1 – Making decisions in Python
Ласкаво просимо до третього модуля! У першому розділі ми дізнаємося про умовні оператори та як їх використовувати для прийняття рішень у Python.
3.1.1 Запитання та відповіді

Програміст пише програму, а програма задає запитання .

Комп'ютер виконує програму і дає відповіді . Програма повинна вміти реагувати відповідно до отриманих відповідей .

На щастя, комп’ютери знають лише два типи відповідей:

так, це правда;
ні, це неправда.
Ви ніколи не отримаєте відповідь на кшталт « Дайте мені подумати....» , «Я не знаю » або «Напевно так», але я не знаю напевно» .

Щоб ставити запитання, Python використовує набір дуже спеціальних операторів . Давайте переглянемо їх один за одним, проілюструвавши їх вплив на кількох простих прикладах.
3.1.2 Порівняння: оператор рівності
Запитання: чи рівні дві величини ?

Щоб поставити це запитання, ви використовуєте==(рівно рівно) оператор.

Не забувайте про цю важливу відмінність:

=є оператором присвоювання , наприклад, a = bприсвоює aзі значенням b;
==питання, чи рівні ці значення? тому a == b порівнює a і b.
Це бінарний оператор із лівостороннім зв’язуванням . Він потребує двох аргументів і перевіряє, чи вони рівні .
Лівостороннє та Правостороннє Зв'язування
Лівостороннє зв'язування (Left-Associative) означає, що операції виконуються зліва направо. Якщо кілька операторів з однаковим пріоритетом знаходяться поруч, вони обробляються зліва направо.

Правостороннє зв'язування (Right-Associative) означає, що операції виконуються справа наліво. Оператори з однаковим пріоритетом обробляються справа наліво.

Приклади Лівостороннього Зв'язування
Більшість операторів у Python мають лівостороннє зв'язування. Розглянемо приклад з оператором додавання:

python
Копіювати код
5 - 3 + 2
Тут операції будуть виконуватись зліва направо:

Спочатку виконується 5 - 3, результатом буде 2.
Потім виконується 2 + 2, результатом буде 4.
Тобто, вираз 5 - 3 + 2 інтерпретується як (5 - 3) + 2.

Приклади Правостороннього Зв'язування
Деякі оператори, такі як оператор присвоєння та оператор піднесення до степеня, мають правостороннє зв'язування. Розглянемо приклад з оператором піднесення до степеня:

python
Копіювати код
2 ** 3 ** 2
Тут операції будуть виконуватись справа наліво:

Спочатку виконується 3 ** 2, результатом буде 9.
Потім виконується 2 ** 9, результатом буде 512.
Тобто, вираз 2 ** 3 ** 2 інтерпретується як 2 ** (3 ** 2).

Лівостороннє Зв'язування в Операторах Присвоєння
Розглянемо приклад з операторами присвоєння:

python
Копіювати код
a = b = c = 1
Тут операції виконуються справа наліво:

Спочатку виконується c = 1.
Потім виконується b = c, де c вже має значення 1.
Нарешті, виконується a = b, де b вже має значення 1.
Таблиця Пріоритетів Операторів у Python
Для кращого розуміння, наведемо спрощену таблицю пріоритетів операторів у Python з урахуванням зв'язування:
![img.png](img.png)
Оператор	Опис	Пріоритет	Зв'язування
**	Піднесення до степеня	Високий	Правостороннє
*, /, //, %	Множення, ділення, модуль	Середній	Лівостороннє
+, -	Додавання, віднімання	Середній	Лівостороннє
<<, >>	Зсув	Середній	Лівостороннє
<, <=, >, >=	Порівняння	Низький	Лівостороннє
==, !=	Рівність, нерівність	Низький	Лівостороннє
=	Присвоєння	Низький	Правостороннє
+=, -=, *=, /=, **=	Присвоєння з операцією	Низький	Правостороннє
Висновок
Лівостороннє зв'язування означає, що операції виконуються зліва направо. Приклад: 5 - 3 + 2.
Правостороннє зв'язування означає, що операції виконуються справа наліво. Приклад: 2 ** 3 ** 2.
Знання про зв'язування операторів є важливим для розуміння та правильного використання виразів у Python, особливо коли вирази стають складними.

3.1.3 Вправи
А тепер задамо кілька запитань. Спробуйте вгадати відповіді.

Питання №1 : Який результат наступного порівняння?

2 == 2

Перевірте
Правда- звичайно, 2 дорівнює 2. Python відповістьПравда(запам'ятайте цю пару попередньо визначених літералів,Правдаіпомилковий- це також ключові слова Python).


Запитання №2 : Який результат наступного порівняння?

2 == 2.

Перевірте
Це питання не таке просте, як перше. На щастя, Python може перетворити ціле число в його дійсний еквівалент, і, отже, відповідь така:Правда.

Запитання №3 : Який результат наступного порівняння?

1 == 2

Перевірте
Це повинно бути легко. Відповідь буде (вірніше, завжди)помилковий.

3.1.4 Оператори
Рівність: оператор дорівнює ( == )
The==Оператор (дорівнює) порівнює значення двох операндів. Якщо вони рівні, результат порівняння єПравда. Якщо вони не рівні, результат порівняння єпомилковий.

Подивіться на порівняння рівності нижче – який результат цієї операції?


var == 0
 
Зауважте, що ми не можемо знайти відповідь, якщо не знаємо, яке значення наразі зберігається у зміннійвар.

Якщо змінна змінювалася багато разів під час виконання вашої програми або її початкове значення вводиться з консолі, відповідь на це питання може дати тільки Python і тільки під час виконання.

А тепер уявіть програміста, який страждає від безсоння, і йому доводиться окремо рахувати чорних і білих овець, якщо чорних овець рівно вдвічі більше, ніж білих.

Питання буде наступним:


black_sheep == 2 * white_sheep
 
Через низький пріоритет==оператор, питання розглядається як еквівалентне цьому:


black_sheep == (2 * white_sheep)
 
Отже, давайте попрактикуємося у вашому розумінні==оператор зараз – чи можете ви вгадати результат коду нижче?

play_arrow
sync
download
light_mode
dark_mode



Console 
terminal
sync
True
False
Запустіть код і перевірте, чи ви маєте рацію.

Нерівність: оператор не дорівнює ( != )
The!=Оператор (не дорівнює) також порівнює значення двох операндів. Ось різниця: якщо вони рівні, результат порівняння єПомилковий. Якщо вони не рівні, результат порівняння єПравда.

Тепер подивіться на порівняння нерівностей нижче – чи можете ви вгадати результат цієї операції?


var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)
 
Запустіть код і перевірте, чи ви маєте рацію.

Оператори порівняння: більше
Ви також можете задати порівняльне запитання за допомогою>(більше ніж) оператор.

Якщо ви хочете дізнатися, чи чорних овець більше, ніж білих, ви можете написати це так:


black_sheep > white_sheep  # Greater than
 
Правдапідтверджує це;помилковийзаперечує це.

Оператори порівняння: більше або дорівнює
Оператор більше має ще один спеціальний, нестрогий варіант, але він позначається інакше, ніж у класичній арифметичній нотації:>=(більше або дорівнює).

Є дві наступні ознаки, а не одна.

Обидва ці оператори (суворий і нестрогий), а також два інших, розглянуті в наступному розділі, є двійковими операторами з лівостороннім прив’язуванням , і їхній пріоритет більший, ніж показаний==і!=.

Якщо ми хочемо дізнатися, чи потрібно нам носити теплу шапку, ми задаємося наступним питанням:


centigrade_outside >= 0.0  # Greater than or equal to
 
Оператори порівняння: менше/менше або дорівнює
Як ви, напевно, вже здогадалися, у цьому випадку використовуються такі оператори: the<(менше) оператор і його нестрогий брат:<=(менше або дорівнює).

Подивіться на цей простий приклад:


current_velocity_mph < 85  # Less than
current_velocity_mph <= 85  # Less than or equal to
 
Перевіримо, чи є ризик бути оштрафованим ДАІ (перше питання суворе, друге – ні).


3.1.5 Використання відповідей
Що можна зробити з відповіддю (тобто результатом операції порівняння), отриманою з комп’ютера?

Є принаймні дві можливості: по-перше, ви можете запам’ятати його ( зберегти в змінній ) і використати пізніше. Як ти це робиш? Ну, ви використовуєте довільну змінну так:


answer = number_of_lions >= number_of_lionesses
 
Вміст змінної підкаже відповідь на поставлене запитання.

Другий варіант більш зручний і набагато поширеніший: ви можете використовувати отриману відповідь, щоб прийняти рішення про майбутнє програми .

Для цього потрібна спеціальна інструкція, і ми її обговоримо найближчим часом.

Тепер нам потрібно оновити нашу таблицю пріоритетів і додати в неї всі нові оператори. Тепер це виглядає так:

![img_1.png](img_1.png)