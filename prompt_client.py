from bravado.client import SwaggerClient

client = SwaggerClient.from_url('http://127.0.0.1:8000/openapi.json')
# pet = client.pet.getPetById(petId=1).response().result
res = client.daw.get().response().result
print(res)
