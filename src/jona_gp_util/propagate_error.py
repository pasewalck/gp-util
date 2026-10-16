import numpy as np

def mc_propagate_error(fn, param_values, param_errors,n=20000, dist="normal"):
    vals = [np.asarray(v) for v in param_values]
    errs = [np.asarray(e) for e in param_errors]

    shape = np.broadcast_shapes(*[a.shape for a in vals],
                                *[a.shape for a in errs])
    x0 = np.asarray([np.broadcast_to(a, shape) for a in vals], float)
    raw = np.asarray([np.broadcast_to(a, shape) for a in errs], float)

    s = raw / np.sqrt(3.0) if dist == "uniform" else raw
    cov = np.diag(s ** 2)

    rng = np.random.default_rng(None)

    draws = rng.multivariate_normal(x0, cov, n)

    ys = np.array([fn(*row) for row in draws])
    return ys.mean(), ys.std(ddof=1)
