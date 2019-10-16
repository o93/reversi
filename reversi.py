import random, re, itertools
import numpy as np

# ボードパターン 無し:白:黒
NONE, WHITE, BLACK = 0, 1, 2
# 石
STONE = ('.', 'o', 'x')
# 8方向
VEC8 = tuple([vec for vec in itertools.product(range(-1, 2), range(-1, 2)) if vec != (0, 0)])

class Reversi:
    """ リバーシボードクラス """
    
    def __init__(self, size=4):
        self.size = size
        
        self.reset()
    
    def reset(self):
        """ ゲームのリセット """
        
        # ボードを初期状態に
        self.board = np.zeros((self.size, self.size), dtype=np.int8)
        mid = self.size // 2
        self.board[mid, mid] = WHITE
        self.board[mid - 1, mid - 1] = WHITE
        self.board[mid - 1, mid] = BLACK
        self.board[mid, mid - 1] = BLACK
        
        self.count = 0 # 手数
        self.winner = NONE # 勝者
        self.turn = BLACK # 最初のターン
        self.pass_count = 0 # パス数
        self.game_end = False # ゲーム終了
        self.black_count = 0 # 黒の数
        self.white_count = 0 # 白の数
        
        # 置ける位置
        self.available_pos = self.search_positions()
    
    def search_positions(self):
        """ 置ける場所の検索 """
        
        # 石が無い位置
        empty_pos = np.array(np.where(self.board == 0)).T
        # 有効な位置を返す
        return [tuple(pos) for pos in empty_pos if self.is_available(pos)]
    
    def pass_and_change(self):
        self.pass_count += 1
        self.change_turn()
        self.check_game_end()
        
    def put_stone(self, pos):
        """ 石を置く """
        
        pos = np.array(pos)
        
        if not self.is_available(pos):
            return False
        
        self.count += 1
        self.board[pos[0], pos[1]] = self.turn
        self.reverse(pos)
        self.change_turn()
        self.count_stone()
        self.check_game_end()
            
        if self.game_end:
            return True
        
        if len(self.available_pos) == 0:
            self.pass_and_change()
        
            if self.game_end:
                return True
            elif len(self.available_pos) == 0:
                self.pass_and_change()
        
        return True
    
    def next_turn(self):
        """ 次のターンを取得 """
        
        return BLACK if self.turn == WHITE else WHITE
    
    def change_turn(self):
        """ ターンチェンジ """
        
        self.turn = self.next_turn()
        self.available_pos = self.search_positions()
    
    def count_stone(self):
        self.black_count = len(np.where(self.board == BLACK)[0])
        self.white_count = len(np.where(self.board == WHITE)[0])
    
    def check_game_end(self):
        """ ゲーム終了かをチェック """

        if np.count_nonzero(self.board) == self.size * self.size or self.pass_count > 1:
            self.game_end = True
            if self.black_count == self.white_count:
                self.winner = NONE
            else:
                self.winner = BLACK if self.black_count > self.white_count else WHITE
    
    def reverse(self, pos):
        """ 裏返す """
        
        pos = np.array(pos)
        
        # 相手
        opp = self.next_turn()
        # 一番端を除く範囲
        begin, end = 0, self.size - 1

        # 8方向分
        for vec in VEC8:
            # 最初に1つ進めておく
            i = pos + vec
            # 挟めそうフラグ
            sand = False
            sand_pos = []

            while begin <= i[0] <= end and begin <= i[1] <= end:
                # 端まで1つずつ進める
                s = self.board[i[0], i[1]]
                
                if s == NONE or (not sand and s == self.turn):
                    # 空白か自石なので挟めない
                    break
                elif s == opp:
                    # 相手石なので挟めそう
                    sand = True
                    sand_pos.append(i.copy())
                elif sand and s == self.turn:
                    # 挟んでいるのでひっくり返す
                    for p in sand_pos:
                        self.board[p[0], p[1]] = self.turn
                    break
                    
                i += vec
                
    def is_available(self, pos):
        """ 置ける位置か """
        
        pos = np.array(pos)
        if self.board[pos[0], pos[1]] != NONE:
            return False
        
        # 相手
        opp = self.next_turn()
        # 端から端までの範囲
        begin, end = 0, self.size - 1
    
        # 8方向分
        for vec in VEC8:
             # 最初1つ進めておく
            i = pos + vec
            # 挟めそうフラグ
            sand = False
            
            while begin <= i[0] <= end and begin <= i[1] <= end:
                # 端まで1つずつ進める
                s = self.board[i[0], i[1]]
                
                if s == NONE or (not sand and s == self.turn):
                    # 空白か自石なので挟めない
                    break
                elif s == opp:
                    # 相手石なので挟めそう
                    sand = True
                elif sand and s == self.turn:
                    # 挟んでいる
                    return True

                i += vec
                
        return False
    
    def show(self):
        """ コンソール表示 """
        
        if self.game_end:
            print('winner:', ('DRAW', 'WHITE', 'BLACK')[self.winner])
            print('no:{} white:{} black:{}'.format(self.count, self.white_count, self.black_count))
        else:
            print('no:{} white:{} black:{} pass:{} turn:{}'.format(
                self.count, self.white_count, self.black_count, self.pass_count, STONE[self.turn]))

        for i in range(self.size):
            for j in range(self.size):
                s = self.board[i, j]
                if (i, j) in self.available_pos:
                    print('+ ', end='')
                else:
                    print(STONE[s] + ' ', end='')
            print()


class Player:
    """ リバーシプレイヤー基底クラス """

    def __init__(self, stone, name):
        self.stone = stone
        self.name = name
    
    def move(self, reversi):
        """ 最初の位置を返す """

        return reversi.available_pos[0]

class RandomPlayer(Player):
    """ ランダムに指すプレイヤークラス """

    def move(self, reversi):
        """ ランダムな位置を返す """

        return reversi.available_pos[random.randrange(len(reversi.available_pos))]

class InputPlayer(Player):
    """ 標準入力プレイヤークラス """

    def move(self, reversi):
        """ ユーザーによる入力 """
        
        invalid = True
        while invalid:
            try:
                # 入力値を取得
                message = '{} turn {}:'.format(self.name, reversi.available_pos)
                index = re.sub('[ \(\)]', '', str(input(message))).split(',')
                index = tuple([int(i) for i in index])
                print(index)
                if index not in reversi.available_pos:
                    # 入力できない位置だったらやり直す
                    print('invalid value..')
                    continue

                invalid = False
            except:
                # その他のエラーはやり直す
                print('invalid value..')

class Game:
    """ ゲームクラス """
    
    def __init__(self, reversi=None, p1=Player(BLACK, 'BLACK'), p2=Player(WHITE, 'WHITE')):
        self.reversi = Reversi() if reversi is None else reversi
        self.p1 = p1
        self.p2 = p2
        
    def start(self):
        """ ゲーム開始 """
        
        print(self.reversi.show())
        
        while not self.reversi.game_end:
            # 今回のプレイヤー
            p = self.p1 if self.reversi.turn == self.p1.stone else self.p2
            # 石を置く
            self.reversi.put_stone(p.move(self.reversi))
            # 表示
            self.reversi.show()