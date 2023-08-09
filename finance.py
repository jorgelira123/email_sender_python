import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_data(ticket):
    dados = yf.Ticker(ticket)
    tabela = dados.history("6mo")

    fechamento = tabela['Close']
    fechamento.plot()

    plt.title(f"Preços de Fechamento para {ticket}")
    plt.xlabel("Data")
    plt.ylabel("Preço de Fechamento")
    plt.show()

    maxima = fechamento.max()
    minima = fechamento.min()
    atual = fechamento.iloc[-1]

    return ticket, maxima, minima, atual

