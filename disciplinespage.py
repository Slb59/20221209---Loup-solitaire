import customtkinter

class PlayerPage(customtkinter.CTkFrame):


    def __init__(self, parent, controller):

        customtkinter.CTkFrame.__init__(self, parent, width=900)

        self.controller = controller
        self.id = controller.id

        self.player = self.controller.player

        self.create_widget()

    def create_widget(self):

        text = f"Au cours des siècles, les Moines Kaï ont appris à maîtriser toutes les techniques du guerrier." \
                f"Ces techniques sont connues sous le nom de Disciplines Kaï et enseignées aux seigneurs Kaï. " \
                f"Vous avez été initié à {len(self.player.kai_discipline)} des techniques décrites ci-dessous." \
                f"Il vous appartient de choisir vous-même ces disciplines limitées au nombre de 5 lors de votre" \
                f"première aventure. Chaque discipline peut vous être utile à un moment ou à un autre de votre quête " \
                f"et votre choix devra être le plus judicieux possible : dans certaines circonstances, une habile " \
                f"mise en pratique de l'une de ces techniques peut vous sauver la vie. Les techniques apprises ne " \
                f"peuvent pas être remplacées."

        t = customtkinter.CTkLabel(master=self,
                                   text=text, font=self.controller.textfont)
        t.grid(row=0, column=0, sticky="ew", padx=20)
