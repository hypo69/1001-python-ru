### `question_502.md`

**Вопрос 502.** Вы только что сделали коммит, но сразу поняли, что забыли добавить в него один важный файл. Какую последовательность команд следует использовать, чтобы добавить этот файл в *самый последний* коммит, не создавая при этом нового коммита в истории?

A. Сначала добавить забытый файл командой `git add <file>`, а затем выполнить `git commit --amend --no-edit`, чтобы обновить последний коммит.
B. Выполнить `git revert HEAD`, чтобы отменить последний коммит, а затем создать новый, правильный коммит.
C. Использовать `git update <file>` для прямого добавления файла в уже существующий коммит.
D. Создать новый коммит с этим файлом, а затем использовать `git merge HEAD~1`, чтобы объединить его с предыдущим.

**Правильный ответ: A**

**Объяснение:**

Для модификации самого последнего коммита в Git предназначена команда `git commit` с флагом `--amend`. Это позволяет "дополнить" или "исправить" предыдущий коммит, добавив в него новые изменения или изменив его сообщение.

*   **`git commit --amend`**: Эта команда берет все изменения, которые находятся в "staging area" (проиндексированные изменения), и объединяет их с изменениями из последнего коммита. Фактически, она не "изменяет" старый коммит, а **создает новый коммит, который заменяет предыдущий**.
*   **Флаг `--no-edit`**: Этот полезный флаг позволяет выполнить `amend` без открытия редактора для изменения сообщения коммита. Сообщение останется таким же, как и у "исправляемого" коммита.

**Разбор вариантов:**
*   **A.** Верно. Это стандартный и наиболее прямой способ решить поставленную задачу.
*   **B.** Неверно. `git revert` не изменяет историю, а создает *новый* коммит, который является "анти-коммитом" и отменяет изменения указанного коммита. Это не подходит для исправления ошибки в последнем коммите.
*   **C.** Неверно. Команды `git update` для этой цели не существует, это вымышленный вариант.
*   **D.** Неверно. Этот подход излишне сложен и приведет к созданию лишних коммитов слияния, засоряя историю.

*   **Ключевой аспект 1: Перезапись истории:** `git commit --amend` является командой, которая *перезаписывает историю*. Это означает, что хеш замененного коммита изменится. Поэтому её следует использовать только для локальных коммитов, которые еще не были отправлены (`push`) в общий репозиторий.
*   **Ключевой аспект 2: Staging Area:** Перед вызовом `git commit --amend` необходимо добавить нужные изменения в staging area с помощью `git add`. Команда `amend` работает именно с этими проиндексированными изменениями.

**Пример:**

```bash
# Создаем и добавляем первый файл
echo "content1" > file1.txt
git add file1.txt
git commit -m "Add file1"

# Осознаем, что забыли добавить второй файл
echo "content2" > file2.txt

# Добавляем забытый файл в staging area
git add file2.txt

# Используем --amend, чтобы добавить file2.txt в последний коммит, сохраняя старое сообщение
git commit --amend --no-edit

# Проверяем историю. Мы увидим только ОДИН коммит, содержащий оба файла.
git log --oneline --stat
# Вывод будет примерно таким (с другим хешем):
# a1b2c3d (HEAD -> main) Add file1
#  file1.txt | 1 +
#  file2.txt | 1 +
```

**В результате:**

Самый правильный и прямой способ добавить забытый файл в последний коммит — это использовать `git add`, а затем `git commit --amend`.

Таким образом, вариант A является правильным.