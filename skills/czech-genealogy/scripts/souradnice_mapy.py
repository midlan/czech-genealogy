#!/usr/bin/env python3
"""Souřadnice domů podle čísla popisného přes Mapy.com REST API (geokódování).

Vstup: CSV (oddělovač ;, UTF-8) se sloupci
    id;dotaz;cast;cp[;obec]
  id    – libovolný identifikátor (např. ID místa v Gramps)
  dotaz – text hledání, např. „Vlašim 353“ nebo „Podchlumí 78, Mladá Boleslav“
  cast  – očekávaná část obce (municipality_part), např. „Podchlumí“; u obce
          bez částí její název
  cp    – číslo popisné, které musí výsledek mít
  obec  – nepovinné: obec, pod kterou část musí patřit (rozliší stejně
          pojmenované části různých obcí, např. Radošovice × Bystřice-Radošovice)

Výstup: CSV (UTF-8) se sloupci
    id;dotaz;stav;lat;lon;nalezeno;kandidati
  stav OK          – adresa s daným čp. v dané části obce
       nenalezeno  – nic přesně nesedí; zkontroluj sloupec kandidati (každý
                     kandidát i se souřadnicemi a částí obce)
       chyba       – chyba volání API

Použití:
    python souradnice_mapy.py mista.csv -o souradnice.csv
    python souradnice_mapy.py mista.csv            # výstup na stdout

API klíč: proměnná prostředí MAPY_API_KEY; když chybí a skript běží
v terminálu, zeptá se. Klíč získáš na https://developer.mapy.com/account/projects
(základní tarif zdarma, 250 000 kreditů/měsíc, jedno hledání = 4 kredity).
Jen standardní knihovna Pythonu.

Upozornění: najde DNEŠNÍ dům s daným čp. Historická čísla popisná se mohla
přečíslovat – shodu s historickým domem uváděj jako předpoklad.
"""
import argparse, csv, getpass, io, json, os, re, sys, time, urllib.parse, urllib.request

KEY_URL = "https://developer.mapy.com/account/projects"
API = "https://api.mapy.com/v1/geocode"


def api_key():
    key = os.environ.get("MAPY_API_KEY")
    if key:
        return key
    msg = f"Chybí API klíč Mapy.com. Získáš ho na {KEY_URL} (Projekty → API klíč)."
    if sys.stdin.isatty():
        key = getpass.getpass(msg + "\nZadej API klíč (nebo nastav MAPY_API_KEY): ").strip()
        if key:
            return key
    sys.exit(msg + " Pak ho nastav do proměnné prostředí MAPY_API_KEY.")


def geocode(key, query, limit=15):
    url = API + "?" + urllib.parse.urlencode(
        {"query": query, "lang": "cs", "limit": limit, "type": "regional.address", "apikey": key})
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.load(r).get("items", [])


CP_RE = re.compile(r"(?<!ev\. č\. )(?<!\d)(\d+)(?:/\d+[a-zA-Z]?)?$")  # „Ulice 268/21“ → 268; čo se ignoruje


def parts(item):
    s = {x.get("type", "").replace("regional.", ""): x.get("name", "") for x in item.get("regionalStructure", [])}
    return s.get("municipality_part", ""), s.get("municipality", "")


def matches(item, cast, cp, obec=""):
    if "ev. č." in item.get("name", ""):
        return False
    m = CP_RE.search(item.get("name", "").strip())
    if not m or m.group(1) != cp:
        return False
    part, muni = parts(item)
    if obec and muni != obec:
        return False
    return part == cast or (not part and muni == cast)


def describe(item):
    pos = item.get("position", {})
    part, muni = parts(item)
    return f'{item.get("name")} [{muni} – {part}] ({pos.get("lat", 0):.6f}, {pos.get("lon", 0):.6f})'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("vstup", help="CSV id;dotaz;cast;cp[;obec] (UTF-8, oddělovač ;)")
    ap.add_argument("-o", "--vystup", help="výstupní CSV (UTF-8); bez něj stdout")
    a = ap.parse_args()
    key = api_key()
    with open(a.vstup, encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f, delimiter=";") if r.get("id")]
    out = open(a.vystup, "w", encoding="utf-8", newline="") if a.vystup else \
        io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="")
    w = csv.writer(out, delimiter=";")
    w.writerow(["id", "dotaz", "stav", "lat", "lon", "nalezeno", "kandidati"])
    for r in rows:
        q, cast, cp = r["dotaz"].strip(), r["cast"].strip(), r["cp"].strip()
        obec = (r.get("obec") or "").strip()
        try:
            items = geocode(key, q)
        except Exception as e:
            w.writerow([r["id"], q, "chyba", "", "", str(e), ""]); continue
        hit = next((it for it in items if matches(it, cast, cp, obec)), None)
        kand = " | ".join(describe(it) for it in items)
        if hit:
            pos = hit["position"]
            w.writerow([r["id"], q, "OK", f'{pos["lat"]:.6f}', f'{pos["lon"]:.6f}', describe(hit), kand])
        else:
            w.writerow([r["id"], q, "nenalezeno", "", "", "", kand])
        out.flush()
        time.sleep(0.2)
    if a.vystup:
        out.close()


if __name__ == "__main__":
    main()
