import strawberry
from typing import List
from . import models

@strawberry.type
class AuthorType:
    id: int
    name: str
@strawberry.django.type(models.Post)
class BlogPostType:
    id: int
    title: str
    author: AuthorType
    content: str