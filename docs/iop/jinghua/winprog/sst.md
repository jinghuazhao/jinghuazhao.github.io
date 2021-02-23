---
layout: article
title: The SST Class Hierarchy by Marshall Brain & Kelly Campbell
---

The concept of a *class hierarchy* is often an extremely difficult one
for new C++ programmers to master. While simple to define (A class
hierarchy is a set of classes that build on top of each other using
inheritance and virtual functions) and simple to justify (the main
reason to create class hierarchies is reusability), it is rather
difficult to move from concept to proficiency because hierarchies tend
to be large self-referencing masses of code. It can take quite a bit of
time to master a large hierarchy, especially if it is your first.

None the less, one of the best ways to learn about C++ is to examine and
use existing hierarchies. In this way you can begin to understand the
advantages of inheritance and polymorphism, and you can also gain access
to a number of valuable design techniques. The problem with existing
hierarchies is that in most cases they are quite complex. For example,
the MFC class hierarchy contains hundreds of classes, thousands of
member functions and tens of thousands of lines of code. People may
spend years completely understanding all aspects of the hierarchy.

The purpose of this article is to introduce SST - the Super Simple
Toolkit - as an example class hierarchy. SST is a GUI class hierarchy
that allows you to create super simple GUI applications very easily. As
such, you can compare it to MFC, Borland\'s OWL classes, Turbo Vision,
the Java class hierarchy, etc. SST is, as the name implies, super
simple. However, in its simplicity it carries three important
advantages:

1.  Because it is so simple, you can master SST in just a day or two.
    That is, you can completely understand the use of the hierarchy,
    create simple applications with it, add several new controls to it,
    and understand the source code that creates it, in just a couple of
    days.
2.  SST, although small, carries all the core ideas found in larger
    class hierarchies. By exposing you to these fundamental concepts,
    SST can make it much easier to understand larger hierarchies
3.  SST is extremely portable, and has been compiled under Visual C++,
    Borland C++, AT&T\'s C-Front compiler, etc. It is therefore very
    easy to adapt to a variety of learning environments.

SST is therefore a valuable learning tool for the beginning C++ programmer.

### Introduction to the SST Hierarchy

All GUI hierarchies let you create standard GUI objects such as buttons,
labels, scroll bars, etc. SST is no different: It is just a bit simpler.
The SST toolkit lets you create buttons, labels, and edit areas. It is
simple enough to be used, understood and extended in just a few days. In
addition, you can examine the source code (all source code for SST
appears at the end of this article) and learn from the inheritance
techniques that it contains. SST follows standard usage patterns seen in
most GUI toolkits.

SST is a portable, character-based toolkit. This feature allows it to
run on almost any platform, although it does inhibit beauty just a bit.
A typical program created using SST looks like this:

![SST Application Example](screenshot.gif){width="349" height="224"}
SST Application Example

In this window, there are static labels (\"Celsius Temperature\",
\"Fahrenheit Temperature\", and \"212\"), an Input area into which the
value 100 has been typed, and two buttons (\"Convert\" and \"Quit\").
The Input area has focus, as represented by the \'=\' (equal sign)
around it. The application shown implements a simple
Celsius-to-Fahrenheit converter.

An SST program can contain the following GUI objects:

-   main window (one)
-   labels
-   buttons
-   input areas

SST understands the following keyboard semantics:

-   change control focus with the tab key (or Shift-tab)
-   activate buttons with the return key

Edit controls accept keystrokes and the backspace character.

|-----------------------------------------------------------------------|
| Visualizing Class Hierarchies                                         |
|=======================================================================|
| One of the most frusterating things when you are first using class    |
| hierarchies is the \"Where am I?\" feeling you get. Many larger       |
| hierarchies have *hundreds* of classes. A good way to get around this |
| feeling is to use a class hierarchy visualization tool like           |
| [CodeVizor](http://codevizor.iftech.com/rd/r_dcsb2cv.asp). With       |
| CodeVizor you can drag the SST source code into the CodeVizor tool    |
| and in about 30 seconds have a beautiful, clickable (and printable!)  |
| class hierarchy chart. You can even color classes individually or in  |
| groups so that they stand out!\                                       |
| Get CodeVizor and see how much easier undestanding class hierarchies  |
| becomes!                                                              |
|                                                                       |
| [CodeVizor Web Site](http://codevizor.iftech.com/rd/r_dcsb2cv.asp)    |
|-----------------------------------------------------------------------|

The SST hierarchy contains 10 classes. Six of the classes are arranged
in a hierarchy as shown below:

![The SST class hierarchy](hier.gif){width="200" height="125"}

The remaining four are Auxiliary classes:

-   Event - event class used in Object::HandleEvent
-   ObjectList - object list class used in Window
-   Screen - screen drawing class used in Object
-   Strclass - a simple string class used in Input

In the following sections you will learn how to create simple
applications using these classes, and you will also learn how the source
code for the classes works.

### Creating the Simplest SST Application

All SST applications share several fundamental elements. No matter how
simple or complex, you will always take the following steps in every SST
application:

-   Derive your application from the Window class. Declare its controls
    as members
-   Create a constructor for the derived class that creates and
    initializes the controls inside the window
-   Override the HandleEvent member of the window class to handle events
    from buttons

Using these steps, the simplest possible application that you can create
is a window that contains a quit button. To create such an application,
you would start by inheriting from the Window class:

```c
    #include <IOSTREAM.H>
    #include <STRSTREA.H>

    #include "button.h"
    #include "rect.h"

    #include "window.h"
    class App: public Window
    {
    public:
        App( char *s, Rect &r );
        virtual void HandleEvent( Event &event );
    };

    App app( "Test", Rect(1, 1, 80, 24) );

    ...

    void main()
    {
        app.Execute();
    }
```

Note that this code declares a class named App derived from Window, and
this derived class overrides the constructor and the HandleEvent
function. Next the program creates an instance of this class as a global
variable and passes it the string \"Test\" (which will act as the
window\'s name) and the size and position of the Window on the screen
(you can assume the screen to be a 2-D character grid with a size of 80
characters wide by 24 characters high, so the size specification here
fills the screen). Then the code calls the class\'s Execute member in
the main function to get the ball rolling.

You would then create a new constructor for the App class. This
constructor\'s job is to Insert controls into the window:

```c
    const int QUIT  = 100;

    App::App( char *s, Rect &r ): 
        Window( s, r ), count( 0 )
    {
        Insert( new Button(" Quit", Rect(50, 18, 57, 20), QUIT) );
    } 
```
The Insert function creates a new instance of the Button class, passing
the button its title (\"Quit\"), location and size, and an ID of 100 in
the constant named QUIT. The ID will be used to handle events generated
by the button.

You would then override the HandleEvent member function in the Window
class to handle events produced by the Quit button:

```c
    void App::HandleEvent( Event &event)
    {
        Window::HandleEvent( event );

        if( event.type == COMMAND )
        {
            switch( event.message )
            {
                case QUIT:
                  Close();
                  screen.Clear();
                  break;
            }
        }
        event.type = CLEAR;
    }
```
This code first calls the Window class\'s default HandleEvent function
so it can handle any events it understands automatically. Any unhandled
events are then tested to see if they are COMMAND events. If so, then
they are tested to see if they come from the QUIT button. If so, the
application terminates by closing the window and clearing the screen.

If you assemble these pieces and run the application, you will find that
the window appears, that it contains a quit button, and when you press
the return key (to activate the button) the application terminates. The
easiest way to compile the program is to take all of the SST classes
(shown at the end of the article) and place them in a directory. Add the
code shown here to an additional CPP file. Include all of the CPP files
in a project or MAKEFILE and compile and link them (If you are using the
Visual C++ or Borland compilers, you will want to create a normal
text-based console application). Then execute the application. SST
assumes that the output window handles ANSI character sequences, so if
you are using DOS or Win 95 be sure to set a device to ANSI.SYS in the
config.sys file (in other words, add \"DEVICE=ANSI.SYS\" to the
config.sys file) and reboot. If you are using NT or UNIX, special
versions of appropriate files are supplied.

Below is a slightly more advanced program that makes use of two of the
controls available in SST (labels and buttons). This program implements
a simple increment facility. When you activate the \"Increment\" button,
the counter increments by one. When you activate the \"Quit\" button the
program terminates. You move focus between the two buttons by pressing
the Tab key, and activate the currently focused button by hitting the
return key.

```c
    // Counter program

    #include <IOSTREAM.H>
    #include <STRSTREA.H>

    #include "button.h"
    #include "input.h"
    #include "label.h"
    #include "rect.h"
    #include "window.h"

    class App: public Window
    {
        Label *number;
        int count;
    public:
        App( char *s, Rect &r );
        virtual void HandleEvent( Event &event );
    };

    App app( "Test", Rect(1, 1, 80, 24) );

    const int QUIT = 100;
    const int COUNT = 101;

    App::App( char *s, Rect &r ): 
        Window( s, r ), count( 0 )
    {
        Insert( new Label("Count: ", 
            Rect(20, 5, 30, 7)) );
        number = new Label("0", 
            Rect(31, 5, 40, 7));
        Insert( number );

        Insert( new Button(" Increment", 
            Rect(28, 18, 40, 20), COUNT) );
        Insert( new Button(" Quit", 
            Rect(50, 18, 57, 20), QUIT) );
    }

    void main()
    {
        app.Execute();
    }

     void App::HandleEvent( Event &event)
    {
        char t[100];
        ostrstream ostr ( t, 100 );

        Window::HandleEvent( event );

        if( event.type == COMMAND )
        {
            switch( event.message )
            {
                case COUNT:
                    count++;
                    ostr.width(4);
                    ostr << count << ends;                  
                    number->SetTitle( t );
                    break;

                case QUIT:
                    Close();
                    screen.Clear();
                    break;
            }
        }
        event.type = CLEAR;
    }
```
The only difference between this program and the first program is the
fact that more controls are inserted into the window in the window
constructor, and the HandleEvent function handles two events instead of
one: one coming from the COUNT button and the other coming from the QUIT
button.

**Exercise:** A good exercise at this point would be to add a new button
to this program named \"Decrement\" and have it decrement the counter.
To do this, insert a new button (perhaps rearranging the other controls
in the process) and add a new event handler. You might also add a
\"Clear\" button to reset the counter to zero.

As a final example, the following code implements the temperature
conversion program seen earlier. This code demonstrates the use of an
Input control.

```c
    #include <iostream.h>
    #include <strstrea.h>

    #include "button.h"
    #include "input.h"
    #include "label.h"
    #include "rect.h"
    #include "window.h"

    class App: public Window
    {
        InputLine *fahr;
        Label *cel;
    public:
        App( char *s, Rect &r );

        virtual void HandleEvent( Event &event );
    };

    const int QUIT = 100;
    const int CONVERT = 101;

    App app( "Test", Rect(1, 1, 80, 24) );

    App::App( char *s, Rect &r ): Window( s, r )
    {
        fahr = new InputLine ("fahr", Rect(40, 5, 50, 7) );

        Insert( fahr );

        Insert( new Label("Fahrenheit Temperature:   ", Rect(14, 5, 38, 7)) );
        Insert( new Label("Celsius Temperature:", Rect(14, 9, 38, 11)) );
        cel = new Label("0", Rect(40, 9, 45, 11));
        Insert( cel );

        Insert( new Button(" Convert", Rect(28, 18, 40, 20), CONVERT) );
        Insert( new Button(" Quit", Rect(50, 18, 57, 20), QUIT) );
    }

    void App::HandleEvent( Event &event)
    {
        char s[100];
        char t[100];
        float f;
        istrstream istr( s, 100 );
        ostrstream ostr( t, 100 );

        Window::HandleEvent( event );

        if( event.type == COMMAND )
        {
            switch( event.message )
            {
                case CONVERT:
                    fahr->GetText( s, 100 );
                    istr >> f;
                    ostr.width(6);
                    ostr.precision(2);
                    ostr << (f-32) * 5/9.0 << ends;
                    cel->SetTitle( t );
                    break;

                case QUIT:
                    Close();
                    screen.Clear();
                    break;
            }
        }
        event.type = CLEAR;
    }

    void main()
    {
        app.Execute();
    }
```
When running this program, use the tab key to move focus between the
input control and the two buttons. Press return to activate a button.
When the Input control has focus, you may type characters or the
backspace key.

### Understanding the SST class hierarchy

To understand the three programs shown above, it is helpful to look at
several of the classes in the SST hierarchy and understand how they
relate to one another. Let\'s start with the hierarchy\'s base class:
Rect:\

```c
    class Rect
    {
    public:
        int top, bottom, left, right;
        Rect();
        Rect( int x1, int y1, int x2, int y2 );
        int Height();
        void SetSize( Rect &r );
        int Width();
    };
```
The Rect class is very simple (if you look at the CPP file at the end of
this article you can see just how simple it really is - each function
contains just a line or two of code). The class contains the four data
members needed to hold the top, left, right and bottom coordinates of
the rectangle. The default constructor sets these coordinates to zero.
There is also a second constructor that initializes them to specified
values. The Height and Width members calculate the height and width of
the rectangle through simple subtraction. The SetSize member allows you
to change the coordinates of the rectangle at any time.

The Object class inherits from the Rect class (you could argue that the
object class should be the base class and it should have a \"uses a\"
relationship with the Rect class as opposed to the \"is a\" relationship
found in this hierarchy - that is good reasoning, so change the
hierarchy if you like). The object class knows how to handle events and
accept focus:

```c
    class Object: public Rect
    {
    protected:
            char *title;
            int takesFocus;
            int focused;
            Screen screen;

    public:
        Object();
        Object( char *s, Rect &r );
        virtual ~Object();
        int AcceptsFocus();
        virtual void Draw();
        virtual void HandleEvent( Event &event );
        virtual void ReleaseFocus();
        virtual void SetFocus();
        virtual void SetTitle( char *s );
    };
```
The class has two constructors, the second one being the one generally
used. This constructor accepts a string that acts as the title for the
object and a rectangle that controls the size and placement of the
object. An object can accept focus of not (a label is a control that
does not accept focus, while a button does). You can query the
AcceptsFocus function to determine whether or not the object accepts
focus. All objects know how to draw themselves, and you cause them to
draw themselves by calling the Draw member. This function draws a
rectangle around the object. All objects also can handle events, and do
so in their HandleEvent member. You can give an object focus by calling
its SetFocus member and take it away with ReleaseFocus. Finally, you can
change the title string with SetTitle. Look at OBJECT.CPP and you will
find that all of the member functions are extremely simple.

The Object class makes use of the Screen helper class. The Screen class
knows draw onto the screen, and contains three members: GotoXY moves the
cursor on the screen, CharXY draws a character at a specific location,
and Clear clears the whole screen. Look at SCREEN.H to see how simple
the class is. The class uses standard ANSI escape sequences to move the
cursor around and clear the screen.

The Window class inherits from the Object class. The Window class is an
Object, and it also holds a list of other objects. In the list goes all
of the controls contained by the window. Because it knows of all of its
controls, the window class can do several things.

-   It can refresh itself by traversing the list and calling the Draw
    member function of all controls in the list.
-   It can change the control with focus by calling ReleaseFocus on the
    object that has focus and SetFocus on the object to get focus.
-   It can pass events that it cannot handle to the control that has
    focus.

The Window class contains the following functions:\

```c
    class Window: public Object
    {
    protected:
        ObjectList list;
        int running;

    public:
        Window();
        Window( char *s, Rect &r );
        ~Window();
        int Close();
        virtual void Draw();
        void Execute();
        virtual void HandleEvent( Event &event );
        void Insert( Object *obj );
        void MoveFocus( char direction );
        void Remove( Object *obj );
        int WindowRunning();
    };
```
You have seen in the example programs that the main function must call
the window\'s Execute function. This function, if you look at the code,
simply loops and retrieves keystrokes, passing them to the HandleEvent
function. The HandleEvent function moves focus if the Tab key is
pressed, terminates if the ESC key is pressed, or passes the event on to
the focused object otherwise.

It is in the Draw and HandleEvent functions where virtual functions come
into play. For example, look at the Draw function in the Window class.
It loops through all of the objects in the object list and calls the
Draw function. Each object, depending on its type (Button, Input, Label)
has its own implementation for the Draw function so each one draws
itself appropriately. The HandleEvent function in the Window class is
another good example. The Execute function calls HandleEvent. Since we
have inherited from the Window class, out version of HandleEvent gets
called first. In our code, we call back down to the default function
Window::HandleEvent so it can do any automatic handling on the TAB or
ESC keys, and also gives the focused object a crack at handling events
it understands. If either can handle the event they do, and they also
clear the event to mark it as handled. When Window::HandleEvent returns,
our code can process any events left over.

If you look in EVENT.H, you will see that the event helper class knows
of only three event types:

```c
    const char KEYBOARD = 100;
    const char COMMAND  = 101;
    const char CLEAR = 102;
```

The window can create KEYSTROKE events. A button control can massage a
KEYSTROKE into a COMMAND event. To mark an event as \"handled\" it is
set to CLEAR.

The Insert function, also seen in the examples, simply inserts a control
into the list of controls. Remove is able to remove a control from the
list.

The three controls are very simple and are easily understood by looking
at their H and CPP files at the end of this article. The Label control
displays text. You can change its text at any time. It does not accept
focus, so it never handles events. The Input control accepts keystrokes
and displays them. It holds the keystrokes in a string. You can
initialize it with SetText or retrieve the string with GetText. The
Button class inherits from the label class. Its main goal is to look for
return keys and massage the event into a command event.

As you can see, there is not a lot of code involved. What is interesting
is the way the code intertwines to create a self-referential whole. Any
larger GUI hierarchy works exactly the same way, but obviously handles
more capabilities. What is interesting, however, is the fact that larger
hierarchies rest on exactly the same principles. For example, user input
is limited, generally, to the keyboard and the mouse. That is it. So
while the variety and diversity of a class hierarchy can implement far
more frills, the basic foundation is the same as that seen here in SST.

### Adding a New Control

You can learn a bit more about SST by creating a new control. Here we
will create a new scale control and use it to modify the temperature
conversion program. A scale control will look like this:

```
    +---------------+
    |   20          |
    | o--x--------o |
    | 0         100 |
    +---------------+
```
By pressing the \'j\' and \'k\' keys the scale will decrement and
increment by 1. By pressing the \'h\' and \'l\' keys it will decrement
or increment by one \"notch\". It can be extremely educational to
attempt to create this control yourself before looking at the code. Ask
yourself the following questions in order to get started:

-   How do you go about designing this control?
-   What data members does it need?
-   What member functions does it need?
-   How do you fit it into the existing hierarchy?

Try to create a version of the control yourself using the existing
controls as examples.

Here is one solution to the problem:

#### SCALE.H

```c
    class Scale: public Object
    {
        int minValue, maxValue, currentValue, numNotches;
        float notchValue;

    public:
        Scale();
        Scale( char *s, Rect &r, int min = 0, int max = 100 );
        void Dec( int number = 1 );
        void DecNotch( int number = 1 );
        virtual void Draw();
        int GetPosition();
        virtual void HandleEvent( Event &event );
        void Inc( int number = 1 );
        void IncNotch( int number = 1 );
        void SetPosition( int value );
    };
```

#### SCALE.CPP

```c
    #include "scale.h"

    Scale::Scale() : Object(), minValue(0), maxValue(0),
        currentValue(0), numNotches(0), notchValue(0)
    {}

    Scale::Scale( char *s, Rect &r, int min, int max )
        : Object( s, r ), minValue(min), maxValue(max),
        currentValue(min), numNotches(0), notchValue(0)
    {
        numNotches = right - left - 6;
        notchValue = (maxValue - minValue) / (float)numNotches;
    }

    void Scale::Dec( int number )
    {
        if( currentValue - number >= minValue )
        {
            currentValue -= number;
            Draw();
        }
    }

    void Scale::DecNotch( int number )
    {
        if( (currentValue - notchValue * number) >= minValue )
            currentValue -= notchValue * number;
        else
            currentValue = minValue;

        Draw();
    }

    void Scale::Draw()
    {
        int i, pos;

        Object::Draw();

        // draw the ends of the scale
        screen.CharXY( left+2, top+2, 'O' );
        screen.CharXY( right-2, top+2, 'O' );

        // draw the middle of the scale
        for( i = 0; i <= numNotches; i++ )
        {
            screen.CharXY( left+3+i, top+2, '-' );
        }

        // draw the min and max values of the scale
        screen.GotoXY( left+2, top+3 );
        cout << minValue;

        screen.GotoXY( right-2-2, top+3 );
        cout << setiosflags(ios::right) << setw(3) << maxValue;

        // draw the current position
        pos = (left + 3) +  ((currentValue - minValue) / notchValue);
        screen.CharXY( pos, top+2, 'x' );

        // clear old value and draw new value
        for( i = left+1; i < right; i++ )
            screen.CharXY( i, top+1, ' ' );

        screen.GotoXY( pos-2, top+1 );
        cout << setiosflags(ios::right) << setw(3) << currentValue;
    }

    int Scale::GetPosition()
    {
        return currentValue;
    }

    void Scale::HandleEvent( Event &event )
    {
        if( event.type == KEYBOARD )
        {
            switch( event.message )
            {
                case 'j':
                    Dec();
                    break;

                case 'k':
                    Inc();
                    break;

                case 'h':
                    DecNotch();
                    break;

                case 'l':
                    IncNotch();
                    break;
            }
        }
    }

    void Scale::Inc( int number )
    {
        if( currentValue + number <= maxValue )
        {
            currentValue += number;
            Draw();
        }
    }

    void Scale::IncNotch( int number )
    {
        if( (notchValue * number + currentValue) <= maxValue )
            currentValue += notchValue * number;
        else
            currentValue = maxValue;

        Draw();
    }

    void Scale::SetPosition( int value )
    {
        if( (value >= minValue) && (value <= maxValue) )
            currentValue = value;

        Draw();
    }
```

#### F2C2.CPP: A Sample program

The following program recreates the temperature conversion program seen
previously using the scale control

```c
    #include <iostream.h>
    #include <strstrea.h>

    #include "button.h"
    #include "input.h"
    #include "label.h"
    #include "rect.h"
    #include "scale.h"
    #include "window.h"

    class App: public Window
    {
        Label *cel;
        Scale *scale;
    public:
        App( char *s, Rect &r );

        virtual void HandleEvent( Event &event );
    };

    const int QUIT        = 100;
    const int CONVERT    = 101;

    App app( "Test", Rect(1, 1, 80, 24) );

    App::App( char *s, Rect &r ): Window( s, r )
    {
        scale = new Scale("scale", Rect(40,4,66,8), 0, 100 );
        Insert( scale );

        Insert( new Label("Fahrenheit Temperature:   ", Rect(14, 5, 38, 7)) );
        Insert( new Label("Celsius Temperature:", Rect(14, 9, 38, 11)) );
        cel = new Label("0", Rect(40, 9, 45, 11));
        Insert( cel );

        Insert( new Button(" Convert", Rect(28, 18, 40, 20), CONVERT) );
        Insert( new Button(" Quit", Rect(50, 18, 57, 20), QUIT) );
    }

    void App::HandleEvent( Event &event)
    {
        char s[100];

        Window::HandleEvent( event );

        if( event.type == COMMAND )
        {
            switch( event.message )
            {
                case CONVERT:
                    int f = scale->GetPosition();

                    ostrstream ostr ( s, 100 );
                    ostr << (f-32) * 5/9.0 << ends;
                    cel->SetTitle( s );
                    break;

                case QUIT:
                    Close();
                    screen.Clear();
                    break;
            }
        }
        event.type = CLEAR;
    }

    void main()
    {
        app.Execute();
    }
```

### Conclusion

In this article you have seen how to use a simple GUI class hierarchy
called SST. You have also had the chance to extend the hierarchy and
understand its inner workings. We hope that this exprience helps you to
more easily understand larger class hierarchies in the future.

### Code Listings

The following listings contain all of the code for the SST classes.

<!-- -->

```c
    /* ----------------------------------------------------------------------- *
     * b u t t o n . h
     *
     * buttons are windows that display a label and respond to the enter
     * key when they have focus.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __BUTTON_H
    #define __BUTTON_H

    #include "keys.h"
    #include "rect.h"
    #include "label.h"

    class Button: public Label
    {
        int data;
    public:
        Button();

        Button( char *s, Rect &r, int d );

        virtual void Draw();

        virtual void HandleEvent( Event &event );

        void SetData( int d );
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * b u t t o n . c p p
     *
     * buttons are windows that display a label and respond to the enter
     * key when they have focus.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "button.h"

    Button::Button(): Label()
    {
        takesFocus = 1;
        focused = 0;
    }

    Button::Button( char *s, Rect &r, int d )
        : data(d), Label( s, r )
    {
        takesFocus = 1;
        focused = 0;
    }

    void Button::Draw()
    {
        Label::Draw();
        Object::Draw();
    }

    void Button::HandleEvent( Event &event )
    {
        if( (event.type == KEYBOARD) && (event.message == RETURN) )
        {
            event.type = COMMAND;
            event.message = data;
        }
    }

    void Button::SetData( int d )
    {
        data = d;
    }

     /* ----------------------------------------------------------------------- *
     * e v e n t . h
     *
     * class for events
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __EVENT_H
    #define __EVENT_H

    const char KEYBOARD = 100;
    const char COMMAND  = 101;
    const char CLEAR    = 102;

    class Event
    {
    public:
        char type;
        char message;

        Event(): type(COMMAND), message(0) {}

        Event( char t, char k ): type(t), message(k) {}
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * i n p u t . h
     *
     * a simple class to get input from the user.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __INPUT_H
    #define __INPUT_H

    #include "keys.h"
    #include "object.h"
    #include "strclass.h"

    class InputLine: public Object
    {
        String input;

    public:
        InputLine();

        InputLine( char *s, Rect &r );

        void GetText( char *s, int n );

        virtual void Draw();

        virtual void HandleEvent( Event &event );

        void SetText( char *s );
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * i n p u t . c p p
     *
     * a simple class to get input from the user.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "input.h"

    InputLine::InputLine()
    {
        takesFocus = 1;
        focused = 0;
    }

    InputLine::InputLine( char *s, Rect &r )
        : Object( s, r )
    {
        takesFocus = 1;
        focused = 0;
    }

    void InputLine::GetText( char *s, int n )
    {
        strncpy( s, input.GetString(), n );
    }

    void InputLine::Draw()
    {
        int i;

        Object::Draw();
        if( (Height() > 2) && (Width() > 2) )
        {
            screen.GotoXY( left + 1, top + 1 );
            cout << input.GetString();

            for( i = left + input.GetLength(); i < right - 1; i++ )
                cout << " ";
        }
    }

    void InputLine::HandleEvent( Event &event )
    {
        if( event.type == KEYBOARD )
        {
            switch( event.message )
            {
                case BACKSPACE:
                    if( input.GetLength() > 0 )
                    {
                        screen.GotoXY( left + input.GetLength(), top + 1 );
                        cout << " ";
                        screen.GotoXY( left + input.GetLength(), top + 1 );
                        input.Remove();
                    }
                    break;

                case RETURN:
                    break;

                default:
                    if( event.message == 0 )
                        break;
                    if( input.GetLength() + left < right - 1 )
                    {
                        input.Insert(event.message);
                        screen.GotoXY( left + input.GetLength(), top + 1 );
                        cout << char(event.message);
                    }
                    break;
            }
        }
    }

    void InputLine::SetText( char *s )
    {
        input.Clear();
        input.Insert( s );
        Draw();
    }

     /* ----------------------------------------------------------------------- *
     * k e y s . h
     *
     * defines useful keyboard key codes.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __KEYS_H
    #define __KEYS_H

    const char BACKSPACE     = 8;
    const char TAB          = 9;
    const char RETURN         = 13;
    const char SHIFT_TAB    = 15;
    const char ESC            = 27;

    #endif
     /* ----------------------------------------------------------------------- *
     * l a b e l . h
     *
     * a static label class.  labels do not process events.
     * ----------------------------------------------------------------------- */

    #ifndef __LABEL_H
    #define __LABEL_H

    #include <iostream.h>
    #include <iomanip.h>
    #include "object.h"

    class Label: public Object
    {
    public:
        Label();

        Label( char *s, Rect &r );

        virtual void Draw();

        void SetTitle( char *s );
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * l a b e l . c p p
     *
     * a static label class.  labels do not process events.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "label.h"

    Label::Label(): Object()
    {
        takesFocus = 0;
        focused = 0;
    }

    Label::Label( char *s, Rect &r )
        : Object( s, r )
    {
        takesFocus = 0;
        focused = 0;
    }

    void Label::Draw()
    {
        if( (Height() > 2) && (Width() > 2) )
        {
            screen.GotoXY( left + 1, top + 1 );
            cout << title;
        }
    }

    void Label::SetTitle( char *s )
    {
        Object::SetTitle( s );
        Draw();
    }

     /* ----------------------------------------------------------------------- *
     * o b j e c t. h
     *
     * the base class for all screen objects.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __OBJECT_H
    #define __OBJECT_H

    #include <string.h>
    #include "event.h"
    #include "rect.h"
    #include "screen.h"

    class Object: public Rect
    {
    protected:
        char *title;
        char takesFocus;
        char focused;
        Screen screen;

    public:
        Object();

        Object( char *s, Rect &r );

        ~Object();

        char AcceptsFocus();

        virtual void Draw();

        virtual void HandleEvent( Event &event );

        virtual void ReleaseFocus();

        virtual void SetFocus();

        virtual void SetTitle( char *s );
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * o b j e c t . c p p
     *
     * the base class for all screen objects.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include <iostream.h>
    #include "object.h"

    Object::Object(): Rect(), title(0), takesFocus(1)
    {
    }

    Object::Object( char *s, Rect &r )
        : Rect( r )
    {
        title = new char[ strlen(s) + 1 ];
        strcpy( title, s );
        takesFocus = 1;
    }

    Object::~Object()
    {
        delete [] title;
    }

    char Object::AcceptsFocus()
    {
        return takesFocus;
    }

    void Object::Draw( )
    {
        char style;
        int i;

        if( focused )
            style = '=';
        else
            style = '-';

        for( i = left + 1; i < right; i++ )
        {
            screen.CharXY( i, top, style );
            screen.CharXY( i, bottom, style );
        }
        for( i = top + 1; i < bottom; i++ )
        {
            screen.CharXY( left, i, '|' );
            screen.CharXY( right, i, '|' );
        }
        screen.CharXY( left, top, '+' );
        screen.CharXY( right, top, '+' );
        screen.CharXY( left, bottom, '+' );
        screen.CharXY( right, bottom, '+' );
    }

    void Object::HandleEvent( Event &event )
    {
    }

    void Object::ReleaseFocus()
    {
        focused = 0;
    }

    void Object::SetFocus()
    {
        focused = 1;
    }

    void Object::SetTitle( char *s )
    {
        delete [] title;
        title = new char[ strlen(s) + 1 ];
        strcpy( title, s );
    }

     /* ----------------------------------------------------------------------- *
     * o b j l i s t . h
     *
     * a class to manage a list of objects in a window.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __OBJLIST_H
    #define __OBJLIST_H

    class Object;

    typedef struct ObjectNode
    {
        Object *object;
        ObjectNode *next;
        ObjectNode *prev;
    } ObjectNode;

    class ObjectList
    {
        ObjectNode *top;
        ObjectNode *bottom;
        ObjectNode *current;

    public:
        ObjectList();

        ~ObjectList();

        void Insert( Object *obj );

        Object *GetCurrent();

        Object *GetFirst();

        Object *GetLast();

        Object *GetNext();

        Object *GetPrev();

        void Remove( Object *obj );

        void SetCurrent( Object *obj );
    };
    #endif

     /* ----------------------------------------------------------------------- *
     * o b j l i s t . c p p
     *
     * implementation of a class to manage a list of objects for a window.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "objlist.h"

    ObjectList::ObjectList(): top(0), bottom(0), current(0)
    {
    }

    ObjectList::~ObjectList()
    {
        current = top;

        while( current != 0 )
        {
            top = current->next;
            delete current;
            current = top;
        }
    }

    void ObjectList::Insert( Object *obj )
    {
        if( obj == 0 )
            return;

        if( top == 0 )
        {
            top = new ObjectNode;

            top->object = obj;
            top->next = 0;
            top->prev = 0;

            bottom = current = top;
        }
        else
        {
            bottom->next = new ObjectNode;
            bottom->next->prev = bottom;
            bottom = bottom->next;
            bottom->object = obj;
            bottom->next = 0;
        }
    }

    Object *ObjectList::GetCurrent()
    {
        if( current == 0 )
            return 0;
        else
            return current->object;
    }

    Object *ObjectList::GetFirst()
    {
        if( top == 0 )
            return 0;

        current = top;
        return top->object;
    }

    Object *ObjectList::GetLast()
    {
        if( bottom == 0 )
            return 0;

        current = bottom;
        return bottom->object;
    }

    Object *ObjectList::GetNext()
    {
        if( current == 0 )
            return 0;

        current = current->next;

        if( current == 0 )
            return 0;
        else
            return current->object;
    }

    Object *ObjectList::GetPrev()
    {
        if( current == 0 )
            return 0;

        current = current->prev;

        if( current == 0 )
            return 0;
        else
            return current->object;
    }

    void ObjectList::Remove( Object *obj )
    {
        ObjectNode *temp;

        if( obj == 0 )
            return;

        temp = top;

        while( (temp != 0) && (temp->object != obj) )
            temp = temp->next;

        if( temp->object == obj )
        {
            if( temp == top )
            {
                top = temp->next;

                if( top == 0 )
                    bottom = 0;
                else
                    top->prev = 0;

                if( current == temp )
                    current = top;
            }
            else if( temp == bottom )
            {
                bottom = temp->prev;

                if( bottom == 0 )
                    top = 0;
                else
                    bottom->next = 0;

                if( current == temp )
                    current = bottom;
            }
            else
            {
                temp->next->prev = temp->prev;
                temp->prev->next = temp->next;

                if( current == temp )
                    current = temp->next;
            }

            delete temp;
        }
    }

    void ObjectList::SetCurrent( Object *obj )
    {
        current = top;

        while( (current != 0) && (current->object != obj) )
            current = current->next;

        if( current == 0 )
            current = top;
    }

     /* ----------------------------------------------------------------------- *
     * r e c t . h
     *
     * a simple rectangle class.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __RECT_H
    #define __RECT_H

    class Rect
    {
    public:
        char top, bottom, left, right;

        Rect();

        Rect( int x1, int y1, int x2, int y2 );

        char Height();

        void SetSize( Rect &r );

        char Width();
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * r e c t . c p p
     *
     * a simple rectangle class.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "rect.h"

    Rect::Rect(): top(0), bottom(0),
        right(0), left(0)
    {
    }

    Rect::Rect( int x1, int y1, int x2, int y2 )
        : left(x1), top(y1), right(x2), bottom(y2)
    {
    }

    char Rect::Height()
    {
        return bottom - top;
    }

    void Rect::SetSize( Rect &r )
    {
        top = r.top;
        bottom = r.bottom;
        right = r.right;
        left = r.left;
    }

    char Rect::Width()
    {
        return right - left;
    }

     /* ----------------------------------------------------------------------- *
     * s c r e e n . h
     *
     * a class to manage an ansi text screen.  allows moving to
     * an x, y location and clearing the screen.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __SCREEN_H
    #define __SCREEN_H

    #include <iostream.h>


    class Screen
    {
    public:
        Screen( )
        {
        }

        void GotoXY( int x, int y )
        {
            cout << "\033[" << y
                << ";" << x << "H";
        }

        void CharXY( int x, int y, char c)
        {
            GotoXY( x, y );
            cout << c;
        }

        void Clear()
        {
            cout << "\033[2J";
        }
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * s t r c l a s s . h
     *
     * a simple string class.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __STRCLASS_H
    #define __STRCLASS_H

    #include <string.h>

    class String
    {
    protected:
        char string[80];
        int pos;
    public:
        String();

        String( char *s );

        void Clear();

        int GetLength();

        const char *GetString();

        void Insert( char c );

        void Insert( char *s );

        void Remove();
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * s t r c l a s s . c p p
     *
     * a simple string class.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "strclass.h"

    String::String(): pos(0)
    {
        string[0] = 0;
    }

    String::String( char *s )
    {
        strcpy( string, s );
        pos = strlen( string );
    }

    void String::Clear()
    {
        string[0] = 0;
        pos = 0;
    }

    int String::GetLength()
    {
        return pos;
    }

    const char *String::GetString()
    {
        return string;
    }

    void String::Insert( char c )
    {
        string[pos] = c;
        pos++;
        string[pos] = 0;
    }

    void String::Insert( char *s )
    {
        strcat( string, s );
        pos = strlen( string );
    }

    void String::Remove()
    {
        if( pos > 0 )
        {
            pos--;
            string[pos] = 0;
        }
    }

     /* ----------------------------------------------------------------------- *
     * w i n d o w . h
     *
     * the basic window class.  all screen objects are derived from
     * this class.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __WINDOW_H
    #define __WINDOW_H

    #include <conio.h>    // !!!
    #include <string.h>
    #include <iostream.h>
    #include <iomanip.h>
    #include "event.h"
    #include "keys.h"
    #include "object.h"
    #include "objlist.h"
    #include "rect.h"

    const char WIN_NEXT    = 1;
    const char WIN_PREV    = 2;

    class Window: public Object
    {
    protected:
        ObjectList list;
        char running;
    public:
        Window();

        Window( char *s, Rect &r );

        ~Window();

        int Close();

        virtual void Draw();

        void Execute();

        virtual void HandleEvent( Event &event );

        void Insert( Object *obj );

        void MoveFocus( char direction );

        void Remove( Object *obj );

        char WindowRunning();
    };

    #endif

     /* ----------------------------------------------------------------------- *
     * w i n d o w . c p p
     *
     * the basic window class.  all screen objects are derived from
     * this class.
     * 
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "window.h"

    Window::Window(): running(1)
    {
        takesFocus = 1;
    }

    Window::Window( char *title, Rect &r )
        : Object( title, r )
    {
        running = 1;
        takesFocus = 1;
    }

    Window::~Window()
    {
    }

    int Window::Close( )
    {
        running = 0;
        return 1;
    }

    void Window::Draw( )
    {
        Object *temp, *current = list.GetCurrent();

        SetFocus();
        Object::Draw();

        // draw all the child objects
        temp = list.GetFirst();
        while( temp != 0 )
        {
            temp->Draw();
            temp = list.GetNext();
        }

        list.SetCurrent( current );
    }

    void Window::Execute( )
    {
        Event event;

        list.GetLast();
        MoveFocus( WIN_NEXT );
        screen.Clear();
        Draw();

        do
        {
            event.type = KEYBOARD;
            event.message = getch();
            HandleEvent( event );
        } while( WindowRunning() );
    }

    void Window::HandleEvent( Event &event )
    {
        if( event.type == KEYBOARD )
        {
            switch( event.message )
            {
                case TAB:
                case SHIFT_TAB:
                    if( list.GetCurrent() == 0 )
                        break;

                    if( event.message == TAB )
                        MoveFocus( WIN_NEXT );
                    else
                        MoveFocus( WIN_PREV );

                    event.type = CLEAR;
                    break;

                case ESC:
                    Close();
                    break;

                default:
                    if( list.GetCurrent() == 0 )
                        break;

                    list.GetCurrent()->HandleEvent( event );
                    break;
            }
        }
    }

    void Window::Insert( Object *obj )
    {
        list.Insert( obj );
        obj->Draw();
    }

    void Window::MoveFocus( char direction )
    {
        int listScanned = 0;
        Object *current = list.GetCurrent();

        if( current == 0 )
            return;

        current->ReleaseFocus();
        current->Draw();

        do
        {
            if( direction == WIN_NEXT )
                current = list.GetNext();
            else
                current = list.GetPrev();

            if( current == 0 )
            {
                listScanned++;
                if( direction == WIN_NEXT )
                    current = list.GetFirst();
                else
                    current = list.GetLast();
            }
        } while( (listScanned < 2) && !current->AcceptsFocus() );
        if( current->AcceptsFocus() )
        {
            current->SetFocus();
            current->Draw();
        }
        listScanned = 0;
    }

    void Window::Remove( Object *obj )
    {
        Object *current;

        current = list.GetCurrent();
        if( current )
            current->ReleaseFocus();

        list.Remove( obj );

        current = list.GetCurrent();
        if( current )
            current->SetFocus();

        screen.Clear();
        Draw();
    }

    char Window::WindowRunning()
    {
        return running;
    }

### If you are working in NT, the following modified files will be useful (we were unable to get the NT command prompt to understand ANSI sequences)


    /* ----------------------------------------------------------------------- *
     * s c r e e n . h
     *
     * a class to manage a Windows NT console.  allows moving to
     * an x, y location and clearing the screen.
     *
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __SCREEN_H
    #define __SCREEN_H

    #include <iostream.h>

    class Screen
    {
    public:
        Screen();
        ~Screen();
        void GotoXY( int x, int y );
        void CharXY( int x, int y, char c);
        void Clear();
    };

    #endif

    /* ----------------------------------------------------------------------- *
     * s c r e e n . c p p
     *
     * a class to manage an Windows NT console.  allows moving to
     * an x, y location and clearing the screen.
     *
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    // for NT Screen Console functions
    #include <windows.h>
    #include "screen.h"

    static HANDLE hConsole = 0;
    static int instanceCount = 0;

    Screen::Screen()
    {
        if( instanceCount == 0 )
        {
            hConsole = GetStdHandle( STD_OUTPUT_HANDLE );
        }

        instanceCount++;

        Clear();
    }


    Screen::~Screen()
    {
        instanceCount--;

        if( instanceCount == 0 )
        {
    //        CloseHandle( hConsole );
        }
    }


    void Screen::GotoXY( int x, int y )
    {
        COORD coord;

        coord.X = x - 1;
        coord.Y = y - 1;
        
        SetConsoleCursorPosition( hConsole, coord );
    }


    void Screen::CharXY( int x, int y, char c)
    {
        COORD coord;
        DWORD numWritten;

        coord.X = x - 1;
        coord.Y = y - 1;
        
        SetConsoleCursorPosition( hConsole, coord );
        WriteConsoleOutputCharacter( hConsole, &c, 1, coord, &numWritten );
    }


    void Screen::Clear()
    {
      COORD coordScreen = { 0, 0 }; /* here's where we'll home the cursor */
      BOOL bSuccess;
      DWORD cCharsWritten;
      CONSOLE_SCREEN_BUFFER_INFO csbi; /* to get buffer info */
      DWORD dwConSize; /* number of character cells in the current buffer */

      /* get the number of character cells in the current buffer */
      bSuccess = GetConsoleScreenBufferInfo(hConsole, &csbi);

      dwConSize = csbi.dwSize.X * csbi.dwSize.Y;
      /* fill the entire screen with blanks */
      bSuccess = FillConsoleOutputCharacter(hConsole, (TCHAR) ' ',
          dwConSize, coordScreen, &cCharsWritten);

      /* get the current text attribute */
      bSuccess = GetConsoleScreenBufferInfo(hConsole, &csbi);

      /* now set the buffer's attributes accordingly */
      bSuccess = FillConsoleOutputAttribute(hConsole, csbi.wAttributes,
          dwConSize, coordScreen, &cCharsWritten);

      /* put the cursor at (0, 0) */
      bSuccess = SetConsoleCursorPosition(hConsole, coordScreen);

      return;
    }

 

### If you are working in UNIX, the following modified files will be useful

 


    /* ----------------------------------------------------------------------- *
     * v e r s i o n . h
     *
     * defines whether we are building an msdos or unix version
     *
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    //#define SST_UNIX  // uncomment this line to build a UNIX version

    /* ----------------------------------------------------------------------- *
     * k e y s . h
     *
     * defines useful keyboard key codes.
     *
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __KEYS_H
    #define __KEYS_H

    #include "version.h"

    const char BACKSPACE = 8;
    const char TAB = 9;

    #ifdef SST_UNIX
            const char RETURN = 10;
    #else
            const char RETURN = 13;
    #endif

    const char SHIFT_TAB = 15;
    const char ESC = 27;

    #endif

    /* ----------------------------------------------------------------------- *
     * w i n d o w . h
     *
     * the basic window class.  all screen objects are derived from
     * this class.
     *
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #ifndef __WINDOW_H
    #define __WINDOW_H

    #include "version.h"

    #ifdef SST_UNIX
        #include <stdio.h>
        #include <ctype.h>
        #include <termio.h>
    #else
        #include <conio.h> // dos specific
    #endif

    #include <string.h>
    #include <iostream.h>
    #include <iomanip.h>
    #include "event.h"
    #include "keys.h"
    #include "object.h"
    #include "objlist.h"
    #include "rect.h"

    const char WIN_NEXT = 1;
    const char WIN_PREV = 2;

    class Window: public Object
    {
    protected:
        ObjectList list;
        int running;

    public:
        Window();

        Window( char *s, Rect &r );

        ~Window();

        int Close();

        virtual void Draw();

        void Execute();

        virtual void HandleEvent( Event &event );

        void Insert( Object *obj );

        void MoveFocus( char direction );

        void Remove( Object *obj );

        int WindowRunning();
    };

    #endif

    /* ----------------------------------------------------------------------- *
     * w i n d o w . c p p
     *
     * the basic window class.  all screen objects are derived from
     * this class.
     *
     * Copyright 1996 by Interface Technologies, Inc. All Rights Reserved.
     * ----------------------------------------------------------------------- */

    #include "window.h"

    #ifdef SST_UNIX
        static struct termio ostate;
    #endif

    Window::Window(): running( 0 )
    {
        #ifdef SST_UNIX
            struct  termio  nstate;

            ioctl(0, TCGETA, &ostate);
            nstate = ostate;
            nstate.c_lflag &= ~(ICANON|ECHO|ECHOE|ECHOK|ECHONL);
            nstate.c_cc[VMIN] = 1;
            nstate.c_cc[VTIME] = 0;
            ioctl(0, TCSETAW, &nstate);
        #endif

        takesFocus = 1;
    }

    Window::Window( char *title, Rect &r )
        : running( 0 ), Object( title, r )
    {
        #ifdef SST_UNIX
            struct  termio  nstate;

            ioctl(0, TCGETA, &ostate);
            nstate = ostate;
            nstate.c_lflag &= ~(ICANON|ECHO|ECHOE|ECHOK|ECHONL);
            nstate.c_cc[VMIN] = 1;
            nstate.c_cc[VTIME] = 0;
            ioctl(0, TCSETAW, &nstate);
        #endif

        takesFocus = 1;
    }

    Window::~Window()
    {
        #ifdef SST_UNIX
            ioctl( 0, TCSETAW, &ostate );
        #endif
    }

    int Window::Close( )
    {
        running = 0;
        return 1;
    }

    void Window::Draw( )
    {
        Object *temp, *current = list.GetCurrent();

        SetFocus();
        Object::Draw();

        // draw all the child objects
        temp = list.GetFirst();
        while( temp != 0 )
        {
            temp->Draw();
            temp = list.GetNext();
        }

        list.SetCurrent( current );
    }

    void Window::Execute( )
    {
        Event event;

        // make cin and cout work with buffers of length 1
        cin.setf( ios::unitbuf );
        cout.setf( ios::unitbuf  );
        
        // we are now up and running
        running = 1;

        list.GetLast();
        MoveFocus( WIN_NEXT );
        screen.Clear();
        Draw();

        do
        {
            event.type = KEYBOARD;

            #ifdef SST_UNIX
                event.message = getchar();
            #else
                event.message = getch();
            #endif

            HandleEvent( event );
        } while( WindowRunning() );
    }

    void Window::HandleEvent( Event &event )
    {
        if( event.type == KEYBOARD )
        {
            switch( event.message )
            {
                case TAB:
                case SHIFT_TAB:
                    if( list.GetCurrent() == 0 )
                        break;

                    if( event.message == TAB )
                        MoveFocus( WIN_NEXT );
                    else
                        MoveFocus( WIN_PREV );

                    event.type = CLEAR;
                    break;

                case ESC:
                    Close();
                    break;

                default:
                    if( list.GetCurrent() == 0 )
                        break;

                    list.GetCurrent()->HandleEvent( event );
                    break;
            }
        }
    }

    void Window::Insert( Object *obj )
    {
        list.Insert( obj );
        if( WindowRunning() )
            obj->Draw();
    }

    void Window::MoveFocus( char direction )
    {
        int listScanned = 0;
        Object *current = list.GetCurrent();

        if( current == 0 )
            return;

        current->ReleaseFocus();
        current->Draw();

        do
        {
            if( direction == WIN_NEXT )
                current = list.GetNext();
            else
                current = list.GetPrev();

            if( current == 0 )
            {
                listScanned++;
                if( direction == WIN_NEXT )
                    current = list.GetFirst();
                else
                    current = list.GetLast();
            }
        } while( (listScanned < 2) && !current->AcceptsFocus() );

        if( current->AcceptsFocus() )
        {
            current->SetFocus();
            current->Draw();
        }
        listScanned = 0;
    }

    void Window::Remove( Object *obj )
    {
        Object *current;

        current = list.GetCurrent();
        if( current )
            current->ReleaseFocus();

        list.Remove( obj );

        current = list.GetCurrent();
        if( current )
            current->SetFocus();

        screen.Clear();
        Draw();
    }

    int Window::WindowRunning()
    {
        return running;
    }
```
