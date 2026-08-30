#!/usr/bin/env python3
"""mc siklarini yeniden dagit: dogru cevap dosya icinde sirayla A,B,C,D pozisyonlarina gider.
Kullanim: spread.py <dosya.js> [--dry]   (metni degistirmez, yalnizca sirayi ve antwoord'u duzeltir)"""
import re, sys, io

OPT_RE = re.compile(
    r'(?P<head>opties:\s*\[\s*\n)(?P<body>(?:[^\[\]]*?\n)??)(?P<tail>\s*\],\s*\n\s*antwoord:\s*)(?P<ans>\d+)',
    re.S)

def split_options(body):
    """Her secenek satirini (cok satirli olabilir) ayikla."""
    lines = body.rstrip('\n').split('\n')
    opts, cur = [], []
    for ln in lines:
        cur.append(ln)
        s = ln.rstrip()
        # bir secenek, satir sonu tirnak+virgul ya da tirnakla biterse tamamlanir
        if s.endswith('",') or s.endswith('"'):
            opts.append('\n'.join(cur)); cur = []
    if cur:
        opts.append('\n'.join(cur))
    return opts

def normalize(opts):
    """Son elemanin virgulunu kaldir, digerlerine ekle."""
    out = []
    for i, o in enumerate(opts):
        stripped = o.rstrip()
        if stripped.endswith(','):
            stripped = stripped[:-1]
        out.append(stripped + (',' if i < len(opts) - 1 else ''))
    return out

def process(path, dry=False):
    src = open(path, encoding='utf-8').read()
    counter = [0]
    changed = [0]

    def repl(m):
        body, ans = m.group('body'), int(m.group('ans'))
        opts = split_options(body)
        if len(opts) < 2 or ans >= len(opts):
            return m.group(0)
        target = counter[0] % len(opts)
        counter[0] += 1
        if target != ans:
            opts[ans], opts[target] = opts[target], opts[ans]
            changed[0] += 1
        new_body = '\n'.join(normalize(opts)) + '\n'
        return m.group('head') + new_body + m.group('tail') + str(target)

    out = OPT_RE.sub(repl, src)
    if not dry and out != src:
        open(path, 'w', encoding='utf-8').write(out)
    return counter[0], changed[0]

if __name__ == '__main__':
    files = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry' in sys.argv
    tot = ch = 0
    for f in files:
        n, c = process(f, dry)
        tot += n; ch += c
        print(f'  {f.split("/")[-1]}: {n} mc, {c} yeri degisti')
    print(f'TOPLAM {tot} mc sorusu, {ch} tanesinin dogru sikki tasindi')

# --- ek: tek satirlik  opties: ["a","b","c","d"],  bicimi ---
ONE_RE = re.compile(r'(?P<head>opties:\s*\[)(?P<body>[^\n]*?)(?P<tail>\],\s*\n\s*antwoord:\s*)(?P<ans>\d+)')

def split_inline(body):
    """Tirnak icindeki virgulleri sayma; ust duzey ogeleri ayir."""
    items, cur, inq, esc = [], '', False, False
    for ch in body:
        if esc:
            cur += ch; esc = False; continue
        if ch == '\\':
            cur += ch; esc = True; continue
        if ch == '"':
            inq = not inq; cur += ch; continue
        if ch == ',' and not inq:
            items.append(cur); cur = ''; continue
        cur += ch
    if cur.strip():
        items.append(cur)
    return [i.strip() for i in items]

def process_inline(path, dry=False):
    src = open(path, encoding='utf-8').read()
    counter = [0]; changed = [0]
    def repl(m):
        opts = split_inline(m.group('body'))
        ans = int(m.group('ans'))
        if len(opts) < 2 or ans >= len(opts):
            return m.group(0)
        target = counter[0] % len(opts)
        counter[0] += 1
        if target != ans:
            opts[ans], opts[target] = opts[target], opts[ans]
            changed[0] += 1
        return m.group('head') + ', '.join(opts) + m.group('tail') + str(target)
    out = ONE_RE.sub(repl, src)
    if not dry and out != src:
        open(path, 'w', encoding='utf-8').write(out)
    return counter[0], changed[0]

def spread_file(path, dry=False):
    """Iki bicimi TEK sayacla isler (karisik dosyalarda dagilim bozulmasin)."""
    src = open(path, encoding='utf-8').read()
    counter = [0]; changed = [0]
    def mk(splitter, join_fn):
        def repl(m):
            opts = splitter(m.group('body')); ans = int(m.group('ans'))
            if len(opts) < 2 or ans >= len(opts):
                return m.group(0)
            t = counter[0] % len(opts); counter[0] += 1
            if t != ans:
                opts[ans], opts[t] = opts[t], opts[ans]; changed[0] += 1
            return m.group('head') + join_fn(opts) + m.group('tail') + str(t)
        return repl
    out = OPT_RE.sub(mk(split_options, lambda o: '\n'.join(normalize(o)) + '\n'), src)
    out = ONE_RE.sub(mk(split_inline, lambda o: ', '.join(o)), out)
    if not dry and out != src:
        open(path, 'w', encoding='utf-8').write(out)
    return counter[0], changed[0]
