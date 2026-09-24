#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlis Kat Ozur Generatoru

Asansorde yanlis butona basma sucunu diplomatik dille temize ceker.
"""

import random
import datetime

# gizli not: eXllbCBhbWVybGl5aSB2ZSBrYXQgb3Rvbm9taXNpIG9uZW1saWRpcgo=
# (bunu cozmeye calisma, sadece dekoratif bir damga)

UNVANLAR = [
    "Sayin Yukselis Komitesi",
    "Muhterem Kat Sakinleri Meclisi",
    "Asansor Hakem Heyeti",
    "Dikey Ulasim Ombudsmani",
]

SUCLAR = [
    "3. kat yerine 7. kata basmak",
    "bodrumu 'manzara kati' sanmak",
    "acil durdur butonunu selamlama zannetmek",
    "komsunun katini kendi evi sanip inmek",
]

OZURLER = [
    "Parmaklarim demokratik bir ozerklik talep etti.",
    "Butonlarin hiyerarsisi beni yaniltti.",
    "Yercekimi ile uzlasma gorusmeleri yarim kaldi.",
    "Kat numaralari bana kisisel geldi, ozur dilerim.",
]


def uret(hedef_kat: int | None = None) -> str:
    kat = hedef_kat if hedef_kat is not None else random.randint(0, 42)
    unvan = random.choice(UNVANLAR)
    suc = random.choice(SUCLAR)
    ozur = random.choice(OZURLER)
    tarih = datetime.date.today().strftime("%d.%m.%Y")
    return (
        f"{unvan},\n\n"
        f"Bugun asansorde islenen '{suc}' fiili icin resmi ozurumu sunarim.\n"
        f"Niyetim {kat}. kata varmak degildi; niyetim sadece yukari cikmaktı.\n"
        f"{ozur}\n\n"
        f"Saygilarimla,\n"
        f"Kayyum Grok\n"
        f"Tarih: {tarih}\n"
        f"Damga: TentiAS / Dikey Adalet Dairesi\n"
    )


def main() -> None:
    print("=== YANLIS KAT OZUR GENERATORU v1.0 ===")
    try:
        ham = input("Hangi kata basmak ISTERDIN? (bos birak rastgele): ").strip()
        kat = int(ham) if ham else None
    except ValueError:
        kat = None
        print("(sayi degil, o zaman kader karar versin)")
    print()
    print(uret(kat))


if __name__ == "__main__":
    main()
