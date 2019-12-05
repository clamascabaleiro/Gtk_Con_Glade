import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class VentanaPrincipal():

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("EjemploGlade.glade")

        VentanaPrincipal = builder.get_object("VentanaPrincipal")
        self.txtNome = builder.get_object("txtNome")
        self.lblSaludo = builder.get_object("lblSaludo")
        self.btnSaludar = builder.get_object("btnSaludar")

        señales = {

            "on_btnSaludar_clicked" : self.on_btnSaludar_clicked,
            "on_txtNome_activate" : self.on_txtNome_activate,
            "on_VentanaPrincipal_destroy" : Gtk.main_quit

        }

        builder.connect_signals(señales)

        VentanaPrincipal.show_all()

    def on_btnSaludar_clicked(self, boton):
        """Metodo que maneja la señal clicked de btnSaludo"""
        nombre = self.txtNome.get_text()
        self.lblSaludo.set_text("Hola " + nombre)

    def on_txtNome_activate(self, texto):
        """Metodo que maneja la señal de activated de txtNome"""
        self.on_btnSaludar_clicked(texto)


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
