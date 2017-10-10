# Kivy Gamepad

The basic idea is to create a touch screen controller for a kivy game that is re-useable.

## Design

*Start Screen* should have a large game title, smaller game company label, and start button
Label text should be configured in a common location.
The start button should take the player to the game demo screen.

*Game Demo Screen* should have a transparent bar over the bottom 25% of the screen.
The bar should have a left side 9 button directional pad and a right side 4 different colored action buttons in a diamond formation.
The last 10 key presses should be displayed in a stack somewhere on the screen; think mortal kombat training practice sessions.

## Why

Standardizing the UI controls will make it faster to create games for phones and tablets.
I think having a boilerplate project with event hooks and button functions would be cool.
So that is what I am going to do.