from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

session = WolframLanguageSession()

class Wolfram:

    def __init__(self):
        self.session = WolframLanguageSession()

    def wolfram_run(self, expr):
        return self.session(wlexpr(expr))

