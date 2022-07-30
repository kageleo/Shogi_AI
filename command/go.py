
def go(option):

    limits = {}

    if len(option) > 0:
        # stopコマンドが送られるまで思考
        if option[0] == "infinite":
            limits["infinite"] = True

        # 詰将棋
        elif option[0] == "mate":
            limits["mate"] = True

        else:
            # 先読み思考
            if option[0] == "ponder":
                limits["ponder"] = True
                option.remove("ponder")

            # 制限時間を設定（btime,wtime,byoyomi,binc,winc）
            if option:
                for i in range(0, len(option)-1, 2):
                    limits[option[i]] = option[i+1]        

    # 上記で追加した条件の元、思考開始
    print(f'{limits} の条件で、思考開始')
            
    
    



    

    
    
    

    
    