# Building Murder Mystery

This week, we'll work step by step to build a simple Ren'Py muder mystery. We'll cover key components like UI screens, variables, scene transitions, and interactions.

## 1. Setting Up the Game

Create a new Ren'Py project and open the `script.rpy` file in an editor like VS Code. Add the following basic structure:

```renpy
# Define characters
define s = Character("Mary", color="#c8ffc8")
define m = Character("Me", color="#c8c8ff")
define x = Character("Max", color="#ffc8c8")

# Game state variables
default suspicion = 0
default inventory = []
```

## 2. Creating UI Elements

We add a **Suspicion Meter** and **Inventory Display** using Ren'Py screens:

```renpy
screen suspicion_meter():
    frame:
        xalign 0.05 yalign 0.02
        text "Suspicion: [suspicion]"

screen inventory():
    frame:
        xalign 0.95 yalign 0.02
        if inventory:
            text "Inventory: [', '.join(inventory)]"
        else:
            text "Inventory: Empty"
```

These screens update automatically as variables change.

## 3. Starting the Game

In the `start` label, we show the UI elements and set the scene. Make sure your music file is designed to loop, and use the name of the file that you place in your audio folder:

```renpy
label start:
    show screen suspicion_meter
    show screen inventory
    play music "background.mp3"
    
    scene bg lecturehall with fade
    "The usual chatter of students fades as I stare at the empty seat in the front row."
    "It belongs to Ryan. He never missed a class."
    "But today, he's missing. And not just from class."
```

## 4. Scene Transitions and Narration

Use `scene` and `with fade` to switch locations smoothly:

```renpy
scene bg uni with fade
"Outside, the campus is abuzz with whispers. A body was found near the library."
"Ryan's body."
```

## 5. Adding Choices

Choices affect the game's state. Example:

```renpy
menu:
    "Talk to Mary."
    "Investigate the scene."

    "Talk to Mary.":
        jump talk_mary
    "Investigate the scene.":
        jump investigate
```

Each choice jumps to a different label.

## 6. Handling Inventory and Suspicion

Updating variables dynamically:

```renpy
label talk_mary:
    s "I saw Ryan yesterday. He looked worried."
    $ suspicion += 1
    return

label investigate:
    "You find a torn note."
    $ inventory.append("Torn Note")
    return
```

## 7. Ending the Game

You can define conditions for different endings:

```renpy
if suspicion > 5:
    "Your investigation has drawn too much attention. Game Over."
    return
```

## 8. Images

All images used in the game need to be included in the images folder. Names of files should exactly match the code, including spaces. Use the same resolution as your game settings, and make sure your characters have transparent backgrounds.

## 9. Build for Web

In the main menu, select "web" under build. Choose "Open Build Directory" and copy that folder to your GitHub pages repository to prepare your website for submission. The completed demo is deployed as an [example](/renpy/).

