В WordPress CLI для добавления поста используется команда `wp post create`. Вот основные способы:

## Базовая команда
```bash
wp post create --post_title="Заголовок поста" --post_content="Текст поста"
```

## Основные параметры

```bash
# Создание поста с различными параметрами
wp post create \
  --post_title="Мой пост" \
  --post_content="Содержание поста" \
  --post_status=publish \
  --post_author=1 \
  --post_category=1,2 \
  --post_date="2024-01-15 10:00:00"
```

## Параметры статуса
```bash
# Опубликовать сразу
--post_status=publish

# Черновик
--post_status=draft

# Ожидает проверки
--post_status=pending
```

## Создание из файла
```bash
# Из текстового файла
wp post create --post_title="Пост из файла" < content.txt

# Указание файла с контентом
wp post create --post_title="Пост из файла" --post_content="$(cat content.txt)"
```

## Практические примеры

```bash
# Быстрое создание поста
wp post create --post_title="Быстрый пост" --post_status=publish

# Создание с категорией и тегами
wp post create \
  --post_title="Пост с категориями" \
  --post_content="Текст" \
  --post_category=1 \
  --tags="tag1,tag2" \
  --post_status=draft

# Создание с определенной датой
wp post create \
  --post_title="Запланированный пост" \
  --post_content="Текст" \
  --post_date="2024-12-31 23:59:59" \
  --post_status=future
```

## Полезные опции
- `--post_type` - тип записи (post, page, custom)
- `--post_excerpt` - краткое описание
- `--comment_status` - открыть/закрыть комментарии
- `--ping_status` - разрешить пинги
- `--post_password` - установить пароль

Для полного списка параметров используйте:
```bash
wp post create --help
```