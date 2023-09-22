import os
import time
from datetime import datetime
from src.api.mk.mk_driver import Mk
from src.api.mk.coin.coin import Integradores
from src.api.mk.aside.aside_integradores import GerenciamentoTv
from src.api.mk.aside.aside_integradores import GerenciamentoTv_ClientesDeTv
from dotenv import load_dotenv

load_dotenv()

def att_watch(mk):
    hora = datetime.now()
    print(f'Iniciou att watch {hora.strftime("%d/%m/%Y %H:%M")} MK:{mk:02}')
    error = f"\033[91mERROR\033[0m;ATT WATCH;{hora.strftime('%d/%m/%Y %H:%M')}"
    sucess = f"\033[92mSUCESS\033[0m;ATT WATCH;{hora.strftime('%d/%m/%Y %H:%M')}"

    prefixo_log_watch = f'MK:{mk}'

    if mk == 1:
        instance = Mk(
            username=os.getenv('USERNAME_MK1'),
            password=os.getenv('PASSWORD_MK1'),
            url=os.getenv('URL_MK1'),
        )
    elif mk == 3:
        instance = Mk(
            username=os.getenv('USERNAME_MK3'),
            password=os.getenv('PASSWORD_MK3'),
            url=os.getenv('URL_MK3'),
        )

    else:
        print(f'{error};{prefixo_log_watch};Não foi possível criar instancia do mk...')
        return False

    integradores = Integradores()
    gerenciamento_tv = GerenciamentoTv()
    cliente_tv = GerenciamentoTv_ClientesDeTv()

    # login no sistema mk
    try:
        instance.login()
    except:
        print(f'{error};{prefixo_log_watch};Login.')
        instance.close()
        return False

    # atualização de cadastro
    try:
        instance.iframeMain()
        instance.click('//div[@class="OptionClose"]')
    except:
        pass
    
    # click na moeda Integradores
    try:
        instance.iframeCoin()
        instance.click(integradores.xpath())
    except:
        instance.close()
        print(f'{error};{prefixo_log_watch};Click moeda Integradores.')
        return False

    # click aside Gerenciamento TV
    try:
        instance.iframeAsideCoin(integradores)
        instance.click(gerenciamento_tv.xpath())
    except:
        instance.close()
        print(f'{error};{prefixo_log_watch};Click gerenciamento TV.')
        return False

    # click aside Clientes de TV
    try:
        instance.iframeAsideCoin(integradores)
        instance.click(cliente_tv.xpath())
    except:
        instance.close()
        print(f'{error};{prefixo_log_watch};Click cliente TV.')
        return False

    # click cliente
    try:
        instance.iframeGrid(coin=integradores, aside=gerenciamento_tv)
        instance.click('//div[@column="0"]/div[1]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_watch};click cliente')
        return False
    
    # click Dispositivos deste contrato
    try:
        instance.iframePainel(coin=integradores, aside=gerenciamento_tv)
        instance.click('//*[@title="Dispositivos deste contrato"]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_watch};click abrir contrato')
        return False
    
    # Contrato ainda não foi ativado
    try:
        instance.iframeForm()
        instance.click('//div[@id="intTitleClose"]')
    except:
        pass

    # click Atualizar
    try:
        instance.iframeForm()
        instance.click('//span[text()="Atualizar"]')
    except:
        instance.close()
        print(f'{error};{prefixo_log_watch};click Atualizar')
        return False

    time.sleep(5)
    instance.close()
    print(f'{sucess};{prefixo_log_watch};Atualização watch conluída')
    return True