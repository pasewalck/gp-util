import matplotlib.pyplot as plt

class use_figure:
    def __init__(self, path=None,usetex=True,use_locale=True,figsize = (14, 3)):
        self.path = path
        self.figsize = figsize
        self.usetex = usetex
        self.use_locale = use_locale

    def __enter__(self):
        plt.rcParams.update({
            'font.family': 'Liberation Serif',
            'text.usetex': self.usetex,
            'text.latex.preamble': r'\usepackage{icomma}',
            'axes.formatter.use_locale': self.use_locale
        })

        plt.rcParams.update({'font.size': 16})
        plt.rcParams.update({'axes.linewidth': 0.5})

        fig = plt.figure(figsize=self.figsize)

        return fig

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.path is not None:
            plt.savefig(self.path, bbox_inches='tight')
        plt.show()
