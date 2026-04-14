
import discord
from discord.ext import commands
import asyncio

import discord
from discord.ext import commands
points = 0
max_points = 0
number = 0
intents = discord.Intents.default()
intents.message_content = True
pytanie = -1
bot = commands.Bot(command_prefix='$', intents=intents)
time = 10*60#sekund
score = 0
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

#@bot.command()
#async def hello(ctx):
#    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

#@bot.command()
#async def heh(ctx, count_heh = 5):
#    await ctx.send("he" * count_heh)
    
    
    
@bot.command()
async def quiz(ctx):
    global pytanie
    if pytanie == -1:
        await ctx.send(f"      Masz {time/60}minut aby to przeczytać i zapoznać się z tematem!      ",delete_after=time)
        await ctx.send("Zmiany klimatu to jedno z najbardziej złożonych wyzwań naszych czasów. Choć klimat Ziemi zmieniał się naturalnie na przestrzeni milionów lat (epoki lodowcowe, okresy ocieplenia), obecne zjawisko wyróżnia się tempem oraz przyczyną.",delete_after=time)
        await ctx.send("Kluczowe dowody i wskaźniki Zmiany klimatu to nie tylko cieplejsze lata. To cała kaskada zmian w systemie planetarnym:   Średnia temperatura globalna wzrosła już o około 1,1°C do 1,2°C w porównaniu z erą przedprzemysłową.Szybkie znikanie lodowców górskich, lądolodu Grenlandii i Antarktydy oraz lodu morskiego w Arktyce.Wzrost poziomu mórz wynika z topnienia lodowców oraz rozszerzalności cieplnej wody (cieplejsza woda zajmuje więcej miejsca). Oceany pochłaniają 1/4 antropogenicznego CO2, co zmienia ich odczyn i zagraża rafom koralowym.",delete_after=time)
        await ctx.send("Skutki dla ekosystemów i ludzi"+
        "Zmiana klimatu nie oznacza, że wszędzie będzie po prostu przyjemniej. To przede wszystkim destabilizacja: "+
        "Ekstremalne zjawiska pogodowe: Częstsze i silniejsze fale upałów, susze, ale także gwałtowne powodzie błyskawiczne i potężniejsze huragany. "+
        "Bezpieczeństwo żywnościowe: Zmiany cyklów opadów utrudniają uprawę roli w regionach, które dotychczas były spichlerzami świata. "+
        "Utrata bioróżnorodności: Gatunki nie nadążają z adaptacją do szybko zmieniających się nisz ekologicznych, co prowadzi do wymierania. "+
        "Migracje klimatyczne: Ludzie zmuszeni są opuszczać tereny zalewane przez morza lub niszczone przez permanentne susze. "
        ,delete_after=time)
        await ctx.send("Często słyszy się argument, że klimat zawsze się zmieniał. To prawda, ale obecna zmiana jest bezprecedensowa. Naturalne zmiany (np. cykle Milankovicia dotyczące orbity Ziemi) zachodzą w skali dziesiątek tysięcy lat. My dokonaliśmy drastycznego skoku temperatury w zaledwie 150 lat. "+
        "Warto wiedzieć: Według raportów IPCC (Międzyrządowego Zespołu ds. Zmian Klimatu), mamy coraz mniej czasu, aby ograniczyć ocieplenie do poziomu 1,5°C, co pozwoliłoby uniknąć najbardziej katastrofalnych scenariuszy. "
        ,delete_after=time)
        await asyncio.sleep(time + 5)
        pytanie += 1
        #Prawidłowe działanie
        #pytanie = 0,max_points = 0                          pytanie = max_points
        #pytanie = 1(po wyświetleniu),max_points = 0         pytanie = max_points + 1
        #pytanie = 1,max_points = 0(po podaniu odpowiedzi)   pytanie = max_points
        
        
        
        #błąd 1(wpisanie $quiz więcej niż 1 raz pod rząd):
        #pytanie = 0,max_points = 0    pytanie = max_points    $quiz  \ norma
        #pytanie = 1,max_points = 0    pytanie = max_points + 1       /
        #pytanie = 2,max_points = 0    pytanie = max_points + 2$quiz
        
        
        
        
        #błąd 2(nabijanie punktów przez spamowanie $check + poprawna odpowiedź(bez wyświetlenia pytania))
        #pytanie = 0,max_points = 0    pytanie = max_points       $quiz            \
        #pytanie = 1,max_points = 0    pytanie = max_points - 1                     |norma
        #pytanie = 1,max_points = 1    pytanie = max_points       $check A/B/C/D   /
        #pytanie = 1, max_points = 2   pytanie = max_points + 1   $check A/B/C/D
        #if max_points < pytanie
        
        
        #błąd 3($check bez argumentu(odpowiedzi))
    if pytanie - max_points <= 0 and pytanie >= 0: #Jeśli wartość różnicy zmiennej pytanie i max_points jest mniejszy niż 2,kod zadziała normalnie(W wyniku wyświetlenia zagadnienia wartość zmiennej pytanie rośnie o 1)
        if pytanie == 0:
            
                value = "O ile stopni Celsjusza wzrosła średnia globalna temperatura od czasów przedprzemysłowych?"
                answerA = "A) 0,5°C"
                answerB = "B) 1,1°C – 1,2°C"
                answerC = "C) 2,5°C"
                answerD = "D) 5,0°C"
                pytanie +=  1
        elif pytanie == 1:
                value = "Który z wymienionych gazów jest głównym gazem cieplarnianym emitowanym przez człowieka?"
                answerA = "A) Tlen"
                answerB = "B) Argon"
                answerC = "C) Dwutlenek węgla"
                answerD = "D) Hel"
                pytanie += 1
        elif pytanie == 2:
                value = "Co jest przyczyną wzrostu poziomu mórz i oceanów?"
                answerA = "A) Tylko topnienie lodowców"
                answerB = "B) Tylko większe opady deszczu"
                answerC = "C) Rozszerzalność cieplna wody i topnienie lodowców"
                answerD = "D) Silniejsze wiatry na oceanach"
                pytanie += 1
        elif pytanie == 3:
                value = "Na czym polega mechanizm efektu cieplarnianego?"
                answerA = "A) Gazy w atmosferze zatrzymują ciepło, które powinno uciec w kosmos"
                answerB = "B) Słońce świeci mocniej niż 100 lat temu"
                answerC = "C) Warstwa ozonowa staje się zbyt gruba"
                answerD = "D) Ciepło z wnętrza Ziemi wydostaje się na powierzchnię"
                pytanie+= 1
        elif pytanie == 4:
                value = "Czym skutkuje pochłanianie CO2 przez oceany?"
                answerA = "A) Odsalaniem wody"
                answerB = "B) Zakwaszeniem wód oceanicznych"
                answerC = "C) Zwiększeniem liczby raf koralowych"
                answerD = "D) Oczyszczaniem wody z plastiku"
                pytanie = -1
        
            
            #await asyncio.sleep(3)
            
        await ctx.send("Oto pytanie: ")
        await ctx.send(value)
        await ctx.send(answerA)
        await ctx.send(answerB)
        await ctx.send(answerC)
        await ctx.send(answerD)
        await ctx.send("napisz $check A/B/C/D")
        #await asyncio.sleep(15)
    else:
        pytanie = pytanie
        await ctx.send("Wpisz $check A/B/C/D!")
@bot.command()

async def check(ctx,user_answer):
    global pytanie
    global points
    global max_points
    global score
    if max_points < pytanie:
        if pytanie == 1:
            if user_answer == "B":
                points += 1
                max_points += 1
                await ctx.send(f"dobrze! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było B.")
            else:
                points = points
                max_points += 1
                await ctx.send(f"Źle!!! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było B.")
            
            score = points/max_points * 100
        elif pytanie == 2:
            if user_answer == "C":
                points += 1
                max_points += 1
                await ctx.send(f"dobrze! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było C.")
            else:
                points = points
                max_points += 1
                await ctx.send(f"Źle!!! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było C.")
            
            score = points/max_points * 100
        elif pytanie == 3:
            if user_answer == "C":
                points += 1
                max_points += 1
                await ctx.send(f"dobrze! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było C.")
            else:
                points = points
                max_points += 1
                await ctx.send(f"Źle!!! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było C.")
            
            score = points/max_points * 100
        elif pytanie == 4:
            if user_answer == "A":
                points += 1
                max_points += 1
                await ctx.send(f"dobrze! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było A.")
            else:
                points = points
                max_points += 1
                await ctx.send(f"Źle!!! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było A.")
            
            score = points/max_points * 100
        elif pytanie == 5:
            if user_answer == "B":
                points += 1
                max_points += 1
                await ctx.send(f"dobrze! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było B.")
                
                
            else:
                points = points
                max_points += 1
                await ctx.send(f"Źle!!! Wpisz $quiz aby otrzymać kolejne pytanie! Twój wynik to {points}/{max_points}.Odpowiedzią do zadania {pytanie} było B.")
                
            
            score = points/max_points * 100
        else:
            await ctx.send("Wpisz $quiz i poczekaj 10min!")
        if pytanie >= 5 or max_points > 6:
            await ctx.send(f"Twój wynik to {points}/{max_points} ---> {score}%")
            pytanie = -1
            points = 0
            max_points = 0
            score = 0
    else:
        await ctx.send("Wpisz $quiz")






@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Twoje polecenie nie zostało poprawnie wywołane!")
    else:
        print(f"Wystąpił błąd!")
        
        
    
    
        
#@bot.command()
#async def get_level(ctx):
#    global pytanie
#    await ctx.send(pytanie)
    
    
            
            
        
#@bot.command()
#async def get_max_points(ctx):
#    global max_points
#    await ctx.send(max_points)
    
    
    
#@bot.command()
#async def clear(ctx, amount = 20):
#    await ctx.channel.purge(limit = amount)
        

        

            
bot.run()