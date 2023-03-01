class Colors:
    def __init__(self):
        self.reset = "\033[0m"
        self.style = lambda styled_text: f"{styled_text}{self.reset}"
        self.bold = lambda text: self.style(f"\033[01m{text}")
        self.disable = "\033[02m"
        self.underline = "\033[04m"
        self.reverse = "\033[07m"
        self.strikethrough = "\033[09m"
        self.invisible = "\033[08m"
        self.black = lambda text: self.style(f"\033[30m{text}")
        self.red = lambda text: self.style(f"\033[31m{text}")
        self.green = lambda text: self.style(f"\033[32m{text}")
        self.orange = lambda text: self.style(f"\033[33m{text}")
        self.blue = lambda text: self.style(f"\033[34m{text}")
        self.purple = lambda text: self.style(f"\033[35m{text}")
        self.cyan = lambda text: self.style(f"\033[36m{text}")
        self.lightgrey = lambda text: self.style(f"\033[37m{text}")
        self.darkgrey = lambda text: self.style(f"\033[90m{text}")
        self.lightred = lambda text: self.style(f"\033[91m{text}")
        self.lightgreen = lambda text: self.style(f"\033[92m{text}")
        self.yellow = lambda text: self.style(f"\033[93m{text}")
        self.lightblue = lambda text: self.style(f"\033[94m{text}")
        self.pink = lambda text: self.style(f"\033[95m{text}")
        self.lightcyan = lambda text: self.style(f"\033[96m{text}")
