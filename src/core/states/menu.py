import pygame

from core.graphics import Resources
from core.connection import Network
from assets.components import Button, Text

from .state import State


class Menu(State):
    def init(self):
        """Inicializa los componentes del menú."""
        self._client.add_component(
            Button("Unirse", 50, 300,
                   font_size=72,
                   on_click=self.change_state))

        self._client.add_component(
            Button("Anfitrion", 50, 350,
                   font_size=72,
                   on_click=self.change_state))

        self._client.add_component(
            Button("Creditos", 50, 400,
                   font_size=72,
                   on_click=self.change_state))

        self._client.add_component(
            Text("ITESO (2023)", 10, 580, font_size=16))

    def change_state(self, button: Button):
        """Cambia el estado del juego según el botón presionado."""
        match button.text:
            case "Unirse":
                from .join import Join
                state = Join(self._client)
            case "Anfitrion":
                from .host import Host
                state = Host(self._client)
            case "Creditos":
                from .credits import Credits
                state = Credits(self._client)
            case _:
                return

        self._client.state = state

    def update(self, dt: float):
        pass

    def update_server(self, network: Network):
        pass

    def draw(self, surface: pygame.Surface):
        """Dibuja la interfaz gráfica del menú."""
        surface.blit(Resources.MENU_BACKGROUND, (0, 0))
