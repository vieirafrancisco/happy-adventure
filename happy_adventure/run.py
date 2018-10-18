import pygame

from player import Player

# Main class
class Game:

    # Constructor
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.screen = None
        self.running = True
        self.player = None

    # Initialization
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0,145,0))
        self.player = Player(self.screen, 100, 100, 25, 25)

        self.running = True

    # Finalization
    def on_cleanup(self):
        pygame.quit()

    # Event handler
    def on_event(self, event):
        print(event)
        if event.type == pygame.QUIT:
            self.running = False

    # Loop
    def on_loop(self):
        pygame.display.update()

    # Renderer
    def on_render(self):
        self.player.draw()

    # Run the code
    def on_execute(self):
        if(self.on_init() == False):
            self.running = False

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_render()
            self.on_loop()

        self.on_cleanup()


if __name__ == '__main__':
    game = Game()
    game.on_execute()