print("Nevíš proč ani jak, ale objevil ses uprostřed hor. Okolo je mlha a jediné co vidíš okolo jsou stromy a kamení...")
print("V dálce vidíš jeskyni, na zemi vedle tebe leží sekera")
print("Co se chystáš udělat?")
print("1)Porozhlédnout se po okolí")
print("2)Vzít sekeru a pokácet strom")
print("3)Vzít kámen a jít do jeskyně")
print("4)Vzít sekeru a jít do jeskyně")

choice=int(input())
explored=False
weapon="Žádná zbraň"

if choice==1:
    print("Všude jen mlha, stromy a kamení... nic nového jsi neobjevil")    
    print("2)Vzít sekeru a pokácet strom")
    print("3)Vzít kámen a jít do jeskyně")
    print("4)Vzít sekeru a jít do jeskyně")
    explored=True
    choice=int(input())
    
    
if choice==2:
    print("Vzal jsi sekeru a pokácel jsi malý strom, po chvíli obrušování sekerou se ti podařilo z jeho kmenu vyrobit dřevěný meč.")
    if explored==False:
        print("1)Porozhlédnout se po okolí")
    print("3)Vzít kámen a jít do jeskyně")
    print("4)Vzít sekeru a jít do jeskyně")
    print("5)Vzít dřevěný meč a jít do jeskyně")
    choice=int(input())
    

    if choice==1 and explored==False:
        print("Všude jen mlha, stromy a kamení... nic nového jsi neobjevil")    
        print("3)Vzít kámen a jít do jeskyně")
        print("4)Vzít sekeru a jít do jeskyně")
        print("5)Vzít dřevěný meč a jít do jeskyně")
        choice=int(input())
       
if choice==3:
    print("Vzal jsi kámen a vstoupil jsi do jeskyně")
    weapon="Kámen"
    
elif choice==4:
    print("Vzal jsi sekeru a vstoupil jsi do jeskyně")
    weapon="Sekera"
    
elif choice==5:
    print("Vzal jsi dřevěný meč a vstoupil jsi do jeskyně")
    weapon="Dřevěný meč"
    
print("Okolo vidíš krápníky, které vytvářela příroda statisíce let...")
print("Ehm i když... Byla to skutečně příroda, kdo je vytvořil?")
print("Najednou jsi uslyšel něco velkého se pohnout uvnitř jeskyně...")
print("A teď už jsi ho i zahlédl...")
print("V jeskyni se ukrývá obrovský červený drak!")
print("Z legend jsi o něm slyšel, že prý je schopný chrlit oheň tak žhavý jako je láva...")
print("Pokud je to pravda, tak bys asi něco měl udělat")

print("1)Vzít nohy na ramena a utéct")
print("2)Vzít zbraň "+weapon+", rozběhnout se a zabít ho dobře mířeným úderem dřív než si ze mě udělá grilovanou pochoutku")
print("3)Nedělat nic a čekat až mě sežere")

choice2=int(input())

if choice2==1:
    print("Naštěstí se ti podařilo utéct ještě předtím, než si tě drak všiml.")
    print("Jsi znovu před jeskyní, mlha se rozplynula a v dálce vidíš město, do kterého by ses mohl vydat.")
    print("1)Vrátit se zpátky do jeskyně")
    print("2)Vydat se do města")
    choice3=int(input())

elif choice2==2:
    if weapon=="Sekera":
        print("Rozběhl ses, a ještě než si to drak stihl uvědomit, zaseknul jsi sekeru mezi jeho šupiny na hrudi")
        print("To určitě nemohl přežít...")
        print("Drak si tě ale díky tomu všiml, očividně mu jedna sekera zaseknutá mezi šupinami vůbec neublížila...")
        print("Usmažil ses v jeho smrtícím ohni...")
        print("GAME OVER")
        
    elif weapon=="Kámen":
        print("Rozběhl ses, a ještě než si to drak stihl uvědomit, jsi mu hodil kámen přímo mezi oči...")
        print("Drakovi to nic neudělalo, ale všiml si tě a rozhodl si z tebe udělat svačinku")
        print("Usmažil ses v jeho smrtícím ohni...")
        print("GAME OVER")
        
    elif weapon=="Dřevěný meč":
        print("Rozběhl ses, a ještě než si to drak stihl uvědomit, jsi ho bodl dřevěným mečem,")
        print("který se při nárazu na jeho šupiny okamžitě zlomil... Teď už ho těžko zabiješ...")
        print("Drak si tě díky tvému hlasitému bojovému pokřiku hned všiml a rozhodl se napíchnout tě na jeden ze svých obrovských drápů")
        print("Drak tě potom sežral...")
        print("GAME OVER")
    choice3=0
        
elif choice2==3:
    print("Myslet si, že si tě drak po několika dnech hladovění nevšimne bylo hodně naivní...")
    print("Netrvalo to ani 10 vteřin a drak si tě všiml. Už není cesty zpět...")
    print("Zřejmě tě čeká stejný osud jako dalších několik koster na zemi, některé jelení, králičí, ale v posledních vteřinách tam vidíš i lidskou")
    print("Drak tě sežral...")
    print("GAME OVER")
    choice3=0

if choice3==1:
    print("Vrátil ses do jeskyně, drak si tě očividně všiml, když jsi odcházel a počkal si až se vrátíš...")
    print("Ani ses nestihl rozkoukat a stala se z tebe grilovaná pochoutka")
    print("GAME OVER")
    
elif choice3==2:
    print("Vydal ses na dlouhou cestu do vzdáleného města...")
    print("TO BE CONTINUED...")
