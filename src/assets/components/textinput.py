import pygame
from .component import Component

class TextInput(Component):

    def __init__(self, x: int, y: int,
                 width: int, height: int,
                 default: str = "",
                 max_length_input: int | str = "auto",
                 text_align: str = "center",
                 align: str = "topleft",
                 font: str = "ThaleahFat",
                 font_size: int = 32,
                 font_color: tuple[int, int, int] | str = "white",
                 background_color: tuple[int, int, int] | str | None = None,
                 border_radius: int = 0,
                 border_width: int = 0,
                 border_color: tuple[int, int, int] | str = "black",
                 numeric: bool = False):

        """
        Inicializa un componente de entrada de texto en el juego.

        Args:
            x (int): Posición x de la caja de texto.
            y (int): Posición y de la caja de texto.
            width (int): Ancho de la caja de texto.
            height (int): Alto de la caja de texto.
            default (str, opcional): Texto por defecto. Por defecto es "".
            max_length_input (int | str, opcional): Longitud máxima del texto. Por defecto es "auto".
            text_align (str, opcional): Alineación del texto. Por defecto es "center".
            align (str, opcional): Alineación de la caja de texto. Por defecto es "topleft".
            font (str, opcional): Fuente del texto. Por defecto es "ThaleahFat".
            font_size (int, opcional): Tamaño de la fuente. Por defecto es 32.
            font_color (tuple[int, int, int] | str, opcional): Color de la fuente. Por defecto es "white".
            background_color (tuple[int, int, int] | str | None, opcional): Color de fondo de la caja de texto. Por defecto es None.
            border_radius (int, opcional): Radio del borde de la caja de texto. Por defecto es 0.
            border_width (int, opcional): Ancho del borde de la caja de texto. Por defecto es 0.
            border_color (tuple[int, int, int] | str, opcional): Color del borde de la caja de texto. Por defecto es "black".
            numeric (bool, opcional): Indica si se espera entrada numérica. Por defecto es False.
        """

        # Posición y tamaño de la caja de texto
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

        # Texto
        self.__text_align = text_align
        self.__text_color = font_color
        self.__text_font = pygame.font.Font(f"./src/assets/fonts/{font}.ttf", font_size)
        self.__max_length_input = max_length_input

        # Superficie
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))
        if align == "center":
            self.__rect.center = (self.__x, self.__y)

        self.__background_color = background_color

        # Superficie de la caja de texto
        self.__input_rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))
        if align == "center":
            self.__input_rect.center = (self.__x, self.__y)

        self.__border_width = border_width
        self.__border_radius = border_radius
        self.__border_color = border_color

        # Guarda la entrada de texto del usuario
        self.__user_input = default

        # Verifica si la caja de texto está en foco
        self.__on_focus = False

        # Limita el tipo de entrada
        self.__numeric = numeric

    @property
    def text(self) -> str | int:
        """
        Obtiene el texto actual en la caja de texto.

        Returns:
            str | int: Texto actual en la caja de texto.
        """
        if self.__numeric:
            if self.__user_input == "":
                return 0
            return int(self.__user_input)
        return self.__user_input

    def on_keydown(self, event: pygame.event):
        """
        Maneja el evento de tecla presionada.

        Args:
            event (pygame.event): Evento de tecla presionada.
        """
        if self.__on_focus:
            if event.key == pygame.K_BACKSPACE:  # El Unicode genera un carácter inválido al presionar retroceso
                self.__user_input = self.__user_input[0:-1]
            elif event.unicode.isprintable():  # Verifica si el carácter es imprimible
                if self.__max_length_input == "auto" and self.__text_font.size(self.__user_input)[0] >= self.__width - 30:
                    return  # No añade la entrada si el texto ya está en el límite de la caja de texto

                if self.__max_length_input == "auto" or len(self.__user_input) < self.__max_length_input:
                    if self.__numeric and not event.unicode.isnumeric():
                        return
                    self.__user_input += event.unicode  # Añade la entrada a la cadena, ya sea número o letra

    def update(self, dt: float):
        """
        Actualiza el componente de entrada de texto.

        Args:
            dt (float): Delta time. Tiempo desde el último frame.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            # Quita el foco de la caja de texto
            if not self.__input_rect.collidepoint(mouse_x, mouse_y):
                self.__on_focus = False

            # Pone el foco en la caja de texto
            if self.__input_rect.collidepoint(mouse_x, mouse_y):
                self.__on_focus = True

    def draw(self, surface: pygame.Surface):
        """
        Dibuja el componente de entrada de texto en la superficie especificada.

        Args:
            surface (pygame.Surface): Superficie donde se dibujará el texto.
        """
        # Dibuja el fondo
        if self.__background_color is not None:
            pygame.draw.rect(surface, self.__background_color, self.__rect, border_radius=self.__border_radius)

        # Dibuja la superficie del input
        if self.__border_width > 0:
            pygame.draw.rect(surface, self.__border_color, self.__input_rect,
                             border_radius=self.__border_radius, width=self.__border_width)

        # Coloca la entrada en las coordenadas de la superficie
        input_surface = self.__text_font.render(self.__user_input, True, self.__text_color)
        input_width, input_height = input_surface.get_size()

        # Coloca la entrada en el centro de la superficie
        if self.__text_align == "center":
            surface.blit(input_surface, (
                self.__input_rect.x - input_width / 2 + self.__input_rect.w / 2,
                self.__input_rect.y - input_height / 2 + self.__input_rect.h / 2
            ))
        elif self.__text_align == "left":
            surface.blit(input_surface, (
                self.__input_rect.x + 10,
                self.__input_rect.y + self.__input_rect.h / 2 - input_height / 2
            ))

        # Autoajuste
        self.__input_rect.w = max(self.__width, input_surface.get_width() + 20)
        self.__rect.w = self.__input_rect.w
        self.__rect.x = self.__input_rect.x
