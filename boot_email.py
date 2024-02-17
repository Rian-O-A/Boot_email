import smtplib, email. message


destinos = ['rianoliveira38@gmail.com']

def enviar_email(dest):
    corpo_email = """
    <p>Olá, <b>Tudo bom?</b>!</p>
    <p> Segue e-mail automatico</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Teste automatizado em massa!"
    msg['From'] = 'devshell.technology@gmail.com'
    msg['To'] = dest
    password = 'your_password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # login 
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado!')


for rota in destinos: 
    enviar_email(rota)
