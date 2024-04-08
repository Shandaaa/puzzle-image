import copy
import pygame
pygame.mixer.init()
# colors (r,g,b)
white=(255,255,255)
black=(0,0,0)
red=(133,40,23)
yellwo=(237,190,30)
paige=(193,174,176)
hover=(1,170,255)
darkGray=(70,70,70)
lightGray=(50,45,45)
BGColor=(235,235,235)
title_text_color=(230,0,0)
buttons_col = {'1':(133,40,23),
               '3':(12,63,108),
               '2':(0,42,114)}
backgroud_col ={'1':(203,194,196),
              '2':(190,225,255),
              '3':(190,225,255)}
txt_col = (237,190,30)
reset_col = (50,45,45)
reset_txt_col=(255,255,255)
back_col = (50,45,45)
back_txt_col=(255,255,255)

# game settings
width=1000
hight=600
fps=5
title="Puzzle Game"
geo='Georgia'
#Sounds
Sounds={
    '1':pygame.mixer.Sound('sound/IcyTower.mp3'),
    '2':pygame.mixer.Sound('sound/FeedingFrenzy.mp3'),
    '3':pygame.mixer.Sound('sound/FrogFrenzy.mp3')
}

# intiate start /gaol and set tile,game size for a spacific level
def set_game(gameLevel):
    if gameLevel==1:
        tilesize=300
        gameSize=2
        start=[
            [2,3],
            [1,0]
        ]
        goal=[
            [1,2],
            [3,0]
        ]
    elif gameLevel==2:
        tilesize=200
        gameSize=3
        start=[
            [6,1,2],
            [4,0,3],
            [5,7,8] 
        ]
        goal=[
            [1,2,3],
            [4,5,6],
            [7,8,0]
        ]
    elif gameLevel==3 :
        tilesize=150
        gameSize=4
        start=[
            [2,5,1,4],
            [6,9,3,8],
            [10,13,7,12],
            [14,11,15,0]
            ]
        
        goal=[
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]
        ]
    else:
        tilesize=120
        gameSize=5
        start=[
            [1,7,2,4,5],
            [6,12,3,8,10],
            [11,17,13,9,15],
            [16,22,18,14,19],
            [21,0,23,24,20]
        ]
        
        goal=[
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,0]
        ]

    return tilesize,gameSize,start,goal



# dictionries for photos dirctories


IcyEasy={
        1:"images/IcyEasy/IcyEas1.jpg",
        2:"images/IcyEasy/IcyEas2.jpg",
        3:"images/IcyEasy/IcyEas3.jpg",
        4:"images/IcyEasy/IcyEas4.jpg",
}
FrogEasy = {
        1:"images/FrogEasy/FrogEas1.jpg",
        2:"images/FrogEasy/FrogEas2.jpg",
        3:"images/FrogEasy/FrogEas3.jpg",
        4:"images/FrogEasy/FrogEas4.jpg",

}
FeedingEasy = {
        1:"images/FeedingEasy/FeedingEas1.jpg",
        2:"images/FeedingEasy/FeedingEas2.jpg",
        3:"images/FeedingEasy/FeedingEas3.jpg",
        4:"images/FeedingEasy/FeedingEas4.jpg"
}
IcyMed={
        1:"images/IcyMed/IcyMed1.jpg",
        2:"images/IcyMed/IcyMed2.jpg",
        3:"images/IcyMed/IcyMed3.jpg",
        4:"images/IcyMed/IcyMed4.jpg",
        5:"images/IcyMed/IcyMed5.jpg",
        6:"images/IcyMed/IcyMed6.jpg",
        7:"images/IcyMed/IcyMed7.jpg",
        8:"images/IcyMed/IcyMed8.jpg",
        9:"images/IcyMed/IcyMed9.jpg",
}
FrogMed = {
        1:"images/FrogMed/FrogMed1.jpg",
        2:"images/FrogMed/FrogMed2.jpg",
        3:"images/FrogMed/FrogMed3.jpg",
        4:"images/FrogMed/FrogMed4.jpg",
        5:"images/FrogMed/FrogMed5.jpg",
        6:"images/FrogMed/FrogMed6.jpg",
        7:"images/FrogMed/FrogMed7.jpg",
        8:"images/FrogMed/FrogMed8.jpg",
        9:"images/FrogMed/FrogMed9.jpg"
}
FeedingMed = {
        1:"images/FeedingMed/FeedingMed1.jpg",
        2:"images/FeedingMed/FeedingMed2.jpg",
        3:"images/FeedingMed/FeedingMed3.jpg",
        4:"images/FeedingMed/FeedingMed4.jpg",
        5:"images/FeedingMed/FeedingMed5.jpg",
        6:"images/FeedingMed/FeedingMed6.jpg",
        7:"images/FeedingMed/FeedingMed7.jpg",
        8:"images/FeedingMed/FeedingMed8.jpg",
        9:"images/FeedingMed/FeedingMed9.jpg"
}
IcyHard = {
        1:"images/IcyHard/IcyHard1.jpg",
        2:"images/IcyHard/IcyHard2.jpg",
        3:"images/IcyHard/IcyHard3.jpg",
        4:"images/IcyHard/IcyHard4.jpg",
        5:"images/IcyHard/IcyHard5.jpg",
        6:"images/IcyHard/IcyHard6.jpg",
        7:"images/IcyHard/IcyHard7.jpg",
        8:"images/IcyHard/IcyHard8.jpg",
        9:"images/IcyHard/IcyHard9.jpg",
        10:"images/IcyHard/IcyHard10.jpg",
        11:"images/IcyHard/IcyHard11.jpg",
        12:"images/IcyHard/IcyHard12.jpg",
        13:"images/IcyHard/IcyHard13.jpg",
        14:"images/IcyHard/IcyHard14.jpg",
        15:"images/IcyHard/IcyHard15.jpg",  
        16:"images/IcyHard/IcyHard16.jpg"  
}
FrogHard={
        1:"images/FrogHard/FrogHard1.jpg",
        2:"images/FrogHard/FrogHard2.jpg",
        3:"images/FrogHard/FrogHard3.jpg",
        4:"images/FrogHard/FrogHard4.jpg",
        5:"images/FrogHard/FrogHard5.jpg",
        6:"images/FrogHard/FrogHard6.jpg",
        7:"images/FrogHard/FrogHard7.jpg",
        8:"images/FrogHard/FrogHard8.jpg",
        9:"images/FrogHard/FrogHard9.jpg",
        10:"images/FrogHard/FrogHard10.jpg",
        11:"images/FrogHard/FrogHard11.jpg",
        12:"images/FrogHard/FrogHard12.jpg",
        13:"images/FrogHard/FrogHard13.jpg",
        14:"images/FrogHard/FrogHard14.jpg",
        15:"images/FrogHard/FrogHard15.jpg",
        16:"images/FrogHard/FrogHard16.jpg" 
}
FeedingHard = {
        1:"images/FeedingHard/FeedingHard1.jpg",
        2:"images/FeedingHard/FeedingHard2.jpg",
        3:"images/FeedingHard/FeedingHard3.jpg",
        4:"images/FeedingHard/FeedingHard4.jpg",
        5:"images/FeedingHard/FeedingHard5.jpg",
        6:"images/FeedingHard/FeedingHard6.jpg",
        7:"images/FeedingHard/FeedingHard7.jpg",
        8:"images/FeedingHard/FeedingHard8.jpg",
        9:"images/FeedingHard/FeedingHard9.jpg",
        10:"images/FeedingHard/FeedingHard10.jpg",
        11:"images/FeedingHard/FeedingHard11.jpg",
        12:"images/FeedingHard/FeedingHard12.jpg",
        13:"images/FeedingHard/FeedingHard13.jpg",
        14:"images/FeedingHard/FeedingHard14.jpg",
        15:"images/FeedingHard/FeedingHard15.jpg",
        16:"images/FeedingHard/FeedingHard16.jpg"
}

IcyEx = {
        1:"images/IcyEx/icyEx1.jpg",
        2:"images/IcyEx/icyEx2.jpg",
        3:"images/IcyEx/icyEx3.jpg",
        4:"images/IcyEx/icyEx4.jpg",
        5:"images/IcyEx/icyEx5.jpg",
        6:"images/IcyEx/icyEx6.jpg",
        7:"images/IcyEx/icyEx7.jpg",
        8:"images/IcyEx/icyEx8.jpg",
        9:"images/IcyEx/icyEx9.jpg",
        10:"images/IcyEx/icyEx10.jpg",
        11:"images/IcyEx/icyEx11.jpg",
        12:"images/IcyEx/icyEx12.jpg",
        13:"images/IcyEx/icyEx13.jpg",
        14:"images/IcyEx/icyEx14.jpg",
        15:"images/IcyEx/icyEx15.jpg",
        16:"images/IcyEx/icyEx16.jpg",
        17:"images/IcyEx/icyEx17.jpg",
        18:"images/IcyEx/icyEx18.jpg",
        19:"images/IcyEx/icyEx19.jpg",
        20:"images/IcyEx/icyEx20.jpg",
        21:"images/IcyEx/icyEx21.jpg",
        22:"images/IcyEx/icyEx22.jpg",
        23:"images/IcyEx/icyEx23.jpg",
        24:"images/IcyEx/icyEx24.jpg",
        25:"images/IcyEx/icyEx25.jpg"
}
FeedingEx = {
        1:"images/FeedingEx/FeedingEx1.jpg",
        2:"images/FeedingEx/FeedingEx2.jpg",
        3:"images/FeedingEx/FeedingEx3.jpg",
        4:"images/FeedingEx/FeedingEx4.jpg",
        5:"images/FeedingEx/FeedingEx5.jpg",
        6:"images/FeedingEx/FeedingEx6.jpg",
        7:"images/FeedingEx/FeedingEx7.jpg",
        8:"images/FeedingEx/FeedingEx8.jpg",
        9:"images/FeedingEx/FeedingEx9.jpg",
        10:"images/FeedingEx/FeedingEx10.jpg",
        11:"images/FeedingEx/FeedingEx11.jpg",
        12:"images/FeedingEx/FeedingEx12.jpg",
        13:"images/FeedingEx/FeedingEx13.jpg",
        14:"images/FeedingEx/FeedingEx14.jpg",
        15:"images/FeedingEx/FeedingEx15.jpg",  
        16:"images/FeedingEx/FeedingEx16.jpg",
        17:"images/FeedingEx/FeedingEx17.jpg",
        18:"images/FeedingEx/FeedingEx18.jpg",
        19:"images/FeedingEx/FeedingEx19.jpg",
        20:"images/FeedingEx/FeedingEx20.jpg",
        21:"images/FeedingEx/FeedingEx21.jpg",
        22:"images/FeedingEx/FeedingEx22.jpg",
        23:"images/FeedingEx/FeedingEx23.jpg",
        24:"images/FeedingEx/FeedingEx24.jpg",
        25:"images/FeedingEx/FeedingEx25.jpg"
}

FrogEx = {
        1:"images/FrogEx/FrogEx1.jpg",
        2:"images/FrogEx/FrogEx2.jpg",
        3:"images/FrogEx/FrogEx3.jpg",
        4:"images/FrogEx/FrogEx4.jpg",
        5:"images/FrogEx/FrogEx5.jpg",
        6:"images/FrogEx/FrogEx6.jpg",
        7:"images/FrogEx/FrogEx7.jpg",
        8:"images/FrogEx/FrogEx8.jpg",
        9:"images/FrogEx/FrogEx9.jpg",
        10:"images/FrogEx/FrogEx10.jpg",
        11:"images/FrogEx/FrogEx11.jpg",
        12:"images/FrogEx/FrogEx12.jpg",
        13:"images/FrogEx/FrogEx13.jpg",
        14:"images/FrogEx/FrogEx14.jpg",
        15:"images/FrogEx/FrogEx15.jpg",  
        16:"images/FrogEx/FrogEx16.jpg",
        17:"images/FrogEx/FrogEx17.jpg",
        18:"images/FrogEx/FrogEx18.jpg",
        19:"images/FrogEx/FrogEx19.jpg",
        20:"images/FrogEx/FrogEx20.jpg",
        21:"images/FrogEx/FrogEx21.jpg",
        22:"images/FrogEx/FrogEx22.jpg",
        23:"images/FrogEx/FrogEx23.jpg",
        24:"images/FrogEx/FrogEx24.jpg",
        25:"images/FrogEx/FrogEx25.jpg"
}

image_path={
        '11': IcyEasy,
        '12': IcyMed,
        '13': IcyHard,
        '14': IcyEx,
        '21': FrogEasy,
        '22': FrogMed,
        '23': FrogHard,
        '24':FrogEx,
        '31': FeedingEasy,
        '32': FeedingMed,
        '33': FeedingHard,
        '34': FeedingEx
}

# get image of each tile
def get_image(gameType,image_index):
    image=image_path[gameType]
    return image[image_index]
