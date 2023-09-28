#Programmed by: Wyatt T. Cero
#Laboratory Activity 1
#September 9, 2023

lbs = input('Weight in Pounds (lbs): ')
print('Weight converted to Kilograms (kgs): ',(float(lbs) / 2.205), end='\n')

print('========================================')

mi = input('Length in Miles (mi): ')
print('Length converted in Kilometers (Km): ',(float(mi)*1.6), end='\n')

print('========================================')

F = float(input('Temperature in Farenheit (°F): '))
celsius = (F - 32)*5/9
print('Temperature in Celsius (°C): ',(celsius), end='\n')

print('========================================')

Age1 = float(input('Age of student 1: '))
Age2 = float(input('Age of student 2: '))
Age3 = float(input('Age of student 3: '))
Age4 = float(input('Age of student 4: '))
Age5 = float(input('Age of student 5: '))
Age6 = float(input('Age of student 6: '))
Age7 = float(input('Age of student 7: '))
Age8 = float(input('Age of student 8: '))
Age9 = float(input('Age of student 9: '))
Age10 = float(input('Age of student 10: '))

avg = (Age1+Age2+Age3+Age4+Age5+Age6+Age7+Age8+Age9+Age10)/10

print('The average age of students is: ',avg)

print('========================================')

hero1 = "**Kazuma**"
hero2 = '**Yuji**'
hero3 = '**Haerin**'
hero4 = '**Andrei**'
hero5 = '**Kaiser**'
vil = '**Gojo Saturno**'

eqitem='~Excalibur~'
eqitem2='~AWP~'
eqitem3='~Sheild of Chaos~'
eqitem4='~Enma~'
eqitem5="~Power Wand~"

Kabs = '<Plum Blossom Flying Dragon>'
Gojoab = ["<Hollow Purple>", "<Infinity Knowledge>", "<Reversal Red>"]

item = '<Can of Coke>'

story = f"""In the mystical realm of Eldoris, where magic flowed like rivers and mythical creatures roamed freely
suddenly attacked by a ressurected  demonic deity named "(vil)".
Our heroes,{hero1}, The Pinnacle of human strength; {hero2}; The Tank, {hero3}; The best sniper of Eldoris, {hero4}; The Blind swordsman, and {hero5}; The Beastman
Together they banded together to destroy {vil}.
The battle lasted for 4 whole months, with each month losing one of their members
The first to perish was {hero4}, the Blind Swordsman.
He took an immense blow by tanking the limitless power of {vil} {Gojoab[1]}, rendering {hero1} dead from the vast amounts of knowledge he could not understand
The second to perish was {hero3}, who took a piercing shot from {vil}'s {Gojoab[2]} after she was spotted 1000 miles from the battlefield who was providing long range support.
The third to perish would be {hero2}; The tank, he would suffer severe post traumatic syndrome disorder after seeing countless of lives perish at their inability to slay the resurrected deity.
The Fourth to perish would be {hero5}: The beastman, {hero1}'s best and long time friend, {hero5} suffered a gruesome death at the hands of {vil}'s army as he was tortured day and night until no more.
With {hero1} being the only one left alive, he stormed into the enemies den knowing he would not make it out alive.
{hero1} slayed every enemy that hindered his path and used an item {item} that boosts his attacks, ultimately reaching the deity {vil}'s throne room
Their fight lasted for 3 days,
both trading blows; with {vil} taking out{hero1}'s left arm and {hero1} sneaking an attack that takes out {vil}'s right arm they were both at a stand still as they were
tiring each other equally.
{hero1} reminisces the time he had spent with his fallen comrade as he charges his final and strongest attack {Kabs}.
The deity {vil} acknowledging {hero1} for his strength and will to fight and provide him with entertainment,
also charges his strongest attack {Gojoab[0]}.
Both of them ended up perishing together, leaving no trace of bloodshed within a 50mile radius.
As time went on, the realm of Eldoris slowly began to heal and with its dwellers erecting statues of our mighty heroes."""

print(story)
