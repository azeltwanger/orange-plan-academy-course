import hashlib, sys
def fp(path):
    data = open(path,'rb').read()
    lines = data.split(b'\n')
    if lines and lines[-1] == b'': lines = lines[:-1]
    out = [f"FP {path} {len(lines)}"]
    for i, line in enumerate(lines, 1):
        ascii_bytes = bytes(b for b in line if b < 0x80)
        m = hashlib.md5(ascii_bytes).hexdigest()[:8]
        hb = '.'.join(f"{b:03o}" for b in line if b >= 0x80)
        if hb: hb += '.'
        out.append(f"{i}|{m}|{hb}")
    return '\n'.join(out)
if __name__ == '__main__':
    print(fp(sys.argv[1]))


def _units(s):
    out=[]
    for c in s:
        o=ord(c)
        if o>0xFFFF:
            o-=0x10000
            out.append(0xD800+(o>>10)); out.append(0xDC00+(o&0x3FF))
        else: out.append(o)
    return bytes(u%256 for u in out)

def sandbox_md5(path):
    return hashlib.md5(_units(open(path,'rb').read().decode('utf-8'))).hexdigest()
