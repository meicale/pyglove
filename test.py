import pyglove as pg


@pg.symbolize
class Hello:
    def __init__(self, subject):
        self._greeting = f"Hello, {subject}!"

    def greet(self):
        print(self._greeting)


hello = Hello("bill, I love you")
hello.greet()

hello.rebind(subject="PyGlove")
hello.greet()

hello.rebind(subject=pg.oneof(["World", "PyGlove"]))
for h in pg.iter(hello):
    h.greet()
