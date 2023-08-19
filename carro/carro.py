class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        carro = self.session.get("carro")

        if not carro:
            carro = self.session["carro"] = {}
        else:
            self.carro = carro

    def guardar_carro(self):
            self.session["carro"] = self.carro
            self.session.modified = True        

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value[producto.id] = value["cantidad"] + 1
                    break
        
        self.guardar_carro()

        