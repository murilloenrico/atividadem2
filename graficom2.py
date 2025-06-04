import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.canvas.manager.set_window_title("Controle Imobiliario")

anos = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025" ]
imoveis= [100, 250, 200, 500, 300, 200, 750, 450, 100, 250, 300] # Cadastros


plt.plot(anos, imoveis, color="green", linestyle="-", marker='D', label="Cadastro")


plt.title("Controle Imobiliario Anual de Cadastros")
plt.xlabel("Anos")
plt.ylabel("Imóveis")
plt.grid(True)
plt.legend()

plt.show()