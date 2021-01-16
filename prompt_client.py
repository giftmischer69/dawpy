from bravado.client import SwaggerClient

client = SwaggerClient.from_url("http://127.0.0.1:8000/swagger.json")
res = client.daw.get().response().result
