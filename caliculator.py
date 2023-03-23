import sys

def main():
    hyouji = 0 #計算される側の数値
    hyouji2 = 0 #計算する側の数値
    suuti = [] #整数部(計算される側)
    shousuu = [] #小数部(計算される側)
    suuti2 = [] 
    shousuu2 = [] 
    sisoku = 1 #四則演算の識別(+,-,*,/)
    memo = 0 #メモリーの数値
    shousuu_judge = False #小数以下があるかどうか判定する
    shousuu_judge2 = False 
    enzan = False #計算する側を入力する場面に移ったかどうか
    minus = False #マイナスかどうか
    minus2 = False 
    percent = False #パーセント表示かどうか
    percent2 = False
    dengen = True #電源
    tuika = False #「=」を打った後に続けて計算するかどうか
    tuika2 = False
    equal = False #「=」を打った状態か
    typed3 = ""
    
    
    print(hyouji) #初期
    print_calculator()
    
    #電源がついている場合
    while dengen == True:
        typed2 = input("insert:")
        MRC_second = typed2
        
        #計算される側の数値を入力する場面##############################################
        if enzan == False:
            if typed2 == "電源":
                sys.exit()
            
            #小数を打ち込む場面に移る
            if typed2 == ".":
                shousuu_judge = True
                for i in range(len(suuti)):
                    hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                if minus == True:
                    hyouji = hyouji*(-1)
                if percent == True:
                    hyouji = hyouji*(0.01)
                print('{:.8g}.'.format(hyouji))
                print_calculator()
                hyouji = 0
                continue
            
            #演算子を打ち込む -> 計算する側の数値を入力する場面に移る###########################
            if typed2 == "+"  or typed2 == "-" or typed2 == "×" or typed2 == "÷":
                if typed2 == "+":
                    sisoku = 1
                if typed2 == "-":
                    sisoku = 2
                if typed2 == "×":
                    sisoku = 3
                if typed2 == "÷":
                    sisoku = 4
                enzan = True
                print(hyouji2)
                print_calculator()
                continue
            
            #入力した数値を0にする##################################################
            if typed2 ==  "C" or typed2 == "AC":
                hyouji = 0
                minus = False
                percent = False
                suuti.clear()
                shousuu.clear()
                print(hyouji)
                print_calculator()
                continue
            
            #マイナスにするかしないか#################################################
            if typed2 ==  "+/-":
                #マイナスならプラスに、プラスならマイナスに
                if minus == True:
                    minus = False
                if minus == False:
                    minus = True
                    
                for i in range(len(suuti)):
                    hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                for i in range(len(shousuu)):
                    hyouji += (10**(-(i+1)))*(int(shousuu[i]))
                
                if minus == True:
                    hyouji = hyouji * (-1)
                if percent == True:
                    hyouji = hyouji * (0.01)
                    
                print('{:,.8g}'.format(hyouji))
                print_calculator()
                hyouji = 0
                continue
            
            #パーセントにするかしないか##############################################
            if typed2 ==  "%":
                #パーセントなら数値に、数値ならパーセントに
                if percent == True:
                    percent = False
                else:
                    percent = True
                    
                for i in range(len(suuti)):
                    hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                for i in range(len(shousuu)):
                    hyouji += (10**(-(i+1)))*(int(shousuu[i]))
                
                if percent == True:
                    hyouji = hyouji * (0.01)
                
                if percent == False:
                    hyouji = hyouji * (100)
                    
                print('{:,.8g}'.format(hyouji))
                print_calculator()
                hyouji = 0
                continue
            
            #現在入力している数値をメモリーに加算############################################
            if typed2 ==  "M+":
                for i in range(len(suuti)):
                    hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                for i in range(len(shousuu)):
                    hyouji += (10**(-(i+1)))*(int(shousuu[i]))
                memo += hyouji
                print('memory + {:,.8g}'.format(hyouji))
                print_calculator()
                hyouji = 0
                continue
            
            #現在入力している数値をメモリーに減算#############################################
            if typed2 ==  "M-":
                for i in range(len(suuti)):
                    hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                for i in range(len(shousuu)):
                    hyouji += (10**(-(i+1)))*(int(shousuu[i]))
                memo -= hyouji
                print('memory - {:,.8g}'.format(hyouji))
                print_calculator()
                hyouji = 0
                continue
            
            #メモリーを呼び出す(現在入力していた数値は0になる)#####################################
            if typed2 ==  "MRC":
                hyouji = memo
                minus = False
                percent = False
                suuti.clear()
                shousuu.clear()
                print('MRC = {:,.8g}'.format(memo))
                print_calculator()
                continue
            
            #履歴を呼び出す##################################################################
            if typed2 == "履歴":
                typed3 = 0
                while typed3 == 0:
                    f = open("rireki.txt", "r")
                    print(f.read())
                    f.close()
                    
                    for i in range(len(suuti)):
                        hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                    for i in range(len(shousuu)):
                        hyouji += (10**(-(i+1)))*(int(shousuu[i]))
                    if minus == True:
                        hyouji = hyouji*(-1)   
                    if percent == True:
                        hyouji = hyouji*(0.01)
                        
                    print('{:,.8g}'.format(hyouji))
                    print_calculator()
                    hyouji = 0
                    typed3 = input("戻る = 1 :")
                continue
            
            #数字が入力されたとき#####################################################
            if 0 <= int(typed2) <= 9:
                if shousuu_judge == False:
                    suuti.append(typed2)
                if shousuu_judge == True:
                    shousuu.append(typed2)
                    
                for i in range(len(suuti)):
                    hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                for i in range(len(shousuu)):
                    hyouji += (10**(-(i+1)))*(int(shousuu[i]))
                
                #8桁を超えていないかどうか判定(小数は対処できず)
                if -10**(8) < hyouji < 10**8:
                    if minus == True:
                        hyouji = hyouji*(-1)
                    if percent == True:
                        hyouji = hyouji*(0.01)
                    if hyouji - int(hyouji) == 0:
                        print('{:,.8g}'.format(hyouji))
                    else:
                        print('{:,.8g}'.format(hyouji))
                    print_calculator()
                    hyouji = 0
                    
        #計算する側を入力する場面------------------------------------------------------------------
        if enzan == True:
            if typed2 == "電源":
                sys.exit()
            
            #小数点が入力された場合###############################################
            if typed2 == ".":
                shousuu_judge2 = True
                for i in range(len(suuti2)):
                    hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                if minus2 == True:
                    hyouji2 = hyouji2*(-1)
                if percent2 == True:
                    hyouji = hyouji*(0.01)
                print('{:,.8g}.'.format(hyouji2))
                print_calculator()
                hyouji2 = 0
                continue
            
            #演算子が入力された場合##################################################
            if typed2 == "+"  or typed2 == "-" or typed2 == "×" or typed2 == "÷":
                if typed2 == "+":
                    sisoku = 1
                if typed2 == "-":
                    sisoku = 2
                if typed2 == "×":
                    sisoku = 3
                if typed2 == "÷":
                    sisoku= 4
                print('{:,.8g}'.format(hyouji2))
                print_calculator()
                continue
            
            #計算する側の数値を消す(打ち直し)##############################################
            if typed2 ==  "C":
                hyouji2 = 0
                minus2 = False
                percent2 = False
                suuti2.clear()
                shousuu2.clear()
                print(hyouji2)
                print_calculator()
                continue
            
            #全て消す(初期状態に戻す)#####################################################
            if typed2 ==  "AC":
                hyouji = 0
                hyouji2 = 0
                suuti.clear()
                shousuu.clear()
                suuti2.clear()
                shousuu2.clear()
                sisoku = 1
                shousuu_judge = False
                shousuu_judge2 = False
                enzan = False
                minus = False
                minus2 = False
                percent = False
                percent2 = False
                tuika = False
                tuika2 = False
                equal = False
                print(hyouji)
                print_calculator()
                continue
            
            #計算する側の数値をマイナスかプラスにする###############################################
            if typed2 ==  "+/-":
                if equal == True:
                    hyouji = hyouji *  (-1)
                    print('{:,.8g}'.format(hyouji))
                    print_calculator()
                    continue
                
                if minus2 == True:
                    minus2 = False
                if minus2 == False:
                    minus2 = True
                    
                    
                for i in range(len(suuti2)):
                    hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                for i in range(len(shousuu2)):
                    hyouji2 += (10**(-(i+1)))*(int(shousuu2[i]))
    
                if minus2 == True:
                    hyouji2 = hyouji2 * (-1)
                if percent2 == True:
                    hyouji2 = hyouji2 * (0.01)
                    
                print('{:,.8g}'.format(hyouji2))
                print_calculator()
                hyouji2 = 0
                continue
            
            #計算する側の数値をパーセントにする###############################################3
            if typed2 ==  "%":
                if equal == True:
                    hyouji = hyouji *  (0.01)
                    print('{:,.8g}'.format(hyouji))
                    print_calculator()
                    continue 
                
                if percent2 == True:
                    percent2 = False
                else:
                    percent2 = True
                
                for i in range(len(suuti2)):
                    hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                for i in range(len(shousuu2)):
                    hyouji2 += (10**(-(i+1)))*(int(shousuu2[i]))
    
                if minus2 == True:
                    hyouji2 = hyouji2 * (-1)
                if percent2 == True:
                    hyouji2 = hyouji2 * (0.01)
                    
                print('{:,.8g}'.format(hyouji2))
                print_calculator()
                hyouji2 = 0
                continue
            
            #計算される側と計算する側を計算する#################################################
            if str(typed2) == "=":
                #「=」が1回押された後かどうか
                if tuika == False:
                    for i in range(len(suuti)):
                        hyouji += (10**(len(suuti)-(i+1)))*(int(suuti[i]))
                    for i in range(len(shousuu)):
                        hyouji += (10**(-(i+1)))*(int(shousuu[i]))
                #「MRC」が呼び出された後かどうか
                if tuika2 == False:
                    for i in range(len(suuti2)):
                        hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                    for i in range(len(shousuu2)):
                        hyouji2 += (10**(-(i+1)))*(int(shousuu2[i]))
                
                #マイナス判定ならマイナスを乗算する   
                if minus == True:
                    hyouji = hyouji*(-1)
                if minus2 == True:
                    hyouji2 = hyouji2*(-1)
                    
                #パーセント判定なら0.01を乗算する    
                if percent == True:
                    hyouji = hyouji*(0.01)
                if percent2 == True:
                    hyouji2 = hyouji2*(0.01)
                
                #計算
                f = open("rireki.txt", "a")
                if sisoku == 1:
                    print("{0} + {1}".format(hyouji,hyouji2),file=f)
                    hyouji += hyouji2
                if sisoku == 2:
                    print("{0} - {1}".format(hyouji,hyouji2),file=f)
                    hyouji -= hyouji2
                if sisoku == 3:
                    print("{0} * {1}".format(hyouji,hyouji2),file=f)
                    hyouji = hyouji * hyouji2
                if sisoku == 4:
                    print("{0} / {1}".format(hyouji,hyouji2),file=f)
                    hyouji = hyouji / hyouji2
                f.close()
                
                #結果を表示する(計算する側の数値を0にする)
                print('{:,.8g}'.format(hyouji))
                print_calculator()
                equal = True
                tuika = True
                hyouji2 = 0
                minus2 = False
                percent2 = False
                shousuu_judge2 = False
                suuti2.clear()
                shousuu2.clear()
                continue
            
            #現在の数値をメモリーに加算########################################################
            if typed2 ==  "M+":
                #計算結果をメモリーに加算する場合
                if tuika == True:
                    memo += hyouji
                    print('memory + {:,.8g}'.format(hyouji))
                    print_calculator()
                    continue
                #現在入力している数値をメモリーに加算する場合
                for i in range(len(suuti2)):
                    hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                for i in range(len(shousuu2)):
                    hyouji2 += (10**(-(i+1)))*(int(shousuu2[i]))
                memo += hyouji2
                print('memory + {:,.8g}'.format(hyouji2))
                print_calculator()
                hyouji2 = 0
                continue
            
            #現在の数値をメモリーに減算#########################################################
            if typed2 ==  "M-":
                #計算結果をメモリーに減算する場合
                if tuika == True:
                    memo -= hyouji
                    print('memory - {:,.8g}'.format(hyouji))
                    print_calculator()
                    continue
                #現在入力している数値をメモリーに減算する場合
                for i in range(len(suuti2)):
                    hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                for i in range(len(shousuu2)):
                    hyouji2 += (10**(-(i+1)))*(int(shousuu2[i]))
                memo -= hyouji2
                print('memory - {:,.8g}'.format(hyouji2))
                print_calculator()
                hyouji2 = 0
                continue
            
            #メモリーを呼び出す######################################################3
            if typed2 == "MRC":
                hyouji = memo
                minus = False
                percent = False
                tuika = True
                suuti.clear()
                shousuu.clear()
                print('MRC = {:,.8g}'.format(memo))
                print_calculator()
                continue
            #######################################################
            if typed2 == "履歴":
                typed3 = 0
                while typed3 == 0:
                    f = open("rireki.txt", "r")
                    print(f.read())
                    f.close()
                    
                    for i in range(len(suuti2)):
                        hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                    for i in range(len(shousuu2)):
                        hyouji2 += (10**(-(i+1)))*(int(shousuu2[i]))
                
                    #マイナス判定ならマイナスを乗算する    
                    if minus2 == True:
                        hyouji2 = hyouji2*(-1)
                    
                    #パーセント判定なら0.01を乗算する    
                    if percent2 == True:
                        hyouji2 = hyouji2*(0.01)
                        
                    print('計算する側 = {:,.8g}'.format(hyouji2))
                    print_calculator()
                    hyouji2 = 0
                    typed3 = input("戻る = 1 :")
                continue
            
            
            #計算する側の数値を入力する######################################################    
            if 0 <= int(typed2) <= 9:
                if shousuu_judge2 == False:
                    suuti2.append(typed2)
                if shousuu_judge2 == True:
                    shousuu2.append(typed2)
                    
                for i in range(len(suuti2)):
                    hyouji2 += (10**(len(suuti2)-(i+1)))*(int(suuti2[i]))
                for i in range(len(shousuu2)):
                    hyouji2 += (10**(-(i+1)))*(int(shousuu2[i]))
                    
                if 10**(-8) < hyouji2 < 10**9:
                    if minus2 == True:
                        hyouji2 = hyouji2 * (-1)
                    if percent2 == True:
                        hyouji2 = hyouji2 * (0.01)
                    print('{:,.8g}'.format(hyouji2))    
                    print_calculator()
                    hyouji2 = 0   
                    
#電卓の表示################################################################################
def print_calculator():
    print (
      """--------------------------
[AC] [C] [+/-] [%] [電源] [履歴]\n
[M+] [M-] [MRC]\n
[7] [8] [9] [+]\n
[4] [5] [6] [-]\n
[1] [2] [3] [×]\n
[0] [.] [=] [÷]\n
----------------------------
""")
    
main()
