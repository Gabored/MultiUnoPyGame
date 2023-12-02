import pygame
import threading

from assets.components import Component, WarningText


def on_event(type_: int):
    """Decorador para devoluciones de llamada de eventos.

    Args:
        type_ (int): El tipo de evento.
    """

    def inner(func: callable):
        Engine.add_event(type_, func)
        return func
    return inner


class Engine:
    _width: int
    _height: int
    _fps: int

    _surface: pygame.Surface
    _clock: pygame.time.Clock

    __is_running: bool

    __server_thread: threading.Thread
    __components: dict[str, Component]

    __instances: int = 0
    __events: dict[int, list[callable]] = {}

    def __new__(cls, *args, **kwargs):
        cls.__instances += 1
        if cls.__instances > 1:
            raise RuntimeError("Solo se puede crear una instancia de Engine")
        return super().__new__(cls)

    def __init__(self, width: int = 800, height: int = 600, fps: int = 60, caption: str = "Ventana") -> None:
        """Inicializa el motor del juego.

        Args:
            width (int, opcional): Ancho de la ventana del juego. Predeterminado a 800.
            height (int, opcional): Altura de la ventana del juego. Predeterminado a 600.
            fps (int, opcional): FPS objetivo del juego. Predeterminado a 60.
            caption (str, opcional): Título de la ventana. Predeterminado a "Ventana".
        """

        self._width, self._height = width, height
        self._fps = fps

        pygame.init()

        if not pygame.font.get_init():  # Si la fuente no está inicializada, inicialízala
            pygame.font.init()

        pygame.display.set_caption(caption)
        self._surface = pygame.display.set_mode((self._width, self._height))
        self._clock = pygame.time.Clock()

        self.__is_running = True
        self.__components = {}

        # El servidor necesita estar en un hilo separado para no bloquear el hilo principal
        self.__server_thread = threading.Thread(target=self.__handle_server)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @staticmethod
    def add_event(type_: int, callback: callable) -> None:
        """Añade una devolución de llamada de eventos.

        Args:
            type_ (int): El tipo de evento.
            callback (callable): La devolución de llamada.
        """

        if type_ not in Engine.__events.keys():
            Engine.__events[type_] = []

        Engine.__events[type_].append(callback)

    def __handle_events(self) -> None:
        """Maneja los eventos."""

        for event in pygame.event.get():
            # El usuario cerró la ventana
            if event.type == pygame.QUIT:
                self.__is_running = False

            if event.type == pygame.KEYDOWN:
                try:
                    for comp in self.__components.values():  # Dibuja los componentes
                        comp.on_keydown(event)
                except RuntimeError:
                    pass

            if event.type in self.__events.keys():
                for callback in self.__events[event.type]:
                    callback(self, event)

    def __handle_server(self) -> None:
        """Maneja el servidor."""

        ups = 20  # Limita el servidor a 20 TPS

        last = pygame.time.get_ticks()
        while self.__is_running:
            if pygame.time.get_ticks() - last >= 1000 // ups:
                self.update_server()
                last = pygame.time.get_ticks()

    def add_component(self, component: Component, id: str = None) -> None:
        """Añade un componente a la pantalla.

        Args:
            id (str, opcional): ID del componente. None por defecto.
            component (Component): El componente que se añadirá.
        """

        self.__components[id or str(len(self.__components))] = component

    def get_component(self, id: str) -> Component | None:
        """Obtiene un componente de la pantalla.

        Args:
            id (str): ID del componente.

        Returns:
            Component | None: El componente, si se encuentra.
        """

        return self.__components.get(id, None)

    def clear_components(self) -> None:
        """Elimina todos los componentes de la pantalla."""

        # Filtra para eliminar solo las advertencias
        temp = self.__components.copy()
        self.__components.clear()
        for key, comp in temp.items():
            if isinstance(comp, WarningText):
                self.__components[key] = comp

    def pop_component(self, id: str | None) -> Component | None:
        """Elimina un componente de la pantalla.

        Args:
            id (str): ID del componente.
        """

        return self.__components.pop(id, None)

    def run(self) -> None:
        """Ejecuta el juego."""

        dt = 0
        self.init()  # Inicializa el juego
        self.__server_thread.start()  # Inicia el hilo del servidor
        while self.__is_running:
            self.__handle_events()  # Maneja los eventos

            self.update(dt)  # Actualiza el juego
            try:
                for key, comp in self.__components.items():  # Actualiza los componentes
                    comp.update(dt)
                    if isinstance(comp, WarningText) and comp.is_expired:
                        self.pop_component(key)  # Elimina el componente si ha expirado
            except RuntimeError:
                pass

            self.draw()  # Dibuja el juego
            try:
                for comp in self.__components.values():  # Dibuja los componentes
                    comp.draw(self._surface)
            except RuntimeError:
                pass

            pygame.display.flip()  # Actualiza la pantalla
            dt = self._clock.tick(self._fps) / 1000  # Actualiza el delta de tiempo

    def init(self) -> None:
        """Inicializa el juego."""
        pass

    def update(self, dt: float) -> None:
        """Actualiza el juego."""
        pass

    def update_server(self) -> None:
        """Actualiza el servidor."""
        pass

    def draw(self) -> None:
        """Dibuja el juego."""
        pass
