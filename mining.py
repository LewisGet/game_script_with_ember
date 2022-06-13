import ember
import config
import os
import time


class Execute:
    def __init__(self, em):
        self.em = em
        self.basic_path = os.path.join(os.getcwd(), "ui", "mining")

    def move_to_mining(self):
        for step in range(5):
            image = ember.Image(os.path.join(self.basic_path, "fixing_steps", str(step + 1) + ".png"))

            if step + 1 == 3:
                image.Offset = ember.Location(0, -300)

            self.em.touch_first_image_find(image)
            time.sleep(1.2)

    def execute_mining(self):
        try:
            image = ember.Image(os.path.join(self.basic_path, "execute_steps", "1.png")).set_similarity(0.8)

            self.em.touch_first_image_find(image)
            time.sleep(3)
        except:
            self.move_to_mining()
            time.sleep(30)


def main():
    em = ember.Ember(config)

    for i in range(10):
        Execute(em).execute_mining()


if __name__ == '__main__':
    main()
