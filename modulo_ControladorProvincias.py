from vistaProvincias import ProvinciaView, NewProvincia
from modulo_ManejadorProvincias import ManejadorProvincias

class ControladorProvincias(object):
    
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())
        # comandos de que se ejecutan a través de la vista
    
    def crearProvincia(self):
        nuevaProvincia = NewProvincia(self.vista).show()
        if nuevaProvincia:
            provincia = self.repo.agregarProvincia(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)
    
    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincia[index]
        self.vista.verProvinciaEnForm(provincia)
    
    def modificarProvincia(self):
        if self.seleccion == -1:
            return
        rowid = self.provincia[self.seleccion].rowid
        detallesProvincia = self.vista.obtenerDetalles()
        detallesProvincia.rowid = rowid
        provincia = self.repo.modificarProvincia(detallesProvincia)
        self.provincia[self.seleccion] = provincia
        self.vista.modificarProvincia(provincia, self.seleccion)
        self.seleccion=-1
    
    def start(self):
        for p in self.provincias:
            self.vista.agregarProvincia(p)
            self.vista.mainloop()
    
    def salirGrabarDatos(self):
        self.repo.grabarDatos()

