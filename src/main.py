def main():
    try:
        import pygame
    except ImportError:
        print("ERROR: Pygame no está instalado. Por favor, instálalo usando `pip install pygame`")
        exit(1)

    if pygame.version.vernum < (2, 5, 0):
        print("ERROR: La versión de Pygame es demasiado antigua. Por favor, actualízala usando `pip install pygame --upgrade`")
        exit(1)

    from core.client import Client

    client = Client()
    client.run()


if __name__ == "__main__":
    main()
