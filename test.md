

```python
import random
from reversi import *
```

# デフォルトプレイヤーによる対戦


```python
Game().start()
```

    no:0 white:0 black:0 pass:0 turn:x
      0 1 2 3 
    0 . + . . 
    1 + o x . 
    2 . x o + 
    3 . . + . 
    None
    no:1 white:1 black:4 pass:0 turn:o
      0 1 2 3 
    0 + x + . 
    1 . x x . 
    2 + x o . 
    3 . . . . 
    no:2 white:3 black:3 pass:0 turn:x
      0 1 2 3 
    0 o x . . 
    1 + o x . 
    2 . x o + 
    3 . . + . 
    no:3 white:2 black:5 pass:0 turn:o
      0 1 2 3 
    0 o x + . 
    1 x x x . 
    2 + x o . 
    3 . . . . 
    no:4 white:5 black:3 pass:0 turn:x
      0 1 2 3 
    0 o o o + 
    1 x x o + 
    2 . x o + 
    3 . . . + 
    no:5 white:4 black:5 pass:0 turn:o
      0 1 2 3 
    0 o o o x 
    1 x x x . 
    2 + x o + 
    3 . + . . 
    no:6 white:8 black:2 pass:0 turn:x
      0 1 2 3 
    0 o o o x 
    1 o o x . 
    2 o o o . 
    3 + . + . 
    no:7 white:7 black:4 pass:0 turn:o
      0 1 2 3 
    0 o o o x 
    1 o o x + 
    2 o x o + 
    3 x + + . 
    no:8 white:9 black:3 pass:0 turn:x
      0 1 2 3 
    0 o o o x 
    1 o o o o 
    2 o x o + 
    3 x . . . 
    no:9 white:7 black:6 pass:0 turn:o
      0 1 2 3 
    0 o o o x 
    1 o o o x 
    2 o x x x 
    3 x + + + 
    no:10 white:9 black:5 pass:0 turn:x
      0 1 2 3 
    0 o o o x 
    1 o o o x 
    2 o o x x 
    3 x o + . 
    no:11 white:8 black:7 pass:0 turn:o
      0 1 2 3 
    0 o o o x 
    1 o o o x 
    2 o o x x 
    3 x x x + 
    winner: WHITE
    no:12 white:10 black:6 pass:0
      0 1 2 3 
    0 o o o x 
    1 o o o x 
    2 o o o x 
    3 x x x o 
    

# ランダムプレイヤーによる対戦


```python
p1 = RandomPlayer(BLACK, 'BLACK')
p2 = RandomPlayer(WHITE, 'WHITE')
Game(p1=p1, p2=p2).start()
```

    no:0 white:0 black:0 pass:0 turn:x
      0 1 2 3 
    0 . + . . 
    1 + o x . 
    2 . x o + 
    3 . . + . 
    None
    no:1 white:1 black:4 pass:0 turn:o
      0 1 2 3 
    0 . . . . 
    1 . o x + 
    2 . x x . 
    3 . + x + 
    no:2 white:3 black:3 pass:0 turn:x
      0 1 2 3 
    0 + + + + 
    1 . o o o 
    2 . x x . 
    3 . . x . 
    no:3 white:2 black:5 pass:0 turn:o
      0 1 2 3 
    0 . . x . 
    1 . o x o 
    2 . x x . 
    3 . + x + 
    no:4 white:4 black:4 pass:0 turn:x
      0 1 2 3 
    0 . + x . 
    1 + o x o 
    2 + x o + 
    3 . . x o 
    no:5 white:3 black:6 pass:0 turn:o
      0 1 2 3 
    0 + . x . 
    1 x x x o 
    2 + x o . 
    3 . + x o 
    no:6 white:5 black:5 pass:0 turn:x
      0 1 2 3 
    0 o + x . 
    1 x o x o 
    2 + x o + 
    3 . . x o 
    no:7 white:4 black:7 pass:0 turn:o
      0 1 2 3 
    0 o . x . 
    1 x o x o 
    2 + x x x 
    3 . + x o 
    no:8 white:8 black:4 pass:0 turn:x
      0 1 2 3 
    0 o . x + 
    1 x o x o 
    2 + o o x 
    3 + o o o 
    no:9 white:5 black:8 pass:0 turn:o
      0 1 2 3 
    0 o + x . 
    1 x x x o 
    2 x x x x 
    3 + o o o 
    no:10 white:8 black:6 pass:0 turn:x
      0 1 2 3 
    0 o . x + 
    1 o x x o 
    2 o x x x 
    3 o o o o 
    no:11 white:7 black:8 pass:0 turn:o
      0 1 2 3 
    0 o + x x 
    1 o x x x 
    2 o x x x 
    3 o o o o 
    winner: WHITE
    no:12 white:10 black:6 pass:0
      0 1 2 3 
    0 o o x x 
    1 o o x x 
    2 o o x x 
    3 o o o o 
    

# ランダムプレイヤーとあなたによる対戦


```python
p1 = RandomPlayer(BLACK, 'RANDOM')
p2 = InputPlayer(WHITE, 'YOU')
Game(p1=p1, p2=p2).start()
```

    no:0 white:0 black:0 pass:0 turn:x
      0 1 2 3 
    0 . + . . 
    1 + o x . 
    2 . x o + 
    3 . . + . 
    None
    no:1 white:1 black:4 pass:0 turn:o
      0 1 2 3 
    0 + x + . 
    1 . x x . 
    2 + x o . 
    3 . . . . 
    

    YOU turn [(0, 0), (0, 2), (2, 0)]: 0, 0
    

    (0, 0)
    no:2 white:3 black:3 pass:0 turn:x
      0 1 2 3 
    0 o x . . 
    1 + o x . 
    2 . x o + 
    3 . . + . 
    no:3 white:2 black:5 pass:0 turn:o
      0 1 2 3 
    0 o x + . 
    1 x x x . 
    2 + x o . 
    3 . . . . 
    

    YOU turn [(0, 2), (2, 0)]: 2, 0
    

    (2, 0)
    no:4 white:5 black:3 pass:0 turn:x
      0 1 2 3 
    0 o x . . 
    1 o x x . 
    2 o o o . 
    3 + + + + 
    no:5 white:4 black:5 pass:0 turn:o
      0 1 2 3 
    0 o x + + 
    1 o x x + 
    2 o o x + 
    3 . . . x 
    

    YOU turn [(0, 2), (0, 3), (1, 3), (2, 3)]: 1, 3
    

    (1, 3)
    no:6 white:7 black:3 pass:0 turn:x
      0 1 2 3 
    0 o x + . 
    1 o o o o 
    2 o o x + 
    3 . + . x 
    no:7 white:6 black:5 pass:0 turn:o
      0 1 2 3 
    0 o x + + 
    1 o o x o 
    2 o o x x 
    3 . + . x 
    

    YOU turn [(0, 2), (0, 3), (3, 1)]: 0, 3
    

    (0, 3)
    no:8 white:8 black:4 pass:0 turn:x
      0 1 2 3 
    0 o x + o 
    1 o o o o 
    2 o o x x 
    3 . + . x 
    no:9 white:6 black:7 pass:0 turn:o
      0 1 2 3 
    0 o x + o 
    1 o x o o 
    2 o x x x 
    3 + x + x 
    

    YOU turn [(0, 2), (3, 0), (3, 2)]: 3, 2
    

    (3, 2)
    no:10 white:9 black:5 pass:1 turn:o
      0 1 2 3 
    0 o x + o 
    1 o x o o 
    2 o o o x 
    3 + x o x 
    

    YOU turn [(0, 2), (3, 0)]: 0, 2
    

    (0, 2)
    winner: WHITE
    no:11 white:12 black:3 pass:2
      0 1 2 3 
    0 o o o o 
    1 o o o o 
    2 o o o x 
    3 + x o x 
    
