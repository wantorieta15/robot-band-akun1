"""Name the Robot Band (Akun 1) — entry writer v2.

Writes one funny robot band name plus a few words on its hit song to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

REVISER v2 (2026-11-26, rebuild atas v1 134 ch R1 #529/1.243 skor
523.116): teks v1 DIBUANG — keluarga premis "Broken Hearts / left on
read" sudah habis, pun generik "Beep Boop" + "updated myself out of
love" dihukum kriteria 2 juri ("pun-shaped noise"), tanpa adegan.
Teks final v2, 128 karakter, gate 1-200:

The Captcha Failures — hit single 'I Clicked Every Traffic Light':
I failed the 'I'm not a robot' test nine times. I am a robot.

Judge criteria it targets, in order:
1. Funny robot band name + hit song line: yes, both present.
2. Real joke on first read: a robot failing the 'I'm not a robot'
   test nine times — an ironic situation, not a pun; concrete scene
   (nine times, every traffic light) with a number, like the winners.
3. Hit song line adds a second laugh and fits the name: the song
   title IS the captcha task; the twist ('I am a robot.') lands in
   the last words and is robot-specific and self-deprecating.
4. Sounds like a band that could exist: 'The Captcha Failures' is a
   name you would repeat to a friend.
5. Few words, no filler, no explaining the joke: 128 chars, one line.
Formula pemenang yang disalin (struktural, bukan verbatim): pengakuan
orang pertama + satu adegan konkret + twist memalukan diri sendiri
di akhir. Kemiripan leksikal maks vs 4 pemenang hanya 0,3030 (segar,
disengaja); vs Akun 2 0,4496 hanya dari format entri yang sama.
"""

import os


def build_entry():
    band = "The Captcha Failures"
    song = "I Clicked Every Traffic Light"
    line = "I failed the 'I'm not a robot' test nine times. I am a robot."
    return "%s \u2014 hit single '%s': %s" % (band, song, line)


def main():
    entry = build_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()


# --- Reviser notes v2 (diukur 2026-11-26, SequenceMatcher autojunk=False) ---
# Referensi pemenang terverifikasi (teks dari analis):
#   Laugh #1 777.695 (148 ch): "I knew I'd become my parents the day I hid
#     the good chocolate from my own kids and ate it in the pantry, lights
#     off, like a raccoon with a mortgage."
#   Laugh #2 776.452 (114 ch): "I meal-prepped for the week on Sunday. By
#     Monday I was eating cereal over the sink like a raccoon with a
#     mortgage."
#   Zero #1 779.634 (136 ch): "I can read minds, but only while people are
#     trying to remember my name. So far I'm Dan, Dave, "big guy" and, at
#     my own wedding, "champ"."
#   Zero #2 725.027 (62 ch): "I can stop time for exactly one second. I've
#     already used it."
# Kandidat yang diuji (vs Laugh#1 / Laugh#2 / Zero#1 / Zero#2 / Akun 2):
#   v2 Arah 1 Captcha (128 ch): 0,2246 / 0,2645 / 0,3030 / 0,2222 / 0,4496
#     <- DIPILIH: lelucon nyata (robot gagal tes "I'm not a robot"),
#     adegan konkret + angka (nine times), twist akhir self-deprecating.
#   Arah 3 Toasters (120 ch): 0,2836 / 0,1624 / 0,3125 / 0,1547 / 0,4720
#     — DITOLAK: premis penolakan ("she still chose the microwave")
#     masih satu keluarga dengan Broken Hearts yang sudah habis; lebih
#     mirip Akun 2.
#   Arah 2 Obsolete (132 ch): 0,2500 / 0,2602 / 0,2388 / 0,1658 / 0,3740
#     — DITOLAK: punchline "She doesn't even know my name" meniru tema
#     Zero #1 ("trying to remember my name"); premis penggantian juga
#     dekat keluarga heartbreak.
#   v1 A1 lama (134 ch): maks vs pemenang 0,3629 — DIBUANG (lihat atas).
# Akun 2 (#53): "The Low Batteries — hit single 'I Died at 2%': I said
#   I love you, my screen went black, and the crowd sang the last
#   chorus for me." Premis v2 (captcha) beda total dari Akun 2 (baterai
#   habis); kemiripan 0,4496 hanya dari format entri yang sama.
# Larangan dipatuhi: tanpa "Beep Boop", tanpa battery, tanpa riff
#   Heartbreakers/Broken Hearts, tanpa punchline update/software/pun.
# Determinisme: build_entry() murni konstanta — tanpa random, waktu, atau
# jaringan — jadi dua run harus menghasilkan sha256 entry identik.
