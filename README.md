Para crear el ejecutable instalamos

pip install pyinstaller

y luego hacemos:

pyinstaller --onefile calculadora.py


para crearlo y ademas que no aparesca la terminal y que se agregue el icono que le puse, usamos

pyinstaller --windowed --onefile --add-data "logo.ico:." block_de_notas.py


Si le quiero cambiar el icono que se muestra en escritorio hago esto y me sirve para cambiar el nombre del apk:

pyinstaller --windowed --onefile --icon=logo.ico --add-data "logo.ico;." --name "Block de Notas MF Dev" block_de_notas.py
