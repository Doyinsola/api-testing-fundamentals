from pydantic import BaseModel, TypeAdapter

class PostSchema(BaseModel):
    userId: int
    id: int
    title: str
    body: str 

PostsListSchema = TypeAdapter(list[PostSchema])