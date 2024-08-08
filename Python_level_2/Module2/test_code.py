import gettext
import locale

# Встановлюємо локаль
locale.setlocale(locale.LC_ALL, '')

# Встановлюємо каталог з перекладами
localedir = 'locale'
lang = gettext.translation('myapp', localedir, languages=['es'])
lang.install()

# Використовуємо функцію _() для перекладу
print(_('Hello, World!'))
