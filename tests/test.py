import pytest

from game import Game


def test_get_start_player1():
    """Test to verify that player1 starts"""
    sequence = {
                    "player1":
                        {
                            "movimientos":["D","DSD","S","DSD","SD"],
                            "golpes":["K","P","","K","P"]
                        }, 
                    "player2": {
                        "movimientos":["SA","SA","SA","ASA","SA"],
                        "golpes":["K","","K","P","P"]
                    }
                }

    game = Game(sequence)
    player1 = game.get_player1()
    player2 = game.get_player2()
    
    assert player1 == game.get_start()
    assert 1 == game.get_start().get_type()

def test_get_start_player2():
    """Test to verify that player2 starts"""
    sequence = {
                    "player1":
                        {
                            "movimientos":["D","DSD","S","DSD","SD"],
                            "golpes":["K","P","P","K","P"]
                        }, 
                    "player2": {
                        "movimientos":["SA","SA","SA","ASA","SA"],
                        "golpes":["K","","K","P","P"]
                    }
                }

    game = Game(sequence)
    player1 = game.get_player1()
    player2 = game.get_player2()
        
    assert player2 == game.get_start()
    assert 2 == game.get_start().get_type()

def test_play_winner_player2():
    """Test to run sequence where Player 2 wins"""
    sequence = {
                    "player1":
                        {
                            "movimientos":["D","DSD","S","DSD","SD"],
                            "golpes":["K","P","","K","P"]
                        }, 
                    "player2": 
                        {
                            "movimientos":["SA","SA","SA","ASA","SA"],
                            "golpes":["K","","K","P","P"]
                        }
                }

    game = Game(sequence)
    player1 = game.get_player1()
    player2 = game.get_player2()
    first_play = game.get_start()
    total_mov = game.movs(first_play)
    player_winner = game.play(total_mov)


    assert player1.get_energy() == 0
    assert player2.get_energy() == 2

def test_play_winner_player1():
    """Test to run sequence where Player 1 wins"""
    sequence = {
                    "player1":
                        {
                            "movimientos":["D","DSD","S","DSD","SD"],
                            "golpes":["K","P","P","K","P"]
                        }, 
                    "player2": 
                        {
                            "movimientos":["SA","SA","SA","ASA","SA"],
                            "golpes":["K","","","P","P"]
                        }
                }

    game = Game(sequence)
    player1 = game.get_player1()
    player2 = game.get_player2()
    first_play = game.get_start()
    total_mov = game.movs(first_play)
    player_winner = game.play(total_mov)

    assert player1.get_energy() == 2
    assert player2.get_energy() == 0

def test_play_case1():
    """Test to run sequence where Player 1 wins"""
    sequence = {
                    "player1":
                        {
                            "movimientos":["SDD", "DSD", "SA", "DSD"],
                            "golpes":["K","P","K","P"]
                        }, 
                    "player2": 
                        {
                            "movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],
                            "golpes":["P","K","K","K", "P", "K"]
                        }
                }

    game = Game(sequence)
    player1 = game.get_player1()
    player2 = game.get_player2()
    first_play = game.get_start()
    total_mov = game.movs(first_play)
    player_winner = game.play(total_mov)

    assert player1.get_energy() == -1
    assert player2.get_energy() == 1

def test_play_case2():
    """Test to run sequence where Player 1 wins"""
    sequence = {
                    "player1":
                        {
                            "movimientos":["DSD", "S"],
                            "golpes":["P",""]
                        }, 
                    "player2": 
                        {
                            "movimientos":["", "ASA", "DA", "AAA", "", "SA"],
                            "golpes":["P","","P","K", "K", "K"]
                        }
                }

    game = Game(sequence)
    player1 = game.get_player1()
    player2 = game.get_player2()
    first_play = game.get_start()
    total_mov = game.movs(first_play)
    player_winner = game.play(total_mov)

    assert player1.get_energy() == -1
    assert player2.get_energy() == 3
