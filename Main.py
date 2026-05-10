from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from random import randint

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake = [(10, 10)]
        self.direction = (1, 0)
        self.food = (15, 15)
        Clock.schedule_interval(self.update, 0.2)

    def update(self, dt):
        # Mover cabeza
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        self.snake.insert(0, new_head)
        
        # Comer o seguir
        if new_head == self.food:
            self.food = (randint(0, 19), randint(0, 19))
        else:
            self.snake.pop()

        # Dibujar
        self.canvas.clear()
        with self.canvas:
            Color(1, 0, 0) # Comida roja
            Rectangle(pos=(self.food[0]*20, self.food[1]*20), size=(18, 18))
            Color(0, 1, 0) # Serpiente verde
            for part in self.snake:
                Rectangle(pos=(part[0]*20, part[1]*20), size=(18, 18))

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == '__main__':
    SnakeApp().run()
