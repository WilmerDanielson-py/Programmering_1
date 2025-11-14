import gissa_nummer
import sten_sax_påse
vad_vill_du_spela = input("Vad vill du spela, gissa nummer eller sten sax påse?").lower()

if vad_vill_du_spela == "gissa nummer":
    gissa_nummer.spela()
elif vad_vill_du_spela == "sten sax påse":
    sten_sax_påse.spela()
else:
    print("Ogiltigt val")