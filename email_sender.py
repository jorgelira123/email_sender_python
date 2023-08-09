import finance
import pyautogui
import pyperclip
import time

def send_email(ticket, maxima, minima, atual):
    # Email details
    destinatario = "jorgelira123@gmail.com"
    assunto = "Análise diária"
    mensagem = f"""
    Bom dia,
    Segue abaixo as análises da ação {ticket} dos últimos seis meses:
    Cotação máxima: R${round(maxima, 2)}
    Cotação mínima: R${round(minima, 2)}
    Cotação atual: R${round(atual, 2)}
    Atenciosamente,
    Jorge Lira  .
    """

    # Print email details for verification
    print(destinatario)
    print(assunto)
    print(mensagem)

    # Rest of your automation using pyautogui
    # Configure pause between actions
    pyautogui.PAUSE = 3

    # Open a new tab
    pyautogui.hotkey("ctrl", "t")

    # Copy Gmail URL to clipboard
    pyperclip.copy("www.gmail.com")

    # Paste the Gmail URL and press Enter
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    # Click the Compose button
    pyautogui.click(x=2034, y=210)

    # Fill recipient
    pyperclip.copy(destinatario)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")

    # Fill subject
    pyperclip.copy(assunto)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")

    # Fill message
    pyperclip.copy(mensagem)
    pyautogui.hotkey("ctrl", "v")

    # Click the Send button
    pyautogui.click(x=3107, y=975)

    # Close the Gmail tab
    pyautogui.hotkey("ctrl", "f4")

    # Sleep for a while to allow you to see the mouse position (optional)
    time.sleep(5)
    pyautogui.position()

if __name__ == "__main__":
    ticket, maxima, minima, atual = finance.get_stock_data("GOOGL")  # Replace "GOOGL" with your desired stock ticker
    send_email(ticket, maxima, minima, atual)
