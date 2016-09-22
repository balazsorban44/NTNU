questions = [
    [
    '\n    a) Hva er forskjellen paa primaer og sekundaer lagring? Nevn eksempler paa disse? ',
    'Primaer lagring er mye raskere men vanligvis dyrere enn sekundaer lagring. Primaer lagring er volatilt, sekundaer lagring er permanent.\n    Primaer for eksempel RAM,ROM. Sekundaer: HDD,SSD'

    ],[

    'b) Harddisk, SSD og RAM: Nevn de ulike egenskapene med tanke paa permanent/volatilt og tilfeldig/sekvensiell aksess.\n',
    'Harddisk er permanent og sekvensiell, SSD er permanent og tilfeldig, RAM er volatilt og tilfeldig'

    ],[

    'c) Silisium brukes mye i elektronikk. Hvorfor?',
    'Silisium er et halvledende stoff(semiconductor) som finnes overalt og derfor gjoer det godt brukelig for aa lage transistorer.'

    ],[

    'd) Hvordan kan en datamaskin lagre og behandle bilder, lyd og tekst?',
    'Datamaskiner lagrer alt i form av nullere og enere. 0 betyr ikke stroem, 1 betyr stroem.'

    ],[

    'e) Det overfoeres 32 000 bytes mellom to datamaskiner. Hva maa netthastigheten (maalt i bits) vaere for aa fullfoere denne overfoeringen i loepet av 40 sekunder?', str(32000*8/40/1000) + ' kbit/s',

    ],[

    'f) Hva er et OS og hva brukes det til?',
    'OS (Operating System) er hovedprogrammen som tildeler ressursene for andre programmer paa en datamaskin.( for eksempel: Windows, Linux, macOS)'

    ]
]


i=0
while i < len(questions):
    print('\n\n    ',questions[i][0],'\n    ',questions[i][1],'\n    ',sep='')
    i+=1
