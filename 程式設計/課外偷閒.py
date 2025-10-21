import pygame      # 匯入 pygame 套件
import sys         # 匯入 sys 套件

# 初始化
pygame.init()      # 初始化 pygame
WIDTH, HEIGHT = 800, 600   # 設定視窗寬高
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 建立視窗
pygame.display.set_caption("電流急急棒")           # 設定視窗標題

# 顏色
WHITE = (255, 255, 255)    # 白色
BLUE = (0, 128, 255)       # 藍色
RED = (255, 0, 0)          # 紅色
GREEN = (0, 255, 0)        # 綠色
ORANGE = (255, 165, 0)     # 橘色

# 棒路徑（用多邊形模擬）
path_points = [(100, 300), (200, 200), (400, 200), (600, 400), (700, 300)]  # 路徑上的點
player_radius = 15         # 玩家圓球半徑
player_pos = list(path_points[0])   # 玩家初始位置（路徑起點）

clock = pygame.time.Clock()    # 建立時鐘物件，用來控制畫面更新速度
running = True                 # 遊戲主迴圈控制變數
game_over = False              # 是否失敗
game_started = False           # 是否開始遊戲
game_stopped = False           # 是否暫停遊戲

while running:                 # 遊戲主迴圈
    screen.fill(WHITE)         # 填滿背景為白色
    # 畫路徑
    pygame.draw.lines(screen, BLUE, False, path_points, 8)    # 畫藍色路徑
    # 畫終點
    pygame.draw.circle(screen, GREEN, path_points[-1], 20)    # 畫綠色終點圓
    # 畫玩家
    pygame.draw.circle(screen, RED, player_pos, player_radius) # 畫紅色玩家圓球

    if not game_started:       # 如果還沒開始遊戲
        font = pygame.font.SysFont(None, 60)                  # 設定字型
        text = font.render("CLICK TO START", True, ORANGE)        # 顯示開始提示文字
        screen.blit(text, (WIDTH//2-180, HEIGHT//2-30))       # 將文字畫在畫面中央

    for event in pygame.event.get():      # 處理所有事件
        if event.type == pygame.QUIT:     # 關閉視窗事件
            running = False               # 結束主迴圈
        if not game_started and event.type == pygame.MOUSEBUTTONDOWN:  # 點擊滑鼠開始遊戲
            game_started = True
        if game_started and not game_over and not game_stopped and event.type == pygame.MOUSEMOTION: # 遊戲進行中，滑鼠移動
            player_pos = list(event.pos)  # 玩家位置跟隨滑鼠
            # 計算玩家到路徑各點的最小距離
            min_dist = min([pygame.math.Vector2(player_pos).distance_to(p) for p in path_points])
            if min_dist > 200:             # 如果距離大於200，代表偏離路徑，遊戲失敗
                game_over = True
        if (game_over or game_stopped) and event.type == pygame.KEYDOWN:         # 失敗後按下鍵盤
            if event.key == pygame.K_r:                        # 按 R 鍵重玩
                player_pos = list(path_points[0])              # 玩家回到起點
                game_over = False                              # 重設失敗狀態
                game_started = False      
                game_stopped = False                     # 重設開始狀態

    # 檢查是否到達終點
    if game_started and not game_over and pygame.math.Vector2(player_pos).distance_to(path_points[-1]) < 20:
        font = pygame.font.SysFont(None, 60)                   # 設定字型
        text = font.render("PASS!", True, GREEN)                # 顯示通過文字
        screen.blit(text, (WIDTH//2-80, HEIGHT//2-30))         # 畫在畫面中央
        game_stopped = True                                       # 設定遊戲結束
    if game_over:                                              # 如果失敗
        font = pygame.font.SysFont(None, 60)                   # 設定字型
        text = font.render("FAIL! PRESS R TO RELIVE", True, RED)           # 顯示失敗文字
        screen.blit(text, (WIDTH//2-150, HEIGHT//2+40))        # 畫在畫面中央下方

    pygame.display.flip()      # 更新畫面
    clock.tick(60)            # 控制每秒 60 幀
pygame.quit()                 # 結束 pygame
sys.exit()                    # 結束程