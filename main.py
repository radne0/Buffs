#
import time
from bb import BuffBot
import configparser as cfp


if __name__ == "__main__":

    reg_ex="^(\w+) tells you, \'(\w+)\'"
    config = cfp.ConfigParser()
    config.read('config.ini')
    logpath = config['PATHINFO']['PATH_TO_LOG'] + config['PATHINFO']['LOG_NAME']
    buffs ={}
    print("v2")

    # create dictionary with buff trigger as the key and (gemslot,casttime) as the value
    for buff in config['BUFFINFO']:
        print(buff)
        bl = config['BUFFINFO'][buff].split(',')
        buffs[buff] = (bl[0],bl[1]) 
    s = BuffBot(logpath,buffs,reg_ex)
    s.displayconfig()
    time.sleep(1)
    s.listen()

