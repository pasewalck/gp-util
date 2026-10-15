from jona_gp_util.format_float_to_latex import scale_value,simple_de_format_latex

def simple_de_format_val_err_latex_scaled(val, err,decimals,digits=None):
    scaled_val,exp = scale_value(val,decimals)
    scaled_err,_ = scale_value(err,decimals)
    return rf"\left({scaled_val} \pm {scaled_err}\right)\cdot 10^{{{exp}}}"

def simple_de_format_val_err_latex(val, err,decimals,digits=None):
    return rf"\left({simple_de_format_latex(val,decimals)} \pm {simple_de_format_latex(err,decimals)}\right)"