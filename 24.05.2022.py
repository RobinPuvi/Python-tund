#Teha Pythoni programm, mis vaatab:
#1. Palju on vaba RAMi ja kokku RAMi
#2. Palju on vaba salvestusruumi ja kokku
#3. Kui RAM või Salvestusruum võtab üle 20%, siis kuvab hoiatusteadet (hoiatusteate täituvus % peab olema seadistatav)
#4. Ajalugu programmi käivitusest, vabast ruumist, hoiatuvusteatest peab olema salvestatud logisse (txt fail näiteks)
#5. Vaadata internetist mõnelt veebelehelt või APIst, mis on temperatuur Tallinnas ja see lisada tekstifaili.

#from http import client
#from urllib import response
import requests
import shutil
import psutil
import python_weather
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG,
format="%(asctime)s %(levelname)s %(message)s",
      filename= "log.log",
      filemode="w")

memoryt = psutil.virtual_memory().total / (1024.0 ** 3)
print(memoryt)
memorya = psutil.virtual_memory().available / (1024.0 ** 3)
print(memorya)


total, used, free = shutil.disk_usage("/")
vaba = (free // (2**30))

print("Kokku: %d GB" % (total // (2**30)))
print("Kasutusel: %d GB" % (used // (2**30)))
print("Vaba: %d GB" % (free // (2**30)))
logging.info("Kokku: %d GB" % (total // (2**30)))
logging.info("Kasutusel: %d GB" % (used // (2**30)))
logging.info("Vaba: %d GB" % (free // (2**30)))


if memorya < 3.2:
    print ("Hoiatus")
    logging.info("Hoiatus, mälu on vähe")
if vaba < 47.4:
    print("Warning")
    logging.info("Hoiatus, salvestusruumi on vähe. Vaba: %d GB" % (free // (2**30)))

async def getweather():
    client = python_weather.Client(format=python_weather.METRIC)

    weather = await client.find("Tallinn")

    temp = weather.current.temperature
    print("Praegu on", temp, "C")

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.temperature,"C")
    await client.close()

    with open('ilm.txt', "w") as f:
        f.write(str(temp))

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(getweather())
