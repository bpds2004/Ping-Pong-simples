import pygame
import sys

pygame.init()

# Configurações da tela
largura_tela = 640
altura_tela = 480
cor_preta = (0, 0, 0)
cor_branca = (255, 255, 255)
cor_raquete1 = (0, 255, 0)  # Cor da raquete do jogador 1 (verde)
cor_raquete2 = (255, 0, 0)  # Cor da raquete do jogador 2 (vermelho)
tamanho_raquete = (10, 100)
raquete_velocidade = 10
bola_velocidade = [5, 5]
pontuacao_maxima = 11

# Inicializa a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# Função para desenhar raquetes e bola
def desenhar_objetos(raquete1, raquete2, bola, pontuacao1, pontuacao2):
    tela.fill(cor_preta)
    
    # Desenha as raquetes com suas cores
    pygame.draw.rect(tela, cor_raquete1, raquete1)
    pygame.draw.rect(tela, cor_raquete2, raquete2)
    
    # Desenha a bola
    pygame.draw.ellipse(tela, cor_branca, bola)
    
    # Desenha a linha central
    pygame.draw.aaline(tela, cor_branca, (largura_tela // 2, 0), (largura_tela // 2, altura_tela))
    
    # Desenha a pontuação
    fonte = pygame.font.Font(None, 74)
    texto_pontuacao1 = fonte.render(str(pontuacao1), True, cor_branca)
    texto_pontuacao2 = fonte.render(str(pontuacao2), True, cor_branca)
    tela.blit(texto_pontuacao1, (largura_tela // 4, 20))
    tela.blit(texto_pontuacao2, (largura_tela * 3 // 4 - texto_pontuacao2.get_width(), 20))
    
    pygame.display.flip()

def pong():
    raquete1 = pygame.Rect(10, altura_tela // 2 - tamanho_raquete[1] // 2, *tamanho_raquete)
    raquete2 = pygame.Rect(largura_tela - tamanho_raquete[0] - 10, altura_tela // 2 - tamanho_raquete[1] // 2, *tamanho_raquete)
    bola = pygame.Rect(largura_tela // 2, altura_tela // 2, 15, 15)
    bola_dx, bola_dy = bola_velocidade

    pontuacao1 = 0
    pontuacao2 = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and raquete1.top > 0:
            raquete1.y -= raquete_velocidade
        if teclas[pygame.K_s] and raquete1.bottom < altura_tela:
            raquete1.y += raquete_velocidade
        if teclas[pygame.K_UP] and raquete2.top > 0:
            raquete2.y -= raquete_velocidade
        if teclas[pygame.K_DOWN] and raquete2.bottom < altura_tela:
            raquete2.y += raquete_velocidade
        
        bola.x += bola_dx
        bola.y += bola_dy
        
        if bola.top <= 0 or bola.bottom >= altura_tela:
            bola_dy = -bola_dy
        if bola.colliderect(raquete1) or bola.colliderect(raquete2):
            bola_dx = -bola_dx
        
        if bola.left <= 0:
            pontuacao2 += 1
            if pontuacao2 >= pontuacao_maxima:
                exibir_vencedor("Jogador 2")
                return
            bola.x = largura_tela // 2
            bola.y = altura_tela // 2
            bola_dx = -bola_dx
        if bola.right >= largura_tela:
            pontuacao1 += 1
            if pontuacao1 >= pontuacao_maxima:
                exibir_vencedor("Jogador 1")
                return
            bola.x = largura_tela // 2
            bola.y = altura_tela // 2
            bola_dx = -bola_dx
        
        desenhar_objetos(raquete1, raquete2, bola, pontuacao1, pontuacao2)
        clock.tick(60)

def exibir_vencedor(jogador):
    tela.fill(cor_preta)
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render(f"{jogador} Venceu!", True, cor_branca)
    tela.blit(texto, (largura_tela // 2 - texto.get_width() // 2, altura_tela // 2 - texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

if __name__ == "__main__":
    pong()
