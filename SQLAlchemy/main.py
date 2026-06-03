from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String

load_dotenv('.env')
from database import SessionLocal, engine, Base
from models import Author, Post, Comment
from crud import *

def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        print("Начинаем тестирование")
        print("Создаем авторов")
        author1 = create_author(session, "Анна Петрова", "anna@example.com")
        author2 = create_author(session, "Иван Сидоров", "ivan@example.com")
        print(f"{author1.name} (id={author1.id})")
        print(f"{author2.name} (id={author2.id})\n")

        print("Создаем посты")
        post1 = create_post(session, "Первый пост", "Это содержание первого поста. Оно достаточно длинное.", author1.id,
                            published=True)
        post2 = create_post(session, "Черновик", "Этот пост пока не опубликован.", author1.id, published=False)
        post3 = create_post(session, "Пост Ивана", "Текст от Ивана.", author2.id, published=True)
        print(f"'{post1.title}' (опубликован)")
        print(f"'{post2.title}' (черновик)")
        print(f"'{post3.title}' (опубликован)\n")

        print("Добавляем комментарии...")
        add_comment(session, post1.id, "Читатель1", "Отличная статья, очень полезно!")
        add_comment(session, post1.id, "Читатель2", "Спасибо за материал, жду продолжения.")
        add_comment(session, post1.id, "Аноним", "Коротко.")

        print("3 комментария добавлены к первому посту\n")

    print("Публикуем черновик...")
    success = update_post_status(session, post2.id, published=True)
    if success:
        print(f"'{post2.title}' теперь опубликован\n")

    print("📰 Все опубликованные посты:")
    published = get_published_posts(session)
    for post in published:
        print(f"'{post.title}' — автор: {post.author.name}")
    print()

    print("🏆 Топ авторов по количеству постов:")
    top_authors = get_top_authors_by_posts(session, limit=3)
    for rank, (name, count) in enumerate(top_authors, 1):
        print(f"{rank}. {name}: {count} пост(ов)")
    print()

    print("Поиск автора по email...")
    found = get_author_by_email(session, "anna@example.com")
    if found:
        print(f"Найдено: {found.name}")
    else:
        print("Автор не найден")

        # Задание 1: Поиск автора по имени
    print("\nTask 1. Поиск автора по имени:")
    authors_by_name = find_authors_by_name(session, "Анна")
    if authors_by_name:
        for author in authors_by_name:
            print(f"Найден автор: {author.name}, email: {author.email}")
    else:
        print("Авторы не найдены")

        # Задание 2: Опубликованные посты за определенную дату
    print("\nTask 2. Опубликованные посты за дату:")

    posts_on_date = published_posts_on_date(session, post1.created_at)

    if posts_on_date:
        for post in posts_on_date:
            print(f"Пост: {post.title}, дата: {post.created_at}")
    else:
        print("Опубликованных постов за эту дату нет")

    # Задание 3: Добавление сразу нескольких авторов
    print("\nTask 3. Добавление нескольких авторов:")

    new_authors = create_authors(session, [
        ("Мария Иванова", "maria@example.com"),
        ("Петр Смирнов", "petr@example.com")
    ])

    for author in new_authors:
        print(f"Добавлен автор: {author.name}, email: {author.email}")

        # Задание 4: Пост с комментариями
        print("\nTask 4. Пост с комментариями:")

        get_post_with_comments(session, post1.id)

    except Exception as e:(
        print(f"Ошибка: {e}"))
        session.rollback()

    finally:
        session.close()
        print("\nТестирование завершено. Сессия закрыта.")

if __name__ == "__main__":
    main()

