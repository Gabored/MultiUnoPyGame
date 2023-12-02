import socket
import pickle

from typing import Any
from core.game.match import Match

class Network:
    __id: int
    __host: str
    __port: int

    __running: bool
    __client: socket.socket | None

    def __init__(self, host: str, port: int):
        """Inicializa la conexión con el servidor.

        Args:
            host (str): Dirección del servidor.
            port (int): Puerto del servidor.
        """
        self.__host = host
        self.__port = port
        self.__client = None
        self.__id = self.connect()

    @property
    def id(self) -> int:
        return self.__id

    @staticmethod
    def server_running(ip: str, port: int) -> bool:
        """Verifica si el servidor está en línea."""
        if port < 1 or port > 65535:
            return False
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
            return True
        except socket.error:
            return False

    @staticmethod
    def port_in_use(port: int) -> bool:
        """Verifica si el puerto está en uso."""
        if port < 1 or port > 65535:
            return False
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("localhost", port))
            return False
        except socket.error:
            return True

    def connect(self) -> int:
        """Conecta al cliente con el servidor."""
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect((self.__host, self.__port))
        self.__client.settimeout(0.2)  # Evita que el cliente quede atrapado en recv
        self.__running = True

        print(f"[Network] Conectado a {self.__host}:{self.__port}")
        while True:
            try:
                return int(self.__client.recv(1024).decode())
            except socket.error:
                pass

    def disconnect(self):
        """Desconecta al cliente del servidor."""
        print("[Network] Desconectando cliente...")
        self.__running = False
        self.__client.close()

    def send(self, data: dict[str, Any]) -> Match | None:
        """Envía datos al servidor.

        Args:
            data (dict[str, Any]): Datos a enviar al servidor.

        Returns:
            Match | None: Partida actualizada o None si no se puede enviar/recibir.

        Ejemplos:
            >>> network = Network("localhost", 5555)
            >>> network.send({"type": "GET"})
            Match(...)
        """
        if self.__running:
            data["id"] = self.__id

            try:
                self.__client.send(pickle.dumps(data))  # Envía datos al servidor
                return pickle.loads(self.__client.recv(10240))  # Devuelve la partida (10kb)
            except socket.error as e:
                print(f"[Network] Error: {e}")
            except pickle.UnpicklingError:
                return None
            except EOFError:
                return None
