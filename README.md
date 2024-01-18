# Projekts1
2024. gada "Lietojumprogrammatūras automatizēšanas rīki" kursa projekts.

Man vienmēr ir bijusi problēma ar e-pata laicīgu pārbaudi.
Nereti gadās, ka e-pastu pārbaudu labi ja reizi 3 dienās.

Nolēmu izveidot python programmu, kuru ievietot sava datora startup mapē, kura man atgādinātu izlasīt jaunus e-pastus.

Šim darbam izveidoju jaunu e-pastu, kuru neplānoju izmantot un dzēsīšu pēc vērtējuma iegūšanas.

No sākuma domāju par lasīts / nelasīts pārbaudi, bet uzreiz sapratu, ka pat ja tas būtu iespējams, ir vieglākas metodes.
Beigās nonācu pie metodes, ka saglabāju laiku (ar 1h novirzi gadijumā, ja e-pasts atnāk palaišanas laikā) kad programma tiek palaista , bet pirms tā nolasu laiku, kad tā tika palaista iepriekšējo reizi. Tas man ļauj salīdzināt e-pata sūtīšanas laiku ar pagājušo palaišanu un pārtraukt pārbaudīt e-patsus, kad sasniegti tie kuri atnāca pirms pagājušās pārbaudes. 

Radās problēmas ar datetime formāta iegūšanu (no e-pasta laika formāta), saglabāšanu un nolasīšanu, bet cītīgi meklējot internetu un mēginot visu pēc kārtas nonācu līdz metodēm, kuras strādā.

Izmantojot kodu no lekcijas piemēra man radās problēma ar to, ka e-pasti sarakstā sākas ar vecāko un tad iet uz jaunākiem, kas bojāja manu plānu breakot loop, kad sasniegti vecie e-pasti. Sapratu, ka to var viegli salabot apgriežot secību e-pastu id, pēc to pārveidošanas sarakstā.

Izmantojot iepriekš minētos paņēmienus  varēju viegli izveidot 2 dimensiju sarakstu, kurā katrā plaša saraksta šunā bija 1 e-pata nosūtītājs, temats un laiks.

Nolēmu izveidot pdf failu, kuršs kalpotu, kā vizuālais atgādinājums. Nolēmu izmantot pdf, jo likās kā viegli veidojams variants, kuršš ir aktuāls iepriekš apgūtajam, pat ja izmantoju citu bibliotēku, jo ar kursā apguto (PyPDF2), cik sapratu, jaunu pdf failu izveidot nevar.

Pdf faila izmantošana varētu izraisīt problēmas tā atvēršanā, kura varētu iztraucēt datora pierastu izmantošanu, palaižot pdf lasīšanas programmu, kas var aizņemt lieku laiku. Man pdf default atvēršanas programma ir mans web-browser, kuru es vienalga slēdzu iekšā uzreiz pēc datora, praktiski vienmēr. Ja man tas radīs sarežģījumus apsveru pdf nomainīt uz windows notification vai pop up window.

Izveidoju .cmd failu, kurā ir comanda run ar ši python faila path. Šī cmd faila shortkatu ievietoju sava datora startup mapē.

Beigās esmu apmierināts ar izveidotu programmu un plānoju to izmantot. Vienīgais uztraukums ir par drošibu, jo galu galā man uz datora tagad būs fails ar mana e-pasta robot pieejas paroli teksta formātā (.py failā), bet nedomāju, ka šis ir tik traki, jo ja kādam būs brīva pieeja pie maniem failiem, tad gan jau būtu kaut kas cits kas mani vienalga iegāztu.

Izmantotās bibliotēkas:
* imaplib - Lai darbotos ar e-pastu.
* email - Lai darbotos ar e-pastu.
* datetime - Lai saglabātu, salīdzinātu un rādītu datumus ar laiku.
* reportlab - Lai izveidotu jaunu pdf dokumentu.
* os - Lai pārbaudītu pdf faila eksistenci, vecā pdf faila dzēšanai un jaunā pdf faila atvēršanai.