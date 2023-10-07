from sketchpy import canvas
import turtle as tur
from turtle import Screen
s=Screen()
s.bgcolor("Black")

ab=canvas.sketch_from_svg("pr.svg",scale=75)
ab.draw()

