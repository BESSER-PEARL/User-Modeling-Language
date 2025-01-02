import os, json
from fastapi import FastAPI, HTTPException
from pydantic_classes import *

app = FastAPI()

############################################
#
# Lists to store the data (json)
#
############################################

knownlanguage_list = []
interest_list = []
age_list = []
user_list = []
hobby_list = []
staticproperty_list = []
personalinformation_list = []
nationality_list = []


############################################
#
#   KnownLanguage functions
#
############################################


@app.get("/knownlanguage/", response_model=List[KnownLanguage], tags=["knownlanguage"])
def get_knownlanguage():
    return knownlanguage_list

@app.get("/knownlanguage/{id}/", response_model=KnownLanguage, tags=["knownlanguage"])
def get_knownlanguage(id : int):
    for knownlanguage in knownlanguage_list:
        if knownlanguage.id== id:
            return knownlanguage
    raise HTTPException(status_code=404, detail="KnownLanguage not found")

@app.post("/knownlanguage/", response_model=KnownLanguage, tags=["knownlanguage"])
def create_knownlanguage(knownlanguage: KnownLanguage):
    for existing_knownlanguage in knownlanguage_list:
        if existing_knownlanguage.id == knownlanguage.id:
            raise HTTPException(status_code=400, detail=f"KnownLanguage with id {existing_knownlanguage.id} already exists")

    personalinformation_id = getattr(knownlanguage, 'personalinformation_id', None)
    if personalinformation_id is not None:
        personalinformation_exists = any(personalinformation.id == personalinformation_id for personalinformation in personalinformation_list)
        if not personalinformation_exists:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")


    knownlanguage_list.append(knownlanguage)
    return knownlanguage




@app.put("/knownlanguage/{id}/", response_model=KnownLanguage, tags=["knownlanguage"])
def change_knownlanguage(id : int, updated_knownlanguage: KnownLanguage):
    for index, knownlanguage in enumerate(knownlanguage_list): 
        if knownlanguage.id == id:
            knownlanguage_list[index] = updated_knownlanguage
            return updated_knownlanguage
    raise HTTPException(status_code=404, detail="KnownLanguage not found")

@app.patch("/knownlanguage/{id}/{attribute_to_change}", response_model=KnownLanguage, tags=["knownlanguage"])
def update_knownlanguage(id : int,  attribute_to_change: str, updated_data: str):
    for knownlanguage in knownlanguage_list:
        if knownlanguage.id == id:
            if hasattr(knownlanguage, attribute_to_change):
                setattr(knownlanguage, attribute_to_change, updated_data)
                return knownlanguage
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="KnownLanguage not found")

@app.delete("/knownlanguage/{id}/", tags=["knownlanguage"])
def delete_knownlanguage(id : int):
    for index, knownlanguage in enumerate(knownlanguage_list):
        if knownlanguage.id == id:
            knownlanguage_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="KnownLanguage not found") 

############################################
#
#   Interest functions
#
############################################


@app.get("/interest/", response_model=List[Interest], tags=["interest"])
def get_interest():
    return interest_list

@app.get("/interest/{id}/", response_model=Interest, tags=["interest"])
def get_interest(id : int):
    for interest in interest_list:
        if interest.id== id:
            return interest
    raise HTTPException(status_code=404, detail="Interest not found")

@app.post("/interest/", response_model=Interest, tags=["interest"])
def create_interest(interest: Interest):
    for existing_interest in interest_list:
        if existing_interest.id == interest.id:
            raise HTTPException(status_code=400, detail=f"Interest with id {existing_interest.id} already exists")

    personalinformation_id = getattr(interest, 'personalinformation_id', None)
    if personalinformation_id is not None:
        personalinformation_exists = any(personalinformation.id == personalinformation_id for personalinformation in personalinformation_list)
        if not personalinformation_exists:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")


    interest_list.append(interest)
    return interest




@app.put("/interest/{id}/", response_model=Interest, tags=["interest"])
def change_interest(id : int, updated_interest: Interest):
    for index, interest in enumerate(interest_list): 
        if interest.id == id:
            interest_list[index] = updated_interest
            return updated_interest
    raise HTTPException(status_code=404, detail="Interest not found")

@app.patch("/interest/{id}/{attribute_to_change}", response_model=Interest, tags=["interest"])
def update_interest(id : int,  attribute_to_change: str, updated_data: str):
    for interest in interest_list:
        if interest.id == id:
            if hasattr(interest, attribute_to_change):
                setattr(interest, attribute_to_change, updated_data)
                return interest
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="Interest not found")

@app.delete("/interest/{id}/", tags=["interest"])
def delete_interest(id : int):
    for index, interest in enumerate(interest_list):
        if interest.id == id:
            interest_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Interest not found") 

############################################
#
#   Age functions
#
############################################


@app.get("/age/", response_model=List[Age], tags=["age"])
def get_age():
    return age_list

@app.get("/age/{id}/", response_model=Age, tags=["age"])
def get_age(id : int):
    for age in age_list:
        if age.id== id:
            return age
    raise HTTPException(status_code=404, detail="Age not found")

@app.post("/age/", response_model=Age, tags=["age"])
def create_age(age: Age):
    for existing_age in age_list:
        if existing_age.id == age.id:
            raise HTTPException(status_code=400, detail=f"Age with id {existing_age.id} already exists")

    personalinformation_id = getattr(age, 'personalinformation_id', None)
    if personalinformation_id is not None:
        personalinformation_exists = any(personalinformation.id == personalinformation_id for personalinformation in personalinformation_list)
        if not personalinformation_exists:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")


    age_list.append(age)
    return age




@app.put("/age/{id}/", response_model=Age, tags=["age"])
def change_age(id : int, updated_age: Age):
    for index, age in enumerate(age_list): 
        if age.id == id:
            age_list[index] = updated_age
            return updated_age
    raise HTTPException(status_code=404, detail="Age not found")

@app.patch("/age/{id}/{attribute_to_change}", response_model=Age, tags=["age"])
def update_age(id : int,  attribute_to_change: str, updated_data: str):
    for age in age_list:
        if age.id == id:
            if hasattr(age, attribute_to_change):
                setattr(age, attribute_to_change, updated_data)
                return age
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="Age not found")

@app.delete("/age/{id}/", tags=["age"])
def delete_age(id : int):
    for index, age in enumerate(age_list):
        if age.id == id:
            age_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Age not found") 

############################################
#
#   User functions
#
############################################


@app.get("/user/", response_model=List[User], tags=["user"])
def get_user():
    return user_list

@app.get("/user/{id}/", response_model=User, tags=["user"])
def get_user(id : int):
    for user in user_list:
        if user.id== id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/user/", response_model=User, tags=["user"])
def create_user(user: User):
    for existing_user in user_list:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail=f"User with id {existing_user.id} already exists")



    user_list.append(user)
    return user




@app.put("/user/{id}/", response_model=User, tags=["user"])
def change_user(id : int, updated_user: User):
    for index, user in enumerate(user_list): 
        if user.id == id:
            user_list[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.patch("/user/{id}/{attribute_to_change}", response_model=User, tags=["user"])
def update_user(id : int,  attribute_to_change: str, updated_data: str):
    for user in user_list:
        if user.id == id:
            if hasattr(user, attribute_to_change):
                setattr(user, attribute_to_change, updated_data)
                return user
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{id}/", tags=["user"])
def delete_user(id : int):
    for index, user in enumerate(user_list):
        if user.id == id:
            user_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found") 

############################################
#
#   Hobby functions
#
############################################


@app.get("/hobby/", response_model=List[Hobby], tags=["hobby"])
def get_hobby():
    return hobby_list

@app.get("/hobby/{id}/", response_model=Hobby, tags=["hobby"])
def get_hobby(id : int):
    for hobby in hobby_list:
        if hobby.id== id:
            return hobby
    raise HTTPException(status_code=404, detail="Hobby not found")

@app.post("/hobby/", response_model=Hobby, tags=["hobby"])
def create_hobby(hobby: Hobby):
    for existing_hobby in hobby_list:
        if existing_hobby.id == hobby.id:
            raise HTTPException(status_code=400, detail=f"Hobby with id {existing_hobby.id} already exists")

    personalinformation_id = getattr(hobby, 'personalinformation_id', None)
    if personalinformation_id is not None:
        personalinformation_exists = any(personalinformation.id == personalinformation_id for personalinformation in personalinformation_list)
        if not personalinformation_exists:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")


    hobby_list.append(hobby)
    return hobby




@app.put("/hobby/{id}/", response_model=Hobby, tags=["hobby"])
def change_hobby(id : int, updated_hobby: Hobby):
    for index, hobby in enumerate(hobby_list): 
        if hobby.id == id:
            hobby_list[index] = updated_hobby
            return updated_hobby
    raise HTTPException(status_code=404, detail="Hobby not found")

@app.patch("/hobby/{id}/{attribute_to_change}", response_model=Hobby, tags=["hobby"])
def update_hobby(id : int,  attribute_to_change: str, updated_data: str):
    for hobby in hobby_list:
        if hobby.id == id:
            if hasattr(hobby, attribute_to_change):
                setattr(hobby, attribute_to_change, updated_data)
                return hobby
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="Hobby not found")

@app.delete("/hobby/{id}/", tags=["hobby"])
def delete_hobby(id : int):
    for index, hobby in enumerate(hobby_list):
        if hobby.id == id:
            hobby_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Hobby not found") 

############################################
#
#   StaticProperty functions
#
############################################


@app.get("/staticproperty/", response_model=List[StaticProperty], tags=["staticproperty"])
def get_staticproperty():
    return staticproperty_list

@app.get("/staticproperty/{id}/", response_model=StaticProperty, tags=["staticproperty"])
def get_staticproperty(id : int):
    for staticproperty in staticproperty_list:
        if staticproperty.id== id:
            return staticproperty
    raise HTTPException(status_code=404, detail="StaticProperty not found")

@app.post("/staticproperty/", response_model=StaticProperty, tags=["staticproperty"])
def create_staticproperty(staticproperty: StaticProperty):
    for existing_staticproperty in staticproperty_list:
        if existing_staticproperty.id == staticproperty.id:
            raise HTTPException(status_code=400, detail=f"StaticProperty with id {existing_staticproperty.id} already exists")



    staticproperty_list.append(staticproperty)
    return staticproperty




@app.put("/staticproperty/{id}/", response_model=StaticProperty, tags=["staticproperty"])
def change_staticproperty(id : int, updated_staticproperty: StaticProperty):
    for index, staticproperty in enumerate(staticproperty_list): 
        if staticproperty.id == id:
            staticproperty_list[index] = updated_staticproperty
            return updated_staticproperty
    raise HTTPException(status_code=404, detail="StaticProperty not found")

@app.patch("/staticproperty/{id}/{attribute_to_change}", response_model=StaticProperty, tags=["staticproperty"])
def update_staticproperty(id : int,  attribute_to_change: str, updated_data: str):
    for staticproperty in staticproperty_list:
        if staticproperty.id == id:
            if hasattr(staticproperty, attribute_to_change):
                setattr(staticproperty, attribute_to_change, updated_data)
                return staticproperty
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="StaticProperty not found")

@app.delete("/staticproperty/{id}/", tags=["staticproperty"])
def delete_staticproperty(id : int):
    for index, staticproperty in enumerate(staticproperty_list):
        if staticproperty.id == id:
            staticproperty_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="StaticProperty not found") 

############################################
#
#   PersonalInformation functions
#
############################################


@app.get("/personalinformation/", response_model=List[PersonalInformation], tags=["personalinformation"])
def get_personalinformation():
    return personalinformation_list

@app.get("/personalinformation/{id}/", response_model=PersonalInformation, tags=["personalinformation"])
def get_personalinformation(id : int):
    for personalinformation in personalinformation_list:
        if personalinformation.id== id:
            return personalinformation
    raise HTTPException(status_code=404, detail="PersonalInformation not found")

@app.post("/personalinformation/", response_model=PersonalInformation, tags=["personalinformation"])
def create_personalinformation(personalinformation: PersonalInformation):
    for existing_personalinformation in personalinformation_list:
        if existing_personalinformation.id == personalinformation.id:
            raise HTTPException(status_code=400, detail=f"PersonalInformation with id {existing_personalinformation.id} already exists")

    user_id = getattr(personalinformation, 'user_id', None)
    if user_id is not None:
        user_exists = any(user.id == user_id for user in user_list)
        if not user_exists:
            raise HTTPException(status_code=400, detail="User not found")


    personalinformation_list.append(personalinformation)
    return personalinformation




@app.put("/personalinformation/{id}/", response_model=PersonalInformation, tags=["personalinformation"])
def change_personalinformation(id : int, updated_personalinformation: PersonalInformation):
    for index, personalinformation in enumerate(personalinformation_list): 
        if personalinformation.id == id:
            personalinformation_list[index] = updated_personalinformation
            return updated_personalinformation
    raise HTTPException(status_code=404, detail="PersonalInformation not found")

@app.patch("/personalinformation/{id}/{attribute_to_change}", response_model=PersonalInformation, tags=["personalinformation"])
def update_personalinformation(id : int,  attribute_to_change: str, updated_data: str):
    for personalinformation in personalinformation_list:
        if personalinformation.id == id:
            if hasattr(personalinformation, attribute_to_change):
                setattr(personalinformation, attribute_to_change, updated_data)
                return personalinformation
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="PersonalInformation not found")

@app.delete("/personalinformation/{id}/", tags=["personalinformation"])
def delete_personalinformation(id : int):
    for index, personalinformation in enumerate(personalinformation_list):
        if personalinformation.id == id:
            personalinformation_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="PersonalInformation not found") 

############################################
#
#   Nationality functions
#
############################################


@app.get("/nationality/", response_model=List[Nationality], tags=["nationality"])
def get_nationality():
    return nationality_list

@app.get("/nationality/{id}/", response_model=Nationality, tags=["nationality"])
def get_nationality(id : int):
    for nationality in nationality_list:
        if nationality.id== id:
            return nationality
    raise HTTPException(status_code=404, detail="Nationality not found")

@app.post("/nationality/", response_model=Nationality, tags=["nationality"])
def create_nationality(nationality: Nationality):
    for existing_nationality in nationality_list:
        if existing_nationality.id == nationality.id:
            raise HTTPException(status_code=400, detail=f"Nationality with id {existing_nationality.id} already exists")

    personalinformation_id = getattr(nationality, 'personalinformation_id', None)
    if personalinformation_id is not None:
        personalinformation_exists = any(personalinformation.id == personalinformation_id for personalinformation in personalinformation_list)
        if not personalinformation_exists:
            raise HTTPException(status_code=400, detail="PersonalInformation not found")


    nationality_list.append(nationality)
    return nationality




@app.put("/nationality/{id}/", response_model=Nationality, tags=["nationality"])
def change_nationality(id : int, updated_nationality: Nationality):
    for index, nationality in enumerate(nationality_list): 
        if nationality.id == id:
            nationality_list[index] = updated_nationality
            return updated_nationality
    raise HTTPException(status_code=404, detail="Nationality not found")

@app.patch("/nationality/{id}/{attribute_to_change}", response_model=Nationality, tags=["nationality"])
def update_nationality(id : int,  attribute_to_change: str, updated_data: str):
    for nationality in nationality_list:
        if nationality.id == id:
            if hasattr(nationality, attribute_to_change):
                setattr(nationality, attribute_to_change, updated_data)
                return nationality
            else:
                raise HTTPException(status_code=400, detail=f"Attribute '{attribute_to_change}' does not exist")
    raise HTTPException(status_code=404, detail="Nationality not found")

@app.delete("/nationality/{id}/", tags=["nationality"])
def delete_nationality(id : int):
    for index, nationality in enumerate(nationality_list):
        if nationality.id == id:
            nationality_list.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Nationality not found") 



############################################
# Maintaining the server
############################################
if __name__ == "__main__":
    import uvicorn
    openapi_schema = app.openapi()
    output_dir = os.path.join(os.getcwd(), 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'openapi_specs.json')
    print(f"Writing OpenAPI schema to {output_file}")
    with open(output_file, 'w') as file:
        json.dump(openapi_schema, file)
    uvicorn.run(app, host="127.0.0.1", port=8000)



