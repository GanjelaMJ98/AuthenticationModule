'''
    Модкль контроля доступа

                    - Python 3.6.5
    Used Libraries:
                    - kivy (1.10.0)
                    - json
                    - time
'''

import module as mod                # Модуль контроля доступа

def main():
    print("Hello!")

    '''
    config = input("Enter the configuration path: ")
    log = input("Enter the log path: ")
    name, status = mod.module(config, log)
    '''
    name, status = mod.module("config.json", "log.txt")

    if name == 0 or status == 0:
        quit()

    print(str(name),str(status))


if __name__ == "__main__":
   main()