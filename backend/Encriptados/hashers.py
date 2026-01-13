from django.contrib.auth.hashers import BasePasswordHasher

class PlainTextPasswordHasher(BasePasswordHasher):
    algorithm = "plain"

    def encode(self, password, salt):
        return f"{self.algorithm}$${password}"

    def verify(self, password, encoded):
        print(f"DEBUG: Contraseña que escribiste: {password}")
        print(f"DEBUG: Contraseña que está en la BD: {encoded}")
        
        if '$' not in encoded:
            return password == encoded
        
        algorithm, salt, hash = encoded.split('$', 2)
        print(f"DEBUG: Comparando {password} con {hash}")
        
        return password == hash

    def safe_summary(self, encoded):
        return {'algorithm': self.algorithm}