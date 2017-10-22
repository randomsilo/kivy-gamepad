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

```bash
env PYTHONPATH=/shop/randomsilo/kivy-gamepad
```

## Contribution

if you want to contribute, please make a pull request.
In order to make that process faster please review the basic style guide and expanded conventions.
If the style recommendations bother you please reach out to have a conversation.
I am always learning and I am open to new ways; but, I need to get started and refactor as necessary.
This is where I am starting in regards to style.

Any and all help is appreciated.

### Basic Style Guide

[PEP8](https://www.python.org/dev/peps/pep-0008/)

### Expanded Conventions

Area  | Convention | Notes
--- | ---
Interface            | CamelCaseNameInf | Only abstract methods, no implementations
Abstract Base Case   | CamelCaseNameAbc | Extends from interface, no implementations, has common helper functions
Stock Implementation | CamelCaseNameImplStock | Extends ABC, implements INF
Other Implementation | CamelCaseNameImplOther | Extends stock or ABC, implements or overrides methods
Class Name           | CamelCaseNameCls | A stand alone class has Cls on the end of it
Independant Behavior | CamelCaseNameMixIn | A mix in is encapsulated behavior added by inheritance with no intent to modify
Function Name        | lowercase_with_unscores | The word function is used for functions outside of a class
Method Name          | lowercase_with_unscores | The word method is used for functions inside of a class
Private Variables    | _name_typehint | Private class variables with a type hint for clarity: _count_int, _money_float, _name_str, _name_inst (class instance)

