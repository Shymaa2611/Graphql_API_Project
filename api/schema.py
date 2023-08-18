import strawberry
from typing import List
from .models import Author,Post
from .types import BlogPostType,AuthorType


# Query
# GET or READ
@strawberry.type
class Query:
    @strawberry.field
    def posts(self, title: str = None) -> List[BlogPostType]:
        if title:
            blog = Post.objects.filter(title=title)
            return blog
        return Post.objects.all()

    @strawberry.field
    def postsByLimit(self,limit: int=None) -> List[BlogPostType]:
        blogs = Post.objects.all()[0:limit]
        return blogs

@strawberry.input
class AuthorInput:
    id: int 
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_post(self, title: str, author: AuthorInput, content: str) -> BlogPostType:
        author_instance = Author.objects.get(id=author.id)  
        blog = Post(title=title, author=author_instance, content=content)
        blog.save()
        return blog

    @strawberry.mutation
    def update_post(self,id:int,title: str, author: AuthorInput, content: str) -> BlogPostType:
        blog = Post.objects.get(id=id)
        author_instance = Author.objects.get(id=author.id)  
        blog.title = title
        blog.author = author_instance
        blog.content= content
        blog.save()
        return blog

    @strawberry.field
    def delete_post(self,id: int) -> bool:
        blog = Post.objects.get(id=id)
        blog.delete()
        return True



schema = strawberry.Schema(query=Query, mutation=Mutation)