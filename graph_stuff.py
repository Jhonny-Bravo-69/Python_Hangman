"""graphing all the wins, gusses, and losses"""
import matplotlib.pyplot as plt

# whats in it
categories = ['Wins', 'Losses']
values = []

# presentation
plt.bar(categories, values)
plt.title('Hangman Graph')
