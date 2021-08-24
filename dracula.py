from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

# session = WolframLanguageSession()

class Wolfram:

    def __init__(self):
        print("Starting the Wolfram Engine...")
        self.session = WolframLanguageSession()
        print("Wolfram Engine Started")

    def wolfram_run(self, expr):
        print("Returning evaluated value...\n")
        return self.session.evaluate(wlexpr(expr))

    def walpha_run(self, expr):
        print("Fetching results...\n")
        return self.session.evaluate(wl.WolframAlpha(expr, "Result"))