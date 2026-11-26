"""Entri Make Fun — bounty teks "Name the Robot Band" (Akun 1, v3).

Bounty: beri nama band robot + satu baris lucu (judge AI pairwise).
Teks final v3 (144 karakter, gate 1-200 lolos):

    The Password Managers — hit single 'Your Password Has Expired': I forgot
    the one password I was built to remember. It's on a sticky note. On me.

Kriteria juri: nama band yang lucu dan mudah diingat, satu baris yang
punya adegan konkret + twist memalukan diri di akhir. Sudut v3: pengakuan
orang pertama dari sebuah password manager — perangkat baru (bukan captcha,
bukan baterai, bukan Roomba), jadi tidak bertabrakan dengan tetangga.

Revisi v3 (reviser): teks dipertahankan apa adanya (144 karakter, sudah
lolos gate dan sudah diuji deterministik); main() kini memeriksa sendiri
panjang gate 1-200 sebelum menulis, supaya pelanggaran gate ketahuan
di sisi program, bukan di sisi juri.
"""

import os

ENTRY = (
    "The Password Managers — hit single 'Your Password Has Expired': "
    "I forgot the one password I was built to remember. "
    "It's on a sticky note. On me."
)


def build_entry():
    """Kembalikan teks entri v3 persis."""
    return ENTRY


def main():
    entry = build_entry()
    if not 1 <= len(entry) <= 200:
        raise SystemExit(
            f"entry {len(entry)} karakter, di luar gate 1-200"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
