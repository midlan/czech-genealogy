# czech-genealogy

Skill pro [Claude](https://claude.ai), který pomáhá s **genealogickým výzkumem v českých a slovenských matrikách a archivech** a s údržbou rodokmenu v programu [Gramps](https://gramps-project.org).

*A Claude skill for Czech and Slovak genealogy research: civil and parish registers, regional archives, request templates, reading old records and maintaining a family tree in Gramps. The skill itself is written in Czech.*

## Co skill umí

- **Matriky:** pravidla zákona č. 301/2000 Sb. (lhůty 100/75/30 let, § 25 pro potomky, doslovný výpis, omezení u osvojení) a šablona žádosti na matriční úřad.
- **Archivy:** kde hledat a jak fungují prohlížeče – SOA Praha (eBadatelna), SOA Třeboň (DigiArchiv), Litoměřice, Zámrsk, Plzeň (Porta fontium), Opava, Brno (Actapublica), SOkA, slovenské matriky na FamilySearch.
- **Vojenské prameny:** Databáze legionářů VÚA–VHA, legionářské osobní spisy, žádost přes PDF formulář, co znamenají kódy na kartách.
- **Čtení zápisů:** poznámky na okraji (sňatky, přestupy mezi církvemi, legitimace), nemanželské děti, dobové názvy míst a povolání, typické chyby v přepisech.
- **Pracovní postup:** šablona promptu pro prohlížecího agenta (např. Claude Code s Chromem), který prochází digitalizované matriky a stahuje originály; následná kontrola každého zápisu.
- **Gramps:** doplňování nových údajů do exportu ve formátu Gramps XML (`.gramps`) s citacemi zdrojů, validace proti DTD, rodné a vdané jméno, osvojení, nemanželské děti.

## Instalace

### Claude (claude.ai, desktop)
1. Stáhněte složku [`skills/czech-genealogy`](skills/czech-genealogy) (nebo celý repozitář jako ZIP).
2. Zabalte složku `czech-genealogy` do ZIPu.
3. V nastavení Claude v sekci se skilly nahrajte ZIP jako nový skill.

### Claude Code
Zkopírujte složku do adresáře se skilly:

```bash
git clone https://github.com/midlan/czech-genealogy.git
cp -r czech-genealogy/skills/czech-genealogy ~/.claude/skills/
```

## Použití

Stačí začít mluvit o rodokmenu, matrikách nebo předcích, např.:

- „Pomoz mi sestavit rodokmen z otcovy strany, děda se jmenoval…“
- „Napiš žádost na matriku o doslovný výpis zápisu narození mé babičky.“
- „Přečti tenhle zápis z matriky a doplň ho do mého rodokmenu v Gramps.“ (přiložte obrázek a export `.gramps`)
- „Dej mi prompt pro Claude Code, ať v eBadatelně najde sňatek mých prapraprarodičů.“

## Struktura

```
skills/
└── czech-genealogy/
    └── SKILL.md
```

## Upozornění

Skill obsahuje praktické postupy, nikoli právní radu. Ceníky, provoz badatelen a podmínky archivů se mohou měnit – ověřujte je na webech příslušných institucí. Kopie archiválií slouží obvykle jen ke studijním účelům; řiďte se podmínkami jednotlivých archivů.
