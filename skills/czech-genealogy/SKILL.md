---
name: czech-genealogy
description: Genealogický výzkum v českých a slovenských matrikách a archivech – žádosti na matriky, hledání v digitálních archivech, čtení zápisů a údržba rodokmenu v Gramps.
---

# Česká genealogie: matriky, archivy, Gramps

Postup pro sestavování rodokmenu z českých (a slovenských) pramenů. S uživatelem komunikuj česky.

## Zásady komunikace
- Když se ptáš na chybějící nebo nejasný údaj, vždy uveď **celé jméno osoby a její vztah k uživateli** (např. „Marie Houdková, matka tvého pradědy Jana, neboli praprababička“) a **nápovědu, kde údaj hledat** (konkrétní kniha, snímek, rubrika, doklad v rodině).
- Odlišuj, co je **doloženo zápisem**, co je **rodinné podání** a co je **hypotéza**. Hypotézy nikdy nezapisuj jako fakt.
- Nejistá čtení označuj `[nejisté]` a uváděj varianty.
- **Nikdy nesestavuj odkaz podle vzoru.** Do citací dávej jen adresy, které byly skutečně načteny; když nejde ověřit, uveď místo odkazu vyhledávací dotaz.
- Rodná čísla do rodokmenu nezapisuj (osobní identifikátor, pro rodokmen zbytečný).

## Matriky – právní rámec (zákon č. 301/2000 Sb.)
- **Lhůty:** knihy se předávají do archivu 100 let po POSLEDNÍM zápisu (narození), resp. 75 let (manželství, úmrtí). Výpis „po lhůtě“ vydá matrika komukoli: 100 let u narození, 75 let u manželství, 30 let u úmrtí.
- Kniha, která obsahuje hledaný rok, ale pokračuje přes lhůtu, je ještě na matričním úřadě → žádost na matriku.
- **§ 25:** matriční doklad nebo **doslovný výpis** vydá matrika i potomkovi (vnuk, pravnuk). Příbuznost doložit řetězem rodných listů / výpisů.
- **Doslovný výpis** je pro genealogii lepší než rodný list (všechny údaje v původním i pozměněném znění, lze pořídit kopií zápisu). Poplatek po lhůtě 30 Kč za první stranu + 10 Kč za další.
- **Osvojení:** do zápisu smějí nahlížet jen osvojitelé a osvojenec – potomek doslovný výpis osvojence nedostane, jen údaje podle současného stavu.
- Od 1. 1. 1950 se vedou civilní matriky národních výborů (nejsou v archivech).
- Žádost lze poslat datovou schránkou (bez podpisu). Matriky často odpovídají e-mailem se skeny.

### Šablona žádosti na matriku
Adresát (matriční úřad místa události) – **Věc:** Žádost o vydání doslovného výpisu z knihy narození/manželství – „podle § 25 zákona č. 301/2000 Sb. žádám jako potomek (vnuk/pravnuk) o vydání doslovného výpisu…“ – údaje osoby (jméno, datum a místo, rodiče) – „Výpis může být pořízen i kopií matričního zápisu.“ – přílohy dokládající příbuznost – doručení do datové schránky / e-mailem, jinak poštou – souhlas s úhradou poplatku – žadatel.

## Archivy a portály
Podrobné postupy pro jednotlivé prohlížeče (hledání knih, stahování originálů, zasekávání) jsou v definici čtecího agenta `archive-reader`. Ověřená přiřazení obcí k farnostem a knihám: [`references/farnosti.md`](references/farnosti.md).

- **SOA Praha – eBadatelna** (ebadatelna.soapraha.cz): Středočeský kraj. Hledá se podle lokality/farnosti (v poli lokality je nutné kliknout na návrh), ne podle jména. Velké farnosti mají zvláštní knihy přifařených vesnic. Indexy jsou samostatné knihy (sloupce Index N/O/Z). Snímek knihy: `/d/<ID knihy>/<snímek>`; originál lze stáhnout přímou adresou obrázku.
- **SOA Třeboň – DigiArchiv** (digi.ceskearchivy.cz): jižní Čechy. Bez přihlášení nejde přiblížit ani exportovat; po přihlášení uživatele export ikonou diskety. Obrázky nejdou stáhnout přímou adresou.
- **SOA Litoměřice** (sever, Turnovsko; e-badatelna přes soalitomerice.cz, občas odstávky), **SOA Zámrsk** (východ), **SOA Plzeň – Porta fontium**, **Zemský archiv Opava** (Slezsko, Valašsko, Ostravsko), **MZA Brno – Actapublica**.
- **Slovensko:** starší církevní matriky zdarma na FamilySearch; novější na matrikách.
- **SOkA:** evidence obyvatel, domovské a občanské spisy, farní archivy se svatebními spisy (prohlášení o křtu apod.). Sazebník SOA Praha: rešerše 300 Kč/h, sken 25 Kč; osobní studium v badatelně zdarma.
- **VÚA–VHA:**
  - Databáze legionářů (`vuapraha.cz/legionari/<ID>`); ID jsou abecedně sousední (stejné příjmení = ID ±5). Karta uvádí narození, bydliště, útvary, zajetí, kód, poznámku a prameny, **ne rodiče ani domovskou obec** – ty jsou až ve spise. Karty mohou obsahovat chyby (často rok narození). Kód D = dezerce; „Není legionářem podle zák. 462/1919“ = nedosloužil (často zůstal v Rusku).
  - Digitální badatelna (`vuapraha.cz/badatelna`): hledání jen v názvech, podřetězcově a bez diakritiky. Legionářské osobní spisy (Kancelář čs. legií) online jen pro příjmení A–E.
  - Spisy na žádost: archiv přijímá **jen svůj PDF formulář z webu VÚA, vyplněný přímo v PDF** (ne sken), povinné jméno, datum a místo narození hledané osoby; poslat na podatelna-vua@mo.gov.cz. Platí se jen kopie (sken 25 Kč), max. 20 stran. Kmenové listy ročníků 1887–1900 jsou skartovány.
- **Kramerius** (Česká digitální knihovna): fulltext starých novin. Ověř, že stránka je veřejně přístupná; neveřejné stránky ukážou jen úryvek.
- **MyHeritage / FamilySearch stromy:** jen vodítka; správcům stromů lze psát zdarma.

## Čtení zápisů – na co si dát pozor
- Kurent, latina, němčina, farářské zkratky. „Cop.“ = sňatek, „†“ = zemřelý, „proles legitimata per subsequens matrimonium (die …)“ = nemanželské dítě legitimováno sňatkem rodičů (datum = datum sňatku). V latinských knihách *Levans* = kmotr(a), *Testis* = svědek.
- **Poznámky na okraji** jsou zlatý důl: pozdější sňatek (s datem → potvrzení totožnosti), vystoupení z církve / přestup k Církvi československé (vlny 1920–1921, 1925), návrat do církve, úmrtí.
  - „Cop. <místo> <datum>“ **pod údaji o rodičích** (u narození z 80.–90. let 19. st.) = sňatek **rodičů** – použij dřív, než začneš prohledávat knihy sňatků.
  - „Cop. …“ na **levém okraji** = sňatek **dítěte**.
  - Poznámka může patřit k předchozímu zápisu – ověř, pod kterou čarou leží. Jiným inkoustem dopsané údaje ber jako samostatnou pozdější informaci.
- Matka je v zápisu psána příjmením po manželovi; rodné příjmení je v „dcera X“ / „rozená Y“. Nezaměňuj dítě, matku a nevěstu.
- „Dcera Marie, dcery Jana X“ bez otce = nemanželské dítě; uvedení „rodiče“ jsou ve skutečnosti prarodiče. Otec se může „přihlásit“ (podpis se svědky).
- Příjmení vdovy: „Čapková roz. Žimová“ = Čapková po prvním muži.
- Varianty příjmení i v jednom zápisu (Landr/Lander, Brejla/Breyla, Štohr/Štor) – hledej všechny.
- „Skadlec/tkadlec“ = tkadlec; dobové tvary míst (Hradiště = Mnichovo Hradiště).
- Měsíc bývá uveden jen u prvního zápisu bloku; datum vždy ověř v samotném zápisu, ne jen v hlavičce nebo indexu. Narození bývá 0–3 dny před křtem.
- **Indexy:** řazené podle počátečního písmene, uvnitř písmene chronologicky (projdi celý oddíl písmene). Index sňatků obvykle vede ženicha. Rok v indexu občas nesouhlasí se zápisem.
- Číslo strany/folia v indexu se liší od čísla snímku o malou konstantu pro danou knihu (typicky +2 až +4); po prvním zásahu ji zapiš a používej.
- Den a měsíc souhlasí, rok ne → u zajateckých/legionářských karet běžná chyba; ověř v matrikách, zda existuje alternativní osoba.

## Pracovní postup
1. Ze známých údajů urči další krok: nejdřív **narození** osoby (uvede rodiče, prarodiče, často datum sňatku rodičů), pak **sňatek rodičů** (uvede data narození a rodiče snoubenců).
2. Hledání v digitálních archivech deleguj na **čtecí subagenty** (viz Orchestrace). Pokud subagenty spouštět nemůžeš (např. v chatu bez přístupu k prohlížeči), připrav uživateli **prompt pro prohlížecího agenta** (šablona níže), který spustí sám.
3. **Validuj každý obrázek sám:** přečti originál, porovnej s přepisem čtecího agenta, oprav chyby (časté: povolání, jména obcí, svědci, roky v poznámkách) a výslovně je uživateli uveď.
4. Doplň do rodokmenu (viz Gramps) a pošli soubor.
5. Navrhni další kolo: kde je strom nejkratší a co je online dosažitelné; co vyžaduje žádost (matrika, SOkA, VÚA) a odhad ceny.

**Kde hledat sňatek:** obvykle ve farnosti nevěsty, ale často i v knize obce ženicha nebo v knize přifařené vesnice – prověř obě. Nejrychlejší je poznámka „Cop.“ v rodném zápisu dítěte.

**Ohlášky:** četly se ve farnostech obou snoubenců – místa ohlášek prozradí, kam snoubenci patřili (stopa pro další hledání). Do Gramps je nezakládej jako samostatnou událost, uveď je v poznámce ke sňatku.

**Sourozenci, kmotři, svědci:** sourozence předků nehledej plošně, ale **cíleně tam, kde se linie zasekla**, a jen na pokyn uživatele. Postup: v indexu narození projdi oddíl příjmení za ~25 let po sňatku rodičů a vyber zápisy se stejnými rodiči. Přínos: náhradní zápis místo chybějícího (datum sňatku rodičů, původ prarodičů), rozlišení stejnojmenných osob, kontakty na žijící příbuzné. Kmotři a svědci jsou nejlevnější vodítko k příbuzným (často strýcové a tety).

**Knihy bez indexu:** hledej interpolací – v jedné dávce otevři 3–4 snímky rozložené po knize, z hlaviček zjisti měsíc a rok a zpřesňuj (venkovská farnost ≈ 9 snímků/rok, město ≈ 3–4 snímky/měsíc); pak čti celé stránky kolem cíle.

## Orchestrace: hlavní agent + čtecí subagenti (Claude Code s Chromem)
Cíl: uživatel nemusí ručně přenášet zadání a výsledky mezi modely.

**Role**
- **Hlavní agent = silnější model (Opus).** Plánuje úlohy, píše zadání subagentům, **kontroluje veškerou jejich práci**, čte rukopis, rozhoduje o totožnosti osob, komunikuje s uživatelem a jako jediný zapisuje do rodokmenu.
- **Čtecí subagent = levnější model (Sonnet).** Prochází archivy v Chromu, listuje knihami, stahuje originály a dělá *předběžný* přepis. Do rodokmenu nikdy nezapisuje, nic neobjednává ani neodesílá, nezadává hesla.

**Spuštění**
- Předpoklad: Claude Code s propojeným Chromem (`claude --chrome` nebo `/chrome`), uživatel je v archivech přihlášený sám.
- Subagenta spouštěj nástrojem Agent s `model: "sonnet"`, nejlépe jako předdefinovaného agenta `archive-reader` (soubor `agents/archive-reader.md` v tomto repozitáři).
- Čtecí agent potřebuje kromě Chromu i shell (curl, ořez a zvětšení obrázků) a čtení obrázků – v zadání to výslovně povol.
- Výstupy si určí hlavní agent: subagent ukládá obrázky do pracovní složky (např. `rodokmen/nalezy/`) pod přesnými názvy ze zadání, přepis průběžně zapisuje do pracovního souboru a vrací strukturovaný report.

**Paralelní běh**
- Paralelně spouštěj nejvýš **2–3 subagenty**, každého s jiným archivem nebo jinou knihou. Každý pracuje **ve vlastní nové záložce** a sahá jen na svou záložku.
- Všichni sdílejí jedno rozšíření a jeden prohlížeč; souběh není zaručeně stabilní (záložky se mohou přepínat, archivy mohou omezovat počet požadavků). Pokud se objeví chyby, zasekávání nebo se agenti přetahují o záložky, **přepni na sekvenční běh**.
- Úlohy, které na sobě závisí (např. sňatek rodičů až po nalezení narození), dávej jednomu subagentovi postupně.

**Kontrola práce subagenta (povinná, vždy)**
1. Otevři každý stažený obrázek a přečti zápis sám; přepis subagenta ber jen jako vodítko.
2. Zkontroluj citaci (kniha, snímek, strana, URL) a že obrázek odpovídá citaci.
3. Ověř logiku: data, věk, čísla domů, shoda s už doloženými údaji, poznámky na okraji potvrzující totožnost.
4. Projdi, co subagent **neprošel**. **Negativní nález platí jen pro přečtený rozsah:** „nenalezeno v indexu“ nebo „jen horní zápisy“ neznamená „v knize není“ – zadej doplňující čtení celých stránek nebo jiné místo (jiná farnost, kniha ženichovy obce, matrika).
5. Uživateli shrň nálezy a výslovně uveď, co jsi oproti subagentovi opravil.
6. Teprve potom zapiš do rodokmenu.

### Šablona zadání pro čtecího agenta
```
Piš ČESKY. PRAVIDLA: jen prohlížej, nezadávej hesla, nic neobjednávej;
zaseknutou záložku nahraď novou; každý nález ulož jako ORIGINÁLNÍ obrázek
celé dvoustrany pod uvedeným názvem; nejisté údaje označ [nejisté]
s variantami; odlišuj přepis od výkladu; čti CELÉ stránky, ne jen horní
zápis; u nálezu zkontroluj stranu před a po a v indexu vypiš všechny
zápisy se stejným příjmením; po 2–3 neúspěšných pokusech úlohu popiš
a jdi dál. Smíš používat shell (curl, ořez obrázků) a čtení obrázků.
PŘIHLÁŠENÍ: <v kterých archivech je uživatel přihlášený (např. Třeboň)>
UKLÁDÁNÍ: <složka, podsložka pro vedlejší soubory, pracovní soubor s přepisy>
CO VÍME: <kontext osob, data, místa, čp., varianty příjmení,
  jména rodičů pro ověření totožnosti (aspoň 2 shodné údaje)>
UŽ PROVĚŘENO: <kniha, rozsah, výsledek – neopakovat>
ÚLOHY: <očíslované: archiv, farnost/kniha (ID, pokud je známé), známý posun
  folio↔snímek, přesné datum nebo rozsah let, rozsah k přečtení celý,
  limit snímků, název souboru>
VÝSTUP: u každé úlohy rozsah přečtených snímků a způsob čtení (celé
stránky / index), ID knihy, posun folio↔snímek; úplný přepis (dítě/
snoubenci, rodiče, prarodiče, povolání, bydliště, původ, kmotři/svědci,
poznámky „Cop.“, přestupy, úmrtí) s pozicí na stránce; rozpory se
zadáním; citace (archiv, signatura, snímek, strana, URL); u negativního
výsledku návrh dalšího místa; souhrnná tabulka; seznam vedlejších souborů.
```

## Gramps
- Výměnný formát: **Gramps XML (`.gramps`)**, ne GEDCOM (GEDCOM ztrácí typy rodin, hlavní rodiče a poznámky; `ADDR` u událostí s místem Gramps zahodí).
- **Vždy vycházej z posledního exportu uživatele**, případně z poslední verze, kterou jsi poslal, pokud uživatel potvrdí, že nic neměnil. Uživatel importuje do **nového prázdného** rodokmenu (import do stávajícího = duplicity).
- Změny dělej skriptem (Python, `xml.etree`): nové osoby/události/citace/zdroje/místa/poznámky s unikátními handle a navazujícími ID; existující záznamy upravuj cíleně. Dodržuj pořadí elementů podle DTD (person: gender, name, eventref, …, childof, parentin, noteref, citationref; family: rel, father, mother, eventref, childref, noteref, citationref; event: type, dateval/daterange, place, description, noteref, citationref).
- Datum: `dateval val="YYYY-MM-DD"`, `type="before"` / `"about"`, rozsah `daterange start/stop`.
- Vztah dítěte: `childref` `frel`/`mrel` = Birth, Adopted, Stepchild…; osvojení jako druhá rodina + událost Adopted; hlavní rodiče = první `childof` (uživatel může přeřadit v zobrazení Vztahy → Seřadit).
- Rodné a vdané jméno jako dvě jména (Birth Name + Married Name, `alt="1"`).
- Před odesláním: validace proti DTD (`xmllint --dtdvalid grampsxml.dtd`, DTD z repozitáře gramps-project), kontrola duplicitních handle a neplatných odkazů.

### Zdroje, repozitáře, citace
- **Repozitář** = instituce, kde zdroj leží (SOA Praha, SOA Třeboň, matriční úřad Mladá Boleslav, VÚA–VHA, Rodinný archiv…). **Zdroj** = kniha/fond s odkazem na repozitář a **signaturou** (`reporef callno`, např. „Radošovice 13“). **Citace** = konkrétní stránka/snímek, URL a vazba na médium.
- Každý údaj má citaci; rodinné podání je samostatný zdroj v repozitáři „Rodinný archiv / rodinné podání“.
- **Spolehlivost citace** (Gramps confidence):
  - **velmi vysoká** – jen genetické (DNA) testy,
  - **vysoká** – matriční zápis, doslovný výpis, rodný list a jiný úřední doklad,
  - **normální** – rodinné podání podané jako fakt; přepis zatím neověřený proti originálu,
  - **nízká** – podání typu „možná to tak bylo“; nepřímé odvození (např. datum úmrtí dopočtené z věku),
  - **velmi nízká** – hypotéza (např. ztotožnění s legionářskou kartou).

### Štítky
- `ověřeno` – údaj potvrzený originálem, `hypotéza` – nepotvrzené ztotožnění nebo výklad, `k dohledání` – známá mezera (chybí zápis, nečitelné příjmení). Štítky přiřazuj osobám, událostem i citacím; slouží uživateli jako filtr a seznam práce.

### Místa
- **Hierarchie:** stát (dobový název s rozsahem let, např. Rakousko-Uhersko / Československo / Česko) → kraj → okres (dobový) → obec → část obce → **číslo popisné** jako samostatné místo typu Building/House. Alternativní názvy (německé – Jungbunzlau, Wlaschim) jako další jména místa.
- **Souřadnice pro domy:** dohledej podle čísla popisného na **mapy.com** („Obec čp. X“) nebo v RÚIAN. Historická čísla popisná se mohla přečíslovat nebo dům zanikl – pokud adresu nelze ztotožnit, dej souřadnice obce/části obce a do poznámky místa napiš, že jde jen o obec. Souřadnice obcí pro vyšší úrovně hierarchie.
- Stejné místo zakládej jen jednou a odkazuj na něj (žádné duplikáty textových míst).

### Média (skeny zápisů a dokladů)
- `.gramps` obrázky neobsahuje, jen na ně odkazuje. Používej **relativní cesty** vůči základní cestě k médiím nastavené v Gramps (Předvolby), kterou uživatel nasměruje na složku se skeny.
- **Pojmenování souborů:** `<datum>_<typ>_<příjmení>_<zdroj>.jpg`, jen ASCII bez diakritiky a mezer, např.
  - `1872-01-30_O_Malinovsky-Kozelova_SOAPraha-Radosovice13-s050.jpg`
  - `1881-09-12_N_Malinovsky-Karel_SOATrebon-Milevsko16-s057.jpg`
  - `1953-05-13_N_Malinovsky-Karel_MatrikaMB-N5-str214.jpg`
  - `1974-12-18_RL_Davidek-Robert_rodinny-archiv.jpg`
  - Typ: `N` narození, `O` oddaní, `Z` zemřelí, `RL` rodný list, `DV` doslovný výpis, `OSV` osvojení (dodatečný zápis), `VUA` vojenský archiv, `DOK` jiný dokument. Datum = datum události; u sňatku obě příjmení.
  - **Jeden soubor = jedna událost.** Je-li na stejné dvoustraně další zápis, vytvoř **kopii** pojmenovanou podle té události (celá dvoustrana, žádný výřez). Kopie mají stejnou koncovku zdroje, takže při řazení leží vedle sebe.
  - **Jednou vytvořený název se nikdy nemění** – Gramps odkazuje cestou a přejmenování by rozbilo odkazy. Nový nález = nová kopie.
  - **Originály nikdy neupravuj** (ořez, otočení, kontrast); výřezy dělej v Gramps jako region.
  - Totožné kopie se poznají podle **kontrolního součtu** (např. `sha256sum`, PowerShell `Get-FileHash`). Použij ho ke zjištění, zda už sken máš (před stažením/kopírováním), k seskupení kopií téhož snímku a ke kontrole, že se originál nezměnil.
  - Metadata do EXIF nepiš; autoritou pro to, kdo je na snímku, je Gramps.
- Médium připoj **k citaci**; volitelně i **k osobě s výřezem** (region) jejího zápisu.
- Archivy povolují kopie zpravidla jen pro soukromé studium – strom s obrázky nezveřejňuj (např. veřejný Gramps Web). Pro zálohu nebo přenos i s obrázky lze vytvořit **Gramps XML Package (`.gpkg`)**.

### Kmotři, svědci a další osoby ze zápisu
- **Nezakládej je jako osoby** (výjimka: prokázaný příbuzný). Zapiš je do **poznámky události** ve strukturovaném tvaru, aby se daly později strojově vytěžit:
  `Kmotři: Jméno Příjmení, stav/povolání, obec čp.; … | Svědci: … | Porodní bába: … | Oddávající/křtící: … | Ohlášky: data, farnosti`
