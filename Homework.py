def ConvertFuntion (Coin1, Coin2, Coin3):
    Result1 = ExchangeRate*Coin1
    Result2 = ExchangeRate*Coin2
    Result3 = ExchangeRate*Coin3
    print("El primer monto es" + str(Result1) + " " + str(CoinConvert))
    print("El segundo monto es" + str(Result2) + " " + str(CoinConvert))
    print("El tercer monto es" + str(Result3) + " " + str(CoinConvert))

print("Bienvendo, este es un conversor de moneda")
print("Porfavor ingrese el tipo de moneda")
CoinCurrent = input()
print("A cúal moneda quiere convertir?")
CoinConvert = input()
print("Cúal es la tasa de cambio actual de su moneda a la moneda a convertir?")
ExchangeRate = int(input())
print("Cúal es el primer monto de cambio a realizar")
Coin1 = int(input())
print("Cúal es el segundo monto de cambio a realizar")
Coin2 = int(input())
print("Cúal es el tercer monto de cambio a realizar")
Coin3 = int(input())
ConvertFuntion(Coin1, Coin2, Coin3)
