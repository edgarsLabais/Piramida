ievade = input("Ievadiet plākšņu skaitu: ")
iedotas_plaksnes = int(ievade)
izlietoto_plaksnu_skaits = 0
pari_palikusas_plaksnes = iedotas_plaksnes
i = 0
stavu_skaits = 0

try:
    if iedotas_plaksnes > 0:
        while(izlietoto_plaksnu_skaits < pari_palikusas_plaksnes):
            i+=1
            cikls=i*i
            izlietoto_plaksnu_skaits += cikls
            pari_palikusas_plaksnes -= izlietoto_plaksnu_skaits
            stavu_skaits += 1
        print ("Ar ",iedotas_plaksnes, "plāksnēm var uzbūvēt piramīdu ar ",stavu_skaits, "stāviem.")
    else: 
        print ("Ievadiet korektu informāciju")
except ValueError:
    print("Kaut kas nav pareizi ievadīts")

