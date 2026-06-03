# gestiona_materiales_Biblioteca 
class Material(object):
    _next_id = 1

    def __init__(self, titulo, editorial=None):
        self.id = Material._next_id
        self.titulo = titulo
        self.editorial = editorial
        self.disponible = True
        Material._next_id += 1

    def obtener_detalles(self):
        pass


class Libro(Material):
    def __init__(self, titulo, autor, editorial=None):
        super().__init__(titulo, editorial)
        self.autor = autor

    def obtener_detalles(self):
        txt_autor = self.autor if isinstance(self.autor, str) else self.autor.nombre
        txt_edit = self.editorial if isinstance(self.editorial, str) else self.editorial.nombre
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[LIBRO] ID: {self.id} | Título: {self.titulo} | Autor: {txt_autor} | Editorial: {txt_edit} | Estado: {estado}"


class Revista(Material):
    def __init__(self, titulo, nro_edicion, editorial=None):
        super().__init__(titulo, editorial)
        self.nro_edicion = nro_edicion

    def obtener_detalles(self):
        txt_edit = self.editorial if isinstance(self.editorial, str) else self.editorial.nombre
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[REVISTA] ID: {self.id} | Título: {self.titulo} | Edición: N° {self.nro_edicion} | Editorial: {txt_edit} | Estado: {estado}"