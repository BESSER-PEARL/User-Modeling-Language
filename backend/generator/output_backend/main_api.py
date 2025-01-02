import uvicorn
import os, json
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from pydantic_classes import *
from sql_alchemy import *

############################################
#
#   Initialize the database
#
############################################

def init_db():
    db_host = "127.0.0.1:5432"
    db_name = "user_model"
    db_user = "aaron"
    db_password = "aaron"
    SQLALCHEMY_DATABASE_URL = f"postgresql://{db_host}/{db_name}?user={db_user}&password={db_password}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return SessionLocal

app = FastAPI()

# Initialize database session
SessionLocal = init_db()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

############################################
#
#   Nationality functions
#
############################################

@app.get("/nationality/", response_model=None)
def get_all_nationality(database: Session = Depends(get_db)) -> list[Nationality]:
    nationality_list = database.query(Nationality).all()
    return nationality_list


@app.get("/nationality/{nationality_id}/", response_model=None)
async def get_nationality(nationality_id: int, database: Session = Depends(get_db)) -> Nationality:
    db_nationality = database.query(Nationality).filter(Nationality.id == nationality_id).first()
    if db_nationality is None:
        raise HTTPException(status_code=404, detail="Nationality not found")

    response_data = {
        "nationality": db_nationality,
}
    return response_data



@app.post("/nationality/", response_model=None)
async def create_nationality(nationality_data: NationalityCreate, database: Session = Depends(get_db)) -> Nationality:

    if nationality_data.personalinformation_id is not None:
        db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == nationality_data.personalinformation_id).first()
        if not db_personalinformation:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")
    else:
        raise HTTPException(status_code=400, detail="PersonalInformation ID is required")

    db_nationality = Nationality(
        name=nationality_data.name, personalinformation_id=nationality_data.personalinformation_id    )

    database.add(db_nationality)
    database.commit()
    database.refresh(db_nationality)


    
    return db_nationality


@app.put("/nationality/{nationality_id}/", response_model=None)
async def update_nationality(nationality_id: int, nationality_data: NationalityCreate, database: Session = Depends(get_db)) -> Nationality:
    db_nationality = database.query(Nationality).filter(Nationality.id == nationality_id).first()
    if db_nationality is None:
        raise HTTPException(status_code=404, detail="Nationality not found")

    setattr(db_nationality, 'name', nationality_data.name)
    database.commit()
    database.refresh(db_nationality)
    return db_nationality


@app.delete("/nationality/{nationality_id}/", response_model=None)
async def delete_nationality(nationality_id: int, database: Session = Depends(get_db)):
    db_nationality = database.query(Nationality).filter(Nationality.id == nationality_id).first()
    if db_nationality is None:
        raise HTTPException(status_code=404, detail="Nationality not found")
    database.delete(db_nationality)
    database.commit()
    return db_nationality



############################################
#
#   Interest functions
#
############################################

@app.get("/interest/", response_model=None)
def get_all_interest(database: Session = Depends(get_db)) -> list[Interest]:
    interest_list = database.query(Interest).all()
    return interest_list


@app.get("/interest/{interest_id}/", response_model=None)
async def get_interest(interest_id: int, database: Session = Depends(get_db)) -> Interest:
    db_interest = database.query(Interest).filter(Interest.id == interest_id).first()
    if db_interest is None:
        raise HTTPException(status_code=404, detail="Interest not found")

    response_data = {
        "interest": db_interest,
}
    return response_data



@app.post("/interest/", response_model=None)
async def create_interest(interest_data: InterestCreate, database: Session = Depends(get_db)) -> Interest:

    if interest_data.personalinformation_id is not None:
        db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == interest_data.personalinformation_id).first()
        if not db_personalinformation:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")
    else:
        raise HTTPException(status_code=400, detail="PersonalInformation ID is required")

    db_interest = Interest(
        name=interest_data.name, personalinformation_id=interest_data.personalinformation_id    )

    database.add(db_interest)
    database.commit()
    database.refresh(db_interest)


    
    return db_interest


@app.put("/interest/{interest_id}/", response_model=None)
async def update_interest(interest_id: int, interest_data: InterestCreate, database: Session = Depends(get_db)) -> Interest:
    db_interest = database.query(Interest).filter(Interest.id == interest_id).first()
    if db_interest is None:
        raise HTTPException(status_code=404, detail="Interest not found")

    setattr(db_interest, 'name', interest_data.name)
    database.commit()
    database.refresh(db_interest)
    return db_interest


@app.delete("/interest/{interest_id}/", response_model=None)
async def delete_interest(interest_id: int, database: Session = Depends(get_db)):
    db_interest = database.query(Interest).filter(Interest.id == interest_id).first()
    if db_interest is None:
        raise HTTPException(status_code=404, detail="Interest not found")
    database.delete(db_interest)
    database.commit()
    return db_interest



############################################
#
#   User functions
#
############################################

@app.get("/user/", response_model=None)
def get_all_user(database: Session = Depends(get_db)) -> list[User]:
    user_list = database.query(User).all()
    return user_list


@app.get("/user/{user_id}/", response_model=None)
async def get_user(user_id: int, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    response_data = {
        "user": db_user,
}
    return response_data



@app.post("/user/", response_model=None)
async def create_user(user_data: UserCreate, database: Session = Depends(get_db)) -> User:


    db_user = User(
        name=user_data.name    )

    database.add(db_user)
    database.commit()
    database.refresh(db_user)


    
    return db_user


@app.put("/user/{user_id}/", response_model=None)
async def update_user(user_id: int, user_data: UserCreate, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    setattr(db_user, 'name', user_data.name)
    database.commit()
    database.refresh(db_user)
    return db_user


@app.delete("/user/{user_id}/", response_model=None)
async def delete_user(user_id: int, database: Session = Depends(get_db)):
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    database.delete(db_user)
    database.commit()
    return db_user



############################################
#
#   Age functions
#
############################################

@app.get("/age/", response_model=None)
def get_all_age(database: Session = Depends(get_db)) -> list[Age]:
    age_list = database.query(Age).all()
    return age_list


@app.get("/age/{age_id}/", response_model=None)
async def get_age(age_id: int, database: Session = Depends(get_db)) -> Age:
    db_age = database.query(Age).filter(Age.id == age_id).first()
    if db_age is None:
        raise HTTPException(status_code=404, detail="Age not found")

    response_data = {
        "age": db_age,
}
    return response_data



@app.post("/age/", response_model=None)
async def create_age(age_data: AgeCreate, database: Session = Depends(get_db)) -> Age:

    if age_data.personalinformation_id is not None:
        db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == age_data.personalinformation_id).first()
        if not db_personalinformation:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")
    else:
        raise HTTPException(status_code=400, detail="PersonalInformation ID is required")

    db_age = Age(
        value=age_data.value, personalinformation_id=age_data.personalinformation_id    )

    database.add(db_age)
    database.commit()
    database.refresh(db_age)



    
    return db_age


@app.put("/age/{age_id}/", response_model=None)
async def update_age(age_id: int, age_data: AgeCreate, database: Session = Depends(get_db)) -> Age:
    db_age = database.query(Age).filter(Age.id == age_id).first()
    if db_age is None:
        raise HTTPException(status_code=404, detail="Age not found")

    setattr(db_age, 'value', age_data.value)
    database.commit()
    database.refresh(db_age)
    return db_age


@app.delete("/age/{age_id}/", response_model=None)
async def delete_age(age_id: int, database: Session = Depends(get_db)):
    db_age = database.query(Age).filter(Age.id == age_id).first()
    if db_age is None:
        raise HTTPException(status_code=404, detail="Age not found")
    database.delete(db_age)
    database.commit()
    return db_age



############################################
#
#   Hobby functions
#
############################################

@app.get("/hobby/", response_model=None)
def get_all_hobby(database: Session = Depends(get_db)) -> list[Hobby]:
    hobby_list = database.query(Hobby).all()
    return hobby_list


@app.get("/hobby/{hobby_id}/", response_model=None)
async def get_hobby(hobby_id: int, database: Session = Depends(get_db)) -> Hobby:
    db_hobby = database.query(Hobby).filter(Hobby.id == hobby_id).first()
    if db_hobby is None:
        raise HTTPException(status_code=404, detail="Hobby not found")

    response_data = {
        "hobby": db_hobby,
}
    return response_data



@app.post("/hobby/", response_model=None)
async def create_hobby(hobby_data: HobbyCreate, database: Session = Depends(get_db)) -> Hobby:

    if hobby_data.personalinformation_id is not None:
        db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == hobby_data.personalinformation_id).first()
        if not db_personalinformation:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")
    else:
        raise HTTPException(status_code=400, detail="PersonalInformation ID is required")

    db_hobby = Hobby(
        name=hobby_data.name, personalinformation_id=hobby_data.personalinformation_id    )

    database.add(db_hobby)
    database.commit()
    database.refresh(db_hobby)


    
    return db_hobby


@app.put("/hobby/{hobby_id}/", response_model=None)
async def update_hobby(hobby_id: int, hobby_data: HobbyCreate, database: Session = Depends(get_db)) -> Hobby:
    db_hobby = database.query(Hobby).filter(Hobby.id == hobby_id).first()
    if db_hobby is None:
        raise HTTPException(status_code=404, detail="Hobby not found")

    setattr(db_hobby, 'name', hobby_data.name)
    database.commit()
    database.refresh(db_hobby)
    return db_hobby


@app.delete("/hobby/{hobby_id}/", response_model=None)
async def delete_hobby(hobby_id: int, database: Session = Depends(get_db)):
    db_hobby = database.query(Hobby).filter(Hobby.id == hobby_id).first()
    if db_hobby is None:
        raise HTTPException(status_code=404, detail="Hobby not found")
    database.delete(db_hobby)
    database.commit()
    return db_hobby



############################################
#
#   StaticProperty functions
#
############################################

@app.get("/staticproperty/", response_model=None)
def get_all_staticproperty(database: Session = Depends(get_db)) -> list[StaticProperty]:
    staticproperty_list = database.query(StaticProperty).all()
    return staticproperty_list


@app.get("/staticproperty/{staticproperty_id}/", response_model=None)
async def get_staticproperty(staticproperty_id: int, database: Session = Depends(get_db)) -> StaticProperty:
    db_staticproperty = database.query(StaticProperty).filter(StaticProperty.id == staticproperty_id).first()
    if db_staticproperty is None:
        raise HTTPException(status_code=404, detail="StaticProperty not found")

    response_data = {
        "staticproperty": db_staticproperty,
}
    return response_data



@app.post("/staticproperty/", response_model=None)
async def create_staticproperty(staticproperty_data: StaticPropertyCreate, database: Session = Depends(get_db)) -> StaticProperty:



    database.add(db_staticproperty)
    database.commit()
    database.refresh(db_staticproperty)


    
    return db_staticproperty


@app.put("/staticproperty/{staticproperty_id}/", response_model=None)
async def update_staticproperty(staticproperty_id: int, staticproperty_data: StaticPropertyCreate, database: Session = Depends(get_db)) -> StaticProperty:
    db_staticproperty = database.query(StaticProperty).filter(StaticProperty.id == staticproperty_id).first()
    if db_staticproperty is None:
        raise HTTPException(status_code=404, detail="StaticProperty not found")

    database.commit()
    database.refresh(db_staticproperty)
    return db_staticproperty


@app.delete("/staticproperty/{staticproperty_id}/", response_model=None)
async def delete_staticproperty(staticproperty_id: int, database: Session = Depends(get_db)):
    db_staticproperty = database.query(StaticProperty).filter(StaticProperty.id == staticproperty_id).first()
    if db_staticproperty is None:
        raise HTTPException(status_code=404, detail="StaticProperty not found")
    database.delete(db_staticproperty)
    database.commit()
    return db_staticproperty



############################################
#
#   PersonalInformation functions
#
############################################

@app.get("/personalinformation/", response_model=None)
def get_all_personalinformation(database: Session = Depends(get_db)) -> list[PersonalInformation]:
    personalinformation_list = database.query(PersonalInformation).all()
    return personalinformation_list


@app.get("/personalinformation/{personalinformation_id}/", response_model=None)
async def get_personalinformation(personalinformation_id: int, database: Session = Depends(get_db)) -> PersonalInformation:
    db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == personalinformation_id).first()
    if db_personalinformation is None:
        raise HTTPException(status_code=404, detail="PersonalInformation not found")

    response_data = {
        "personalinformation": db_personalinformation,
}
    return response_data



@app.post("/personalinformation/", response_model=None)
async def create_personalinformation(personalinformation_data: PersonalInformationCreate, database: Session = Depends(get_db)) -> PersonalInformation:

    if personalinformation_data.user_id is not None:
        db_user = database.query(User).filter(User.id == personalinformation_data.user_id).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="User not found")
    else:
        raise HTTPException(status_code=400, detail="User ID is required")

    db_personalinformation = PersonalInformation(
        address=personalinformation_data.address,         name=personalinformation_data.name,         gender=personalinformation_data.gender, user_id=personalinformation_data.user_id    )

    database.add(db_personalinformation)
    database.commit()
    database.refresh(db_personalinformation)


    
    return db_personalinformation


@app.put("/personalinformation/{personalinformation_id}/", response_model=None)
async def update_personalinformation(personalinformation_id: int, personalinformation_data: PersonalInformationCreate, database: Session = Depends(get_db)) -> PersonalInformation:
    db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == personalinformation_id).first()
    if db_personalinformation is None:
        raise HTTPException(status_code=404, detail="PersonalInformation not found")

    setattr(db_personalinformation, 'address', personalinformation_data.address)
    setattr(db_personalinformation, 'name', personalinformation_data.name)
    setattr(db_personalinformation, 'gender', personalinformation_data.gender)
    database.commit()
    database.refresh(db_personalinformation)
    return db_personalinformation


@app.delete("/personalinformation/{personalinformation_id}/", response_model=None)
async def delete_personalinformation(personalinformation_id: int, database: Session = Depends(get_db)):
    db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == personalinformation_id).first()
    if db_personalinformation is None:
        raise HTTPException(status_code=404, detail="PersonalInformation not found")
    database.delete(db_personalinformation)
    database.commit()
    return db_personalinformation



############################################
#
#   KnownLanguage functions
#
############################################

@app.get("/knownlanguage/", response_model=None)
def get_all_knownlanguage(database: Session = Depends(get_db)) -> list[KnownLanguage]:
    knownlanguage_list = database.query(KnownLanguage).all()
    return knownlanguage_list


@app.get("/knownlanguage/{knownlanguage_id}/", response_model=None)
async def get_knownlanguage(knownlanguage_id: int, database: Session = Depends(get_db)) -> KnownLanguage:
    db_knownlanguage = database.query(KnownLanguage).filter(KnownLanguage.id == knownlanguage_id).first()
    if db_knownlanguage is None:
        raise HTTPException(status_code=404, detail="KnownLanguage not found")

    response_data = {
        "knownlanguage": db_knownlanguage,
}
    return response_data



@app.post("/knownlanguage/", response_model=None)
async def create_knownlanguage(knownlanguage_data: KnownLanguageCreate, database: Session = Depends(get_db)) -> KnownLanguage:

    if knownlanguage_data.personalinformation_id is not None:
        db_personalinformation = database.query(PersonalInformation).filter(PersonalInformation.id == knownlanguage_data.personalinformation_id).first()
        if not db_personalinformation:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")
    else:
        raise HTTPException(status_code=400, detail="PersonalInformation ID is required")

    db_knownlanguage = KnownLanguage(
        level=knownlanguage_data.level.value,         name=knownlanguage_data.name, personalinformation_id=knownlanguage_data.personalinformation_id    )

    database.add(db_knownlanguage)
    database.commit()
    database.refresh(db_knownlanguage)


    
    return db_knownlanguage


@app.put("/knownlanguage/{knownlanguage_id}/", response_model=None)
async def update_knownlanguage(knownlanguage_id: int, knownlanguage_data: KnownLanguageCreate, database: Session = Depends(get_db)) -> KnownLanguage:
    db_knownlanguage = database.query(KnownLanguage).filter(KnownLanguage.id == knownlanguage_id).first()
    if db_knownlanguage is None:
        raise HTTPException(status_code=404, detail="KnownLanguage not found")

    setattr(db_knownlanguage, 'level', knownlanguage_data.level.value)
    setattr(db_knownlanguage, 'name', knownlanguage_data.name)
    database.commit()
    database.refresh(db_knownlanguage)
    return db_knownlanguage


@app.delete("/knownlanguage/{knownlanguage_id}/", response_model=None)
async def delete_knownlanguage(knownlanguage_id: int, database: Session = Depends(get_db)):
    db_knownlanguage = database.query(KnownLanguage).filter(KnownLanguage.id == knownlanguage_id).first()
    if db_knownlanguage is None:
        raise HTTPException(status_code=404, detail="KnownLanguage not found")
    database.delete(db_knownlanguage)
    database.commit()
    return db_knownlanguage





############################################
# Maintaining the server
############################################
if __name__ == "__main__":
    import uvicorn
    openapi_schema = app.openapi()
    output_dir = os.path.join(os.getcwd(), 'output_backend')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'openapi_specs.json')
    print(f"Writing OpenAPI schema to {output_file}")
    print("Swagger UI available at 0.0.0.0:8000/docs")
    with open(output_file, 'w') as file:
        json.dump(openapi_schema, file)
    uvicorn.run(app, host="0.0.0.0", port= 8000)



