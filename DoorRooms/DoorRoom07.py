import pygame
import params, Block, imports, Activator

NowLocation = imports.room7_scaled
NowLocationRect = imports.room7_scaled_rect

walls = [
    Block.Block(1920, 10, 0, 520)
]

activator = [
    Activator.Activator(120, 50, 140, 645)
]

newXPos = 960
newYPos = 830