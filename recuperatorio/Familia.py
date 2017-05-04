class Familia(object):
    Personas=[]

    def __init__(self):
        self.Personas=[]

    def AgregarPersonaaF(self,f):
        self.Personas.append(f)

    def setSumarCalorias(self, p):
            resultado = None
            for item in self.Personas:
                if item.nombre==p:
                    for item in self.platos:
                    resultado = resultado + item.cant_calorias

            return resultado

    def setpromediocalorias(self):
        cant_pers=None
        sum=None
        for persona in self.Personas:
                for platodepersona in persona.platos:
                 sum=sum+platodepersona.cant_calorias


        promedio=sum/len(self.Personas)
        return promedio

    def setPersonamascalo(self):
        mayor=0
        for item in self.Personas:
            for i in self.platos:
                sum = sum + i.cant_calorias

            if(sum>mayor)
                mayor=sum


        return item.nombre

    def setPersonamenoscalo(self):

        for item in self.Personas:
            for i in self.platos:
                sum = sum + i.cant_calorias

            if (sum <menor)
                menor = sum

        return item.nombre



