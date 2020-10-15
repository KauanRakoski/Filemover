import shutil
import os
import time


def transfer_file():
    source = r"C:\Users\Kauan\Desktop\src"
    pasta_geral = r'C:\Users\Kauan\Desktop\Conteúdos'

    # Rotas
    pasta_historia = r'C:\Users\Kauan\Desktop\Conteúdos\História'
    pasta_ciencias = r'C:\Users\Kauan\Desktop\Conteúdos\Ciências'
    pasta_ead = r'C:\Users\Kauan\Desktop\Conteúdos\EAD'
    pasta_matematica = r'C:\Users\Kauan\Desktop\Conteúdos\Matemática'
    pasta_proj = r'C:\Users\Kauan\Desktop\Conteúdos\PROJ'

    try:
        for filename in os.listdir(source):
            sourc = os.path.join(source, filename)        

            if filename.startswith('Hist_'):
                shutil.move(sourc, pasta_historia)

            elif filename.startswith('Cie_'):
                shutil.move(sourc, pasta_ciencias)

            elif filename.startswith("EAD_"):
                shutil.move(sourc, pasta_ead)

            elif filename.startswith("Mat_"):
                shutil.move(sourc, pasta_matematica)

            elif filename.startswith("PROJ_"):
                shutil.move(sourc, pasta_proj)
            else:
                conf = input(f'documento {filename} não se enquadra nas classificações. \n Mover pasta geral? [s/n]')

                if conf == 's':
                    shutil.move(sourc, pasta_geral)
                else:
                    pass

        print("Analisando arquivos...")
        time.sleep(1)
        print("\033[33mProcessando...")
        time.sleep(3)
        print('\033[32mOperações bem suscedidas.\033[m')

    except Exception as err:
        print(f'Ocorreu um erro inesperado. Tente resolver o problema e rodar o programa novamente. \n Detalhes: \n {err}')

    
        # print(f'\33[32m Ocorreu um erro: \33[31m {err}')


transfer_file()
