import pygame

# 画面の大きさ
WIDTH = 700
HEIGHT = 480
# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# ボールの座標と速さ
ball_x = 10
ball_y = 10
ball_dx = 5
ball_dy = 5

# パドルの座標とサイズ
paddle_x = 250
paddle_width = 100
paddle_height = 20

# 得点の初期化
score = 0

pygame.init()  # Pygameを初期化
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 画面作成
clock = pygame.time.Clock()  # 時計作成

# 効果音の読み込み
bounce_sound = pygame.mixer.Sound("sound.mp3")  # 効果音読み込み（ファイル形式を確認）

# フォントの設定
font = pygame.font.Font(None, 36)

running = True  # 実行継続フラグ

while running:
    screen.fill(BLACK)  # 画面を塗りつぶす

    for event in pygame.event.get():  # イベント処理
        if event.type == pygame.QUIT:
            running = False  # 終了

    # ボールが壁に当たった場合の処理
    if ball_y >= HEIGHT - 10:  # 下壁に当たった場合（ゲームオーバー）
        ball_dy = -5
        bounce_sound.play()  # 効果音再生
    if ball_y <= 10:  # 上壁に当たった場合
        ball_dy = 5
    if ball_x >= WIDTH - 10:  # 右壁に当たった場合
        ball_dx = -5
    if ball_x <= 10:  # 左壁に当たった場合
        ball_dx = 5

    # パドルとの衝突判定（上辺のみ）
    if paddle_x < ball_x < paddle_x + paddle_width and ball_y + 10 == HEIGHT - paddle_height - 10:
        ball_dy = -5  # ボールを跳ね返す
        score += 1  # 得点を加算
        bounce_sound.play()  # 効果音再生

    # キー操作（左右矢印）でパドルを移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += 5

    # ボール位置を更新
    ball_x += ball_dx
    ball_y += ball_dy

    # ボールとパドルを描画
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)
    paddle_rect = pygame.Rect(paddle_x, HEIGHT - paddle_height - 10, paddle_width, paddle_height)
    pygame.draw.rect(screen, BLUE, paddle_rect)

    # 得点を表示
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # 画面を更新（flip：入れ替え）
    clock.tick(60)  # 描画処理の間隔調整（60 FPS）

pygame.quit()
