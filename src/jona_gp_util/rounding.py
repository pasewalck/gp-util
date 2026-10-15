import math
from decimal import localcontext, Decimal, ROUND_HALF_UP, ROUND_UP

def ceil(value,decimal):
    return math.ceil(value*(10**decimal))/(10**decimal)

# Done as described in din1333
def din_1333_round(value, error, exact=True):
    return din_1333_round_decimal(value,error) if exact else din_1333_round_float(value,error)

def din_1333_round_float(value, error):
    if error == 0 or not math.isfinite(error):
        return value, error, None, None

    abs_error = abs(error)
    log_10 = math.log10(abs_error)
    floored_log_10 = math.floor(log_10)

    decimals = -int(floored_log_10)
    digits=1
    first_significant_digit = round(error, decimals)*(10**decimals)


    if first_significant_digit == 1 or first_significant_digit == 1:
        decimals+=1
        digits+=1

    return round(value, decimals), ceil(error,decimals), decimals, digits

print(din_1333_round_float(0,10))

def din_1333_round_decimal(value, error):
    if error == 0 or not math.isfinite(error):
        return value, error, None, None

    with localcontext() as ctx:
        ctx.prec = 60

        err_abs = Decimal(repr(abs(float(error))))
        err = Decimal(repr(float(error)))
        val = Decimal(repr(float(value)))

        expo = err_abs.adjusted()

        significant_digit = int((err_abs.scaleb(-expo)).to_integral_value(ROUND_HALF_UP))

        if significant_digit == 1 or significant_digit == 2:
            decimals, digits = 1-expo, 2
        else:
            decimals, digits = -expo, 1

        q = Decimal(1).scaleb(-decimals)
        return (float(val.quantize(q, ROUND_HALF_UP)),
                float(err.quantize(q, ROUND_UP)),
                decimals, digits)

def ceil(value,decimal):
    return math.ceil(value*(10**decimal))/(10**decimal)

# Done as described in https://pdg.lbl.gov/2011/reviews/rpp2011-rev-rpp-intro.pdf
# Good read: https://stats.stackexchange.com/questions/100502/significant-digit-354-rule-from-particle-data-group
def pdg_round(value, error, exact=True):
    return pdg_round_decimal(value,error) if exact else pdg_round_float(value,error)

def pdg_round_decimal(value, error):
    if error == 0 or not math.isfinite(error):
        return value, error, None, None

    with localcontext() as ctx:
        ctx.prec = 60

        err_abs = Decimal(repr(abs(float(error))))
        err = Decimal(repr(float(error)))
        val = Decimal(repr(float(value)))

        expo = err_abs.adjusted()
        three_significant_digits = int((err_abs.scaleb(-expo) * 100).to_integral_value(ROUND_HALF_UP))
        if three_significant_digits == 1000:
            three_significant_digits, expo = 100, expo + 1
        if three_significant_digits <= 354:
            decimals, digits = 1 - expo, 2
        elif three_significant_digits >= 950:
            decimals, digits = -expo, 2
        else:
            decimals, digits = -expo, 1

        q = Decimal(1).scaleb(-decimals)
        return (float(val.quantize(q, ROUND_HALF_UP)),
                float(err.quantize(q, ROUND_HALF_UP)),
                decimals, digits)

def pdg_round_float(value, error):
    if error == 0 or not math.isfinite(error):
        return value, error, None, None

    abs_error = abs(error)
    log_10 = math.log10(abs_error)
    floored_log_10 = math.floor(log_10)

    decimals = -int(floored_log_10)
    three_significant_digits = round(error, decimals+2)*(10**(decimals+2))

    if three_significant_digits <= 354:
        return round(value, decimals+1), round(error, decimals+1), decimals+1, 2
    elif three_significant_digits >= 950:
        return round(value, decimals), 10**(1-decimals), decimals, 2
    else:
        return round(value, decimals), round(error, decimals), decimals, 1