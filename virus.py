#!/usr/bin/env python3
#dibuat oleh asep rizki ganteng
# Tidak melakukan koneksi, tidak mengirim file, tidak ada exploit.
# gausah diedit2  cikk
#tools berbahaya loh ya
import time
import random
import sys

# warna terminal (boleh dihapus kalau di Windows tanpa ANSI)
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

TEMPLATES = [
    "Berhasil kirim Virus anies to : {target}",
    "Succsses Send Anies To : {target}",
    "OK — Abah Anies delivered to {target}",
    "Status: Anies terkirim -> {target}",
    "virus anies sent successfully : {target}"
]

def fake_send(target, lines=30, min_delay=0.04, max_delay=0.18):
    for i in range(lines):
        # variasi kata biar keliatan real
        tpl = random.choice(TEMPLATES)
        prefix = random.choice([f"{GREEN}[+]{RESET}", f"{YELLOW}[!]{RESET}", f"{RED}[*]{RESET}"])
        suffix_noise = "" if random.random() < 0.7 else f"  ({random.randint(1,999)}ms)"
        print(f"{prefix} {tpl.format(target=target)}{suffix_noise}")
        # sedikit variasi kecepatan
        time.sleep(random.uniform(min_delay, max_delay))

def main():
    print("=== VIRUS TERMUX BERBAHAYA — VIP ONLY ===")
    target = input("Masukkan target (nomor/ID): ").strip()
    if not target:
        print("Target kosong — keluar.")
        sys.exit(0)

    try:
        lines = int(input("BERAPA SERANGAN YG DIKIRIM? [default 1000]: ") or 1000)
    except ValueError:
        lines = 1000

    print("\nMulai Serang... (Ctrl+C untuk berhenti)...\n")
    try:
        fake_send(target, lines=lines)
    except KeyboardInterrupt:
        print("\nDihentikan. Selesai.")
    print("\nSelesai. HP KORBAN DIPASTIKAN ADA VIRUSNYA.")

if __name__ == "__main__":
    main()