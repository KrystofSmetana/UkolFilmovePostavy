import datetime
import decimal

with open("postavy.txt", "r", encoding="utf-8") as file, open("oblibene-postavy.txt", "w", encoding="utf-8") as file_out:
        
    for line in file:
        if line.strip():  # kontrola, zda řádek není prázdný
            # Rozdělení řádku na jednotlivé položky podle oddělovače "#"
            list_of_items = line.strip().split("#")
            jmeno = list_of_items[0]
            věk = int(list_of_items[1])
            pohlavi = list_of_items[2]
            pohlaví_text = "Muž" if pohlavi == "muž" else "Žena"
            is_zviratko = list_of_items[3].lower() == "ano"
            # Kontrola, pokud zvířátko je "ano" tak se vypíše "Ano" jinak "Ne"
            zviratko_text = "Ano" if is_zviratko else "Ne"
            datum = datetime.datetime.strptime(list_of_items[4], '%Y-%m-%d').date()
            # Float vs Decimal: Používám float, protože se mi nechce psát Decimal 2x
            oblibenost = float(list_of_items[5])
        #kontrola, zda je oblíbenost větší než 2.5 pokud ne tak se nebudou vypisovat do souboru
        if oblibenost > 2.5 :
            # Výpis do konzole
            vystup = f"""Postava:{jmeno}
                Věk: {věk}
                Pohlaví: {pohlaví_text}
                Je zvířátko: {zviratko_text}
                Datum Posledního promítání: {datum}
                Oblíbenost: {oblibenost}"""
            print(vystup)

            # Zápis do výstupního souboru oddělený tabulátory (\t)
            vystup_soubor = f"{jmeno}\t{věk}\t{pohlavi}\t{zviratko_text}\t{datum}\t{oblibenost}\n"
            file_out.write(vystup_soubor)
