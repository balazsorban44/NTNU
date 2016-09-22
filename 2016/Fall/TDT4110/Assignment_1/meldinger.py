
def logg(time, name, message):
    string = ('Klokken ' + time + 'sendte ' + name + 'foelgende melding: "' + message + '"')
    return(string)
def main():
    print(logg('23:59','Mr. Y','Har du mottatt pakken?'))
    print(logg('0:00','Mdm. Evil','Ja. Pakken er mottatt.'))
    print(logg('0:03','Dr. Horrible','All you need is love!'))
    print(logg('0:09','Mr. Y','Dr. Horrible, Dr. Horrible , calling Dr. Horrible .'))
    print(logg('0:09','Mr. Y','Dr. Horrible, Dr. Horrible wake up now.'))
    print(logg('0:09','Dr. Horrible','Up now!'))
main()
