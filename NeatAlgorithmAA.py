from GameSettings import *

def game_loop(genomes, config):

    nets = []
    ge = []
    players = []

    for __, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        players.append(Player())
        g.fitness = 0
        ge.append(g)

    asteroids = [0,
     asteroid(1, playable_height-39, 10.5, 35, 39, 0),
     asteroid(2, playable_height-25, 15, 25, 25, 5),
     asteroid(3, playable_height-30, 12.5, 30, 30, 10),
     asteroid(4, playable_height-35, 10, 35, 35, 30)]

    for x, player in enumerate(players):
        game_over = False
        while not game_over:
            ge[x].fitness += 0.1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                output = nets[x].activate(((player.x/169),
                    GetDistance(1, player, asteroids),
                    GetDistance(2, player, asteroids),
                    GetDistance(3, player, asteroids),
                    GetDistance(4, player, asteroids)))

                if output[0] >= 0.5:
                    player.moveUP()
                elif output[0] < 0.5:
                    player.moveDOWN()

                print(output)



            player.y += player.change

            if player.y > playable_height - player.height:
                player.y = playable_height - player.height
            elif player.y < 0:
                player.y = 0

            window.fill((0, 0, 0))
            window.blit(bg_img, (0, 0))

            player.draw()


            for n in range(1, 5):
                if asteroids[n].x < 0:
                    player.score += 1
                    ge[x].fitness += 5
                asteroids[n].move(player)
                if asteroids[n].collision(player):
                    ge[x].fitness -= 1
                    players.pop(x)
                    nets.pop(x)
                    ge.pop(x)
                    asteroids[n].reset(asteroids)
                    game_over = True


            Text_display("Score: " + str(player.score * 100), white, 0, 200)
            Text_display("Asteroid 1: " + str(GetDistance(1, player, asteroids)), white, 0, 220)
            Text_display("Asteroid 2: " + str(GetDistance(2, player, asteroids)), white, 0, 240)
            Text_display("Asteroid 3: " + str(GetDistance(3, player, asteroids)), white, 0, 260)
            Text_display("Asteroid 4: " + str(GetDistance(4, player, asteroids)), white, 0, 280)
            Text_display("Space Ship Position: " + str(player.y / 169), white, 0, 300)


            pygame.display.update()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    winner = pop.run(game_loop,50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "ConfigFile.txt")
    run(config_path)
