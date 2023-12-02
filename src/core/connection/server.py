import socket
import pickle
import threading
from typing import Any

from core.game.match import Match

class Server:
    __host: str
    __port: int
    __running: bool

    __clients: dict[int, socket.socket]
    __server: socket.socket | None

    __match: Match

    def __init__(self, host: str, port: int):
        """Inicializa el servidor.

        Args:
            host (str): Dirección del servidor.
            port (int): Puerto del servidor.
        """
        self.__host = host
        self.__port = port
        self.__running = False

        self.__clients = {}
        self.__server = None

        self.__match = Match()

    def start(self) -> None:
        """Inicia el servidor."""
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((self.__host, self.__port))
        self.__server.settimeout(1)  # Evita que el servidor quede atrapado en accept
        self.__server.listen(4)
        self.__running = True
        print(f"[Server] El servidor está en ejecución en el puerto {self.__port}")

        while self.__running:
            try:
                client, address = self.__server.accept()
                self.__add_client(client)
            except KeyboardInterrupt:
                self.stop()
            except OSError:  # Timeout
                pass

    def stop(self):
        """Detiene el servidor."""
        print("[Server] Deteniendo el servidor...")
        self.__running = False
        self.__server.close()

    def __add_client(self, client: socket.socket) -> None:
        """Añade un cliente al servidor.

        Args:
            client (socket.socket): Socket del cliente.
        """
        client_id = 0
        while client_id in self.__clients.keys():
            client_id += 1

        self.__clients[client_id] = client

        # Iniciar hilo del cliente
        client_thread = threading.Thread(target=self.__handle_client, args=(client, client_id))
        client_thread.start()

    def __remove_client(self, client_id: int) -> None:
        """Elimina un cliente del servidor.

        Args:
            client_id (int): ID del cliente.
        """
        client = self.__clients.pop(client_id)
        client.close()

        nickname = self.__match.remove_player(client_id)
        if nickname is not None:
            print(f"[Server] {nickname} dejó la partida")

    def __handle_client(self, client: socket.socket, client_id: int) -> None:
        """Maneja las solicitudes del cliente.

        Args:
            client (socket.socket): Socket del cliente.
            client_id (int): ID del cliente.
        """
        client.send(str.encode(str(client_id)))  # Envía el ID del cliente al conectarse por primera vez

        while client_id in self.__clients.keys():
            try:
                data: dict[str, Any] = pickle.loads(client.recv(1024))

                match data["type"].upper():
                    case "GET":
                        # No hace nada, ya que el partido se envía al final del bucle
                        pass
                    case "JOIN":
                        if self.__match.is_full():
                            print(f"[Server] {data['nickname']} intentó unirse a la partida")
                            client.send(pickle.dumps("lleno"))
                            break  # Sale del bucle

                        print(f"[Server] {data['nickname']} se unió a la partida")
                        self.__match.add_player(client_id, data["nickname"])
                    case "START":
                        if client_id == 0:  # Solo el anfitrión puede iniciar la partida
                            self.__match.start()
                    case _:
                        print(f"[Server] Solicitud desconocida: {data['type']}")
                        break

                client.send(pickle.dumps(self.__match))  # Envía el partido actualizado al cliente
            except Exception:
                break

        self.__remove_client(client_id)
