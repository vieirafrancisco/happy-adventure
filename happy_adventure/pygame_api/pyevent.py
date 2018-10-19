import pygame

class Events:
    def __init__(self):
        self.after_events = []
        self.callback_events = []

        self.dict_events = {
            pygame.KEYUP : self.key_release,
            pygame.KEYDOWN : self.key_press,
            pygame.MOUSEMOTION : self.mouse_move,
            30 : self.game_time,
            31: self.key_pressed,
        }

    def mouse_move(self, event):
        pass

    def key_press(self, event):
        pass

    def key_release(self, event):
        pass

    def key_pressed(self, event):
        pass

    def game_time(self, event):
        for after_event in self.after_events:
            time, callback = after_event

            if event.time % time == 0:
                callback(event)

    def add_after_event(self, time, callback):
        self.after_events.append((time, callback))
    
    def add_callback_event(self, event_type, callback):
        self.callback_events.append(event_type, callback)