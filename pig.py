import argparse
import random
import sys
import datetime


def throw_the_die(sides=6):
    """
    dice roll
    """
    return random.randint(1, sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.potential = 0

    def show(self):
        print(f"{self}")

    def __str__(self):
        """String representation"""
        return f"{self.name}'s Total = {self.total}"

    def play_turn(self):
        """
        Play one turn
        """
       
        print("-" * 50)
        print(f"Current player {self.name}")
        print()
        turn_total = 0
        roll_hold = 'r'
        while roll_hold == "r":
            die = throw_the_die()
            if die == 1:
                print(f"Roll: {die}")
                print(f"{self.name} Scratched!")
                self.show
                break

            

            turn_total += die
            self.potential = self.total + turn_total
            # Print some information to the user. My recommendation is to:
            # print turn_total,
            # print possible total if I hold, total + turn_total
            # print real total
            print("-" * 50)
            print(f"Roll: {die}")
            print()
            print()
            print(f"Points this turn: {turn_total}")
            print()
            print(f"Score on hold: {self.potential}")
            print()
            print(f"Current Score: {self.total}")
            print()

            roll_hold = input("Roll(r) or Hold(h)? ").lower()
            print()


        if roll_hold == 'h':
            # update the player's total
            self.total += turn_total

            

        if roll_hold == "x":
            exit()

        self.show()

class ComputerPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def play_turn(self):
        """
        Computer player turn 
        """

        print("-" * 50)
        print(f"Current player {self.name}")
        print()
        turn_total = 0
        scratch = False
        while turn_total >= min(self.total, 100 - self.total):
            die = throw_the_die()
            if die == 1:
                print(f"Roll: {die}")
                print(f"{self.name} scratched!")
                scratch = True
                break 

            if not scratch:
                self.total += turn_total 
                print("-" * 50)
                print(f"Roll: {die}")
                print()
                print()
                print(f"Points this turn: {turn_total}")
                print()
                print(f"Score on hold: {self.total + turn_total}")
                print()
                print(f"Current Score: {self.total}")
                print()
            
            self.show


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):

        for player in self.players:
            if player.total >= 100 or player.potential >= 100:
                self.winner = player
                return True

        return False


    def play_game(self):
        current_player = self.players[0] 

        while not self.check_winner():
            # play the game
            for player in self.players:
                current_player = player
                current_player.play_turn()
                if current_player.total >= 100:
                    break
                
                
        print()
        print()
        print("-" * 50)
        print(f"{self.winner.name} is victorious!")

class TimedGame(Game):

    def __init__(self, player1, player2, time_limit):
        super().__init__(player1, player2)
        self.start_time = datetime.datetime.now()
        self.time_limit = time_limit

    def check_time(self, time_now):
        """
        Check for the time
        :return: True if time expired
        """
        return (time_now - self.start_time).total_seconds() > self.time_limit


    def play_game(self):
        current_player = self.players[0]
        time_flag = False
        while not self.check_winner() or not time_flag:
            for player in self.players:
                current_player = player
                current_player.play_turn()
                if current_player.total >= 100:
                    break
                if time_flag:
                    break

            time_flag = self.check_time(datetime.datetime.now())

            if player1.total > player2.total:
                print()
                print()
                print(f"Time's up!")
                print(f"{player1.name} is vicotorious!")
                exit()
            
            else:
                print()
                print()
                print(f"Time's up!")
                print(f"{player2.name} is vicotorious!")
                exit()

                
def make_player(player_type, player_name):
    """
    Factory function
    :param player_type:
    :param player_name:
    :return:
    """
    if player_type.upper() == 'C':
        return ComputerPlayer(player_name)
    elif player_type.upper() == 'H':
        return Player(player_name)
    else:
        raise ValueError("I don't know what to build!!!!")

def make_game(player1, player2, timed=False):
    if timed:
        return TimedGame(player1, player2, float(60))
        
    else:
        return Game(player1, player2)
    
   
    
       

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--player1")
    parser.add_argument("--player2")
    parser.add_argument("--timed", action='store_true')
    args = parser.parse_args()
    player1 = make_player(args.player1, "John")
    player2 = make_player(args.player2, "HAL")
    print("Welcome to Pig")
    print()
    pig_game = make_game(player1, player2, args.timed)
    pig_game.play_game()

    
