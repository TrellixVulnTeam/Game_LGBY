import pygame
import params, Block, imports, Activator

NowLocation = imports.room4_scaled
NowLocationRect = imports.room4_scaled_rect

walls = [
    Block.Block(1920, 10, 0, 520)
]

activator = [
    Activator.Activator(120, 50, 1105, 625)
]

newXPos = 960
newYPos = 830