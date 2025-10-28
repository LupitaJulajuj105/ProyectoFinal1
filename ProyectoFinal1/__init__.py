
# Load auto-create users signals
try:
    import usuarios_ext.signals_autocreate as _sig
    _sig.ready()
except Exception:
    pass
