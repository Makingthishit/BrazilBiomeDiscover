
import json
import time
import os
with open("Biomas.json") as BiomeList:
    Biome = json.load(BiomeList)

def AwnserTreatment(awnser,YorN,PossibleAwnsrs): #YorN defines the type of the question, if true it means its a boolean awnser but if false it means it is a generic awnser
    replaced = awnser.replace(" ","").lower()
    if YorN == True:
        if replaced == "sim":
            return True
        elif replaced == "nao":
            return False
        else:
            return None
    else:
        for awwnserr in PossibleAwnsrs:
            if awwnserr == replaced:
                return replaced
        return None
            
        


def GetPossibleAwnsers(Characteristic):
    PossibleAwnsers = []
    
    for All in Biome:
        for char in Biome[All]:
          
            if char == Characteristic:
                Value = Biome[All][char]
                
                if Value == True:
                    Value = "Sim"
                elif Value == False:
                    Value = "Nao"
                else:
                    pass
                if not (Value in PossibleAwnsers) :
                    PossibleAwnsers.append(Value)
             
    return PossibleAwnsers


Template = {
    "Clima": str ,
    "Solo_Arenoso":bool,
    "Umidade":bool,
    "TipoVegetacao":str,
    "DensidadeVegetacao":str,
    "FertilidadeSolo":str,
    "Planices":bool,
    "Planaltos":bool
}
        
while True :
    os.system('cls')
    print("------DESCOBRIDOR DE BIOMAS------".center(50))
    Awnser = input("Digite Sim para iniciar: ")
    Call = AwnserTreatment(Awnser,True,None)
    if Call == True:
        TemplateCopy = Template
        for characteristcs in TemplateCopy:
            AllAwnsers = GetPossibleAwnsers(characteristcs)
            print("Responda com estas opçoes:",AllAwnsers)
            print("Se não souber responda: ?")
            text = "Resposta sobre o ", characteristcs ,": "
            AwnserMade = input(''.join(text))
            os.system('cls')
            typeof = TemplateCopy[characteristcs]
            if typeof == bool:
                Result = AwnserTreatment(AwnserMade,True,None)
            elif typeof == str: 
                Result = AwnserTreatment(AwnserMade,False,AllAwnsers)
            TemplateCopy[characteristcs] = Result
        Matches = {"Amazonico":'',
                    "Pampas":'',
                    "Pantanal":'',
                    "Cerrado":'',
                    "Caatinga":'',
                    "MataAtlantica":''}
        for verify in Biome:
            print(verify,Biome[verify])
            GoodAwnsers = 0
            GotBadAwnsers = False
            for charac in TemplateCopy:
                if TemplateCopy[charac] != None:
                    if not (Biome[verify].get(charac) is None ):
                      
                        if Biome[verify][charac] == TemplateCopy[charac]:
                            GoodAwnsers += 1
                        else:
                            GotBadAwnsers = True 
            if GotBadAwnsers == False and GoodAwnsers != 0:
           
                TotalPercentage = round((GoodAwnsers/len(Biome[verify]))*100) 
               
                Matches[verify] = str(TotalPercentage)+"%"
            else:
                Matches[verify] = "0%"
        os.system('cls')
        FormatedMatches = str(Matches).replace("{","").replace("}","").replace("'","")
    
        print("O resultado das suas respostas é:",FormatedMatches)
        input('')
                
            
            

       
            
        
    
    



    


 
  





