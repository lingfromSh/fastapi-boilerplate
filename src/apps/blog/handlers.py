from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi_pagination import Page
from fastapi_pagination import Params
from fastapi_pagination.ext.tortoise import paginate

from apps.blog.models import Author
from apps.blog.models import Blog
from apps.blog.schemas import AuthorCreateInput
from apps.blog.schemas import AuthorOutput
from apps.blog.schemas import AuthorPartialUpdateInput
from apps.blog.schemas import AuthorUpdateInput
from apps.blog.schemas import BlogCreateInput
from apps.blog.schemas import BlogOutput
from apps.blog.schemas import BlogPartialUpdateInput
from apps.blog.schemas import BlogUpdateInput

router = APIRouter(tags=["blog"])


@router.get("/authors", response_model=Page[AuthorOutput], name="get authors")
async def get_authors(params: Params = Depends()):
    """
    Get Authors
    """

    return await paginate(Author.alive_objects.all(), params)


@router.get("/author/{author_id}", response_model=AuthorOutput, name="get author")
async def get_author(author_id: int):
    """
    Get Author
    """
    author = await Author.alive_objects.get_or_none(id=author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.put("/author/{author_id}", response_model=AuthorOutput, name="update author")
async def update_author(author_id: int, input: AuthorUpdateInput):
    """
    Update Author
    """
    author = await Author.alive_objects.get_or_none(id=author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    author.update_from_dict(input.model_dump())
    await author.save()
    return author


@router.patch("/author/{author_id}", response_model=AuthorOutput, name="partial update author")
async def partial_update_author(author_id: int, input: AuthorPartialUpdateInput):
    """
    Partial Update Author
    """
    author = await Author.alive_objects.get_or_none(id=author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    author.update_from_dict(input.model_dump(exclude_unset=True))
    await author.save()
    return author


@router.post("/author", response_model=AuthorOutput, name="create author")
async def create_author(input: AuthorCreateInput):
    """
    Create Author
    """
    author = await Author.create(**input.model_dump())
    return author


@router.delete("/author/{author_id}", name="delete author")
async def delete_author(author_id: int):
    """
    Delete Author
    """
    author = await Author.alive_objects.get_or_none(id=author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    await author.soft_delete()
    return None


@router.get("/blogs", response_model=Page[BlogOutput], name="get blogs")
async def get_blogs(params: Params = Depends()):
    """
    Get Blogs
    """

    return await paginate(Blog.alive_objects.all(), params)


@router.get("/blog/{blog_id}", response_model=BlogOutput, name="get blog")
async def get_blog(blog_id: int):
    """
    Get Blog
    """
    blog = await Blog.alive_objects.get_or_none(id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@router.post("/blog", response_model=BlogOutput, name="create blog")
async def create_blog(input: BlogCreateInput):
    """
    Create Blog
    """
    author = await Author.alive_objects.get_or_none(id=input.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    blog = await Blog.create(**input.model_dump())
    return blog


@router.put("/blog/{blog_id}", response_model=BlogOutput, name="update blog")
async def update_blog(blog_id: int, input: BlogUpdateInput):
    """
    Update Blog
    """
    blog = await Blog.alive_objects.get_or_none(id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.update_from_dict(input.model_dump())
    await blog.save()
    return blog


@router.patch("/blog/{blog_id}", response_model=BlogOutput, name="partial update blog")
async def partial_update_blog(blog_id: int, input: BlogPartialUpdateInput):
    """
    Partial Update Blog
    """
    blog = await Blog.alive_objects.get_or_none(id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.update_from_dict(input.model_dump(exclude_unset=True))
    await blog.save()
    return blog


@router.delete("/blog/{blog_id}", name="delete blog")
async def delete_blog(blog_id: int):
    """
    Delete Blog
    """
    blog = await Blog.alive_objects.get_or_none(id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    await blog.soft_delete()
    return None
