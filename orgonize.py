# ------------------- ------------------- ------------------- 
# alguns trechos se repeten e não foram feitos como função
# por motivos de performance, isso sera repetido centenas de
# vezes, então é melhor deixar o codigo mais feio do que lento
# ------------------- ------------------- ------------------- 

from PIL import Image
import os

total = 0 # Total de imagens renomeadas
count = 1 # Contator de imagens em cada pasta

# Extensões suportadas
extensoes = ["jpg", "jpeg", "jfif", "pjpeg", "pjp", "png", "gif"]

# Primeiro Loop, renomeação de segurança 
# Caso esse passo sejá pulado, caso haja arquivos com nomes foo-x.png, ele podera
# ser sobrescrito com um outro arquivo que ira receber o mesmo nome
for root, _, files in os.walk("./Eevee", topdown=False) :
    print("\nRenomeação de segurança:", root, "\n")
    
    # Lendo todos os arquivos do diretorio atual
    for name in files :    
        
        # Montando o path antigo ./foo/bar.png
        oldRoot = root + "/" + name 

        # Pegando a extenção do arquivo
        ext = name.split(".")[-1]  
        
        # WEBM é uma extenção invalida, então todos os WEBM seram removidos
        # Motivos - Não encontrei uma forma boa de converter para gif
        if ext == "webm" :
            print("Deletando arquivo incompativel:", oldRoot)
            os.remove(oldRoot)

        # Converter WEBP pra JPG
        elif ext == "webp" :
            # Gera o nome para o arquivo, e a sua nova rota
            newName = root.split("/")[-1] + "-" + str(count) + "." + "jpg" 
            newRoot = root + "/" + newName

            print("Convertendo arquivo .webp:", oldRoot, "->", newRoot)
            
            # Converter a iamgem original em WEBP para JPG, e apaga o antigo WEBP
            im = Image.open(oldRoot).convert("RGB")
            im.save(newRoot,"jpeg")
            os.remove(oldRoot)
        
        # Renomeando todos os arquivos compativeis
        elif ext in extensoes :
            newName = root.split("/")[-1] + "---" + str(count) + "." + ext   
            newRoot = root + "/" + newName
            os.rename(oldRoot, newRoot)
            print(oldRoot, "->" ,newRoot)
        
        count += 1
    count = 1

# Loop de renomeação final 
for root, dirs, files in os.walk("./Eevee", topdown=False) :
    
    print("\nRenomeação final:", root, "\n")
    for name in files :    
        oldRoot = root + "/" + name                                  # rota antiga
        ext = name.split(".")[-1]                                    # extenção do arquivo    
        newName = root.split("/")[-1] + "-" + str(count) + "." + ext # novo nome do arquivo
        newRoot = root + "/" + newName                               # nova rota
        os.rename(oldRoot, newRoot)
        print(oldRoot, "->" ,newRoot)
        count += 1
        total += 1
    count = 1

print("Arquivos renomeados:", total)
        
    