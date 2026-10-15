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

def simple_de_format_latex_scaled(val, err,decimals):
    scaled_val,exp = scale_value(val,decimals)
    scaled_err,_ = scale_value(err,decimals)

    return rf"\left({scaled_val} \pm {scaled_err}\right)\cdot 10^{{{exp}}}"