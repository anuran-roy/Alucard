from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

# session = WolframLanguageSession()

class Wolfram:

    def __init__(self):
        print("Wolfram Class Initialized")
        self.session = WolframLanguageSession()
        print("Wolfram Engine Started")

    def wolfram_run(self, expr):
        print("Returning evaluated value...\n")
        return self.session.evaluate(wlexpr(expr))

