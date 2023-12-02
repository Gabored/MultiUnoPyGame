
import pygame

from util import lerp

from .component import Component

class Button(Component):
    def __init__(self,
                 text: str,
                 x: int, y: int,
                 width: int | str = "auto",
                 height: int | str = "auto",
                 text_align: str = "center",
                 align: str = "topleft",
                 font: str = "ThaleahFat",
                 font_size: int = 20,
                 font_color: tuple[int, int, int] | str = "white",
                 hover_color: tuple[int, int, int] | str = "gray",
                 background_color: tuple[int, int, int] | str | None = None,
                 border_radius: int = 0,
                 border_width: int = 0,
                 border_color: tuple[int, int, int] | str = "black",
                 animation: str | None = "right",
                 on_click: callable = None):
        """
        Inicializa un botón en la interfaz del juego Uno.

        Args:
        - text (str): El texto que se mostrará en el botón.
        - x (int): Posición x del botón.
        - y (int): Posición y del botón.
        - width (int | str, opcional): Ancho del botón. Por defecto es "auto".
        - height (int | str, opcional): Alto del botón. Por defecto es "auto".
        - text_align (str, opcional): Alineación del texto en el botón. Por defecto es "center".
        - align (str, opcional): Alineación del botón en la pantalla. Por defecto es "topleft".
        - font (str, opcional): Fuente del texto. Por defecto es "ThaleahFat".
        - font_size (int, opcional): Tamaño de la fuente. Por defecto es 20.
        - font_color (tuple[int, int, int] | str, opcional): Color de la fuente. Por defecto es "white".
        - hover_color (tuple[int, int, int] | str, opcional): Color al pasar el mouse por encima. Por defecto es "gray".
        - background_color (tuple[int, int, int] | str | None, opcional): Color de fondo del botón. Por defecto es None.
        - border_radius (int, opcional): Radio del borde del botón. Por defecto es 0.
        - border_width (int, opcional): Ancho del borde del botón. Por defecto es 0.
        - border_color (tuple[int, int, int] | str, opcional): Color del borde del botón. Por defecto es "black".
        - animation (str | None, opcional): Tipo de animación al pasar el mouse. Por defecto es "right".
        - on_click (callable, opcional): Función a ejecutar al hacer clic en el botón. Por defecto es None.
        """
        self.__text = text
        self.__text_align = text_align
        self.__font = pygame.font.Font(f"./src/assets/fonts/{font}.ttf", font_size)
        self.__font_color = font_color
        self.__hover_color = hover_color

        self.__x = x
        self.__y = y
        self.__width = self.__font.size(text)[0] + 20 if width == "auto" else width
        self.__height = self.__font.size(text)[1] - 20 if height == "auto" else height
        self.__align = align

        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))
        self.__background_color = background_color

        self.__border = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))
        self.__border_color = border_color
        self.__border_width = border_width
        self.__border_radius = border_radius

     
        self.__init_x = x
        self.__init_y = y
        self.__current_color = pygame.Color(font_color)
        self.__animation = animation

        self.__on_click = on_click

        self.__is_pressing = False
    @property
    def text(self) -> str:
        """
        Obtiene el texto actual del botón.

        Returns:
        - str: Texto actual del botón.
        """
        return self.__text

    def __set_pos(self, x: int, y: int):
        """
        Establece la posición del botón gradualmente.

        Args:
        - x (int): Nueva posición x del botón.
        - y (int): Nueva posición y del botón.
        """
        self.__x = lerp(self.__x, x, 0.1)
        self.__y = lerp(self.__y, y, 0.1)

        if self.__align == "topleft":
            self.__rect.topleft = (self.__x, self.__y)
            self.__border.topleft = (self.__x, self.__y)
        elif self.__align == "center":
            self.__rect.center = (self.__x, self.__y)
            self.__border.center = (self.__x, self.__y)

    def __set_color(self, color: tuple[int, int, int] | str):
        """
        Establece el color actual del botón.

        Args:
        - color (tuple[int, int, int] | str): Nuevo color del botón.
        """
        self.__current_color = self.__current_color.lerp(color, 0.1)

    def update(self, dt: float):
        """
        Actualiza el estado del botón en cada fotograma del juego.

        Args:
        - dt (float): Delta de tiempo desde el último fotograma.
        """
        if self.__on_click is None:
            return

        if not pygame.mouse.get_pressed()[0]:
            self.__is_pressing = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.__rect.collidepoint(mouse_x, mouse_y):
            if self.__animation == "right":
                self.__set_pos(self.__init_x + 15, self.__init_y)
            elif self.__animation == "left":
                self.__set_pos(self.__init_x - 15, self.__init_y)
            elif self.__animation == "up":
                self.__set_pos(self.__init_x, self.__init_y - 10)
            elif self.__animation == "down":
                self.__set_pos(self.__init_x, self.__init_y + 10)

            self.__set_color(self.__hover_color)

            if pygame.mouse.get_pressed()[0] and not self.__is_pressing:
                if self.__on_click is not None:
                    self.__on_click(self)
                self.__is_pressing = True
        else:
            self.__set_pos(self.__init_x, self.__init_y)
            self.__set_color(self.__font_color)
       

    def on_keydown(self, event: pygame.event):
        """
        Maneja el evento de presionar una tecla.

        Args:
        - event (pygame.event): Evento de presionar una tecla.
        """
        pass  # No hay acciones específicas para manejar eventos de teclado

    def draw(self, surface: pygame.Surface):
        """
        Dibuja el botón en la superficie especificada.

        Args:
        - surface (pygame.Surface): Superficie en la que se dibujará el botón.
        """
       
        if self.__background_color is not None:
            pygame.draw.rect(surface, self.__background_color, self.__rect, border_radius=self.__border_radius)

     
        if self.__border_width > 0:
            pygame.draw.rect(surface, self.__border_color, self.__border,
                             border_radius=self.__border_radius, width=self.__border_width)


        text = self.__font.render(self.__text, True, self.__current_color)
        txt_rect = text.get_rect()

        x = self.__x
        y = self.__y

        if self.__align == "topleft":
            if self.__text_align == "center":
                x += self.__width // 2
                y += self.__height // 2
            elif self.__text_align == "left":
                x += 10
                y += self.__height // 2
        if self.__align == "center":
            if self.__text_align == "left":
                x -= self.__width // 2 - 10

        if self.__text_align == "center":
            txt_rect.center = (x, y)
        elif self.__text_align == "left":
            txt_rect.midleft = (x, y)

        surface.blit(text, txt_rect)