
# AVERLAND ADVENTURES
___

This is a simple text-based "Choose Your Own Adventure" styled RPG game.

# Five UX Planes

## Strategy

Users will want clean presentation of text.
Users will want unambiguous options presented to them.
Users will want to be able to loop through each area of the game in a logical way.
Users will want a progression system.
Users will want equipment for their character.
Users will want to be able to earn gold for more equipment.
Users will want to be able to defeat enemies.
Users will want to be able to clear quests.
Users will want to be able to restart if they fail.
Users will want the option to quit once they are done.

## Scope

How the app should operate.

## Structure

How the app should be built.
A flowchart was drawn up before any code was written to better understand how each function would lead to one another to create the gameplay loop.<br>
![Image of a flowchart that established the basis for the how the game would operate](assets/readme_images/game_flow_chart.png)

A flowchart was drawn up before any code was written to better map out the road for when it came time to code it.<br>
![Image of a flowchart that established the basis and map for the road 'dungeon'](assets/readme_images/game_road_flow_chart.png)

A flowchart was drawn up before any code was written to better map out the forest for when it came time to code it.<br>
![Image of a flowchart that established the basis and map for the forest 'dungeon'](assets/readme_images/game_forest_flow_chart.png)

### Main Scripts

#### run.py

#### Helper Scripts

##### game_slow_functions

##### game_inside_travels

##### game_outside_travels

### World Scripts

#### game_intro

#### game_hubworld

#### game_road

#### game_forest

### Other Scripts

#### game_characters

#### game_battles

## Skeleton

How the app should execute its code.

## Surface

Description of visuals.

# Features

## Game

## Intro

### Rules

## Hubworld

### Town

### Shop

### Quests

### Adventure

## Merchant Road

## Forest

## Features Left to Implement



# Testing

There were multiple stages of testing as the project developed.<br>

|TEST|PROCESS|EXPECTATION|RESULT|
|--|--|--|--|
| What was test | What I did | What I expected | Did it work |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

# Validating

## run.py
The run.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the run.py validation check](assets/readme_images/linter_images/linter_run_validation.png)

## game_slow_functions
The run.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_slow_functions.py validation check](assets/readme_images/linter_images/linter_game_slow_functions_validation.png)

## game_inside_travels
The game_inside_travels.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_inside_travels.py validation check](assets/readme_images/linter_images/linter_game_inside_travels_validation.png)

## game_outside_travels
The game_outside_travels.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_outside_travels.py validation check](assets/readme_images/linter_images/linter_game_outside_travels_validation.png)

## game_characters
The game_characters.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_characters.py validation check](assets/readme_images/linter_images/linter_game_characters_validation.png)

## game_intro
The game_intro.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_intro.py validation check](assets/readme_images/linter_images/linter_game_intro_validation.png)

## game_hubworld
The game_hubworld.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_hubworld.py validation check](assets/readme_images/linter_images/linter_game_hubworld_validation.png)

## game_road
The game_road.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_road.py validation check](assets/readme_images/linter_images/linter_game_road_validation.png)

## game_forest
The game_forest.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_forest.py validation check](assets/readme_images/linter_images/linter_game_forest_validation.png)

## game_battles
The game_battles.py file was fully checked in the CI Python Linter and returned no errors.<br>
![Image showing the game_battles.py validation check](assets/readme_images/linter_images/linter_game_battles_validation.png)

# Bugs

All known bugs have been found and removed.<br>
Notable bugs included:<br>
1. Example.<br>

2. Example.<br>

3. Example.<br>

4. Example.<br>

# Deployment

This app was deployed through Heroku by being linked to the Github repository.<br>
In order to deply the site:<br>

1. I navigated to my `Dashboard` on Heroku.<br>
2. I selected the `New` dropdown and selected `Create new app`. <br>
3. I gave the app the name "Averland Adventures" and set the region to Europe.<br>
4. I navigated to the `Settings` tab.<br>
5. I added the `heroku/python` and `heroku/nodejs` to by clicking the `Add buildpack` button.<br>
6. I created a `Config Var` by selecting `Reveal Config Vars` and adding "Port" to the `Key` and "8000" to the `Port`. I confirmed this by selecting `Add` <br>
7. I navigated to the `Deploy` tab.
8. I selected `GitHub` as my deployment method.
9. I searched for and connected my repository name under the `App connected to GitHub` selection.
10. I initially deployed it manually by selecting `main` as my branch and selecting `Deploy Branch`.
11. I have since anabled `Automatic Deployments` by selecting `Enable Automatic Deploys`

The live link can be found here - 

# Credits

## Content
