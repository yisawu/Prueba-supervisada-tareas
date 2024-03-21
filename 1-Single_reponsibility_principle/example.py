# Esta clase solo se encarga de guarda los datos del cliente.
class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Esta clase solo se encarga de validar los datos de cliente.
class ClientVerifier:
    def verify_age(client):
        age = client.age
        return age >= 18
    
    def verify_name(client):
        name = client.name
        return name is not None and name.strip()
