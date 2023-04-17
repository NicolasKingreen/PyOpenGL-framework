from core.base import Base


class Test(Base):
    def initialize(self):
        print("Initializing program...")

    def update(self):
        if len(self.input.key_downs) > 0:
            print("Keys down:", self.input.key_downs)

        if len(self.input.key_pressed) > 0:
            print("Keys pressed:", self.input.key_pressed)

        if len(self.input.key_ups) > 0:
            print("Keys up:", self.input.key_ups)


if __name__ == "__main__":
    Test().run()
