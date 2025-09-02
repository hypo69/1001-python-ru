Dentro del directorio `game`, usando el contexto del archivo @life.py, crea un archivo con pruebas `test_life.py`. Usa el framework pytest.

La prueba debe verificar la correcta evolución de un oscilador simple "Blinker" (tres células en fila).

Escenario de prueba:
1.  Importa la clase `Game` de `life`.
2.  Crea una función de prueba, por ejemplo `test_blinker_oscillation`.
3.  Dentro de la prueba, crea una instancia `Game` con un tamaño fijo (por ejemplo, 5x5).
4.  Establece manualmente el estado inicial del campo para que haya una línea horizontal de tres células vivas (Blinker) en el centro.
5.  Llama al método `game.step()`.
6.  Usando `assert` y `numpy.array_equal`, verifica que el campo ha cambiado a una línea vertical de tres células.
7.  Llama al método `game.step()` de nuevo.
8.  Verifica que el campo ha vuelto a su estado horizontal original.