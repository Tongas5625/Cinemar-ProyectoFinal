class Bar:
    def __init__(self):
        self.total = 0
        self.objetos = []

    menu = {'vino': 90,
            'milanesa': 200,
            'cocacola': 75,
            'carne': 300,
            'pollo': 189,
            'helado': 140}

    def add(self, objeto):
        self.objetos.append(objeto)
        self.total += self.menu[objeto]

    def factura(self, impuesto, servicio):
        impuesto = (impuesto/100)*self.total
        servicio = (servicio/100)*self.total
        total = self.total+impuesto+servicio

        for objeto in self.objetos:
            print(objeto, '€', self.menu[objeto])
        print('el total es: ', '€', round(total, 2))


mesa1 = Bar()
mesa1.add('vino')
mesa1.add('carne')
mesa1.factura(5, 6)
