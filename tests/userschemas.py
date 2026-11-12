from pydantic import BaseModel, TypeAdapter

class geoSchema(BaseModel):
    lat: float
    lng: float

class AddressSchma(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: geoSchema

class CompanySchema(BaseModel):
    name: str
    catchPhrase: str
    bs: str

class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: AddressSchma
    phone: str
    website: str
    company: CompanySchema

UserListSchema = TypeAdapter(list[UserSchema])