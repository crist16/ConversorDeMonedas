import requests
class api_convert():
    def __init__(self,monedaEntrada,monedaSalida,baseAmount):
        self.payload = {}
        self.monedaEntrada = monedaEntrada
        self.monedaSalida = monedaSalida
        self.baseAmount = baseAmount
        self.headers = {
            "apikey": "QkmKgMIqLQOmVCL6AL3ADmJeRNQo5qJQ"
        }
        self.API_KEY = "QkmKgMIqLQOmVCL6AL3ADmJeRNQo5qJQ"
        self.baseUrl = f"https://api.apilayer.com/fixer/convert?to={self.monedaSalida}&from={self.monedaEntrada}&amount={self.baseAmount}"

    def GetData(self):
        response = requests.request("GET", self.baseUrl, headers=self.headers, data=self.payload)

        resultado = response.json()["result"]
        print(resultado)
        return resultado
