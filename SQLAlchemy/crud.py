from sqlalchemy.orm import Session
from models import Author, Post, Comment
from datetime import datetime


def create_author(session: Session, name: str, email: str) -> Author:
    new_author = Author(name=name, email=email)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author


def get_author_by_email(session: Session, email: str) -> Author | None:
    return session.query(Author).filter(Author.email == email).first()


def create_post(session: Session, title: str, content: str, author_id: int, published: bool = True) -> Post:
    new_post = Post(title=title, content=content, author_id=author_id, published=published)
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post


def get_published_posts(session: Session, limit: int = 10) -> list[Post]:
    return session.query(Post).filter(Post.published == True).limit(limit).all()


def get_posts_by_author(session: Session, author_id: int, limit: int = 10) -> list[Post]:
    return session.query(Post).filter(Post.author_id == author_id).limit(limit).all()


def update_post_status(session: Session, post_id: int, published: bool) -> bool:
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return False
    post.published = published
    session.commit()
    return True


def add_comment(session: Session, post_id: int, author_name: str, text: str) -> Comment:
    new_comment = Comment(
        post_id=post_id,
        author_name=author_name,
        text=text
    )
    session.add(new_comment)
    session.commit()
    session.refresh(new_comment)
    return new_comment


def get_top_authors_by_posts(session: Session, limit: int = 3) -> list[tuple[str, int]]:
    from sqlalchemy import func, desc

    result = (
        session.query(
            Author.name,
            func.count(Post.id).label("post_count")
        )
        .join(Post)
        .group_by(Author.id)
        .order_by(desc("post_count"))
        .limit(limit)
        .all()
    )

    return result


# Задание 1
def find_authors_by_name(session: Session, name: str) -> list[Author]:
    return session.query(Author).filter(Author.name.ilike(f"%{name}%")).all()


# Задание 2
def published_posts_on_date(session: Session, date: datetime) -> list[Post]:
    from sqlalchemy import func, desc

    return session.query(Post).filter(
        Post.published == True,
        func.date(Post.created_at) == date.date()
    ).all()


# Задание 3
def create_authors(session: Session, authors: list[tuple[str, str]]) -> list[Author]:
    new_authors = [Author(name=name, email=email) for name, email in authors]
    session.add_all(new_authors)
    session.commit()
    for author in new_authors:
        session.refresh(author)
    return new_authors


# Задание 4
def get_post_with_comments(session: Session, post_id: int) -> Post | None:
    post = session.query(Post).filter(Post.id == post_id).first()

    if post is None:
        print("Пост не найден")
        return None

    print(f"Пост: {post.title}")
    print(f"Содержание: {post.content}")
    print(f"Автор: {post.author.name}")

    print("Комментарии:")
    if post.comments:
        for comment in post.comments:
            print(f"- {comment.author_name}: {comment.text}")
    else:
        print("Комментариев нет")

    return post