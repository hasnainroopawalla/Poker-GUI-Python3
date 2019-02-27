import pygame
import random
import time
import os

def pair(j,a,t,r):
    s=[]
    c=[]
    dict1={}
    for i in a:
        s.append(i[0])
    for i in t:
        s.append(i[0])
    for i in s:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for i in dict1:
        if dict1[i]==2:
            if(i[0]=='A'):
                r[j].append(14)
            elif(i[0]=='J'):
                r[j].append(11)
            elif(i[0]=='Q'):
                r[j].append(12) 
            elif(i[0]=='K'):
                r[j].append(13)
            elif(i[0]=='1'):
                r[j].append(10)
            else:               
                r[j].append(int(i[0]))
    return r

def threekind(j,a,t,r):
    s=[]
    dict1={}
    for i in a:
        s.append(i[0])
    for i in t:
        s.append(i[0])
    for i in s:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for i in dict1:
        if dict1[i]==3:
            if(i[0]=='A'):
                r[j]=14
            elif(i[0]=='J'):
                r[j]=11
            elif(i[0]=='Q'):
                r[j]=12 
            elif(i[0]=='K'):
                r[j]=13
            elif(i[0]=='1'):
                r[j]=10
            else:               
                r[j]=int(i[0])
            break
        else:
            r[j]=0
    return r

def straight(j,a,t,r):
    s=[]
    for i in a:
        if(i[0]=='A'):
            s.append(1)
        elif(i[0]=='J'):
            s.append(11)
        elif(i[0]=='Q'):
            s.append(12) 
        elif(i[0]=='K'):
            s.append(13)
        elif(i[0]=='1' and i[1]=='0'):
            s.append(10)
        else:               
            s.append(int(i[0]))
    for k in t:
        if(k[0]=='A'):
            s.append(1)
        elif(k[0]=='J'):
            s.append(11)
        elif(k[0]=='Q'):
            s.append(12) 
        elif(k[0]=='K'):
            s.append(13)
        elif(k[0]=='1' and k[1]=='0'):
            s.append(10)
        else:               
            s.append(int(k[0]))
            
    s.sort()
    s.reverse()
    flag=1
    for k in range (0,3):
        flag=0
        if((10 in s) and (11 in s) and (12 in s) and (13 in s) and (1 in s)):
            r[j]=14
            return r 

        else:
            for i in range(k,k+4):        
                if(s[i+1]==s[i]-1): 
                   flag+=1
                    
        if(flag>=4):
            #print(dict1)
            r[j]=s[k]
            break
        else:
            r[j]=0
    return r

def flush(j,a,t,r):
    s=[]
    fsuit=''
    b=[]
    c=[]
    dict1={'♠':0,'♣':0,'♦':0,'♥':0}
    
    for i in a:
        b.append(i)
    for i in t:
        b.append(i)
        
    for i in a:
        s.append(i[-1])
    for i in t:
        s.append(i[-1])
    for i in s:
        dict1[i]+=1
    for i in s:
        if (dict1[i]>=5):
            fsuit=i
            break

    if(fsuit==''):
        #r[j].append([])
        return r
    
    else:
        for i in b:
            if(i[-1]==fsuit):
                if(i[0]=='A'):
                    c.append(14)
                elif(i[0]=='J'):
                    c.append(11)
                elif(i[0]=='Q'):
                    c.append(12) 
                elif(i[0]=='K'):
                    c.append(13)
                elif(i[0]=='1' and i[1]=='0'):
                    c.append(10)
                else:               
                    c.append(int(i[0]))

        c.sort(reverse=True)
        for i in c:       
            r[j].append(i)
        return r


def four(j,a,t,r):
    s=[]
    dict1={}
    for i in a:
        s.append(i[0])
    for i in t:
        s.append(i[0])
    for i in s:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for i in s:
        if dict1[i]==4:
            if(i=='A'):
                r[j]=14
            elif(i=='J'):
                r[j]=11
            elif(i=='Q'):
                r[j]=12 
            elif(i=='K'):
                r[j]=13
            elif(i=='1'):
                r[j]=10
            else:               
                r[j]=int(i)
            break
        else:
            r[j]=0
    return r

def fullhouse(j,a,t,r):
    s=[]
    dict1={}
    for i in a:
        s.append(i[0])
    for i in t:
        s.append(i[0])
    for i in s:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1    
    for i in dict1:
        if (dict1[i]==3):
           for k in dict1:
               if(dict1[k]>=2 and k!=i):
                   print(i)
                   if(i=='A'):                
                       r[j].append(14)
                   elif(i=='J'):
                       r[j].append(11)
                   elif(i=='Q'):
                       r[j].append(12) 
                   elif(i=='K'):
                      r[j].append(13)
                   elif(i=='1'):
                      r[j].append(10)
                   else:
                       r[j].append(int(i))

                   if(k=='A'):
                      r[j].append(14)
                   elif(k=='J'):
                      r[j].append(11)
                   elif(k=='Q'):
                      r[j].append(12) 
                   elif(k=='K'):
                      r[j].append(13)
                   elif(k=='1'):
                      r[j].append(10)
                   else:       
                       r[j].append(int(k))
                    
                   return r
    return r

def deck2imagesuite(d):
    if(d[-1]=='♠'):
            suite='spades'
    elif(d[-1]=='♣'):
            suite='clubs'
    elif(d[-1]=='♦'):
            suite='diamonds'
    elif(d[-1]=='♥'):
            suite='hearts'
    return suite

def deck2imageval(d):
    if(d[0]=='A'):
        cardval='ace'
    elif(d[0]=='2'):
        cardval='2'
    elif(d[0]=='3'):
        cardval='3'
    elif(d[0]=='4'):
        cardval='4'
    elif(d[0]=='5'):
        cardval='5'
    elif(d[0]=='6'):
        cardval='6'
    elif(d[0]=='7'):
        cardval='7'
    elif(d[0]=='8'):
        cardval='8'
    elif(d[0]=='9'):
        cardval='9'
    elif(d[0]=='1'):
        cardval='10'
    elif(d[0]=='J'):
        cardval='jack'
    elif(d[0]=='Q'):
        cardval='queen'
    elif(d[0]=='K'):
        cardval='king'
    return cardval
    
    
    

pygame.init()
width=1400
height=648
screen = pygame.display.set_mode((width, height ))
pygame.display.set_caption('Poker')

#Cards
p1x=950
p1y=75
p2x=950
p2y=480
p3x=110
p3y=480
p4x=110
p4y=75

t1x=360
t1y=260
t2x=450
t2y=260
t3x=540
t3y=260
t4x=630
t4y=260
t5x=720
t5y=260
#Cards

bg = pygame.image.load("playing_cards/Table2.jpg").convert()
betbutton = pygame.draw.rect(screen,(0,0,240),(300,90,100,50));

myfont = pygame.font.SysFont('Calibri', 20)
myfont1 = pygame.font.SysFont('Calibri', 40)

textsurfacebet = myfont.render('BET', False, (0, 0, 0))
textsurfacecheck = myfont.render('CHECK', False, (0, 0, 0))
textsurfaceview = myfont.render('VIEW HAND', False, (0, 0, 0))
textsurfacefold = myfont.render('FOLD', False, (0, 0, 0))
textsurfacepot = myfont.render('POT: Rs.', False, (0, 0, 0))




deck=['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠', 'A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣', 'A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦', 'A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥']
table=[]
turns=0
pot=0
turnend=0
numplayers=4
player=[[],[],[],[]]
cardshow=[]
tableshow=[]
tdisp=['','']
for i in range(0,2):
    for j in range(0,numplayers):
        card=random.randint(0,51)
        while(deck[card]==0):
            card=random.randint(0,51)
        player[j].append(deck[card])
        
        suite=deck2imagesuite(deck[card])
        cardval=deck2imageval(deck[card])
        
        cardshow.append(cardval+'_'+suite)
        deck[card]=0

print()
print(player)

carddisp=['','','','','','','','']
for i in range(0,8):  
        carddisp[i] = pygame.image.load("playing_cards/"+cardshow[i]+".png").convert()


turnflag=0
running = True
while (running):
        
        screen.blit(bg, [0, 0]) #background
        
        #Buttons and Text
        betbutton = pygame.draw.rect(screen,(192,192,192),(1225,380,100,50));
        checkbutton = pygame.draw.rect(screen,(192,192,192),(1225,440,100,50));
        foldbutton = pygame.draw.rect(screen,(192,192,192),(1225,500,100,50));
        viewbutton = pygame.draw.rect(screen,(192,192,192),(1225,560,100,50));
        screen.blit(textsurfacebet,(1260,397))
        screen.blit(textsurfacecheck,(1251,457))
        screen.blit(textsurfacefold,(1256,517))
        screen.blit(textsurfaceview,(1227,577))
        #Buttons and Text

        
        #Player Cards
        screen.blit(carddisp[0], (p1x,p1y))
        screen.blit(carddisp[1], (p2x,p2y))
        screen.blit(carddisp[2], (p3x,p3y))
        screen.blit(carddisp[3], (p4x,p4y))
        screen.blit(carddisp[4], (p1x+30,p1y))
        screen.blit(carddisp[5], (p2x+30,p2y))
        screen.blit(carddisp[6], (p3x+30,p3y))
        screen.blit(carddisp[7], (p4x+30,p4y))
        
        pygame.draw.rect(screen,(87,87,87),(p1x,p1y,71,96));
        pygame.draw.rect(screen,(49,49,49),(p1x+30,p1y,71,96));
        pygame.draw.rect(screen,(87,87,87),(p2x,p2y,71,96));
        pygame.draw.rect(screen,(49,49,49),(p2x+30,p2y,71,96));
        pygame.draw.rect(screen,(87,87,87),(p3x,p3y,71,96));
        pygame.draw.rect(screen,(49,49,49),(p3x+30,p3y,71,96));
        pygame.draw.rect(screen,(87,87,87),(p4x,p4y,71,96));
        pygame.draw.rect(screen,(49,49,49),(p4x+30,p4y,71,96));
        #Player Cards


        #End of game
        if(turns==4):
            for i in range(0,4):
                if (player[i]==0):
                    if(i==0):
                        pygame.draw.rect(screen,(255,0,0),(p1x-5,p1y-5,111,105))
                    elif(i==1):
                        pygame.draw.rect(screen,(255,0,0),(p2x-5,p2y-5,111,105))
                    elif(i==2):
                        pygame.draw.rect(screen,(255,0,0),(p3x-5,p3y-5,111,105))
                    elif(i==3):
                        pygame.draw.rect(screen,(255,0,0),(p4x-5,p4y-5,111,105))

                        
            screen.blit(carddisp[0], (p1x,p1y))
            screen.blit(carddisp[1], (p2x,p2y))
            screen.blit(carddisp[2], (p3x,p3y))
            screen.blit(carddisp[3], (p4x,p4y))
            screen.blit(carddisp[4], (p1x+30,p1y))
            screen.blit(carddisp[5], (p2x+30,p2y))
            screen.blit(carddisp[6], (p3x+30,p3y))
            screen.blit(carddisp[7], (p4x+30,p4y))
            
            screen.blit(tabledisp[0], (t1x,t1y))
            screen.blit(tabledisp[1], (t2x,t2y))
            screen.blit(tabledisp[2], (t3x,t3y))
            screen.blit(tdisp[0], (t4x,t4y))
            screen.blit(tdisp[1], (t5x,t5y))
            clrtext = pygame.draw.rect(screen,(34,177,76),(588,50,20,20));
            textsurfaceround = myfont.render('GAME OVER', False, (0, 0, 0))
            screen.blit(textsurfaceround,(520,50))
            turnflag=1
            
            pairlist=[[],[],[],[]]
            threelist=[0,0,0,0]
            straightlist=[0,0,0,0]
            flushlist=[[],[],[],[]]
            fourlist=[0,0,0,0]
            fullhouselist=[[],[],[],[]]
            
            for i in range (0,numplayers):
                if(player[i]!=0):
                    pairlist=pair(i,player[i],table,pairlist)
                    threelist=threekind(i,player[i],table,threelist)
                    straightlist=straight(i,player[i],table,straightlist)
                    flushlist=flush(i,player[i],table,flushlist)
                    fourlist=four(i,player[i],table,fourlist)
                    fullhouselist=fullhouse(i,player[i],table,fullhouselist)
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #flushlist=flush(1,['A♠','A♣'],['4♣','9♠','J♠','A♠','3♠'],flushlist)
                    #flushlist=flush(3,['A♠','3♣'],['4♣','9♣','J♠','5♣','3♣'],flushlist)
                    #flushlist=flush(1,['A♠','3♣'],['4♣','Q♣','J♠','5♣','3♣'],flushlist)
                    #threelist=threekind(2,['A♠','A♣'],['3♣','Q♣','J♠','A♣','3♣'],threelist)
                    #fullhouselist=fullhouse(2,['A♠','3♣'],['A♣','Q♣','3♠','4♣','3♣'],fullhouselist)
                    #fourlist=four(2,['Q♠','Q♣'],['Q♣','Q♣','3♠','A♣','A♣'],fourlist)
                    #fourlist=four(3,['K♠','3♣'],['K♣','Q♣','K♠','K♣','10♣'],fourlist)

                    #pairlist=pair(2,['5♠','4A♣'],['2♣','8♣','A♠','10♣','9♣'],pairlist)
                    #pairlist=pair(3,['2♠','J♣'],['2♣','8♣','A♠','10♣','9♣'],pairlist)

                    #straightlist=straight(1,['A♣','8♣'],['10♣','Q♠','J♠','9♠','3♠'],straightlist)
                    #straightlist=straight(3,['3♣','10♣'],['5♣','6♠','4♠','A♠','2♠'],straightlist)
                    print()
                    
                    for j in range(0,4):
                        pairlist[j].sort(reverse=True)
                        
                    print('pair= ',pairlist)
                    print('three=',threelist)
                    print('straight=',straightlist)
                    print('flush=',flushlist)
                    print('four=',fourlist)
                    print('fullhouse=',fullhouselist)

                        
            #WRITE WIN LOGIC HERE
                    f=[]
                    p=[]
                    winner=99
                    flush_winner=0
                    four_winner=0
                    pair_winner=0
                    fullhouse_winner=0
                    three_winner=0
                    straight_winner=0
                    
                    #straight
                    if(max(straightlist)!=0):
                        straight_winner=straightlist.index(max(straightlist))+1
                    #straight

                    #flush
                    for j in range(0,4):
                        if(len(flushlist[j])==0):
                            f.append(0)
                        else:
                            f.append(flushlist[j][0])
                    if(max(f)!=0):
                        flush_winner=f.index(max(f))+1
                    #flush

                    #pair
                    pcheckflag=0
                    for j in pairlist:
                        if(len(j)!=0):
                            pcheckflag=1
                    if(pcheckflag==1):
                        pflag=0
                        for j in range(0,4):
                            if(len(pairlist[j])>=2):
                                p.append(pairlist[j])
                            else:
                                p.append([])

                        for j in p:
                            if(len(j)!=0):
                                pflag=1
                                break
                           
                        if(pflag==1):
                            pair_winner=p.index(max(p))+1
                        else:
                            pair_winner=pairlist.index(max(pairlist))+1
                    #pair

                    #three
                    if(max(threelist)!=0):
                       three_winner=threelist.index(max(threelist))+1
                    #three

                    #four
                    if(max(fourlist)!=0):
                        four_winner=fourlist.index(max(fourlist))+1
                    #four

                    #fullhouse
                    fullhousecheckflag=0
                    for j in fullhouselist:
                        if(len(j)!=0):
                            fullhousecheckflag=1
                    if(fullhousecheckflag==1):
                        fullhouse_winner=fullhouselist.index(max(fullhouselist))+1
                    #fullhouse
                       
                    print()
                    print('Four of a kind winner: Player',four_winner)
                    print('Full House winner: Player',fullhouse_winner)
                    print('Flush winner: Player',flush_winner)
                    print('Straight winner: Player',straight_winner)
                    print('Three of a kind winner: Player',three_winner)
                    print('Pair winner: Player',pair_winner)


                    

                    
                        
                
            #WRITE WIN LOGIC HERE
        #End of game    

            
        
        pygame.display.flip()  #display everything

  
        while(turns<=3 and turnflag==0):
            betflag=0
            if(turns==1):
                for m in range(0,3):
                    card=random.randint(0,51)
                    while(deck[card]==0):
                        card=random.randint(0,51)
                    table.append(deck[card])
                    
                    suite=deck2imagesuite(deck[card])
                    cardval=deck2imageval(deck[card])
                    
                    tableshow.append(cardval+'_'+suite)
                    deck[card]=0
                    
                tabledisp=['','','']
                for i in range(0,3):  
                    tabledisp[i] = pygame.image.load("playing_cards/"+tableshow[i]+".png").convert()
                screen.blit(tabledisp[0], (t1x,t1y))
                screen.blit(tabledisp[1], (t2x,t2y))
                screen.blit(tabledisp[2], (t3x,t3y))
                pygame.display.flip()

            if(turns==2 or turns==3):
                card=random.randint(0,51)
                while(deck[card]==0):
                     card=random.randint(0,51)
                table.append(deck[card])
                
                suite=deck2imagesuite(deck[card])
                cardval=deck2imageval(deck[card])

                tablecardstr=cardval+'_'+suite
                deck[card]=0
                
                if(turns==2):
                    tdisp[0] = pygame.image.load("playing_cards/"+tablecardstr+".png").convert()
                    screen.blit(tdisp[0], (t4x,t4y))
                else:
                    tdisp[1] = pygame.image.load("playing_cards/"+tablecardstr+".png").convert()
                    screen.blit(tdisp[1], (t5x,t5y))
                pygame.display.flip()
            
            
            for i in range(0,numplayers):
                
                nextflag=0
                if(player[i]==0):
                    if(i==0):
                        pygame.draw.rect(screen,(255,0,0),(p1x,p1y,105,96))
                    elif(i==1):
                        pygame.draw.rect(screen,(255,0,0),(p2x,p2y,105,96))
                    elif(i==2):
                        pygame.draw.rect(screen,(255,0,0),(p3x,p3y,105,96))
                    elif(i==2):
                        pygame.draw.rect(screen,(255,0,0),(p4x,p4y,105,96))
                    continue
                
                #Current Player
                pygame.draw.circle(screen,(127,127,127),(1000,60),10)
                pygame.draw.circle(screen,(127,127,127),(1000,590),10)
                pygame.draw.circle(screen,(127,127,127),(160,590),10)
                pygame.draw.circle(screen,(127,127,127),(160,60),10)
                if(i==0):
                    pygame.draw.circle(screen,(255,255,0),(1000,60),10)
                if(i==1):
                    pygame.draw.circle(screen,(255,255,0),(1000,590),10)
                if(i==2):
                    pygame.draw.circle(screen,(255,255,0),(160,590),10)
                if(i==3):
                    pygame.draw.circle(screen,(255,255,0),(160,60),10)

                #Current Player
                    
                print('\n\nRound',turns+1,'\n')
                clrtext = pygame.draw.rect(screen,(34,177,76),(608,50,20,20));
                textsurfaceround = myfont.render('ROUND: '+str(turns+1), False, (0, 0, 0))
                screen.blit(textsurfaceround,(540,50))

                clrtext = pygame.draw.rect(screen,(34,177,76),(628,99,90,40));
                textsurfacepot = myfont1.render('POT: Rs. '+str(pot), False, (0, 0, 0))
                screen.blit(textsurfacepot,(498,100))
                pygame.display.flip()

                print('\t\t',table,'\n')
                print('\nPot- Rs.',pot)
                print('Player',i+1)
                clickflag=0
                while(nextflag!=1):
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()
                            print('clickflag:',clickflag)
                            if(pos[0]>=1225 and pos[0]<=1335 and pos[1]>=380 and pos[1]<=430 and click[0]==1):#bet
                                print('bet')
                                betflag=1
                                pot+=10
                                nextflag=1
                                break
                            elif(pos[0]>=1225 and pos[0]<=1335 and pos[1]>=440 and pos[1]<=490 and click[0]==1):#check
                                print('check')
                                if(betflag==1):
                                    print('Only Bet/Fold allowed.\n\n')
                                else:
                                    nextflag=1
                                    break
                               
                            elif(pos[0]>=1225 and pos[0]<=1335 and pos[1]>=500 and pos[1]<=550 and click[0]==1):#fold
                                print('fold')
                                sure=int(input('Are you Sure? 0- No, 1-Yes: '))
                                if(sure==1):
                                    player[i]=0
                                    nextflag=1
                                    if(i==0):
                                        pygame.draw.rect(screen,(255,0,0),(p1x,p1y,105,96))
                                    elif(i==1):
                                        pygame.draw.rect(screen,(255,0,0),(p2x,p2y,105,96))
                                    elif(i==2):
                                        pygame.draw.rect(screen,(255,0,0),(p3x,p3y,105,96))
                                    elif(i==2):
                                        pygame.draw.rect(screen,(255,0,0),(p4x,p4y,105,96))
                                    print('\nPlayer',i+1,'Folded.\n\n')
                                    break
                                
                            elif(pos[0]>=1225 and pos[0]<=1335 and pos[1]>=560 and pos[1]<=610 and click[0]==1):#view hand
                                if(clickflag==0):
                                    if(i==0):
                                        screen.blit(carddisp[0], (p1x,p1y))
                                        screen.blit(carddisp[4], (p1x+30,p1y))
                                    elif(i==1): 
                                        screen.blit(carddisp[1], (p2x,p2y))
                                        screen.blit(carddisp[5], (p2x+30,p2y))
                                    elif(i==2): 
                                        screen.blit(carddisp[2], (p3x,p3y))
                                        screen.blit(carddisp[6], (p3x+30,p3y))
                                    elif(i==3): 
                                        screen.blit(carddisp[3], (p4x,p4y))
                                        screen.blit(carddisp[7], (p4x+30,p4y)) 
                                    clickflag=1
                                else:
                                    if(i==0):
                                        pygame.draw.rect(screen,(87,87,87),(p1x,p1y,71,96));
                                        pygame.draw.rect(screen,(49,49,49),(p1x+30,p1y,71,96));
                                    elif(i==1):
                                        pygame.draw.rect(screen,(87,87,87),(p2x,p2y,71,96));
                                        pygame.draw.rect(screen,(49,49,49),(p2x+30,p2y,71,96));
                                    elif(i==2):
                                        pygame.draw.rect(screen,(87,87,87),(p3x,p3y,71,96));
                                        pygame.draw.rect(screen,(49,49,49),(p3x+30,p3y,71,96));
                                    elif(i==3):
                                        pygame.draw.rect(screen,(87,87,87),(p4x,p4y,71,96));
                                        pygame.draw.rect(screen,(49,49,49),(p4x+30,p4y,71,96));
                                    clickflag=0
                                pygame.display.flip()
                                print('view hand')
                                        
            pygame.display.flip()                                                        
            turns+=1
                                                                

        if(turns==4 and turnend==0):
            for i in range (0,numplayers):
                if(player[i]!=0):
                    print(player[i])    
                turnend=1
                
            
                
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
pygame.quit()
