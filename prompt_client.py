from bravado.client import SwaggerClient

url_local = "file:///D:/git/dawpy/swagger.json"
client = SwaggerClient.from_url(url_local)
res = client.daw.get().response().result
