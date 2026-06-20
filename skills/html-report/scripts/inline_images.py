#!/usr/bin/env python3
"""
로컬 이미지를 base64 data URI로 인라인해 HTML을 '단일 자체완결 파일'로 만든다.

왜: 보고서 파일 하나만 공유해도 이미지가 보이게 하기 위함. (외부 assets 폴더 의존 제거)

사용법:
    python inline_images.py report.html              # 같은 파일에 덮어쓰기
    python inline_images.py report.html --out out.html

동작:
- <img src="..."> 의 src 가 로컬 경로면 파일을 읽어 base64 data URI 로 치환한다.
- src 가 data: / http(s): / // 로 시작하면 건드리지 않는다.
- 경로는 HTML 파일이 있는 디렉터리 기준으로 해석한다.
- UTF-8 고정(한글 안전).
"""
import sys, os, re, base64, argparse

MIME = {
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
    ".gif": "image/gif", ".webp": "image/webp", ".svg": "image/svg+xml",
    ".avif": "image/avif",
}


def inline(html_path, out_path=None):
    html_path = os.path.abspath(html_path)
    base = os.path.dirname(html_path)
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    stats = {"n": 0, "bytes": 0, "miss": 0}
    pat = re.compile(r'(<img\b[^>]*?\bsrc\s*=\s*)(["\'])(.*?)\2', re.IGNORECASE | re.DOTALL)

    def repl(m):
        prefix, q, src = m.group(1), m.group(2), m.group(3)
        s = src.strip()
        if s[:5] == "data:" or s.startswith(("http://", "https://", "//")):
            return m.group(0)
        p = s.replace("\\", "/")
        cand = p if os.path.isabs(p) else os.path.join(base, p)
        if not os.path.isfile(cand):
            stats["miss"] += 1
            sys.stderr.write("  [skip: not found] %s\n" % s)
            return m.group(0)
        ext = os.path.splitext(cand)[1].lower()
        mime = MIME.get(ext, "application/octet-stream")
        with open(cand, "rb") as imgf:
            data = imgf.read()
        b64 = base64.b64encode(data).decode("ascii")
        stats["n"] += 1
        stats["bytes"] += len(data)
        return "%s%sdata:%s;base64,%s%s" % (prefix, q, mime, b64, q)

    new = pat.sub(repl, html)
    out = out_path or html_path
    with open(out, "w", encoding="utf-8") as f:
        f.write(new)

    print("inlined %d image(s), %.0f KB source -> %s" % (stats["n"], stats["bytes"] / 1024, out))
    if stats["miss"]:
        print("WARNING: %d <img> src not found (left as-is)" % stats["miss"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Inline local images into HTML as base64.")
    ap.add_argument("html", help="path to the HTML file")
    ap.add_argument("--out", default=None, help="output path (default: overwrite input)")
    args = ap.parse_args()
    inline(args.html, args.out)
