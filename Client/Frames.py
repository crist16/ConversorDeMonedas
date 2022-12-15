import tkinter as tk
from tkinter import ttk,Listbox,messagebox
from  Server.api import api_convert

class Frame(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root,width=480,height=320)

        self.root = root
        self.pack()
        self.Campos()




    def Campos(self):
        self.choices = [
"AFN",
"ALL",
"AMD",
"ANG",
"AOA",
"ARS",
"AUD",
"AWG",
"AZN",
"BAM",
"BBD",
"BDT",
"BGN",
"BHD",
"BIF",
"BMD",
"BND",
"BOB",
"BRL",
"BSD",
"BTC",
"BTN",
"BWP",
"BYR",
"BYN",
"BZD",
"CAD",
"CDF",
"CHF",
"CLF",
"CLP",
"CNY",
"COP",
"CRC",
"CUC",
"CUP",
"CVE",
"CZK",
"DJF",
"DKK",
"DOP",
"DZD",
"EGP",
"ERN",
"ETB",
"EUR",
"FJD",
"FKP",
"GBP",
"GEL",
"GGP",
"GHS",
"GIP",
"GMD",
"GNF",
"GTQ",
"GYD",
"HKD",
"HNL",
"HRK",
"HTG",
"HUF",
"IDR",
"ILS",
"IMP"	,
"INR",
"IQD",
"IRR",
"ISK",
"JEP"	,
"JMD",
"JOD",
"JPY",
"KES"	,
"KGS",
"KHR",
"KMF",
"KPW",
"KRW",
"KWD",
"KYD",
"LAK",
"LBP"	,
"LKR",
"LRD"	,
"LSL",
"LVL",
"LYD",
"NAD",
"NOK"	,
"NPR",
"NZD",
"OMR",
"PAB",
"PEN",
"PGK",
"PHP",
"PKR",
"PLN",
"PYG",
"QAR",
"RON",
"RSD",
"RUB",
"RWF",
"SAR",
"SBD",
"SCR",
"SDG",
"SEK",
"SGD"	,
"SHP"	,
"SLL",
"SOS",
"SRD",
"STD",
"SVC",
"SYP",
"SZL",
"THB",
"TJS",
"TMT",
"TND"	,
"TOP",
"TRY",
"TTD",
"TWD"	,
"TZS",
"UAH"	,
"UGX"	,
"USD",
"UYU"	,
"UZS",
"VEF",
"VND",
"VUV",
"WST"	,
"XAF",
"XAG",
"XAU",
"XCD",
"XDR",
"XOF"	,
"XPF",
"YER",
"ZAR",
"ZMK",
"ZMW"	,
"ZWL",
]
        self.choiceVar = tk.StringVar(value=self.choices)
        self.choices2 = [
"AFN",
"ALL",
"AMD",
"ANG",
"AOA",
"ARS",
"AUD",
"AWG",
"AZN",
"BAM",
"BBD",
"BDT",
"BGN",
"BHD",
"BIF",
"BMD",
"BND",
"BOB",
"BRL",
"BSD",
"BTC",
"BTN",
"BWP",
"BYR",
"BYN",
"BZD",
"CAD",
"CDF",
"CHF",
"CLF",
"CLP",
"CNY",
"COP",
"CRC",
"CUC",
"CUP",
"CVE",
"CZK",
"DJF",
"DKK",
"DOP",
"DZD",
"EGP",
"ERN",
"ETB",
"EUR",
"FJD",
"FKP",
"GBP",
"GEL",
"GGP",
"GHS",
"GIP",
"GMD",
"GNF",
"GTQ",
"GYD",
"HKD",
"HNL",
"HRK",
"HTG",
"HUF",
"IDR",
"ILS",
"IMP"	,
"INR",
"IQD",
"IRR",
"ISK",
"JEP"	,
"JMD",
"JOD",
"JPY",
"KES"	,
"KGS",
"KHR",
"KMF",
"KPW",
"KRW",
"KWD",
"KYD",
"LAK",
"LBP"	,
"LKR",
"LRD"	,
"LSL",
"LVL",
"LYD",
"NAD",
"NOK"	,
"NPR",
"NZD",
"OMR",
"PAB",
"PEN",
"PGK",
"PHP",
"PKR",
"PLN",
"PYG",
"QAR",
"RON",
"RSD",
"RUB",
"RWF",
"SAR",
"SBD",
"SCR",
"SDG",
"SEK",
"SGD"	,
"SHP"	,
"SLL",
"SOS",
"SRD",
"STD",
"SVC",
"SYP",
"SZL",
"THB",
"TJS",
"TMT",
"TND"	,
"TOP",
"TRY",
"TTD",
"TWD"	,
"TZS",
"UAH"	,
"UGX"	,
"USD",
"UYU"	,
"UZS",
"VEF",
"VND",
"VUV",
"WST"	,
"XAF",
"XAG",
"XAU",
"XCD",
"XDR",
"XOF"	,
"XPF",
"YER",
"ZAR",
"ZMK",
"ZMW"	,
"ZWL",
]
        self.choiceVar2 = tk.StringVar(value=self.choices2)

        self.l = Listbox(self, height=5, listvariable=self.choiceVar,exportselection=False)
        self.s = ttk.Scrollbar(self, orient="vertical",
                          command=self.l.yview)
        self.s.grid(column=1, row=1, sticky='nes')
        self.l.configure(yscrollcommand=self.s.set)
        self.l.grid(column=1, row=1)

        self.l2 = Listbox(self, height=5, listvariable=self.choiceVar2,exportselection=False)
        self.s2 = ttk.Scrollbar(self, orient="vertical",
                               command=self.l2.yview)
        self.s2.grid(column=3, row=1, sticky='nes')
        self.l2.configure(yscrollcommand=self.s2.set)
        self.l2.grid(column=3, row=1)


        self.amount_value = tk.StringVar()
        self.amount = tk.Entry(self,textvariable=self.amount_value)
        self.amount.grid(column=2,row=1)

        self.btn_Enviar = ttk.Button(self,text="Convertir")
        self.btn_Enviar.configure(command=self.Calcular)
        self.btn_Enviar.grid(column=2,row=2)

        self.lbl_resultado_value = tk.StringVar()

        self.lbl_resultado = ttk.Label(self,text="")
        self.lbl_resultado['textvariable'] = self.lbl_resultado_value
        self.lbl_resultado.grid(column=2,row=3)





    def Calcular(self):
        try:
            idx = self.l.curselection()[0]
            valor_conversion1 = self.l.get(idx)

            idx2 = self.l2.curselection()[0]
            valor_conversion2 = self.l2.get(idx2)
            amount = self.amount_value.get()
            api_conexion = api_convert(monedaEntrada=valor_conversion1,monedaSalida=valor_conversion2,baseAmount=amount)
            resultado = api_conexion.GetData()
            self.lbl_resultado_value.set(resultado)
        except:
            print("LLenar todo los campos")
            titulo = "Error"
            mensaje = "Llene todos los campos, o perdiò comunicaciòn con el servidor"
            messagebox.showwarning(titulo, mensaje)




