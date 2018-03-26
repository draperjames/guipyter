import os


def detect_environ():
    """Check the runtime environment.
    """
    envs = dict()
    kube = list(filter(lambda x: "KUBE" in x, os.environ.keys()))
    bind = list(filter(lambda x: "BINDER" in x, os.environ.keys()))
    jpy = list(filter(lambda x: "JPY" in x, os.environ.keys()))
    qt = list(filter(lambda x: "QT" in x, os.environ.keys()))
    envs["kubernetes"] = bool(len(kube))
    envs["binder"] = bool(len(bind))
    envs["jupyter"] = bool(len(jpy))
    envs["QT"] = bool(len(qt))
    return envs
