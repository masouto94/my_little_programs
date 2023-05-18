from pyverse import Pyverse

lorca="""Este pichón del Turia que te mando,
de dulces ojos y de blanca pluma,
sobre laurel de Grecia vierte y suma
llama lenta de amor do estoy parando.

Su cándida virtud, su cuello blando,
en limo doble de caliente espuma,
con un temblor de escarcha, perla y bruma
la ausencia de tu boca está marcando.

Pasa la mano sobre su blancura
y verás qué nevada melodía
esparce en copos sobre tu hermosura.

Así mi corazón de noche y día,
preso en la cárcel del amor oscuro,
llora sin verte su melancolía."""

storni="""Tú me quieres alba,
Me quieres de espumas,
Me quieres de nácar.
Que sea azucena
Sobre todas, casta.
De perfume tenue.
Corola cerrada

Ni un rayo de luna
Filtrado me haya.
Ni una margarita
Se diga mi hermana.
Tú me quieres nívea,
Tú me quieres blanca,
Tú me quieres alba.

Tú que hubiste todas
Las copas a mano,
De frutos y mieles
Los labios morados.
Tú que en el banquete
Cubierto de pámpanos
Dejaste las carnes
Festejando a Baco.
Tú que en los jardines
Negros del Engaño
Vestido de rojo
Corriste al Estrago.

Tú que el esqueleto
Conservas intacto
No sé todavía
Por cuáles milagros,
Me pretendes blanca
(Dios te lo perdone),
Me pretendes casta
(Dios te lo perdone),
¡Me pretendes alba!

Huye hacia los bosques,
Vete a la montaña;
Límpiate la boca;
Vive en las cabañas;
Toca con las manos
La tierra mojada;
Alimenta el cuerpo
Con raíz amarga;
Bebe de las rocas;
Duerme sobre escarcha;
Renueva tejidos
Con salitre y agua;
Habla con los pájaros
Y lévate al alba.
Y cuando las carnes
Te sean tornadas,
Y cuando hayas puesto
En ellas el alma
Que por las alcobas
Se quedó enredada,
Entonces, buen hombre,
Preténdeme blanca,
Preténdeme nívea,
Preténdeme casta."""


class PoemParser():
    def __init__(self, poem_string) -> None:
        self.initial = poem_string
        self.parsed = self.parse_all(self.initial)

    def get_strophes(self, whole_poem):
        return [strophe for strophe in whole_poem.split("\n\n")]

    def get_verses(self, strophe):
        return [verse for verse in strophe.split("\n")]

    def parse_all(self,poem):
        strophes = self.get_strophes(poem)
        verses=[]
        parsed={}
        for i, strophe in enumerate(strophes):
            parsed[i] = {"verses":self.get_verses(strophe)}
            verses.append(parsed[i].get("verses"))
            parsed[i]["syllables"] = [Pyverse(verse).count for verse in parsed[i]["verses"]]
        self.strophes = verses
        self.verses = [verse for verses in self.strophes for verse in verses]
        return parsed
    
    def get_syllable_count_by_strophe(self):
        return {key:val["syllables"] for key,val in self.parsed.items() }
    
    def get_verse(self,index):
        try:
            if len(index) != 2:
                raise IndexError("Index must be int or an array of size 2")
            return self.strophes[index[0]][index[1]]
        except TypeError:
            return self.verses[index]
    def check_metric(self):
        result=[]
        for counts in self.get_syllable_count_by_strophe().values():
            result.append(all([i == 11 for i in counts ]))
        return all(result)

    def check_structure(self):
        result=[]
        for strophe, counts in self.get_syllable_count_by_strophe().items():
            if strophe in (0,1):
                result.append(len(counts) == 4)
            elif strophe in (2,3):
                result.append(len(counts) == 3)
            else:
                result.append(False)
        return all(result)
lorca_poem = PoemParser(lorca)
storni_poem = PoemParser(storni)

print("Estrofas:\n")
print(lorca_poem.strophes)
print("\nVersos:\n")
print(lorca_poem.verses)
print("\nCuenta de sílabas por verso por estrofa\n")
print(lorca_poem.get_syllable_count_by_strophe())
print("\nCumple las reglas del soneto?:")
print("14 versos endecasílabos: ",lorca_poem.check_metric() )
print("Dos cuartetas y dos tercetas: ", lorca_poem.check_structure())

#par de metrica mas verso
# print(storni_poem.parsed.get(4).get('syllables')[0],storni_poem.parsed.get(4).get('verses')[0])

