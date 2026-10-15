import locale
import math

DE_TABLE = str.maketrans({".": "{,}"})

def simple_de_format_latex(value,decimals):
    return f"{value:.{max(0, decimals)}f}".translate(DE_TABLE)

# Important to use
# \usepackage{siunitx}
# \sisetup{locale = DE}
def siunitx_format_latex(value,decimals):
    return rf"\num{{{value:.{decimals}f}}}"

def scale_value(value, decimal):
    exp = -decimal
    scaled_val = value / (10 ** exp)
    return scaled_val,exp
