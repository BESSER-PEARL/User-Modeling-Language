import sys
sys.path.append("C:/Users/conrardy/Desktop/git/BESSER")


# Import methods and classes
from besser.BUML.notations.structuralPlantUML import plantuml_to_buml
from besser.BUML.metamodel.structural import DomainModel
from besser.generators.backend import BackendGenerator


# PlantUML to B-UML model
user_model: DomainModel = plantuml_to_buml(plantUML_model_path='../metamodel/plantumlfix.txt')

backend = BackendGenerator(model=user_model, http_methods=['GET', 'POST', 'PUT', 'DELETE'], nested_creations = True, docker_image = True)
backend.generate()
