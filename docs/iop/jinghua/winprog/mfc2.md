---
layout: article
title: Introduction to MFC Programming with Visual C++ Version 6.x by Marshall Brain
---

## A Simple MFC Program

In this tutorial we will examine a simple MFC program piece by piece to
gain an understanding of its structure and conceptual framework. We will
start by looking at MFC itself and then examine how MFC is used to
create applications.

### An Introduction to MFC

MFC is a large and extensive C++ class hierarchy that makes Windows
application development significantly easier. MFC is compatible across
the entire Windows family. As each new version of Windows comes out, MFC
gets modified so that old code compiles and works under the new system.
MFC also gets extended, adding new capabilities to the hierarchy and
making it easier to create complete applications.

The advantage of using MFC and C++ - as opposed to directly accessing
the Windows API from a C program-is that MFC already contains and
encapsulates all the normal \"boilerplate\" code that all Windows
programs written in C must contain. Programs written in MFC are
therefore much smaller than equivalent C programs. On the other hand,
MFC is a fairly thin covering over the C functions, so there is little
or no performance penalty imposed by its use. It is also easy to
customize things using the standard C calls when necessary since MFC
does not modify or hide the basic structure of a Windows program.

The best part about using MFC is that it does all of the hard work for
you. The hierarchy contains thousands and thousands of lines of correct,
optimized and robust Windows code. Many of the member functions that you
call invoke code that would have taken you weeks to write yourself. In
this way MFC tremendously accelerates your project development cycle.

MFC is fairly large. For example, Version 4.0 of the hierarchy contains
something like 200 different classes. Fortunately, you don\'t need to
use all of them in a typical program. In fact, it is possible to create
some fairly spectacular software using only ten or so of the different
classes available in MFC. The hierarchy is broken into several different
class categories which include (but is not limited to):

-   Application Architecture
-   Graphical Drawing and Drawing Objects
-   File Services
-   Exceptions
-   Structures - Lists, Arrays, Maps
-   Internet Services
-   OLE 2
-   Database
-   General Purpose

#### Visualizing MFC

One of the most frusterating things when you are first learning MFC is the \"Where am I?\" feeling you get. MFC has *hundreds* of classes. A good 
way to get around this feeling is to use a class hierarchy visualization tool like [CodeVizor](http://codevizor.iftech.com/rd/r_dcsb2cv.asp). With 
CodeVizor you can drag the source code for MFC into the CodeVizor tool and in about 30 seconds have a beautiful, clickable (and printable!) class 
hierarchy chart. Get CodeVizor and see how much easier undestanding MFC becomes!

We will concentrate on visual objects in these tutorials. The list below
shows the portion of the class hierarchy that deals with application
support and windows support.

-   CObject
-   CCmdTarget
-   CWinThread
-   CWinApp
-   CWnd
-   CFrameWnd
-   CDialog
-   CView
-   CStatic
-   CButton
-   CListBox
-   CComboBox
-   CEdit
-   CScrollBar

There are several things to notice in this list. First, most classes in
MFC derive from a base class called **CObject**. This class contains
data members and member functions that are common to most MFC classes.
The second thing to notice is the simplicity of the list. The
**CWinApp** class is used whenever you create an application and it is
used only once in any program. The **CWnd** class collects all the
common features found in windows, dialog boxes, and controls. The
**CFrameWnd** class is derived from **CWnd** and implements a normal
framed application window. **CDialog** handles the two normal flavors of
dialogs: modeless and modal respectively. **CView** is used to give a
user access to a document through a window. Finally, Windows supports
six native control types: static text, editable text, push buttons,
scroll bars, lists, and combo boxes (an extended form of list). Once you
understand this fairly small number of pieces, you are well on your way
to a complete understanding of MFC. The other classes in the MFC
hierarchy implement other features such as memory management, document
control, data base support, and so on.

To create a program in MFC, you either use its classes directly or, more
commonly, you derive new classes from the existing classes. In the
derived classes you create new member functions that allow instances of
the class to behave properly in your application. You can see this
derivation process in the simple program we used in Tutorial 1, which is
described in greater detail below. Both **CHelloApp** and
**CHelloWindow** are derived from existing MFC classes.

### Designing a Program

Before discussing the code itself, it is worthwhile to briefly discuss
the program design process under MFC. As an example, imagine that you
want to create a program that displays the message \"Hello World\" to
the user. This is obviously a very simple application but it still
requires some thought.

A \"hello world\" application first needs to create a window on the
screen that holds the words \"hello world\". It then needs to get the
actual \"hello world\" words into that window. Three objects are
required to accomplish this task:

1.  An application object which initializes the application and hooks it
    to Windows. The application object handles all low-level event
    processing.
2.  A window object that acts as the main application window.
3.  A static text object which will hold the static text label \"hello
    world\".

Every program that you create in MFC will contain the first two objects.
The third object is unique to this particular application. Each
application will define its own set of user interface objects that
display the application\'s output as well as gather input from the user.

Once you have completed the user interface design and decided on the
controls necessary to implement the interface, you write the code to
create the controls on the screen. You also write the code that handles
the messages generated by these controls as they are manipulated by the
user. In the case of a \"hello world\" application, only one user
interface control is necessary. It holds the words \"hello world\". More
realistic applications may have hundreds of controls arranged in the
main window and dialog boxes.

It is important to note that there are actually two different ways to
create user controls in a program. The method described here uses
straight C++ code to create the controls. In a large application,
however, this method becomes painful. Creating the controls for an
application containing 50 or 100 dialogs using C++ code to do it would
take an eon. Therefore, a second method uses *resource files* to create
the controls with a graphical dialog editor. This method is much faster
and works well on most dialogs.

### Understanding the Code for \"hello world\"

The listing below shows the code for the simple \"hello world\" program
that you entered, compiled and executed in Tutorial 1. Line numbers have
been added to allow discussion of the code in the sections that follow.
By walking through this program line by line, you can gain a good
understanding of the way MFC is used to create simple applications.

If you have not done so already, please compile and execute the code
below by following the instructions given in Tutorial 1.
```
    1 //hello.cpp
     
    2 #include <afxwin.h>
     
    3 // Declare the application class
    4 class CHelloApp : public CWinApp
    5 {
    6    public:
    7        virtual BOOL InitInstance();
    8 };
     
    9 // Create an instance of the application class
    10 CHelloApp HelloApp;

    11 // Declare the main window class
    12 class CHelloWindow : public CFrameWnd
    13 { 
    14   CStatic* cs;
    15   public:
    16   CHelloWindow();
    17 };
     
    18 // The InitInstance function is called each
    19 // time the application first executes.
    20 BOOL CHelloApp::InitInstance()
    21 {
    22   m_pMainWnd = new CHelloWindow();
    23   m_pMainWnd->ShowWindow(m_nCmdShow);
    24   m_pMainWnd->UpdateWindow();
    25   return TRUE;
    26 }
     
    27 // The constructor for the window class
    28 CHelloWindow::CHelloWindow()
    29 { 
    30   // Create the window itself
    31   Create(NULL, 
    32       "Hello World!", 
    33       WS_OVERLAPPEDWINDOW,
    34       CRect(0,0,200,200)); 
    35   // Create a static label
    36   cs = new CStatic();
    37   cs->Create("hello world",
    38       WS_CHILD|WS_VISIBLE|SS_CENTER,
    39       CRect(50,80,150,150),
    40       this);
    41 }
```
Take a moment and look through this program. Get a feeling for the \"lay
of the land.\" The program consists of six small parts, each of which
does something important.

The program first includes `afxwin.h` (line 2). This header file
contains all the types, classes, functions, and variables used in MFC.
It also includes other header files for such things as the Windows API
libraries.

Lines 3 through 8 derive a new application class named **CHelloApp**
from the standard **CWinApp** application class declared in MFC. The new
class is created so the **InitInstance** member function in the
**CWinApp** class can be overridden. **InitInstance** is a virtual
function that is called as the application begins execution.

In Line 10, the code declares an instance of the application object as a
global variable. This instance is important because it causes the
program to execute. When the application is loaded into memory and
begins running, the creation of that global variable causes the default
constructor for the **CWinApp** class to execute. This constructor
automatically calls the **InitInstance** function defined in lines 18
though 26.

In lines 11 through 17, the **CHelloWindow** class is derived from the
**CFrameWnd** class declared in MFC. **CHelloWindow** acts as the
application\'s window on the screen. A new class is created so that a
new constructor, destructor, and data member can be implemented.

Lines 18 through 26 implement the **InitInstance** function. This
function creates an instance of the **CHelloWindow** class, thereby
causing the constructor for the class in Lines 27 through 41 to execute.
It also gets the new window onto the screen.

Lines 27 through 41 implement the window\'s constructor. The constructor
actually creates the window and then creates a static control inside it.

An interesting thing to notice in this program is that there is no
**main** or **WinMain** function, and no apparent event loop. Yet we
know from executing it in Tutorial 1 that it processed events. The
window could be minimized and maximized, moved around, and so on. All
this activity is hidden in the main application class **CWinApp** and we
therefore don\'t have to worry about it-event handling is totally
automatic and invisible in MFC.

The following sections describe the different pieces of this program in
more detail. It is unlikely that all of this information will make
complete sense to you right now: It\'s best to read through it to get
your first exposure to the concepts. In Tutorial 3, where a number of
specific examples are discussed, the different pieces will come together
and begin to clarify themselves.

### The Application Object

Every program that you create in MFC will contain a single application
object that you derive from the **CWinApp** class. This object must be
declared globally (line 10) and can exist only once in any given
program.

An object derived from the **CWinApp** class handles initialization of
the application, as well as the main event loop for the program. The
**CWinApp** class has several data members, and a number of member
functions. For now, almost all are unimportant. If you would like to
browse through some of these functions however, search for **CWinApp**
in the MFC help file by choosing the **Search** option in the **Help**
menu and typing in \"CWinApp\". In the program above, we have overridden
only one virtual function in **CWinApp**, that being the
**InitInstance** function.

The purpose of the application object is to initialize and control your
application. Because Windows allows multiple instances of the same
application to run simultaneously, MFC breaks the initialization process
into two parts and uses two functions-**InitApplication** and
**InitInstance**-to handle it. Here we have used only the
**InitInstance** function because of the simplicity of the application.
It is called each time a new instance of the application is invoked. The
code in Lines 3 through 8 creates a class called **CHelloApp** derived
from **CWinApp**. It contains a new **InitInstance** function that
overrides the existing function in **CWinApp** (which does nothing):
```
    3 // Declare the application class
    4 class CHelloApp : public CWinApp
    5 {
    6    public:
    7        virtual BOOL InitInstance();
    8 };
```
Inside the overridden **InitInstance** function at lines 18 through 26,
the program creates and displays the window using **CHelloApp**\'s data
member named **m\_pMainWnd**:
```
    18 // The InitInstance function is called each
    19 // time the application first executes.
    20 BOOL CHelloApp::InitInstance()
    21 {
    22   m_pMainWnd = new CHelloWindow();
    23   m_pMainWnd->ShowWindow(m_nCmdShow);
    24   m_pMainWnd->UpdateWindow();
    25   return TRUE;
    26 }
```
The **InitInstance** function returns a TRUE value to indicate that
initialization completed successfully. Had the function returned a FALSE
value, the application would terminate immediately. We will see more
details of the window initialization process in the next section.

When the application object is created at line 10, its data members
(inherited from **CWinApp**) are automatically initialized. For example,
**m\_pszAppName**, **m\_lpCmdLine**, and **m\_nCmdShow** all contain
appropriate values. See the MFC help file for more information. We\'ll
see a use for one of these variables in a moment.

### The Window Object

MFC defines two types of windows: 1) frame windows, which are fully
functional windows that can be re-sized, minimized, and so on, and 2)
dialog windows, which are not re-sizable. A frame window is typically
used for the main application window of a program.

In the code shown in listing 2.1, a new class named **CHelloWindow** is
derived from the **CFrameWnd** class in lines 11 through 17:
```
    11 // Declare the main window class
    12 class CHelloWindow : public CFrameWnd
    13 { 
    14   CStatic* cs;
    15   public:
    16   CHelloWindow();
    17 };
```
The derivation contains a new constructor, along with a data member that
will point to the single user interface control used in the program.
Each application that you create will have a unique set of controls
residing in the main application window. Therefore, the derived class
will have an overridden constructor that creates all the controls
required in the main window. Typically this class will also have an
overridden destructor to delete them when the window closes, but the
destructor is not used here. In Tutorial 4, we will see that the derived
window class will also declare a message handler to handle messages that
these controls produce in response to user events.

Typically, any application you create will have a single main
application window. The **CHelloApp** application class therefore
defines a data member named **m\_pMainWnd** that can point to this main
window. To create the main window for this application, the
**InitInstance** function (lines 18 through 26) creates an instance of
**CHelloWindow** and uses **m\_pMainWnd** to point to the new window.
Our **CHelloWindow** object is created at line 22:
```
    18 // The InitInstance function is called each
    19 // time the application first executes.
    20 BOOL CHelloApp::InitInstance()
    21 {
    22   m_pMainWnd = new CHelloWindow();
    23   m_pMainWnd->ShowWindow(m_nCmdShow);
    24   m_pMainWnd->UpdateWindow();
    25   return TRUE;
    26 }
```
Simply creating a frame window is not enough, however. Two other steps
are required to make sure that the new window appears on screen
correctly. First, the code must call the window\'s **ShowWindow**
function to make the window appear on screen (line 23). Second, the
program must call the **UpdateWindow** function to make sure that each
control, and any drawing done in the interior of the window, is painted
correctly onto the screen (line 24).

You may wonder where the **ShowWindow** and **UpdateWindow** functions
are defined. For example, if you wanted to look them up to learn more
about them, you might look in the MFC help file (use the **Search**
option in the **Help** menu) at the **CFrameWnd** class description.
**CFrameWnd** does not contain either of these member functions,
however. It turns out that **CFrameWnd** inherits its behavior-as do all
controls and windows in MFC-from the **CWnd** class (see figure 2.1). If
you refer to **CWnd** in the MFC documentation, you will find that it is
a huge class containing over 200 different functions. Obviously, you are
not going to master this particular class in a couple of minutes, but
among the many useful functions are **ShowWindow** and **UpdateWindow**.

Since we are on the subject, take a minute now to look up the
**CWnd::ShowWindow** function in the MFC help file. You do this by
clicking the help file\'s **Search** button and entering \"ShowWindow\".
As an alternative, find the section describing the **CWnd** class using
the **Search** button, and then find the **ShowWindow** function under
the Update/Painting Functions in the class member list. Notice that
**ShowWindow** accepts a single parameter, and that the parameter can be
set to one of ten different values. We have set it to a data member held
by **CHelloApp** in our program, **m\_nCmdShow** (line 23). The
**m\_nCmdShow** variable is initialized based on conditions set by the
user at application start-up. For example, the user may have started the
application from the Program Manager and told the Program Manager to
start the application in the minimized state by setting the check box in
the application\'s properties dialog. The **m\_nCmdShow** variable will
be set to SW\_SHOWMINIMIZED, and the application will start in an iconic
state. The **m\_nCmdShow** variable is a way for the outside world to
communicate with the new application at start-up. If you would like to
experiment, you can try replacing **m\_nCmdShow** in the call to
**ShowWindow** with the different constant values defined for
**ShowWindow** . Recompile the program and see what they do.

Line 22 initializes the window. It allocates memory for it by calling
the **new** function. At this point in the program\'s execution the
constructor for the **CHelloWindow** is called. The constructor is
called whenever an instance of the class is allocated. Inside the
window\'s constructor, the window must create itself. It does this by
calling the **Create** member function for the **CFrameWnd** class at
line 31:
```
    27 // The constructor for the window class
    28 CHelloWindow::CHelloWindow()
    29 { 
    30   // Create the window itself
    31   Create(NULL, 
    32       "Hello World!", 
    33       WS_OVERLAPPEDWINDOW,
    34       CRect(0,0,200,200));
```
Four parameters are passed to the create function. By looking in the MFC
documentation you can see the different types. The initial NULL
parameter indicates that a default class name be used. The second
parameter is the title of the window that will appear in the title bar.
The third parameter is the style attribute for the window. This example
indicates that a normal, overlappable window should be created. Style
attributes are covered in detail in Tutorial 3. The fourth parameter
specifies that the window should be placed onto the screen with its
upper left corner at point 0,0, and that the initial size of the window
should be 200 by 200 pixels. If the value **rectDefault** is used as the
fourth parameter instead, Windows will place and size the window
automatically for you.

Since this is an extremely simple program, it creates a single static
text control inside the window. In this particular example, the program
uses a single static text label as its only control, and it is created
at lines 35 through 40. More on this step in the next section.

### The Static Text Control

The program derives the **CHelloWindow** class from the **CFrameWnd**
class (lines 11 through 17). In doing so it declares a private data
member of type **CStatic\***, as well as a constructor.

As seen in the previous section, the **CHelloWindow** constructor does
two things. First it creates the application\'s window by calling the
**Create** function (line 31), and then it allocates and creates the
control that belongs inside the window. In this case a single static
label is used as the only control. Object creation is always a two-step
process in MFC. First, the memory for the instance of the class is
allocated, thereby calling the constructor to initialize any variables.
Next, an explicit Create function is called to actually create the
object on screen. The code allocates, constructs, and creates a single
static text object using this two-step process at lines 36 through 40:
```
    27 // The constructor for the window class
    28 CHelloWindow::CHelloWindow()
    29 { 
    30   // Create the window itself
    31   Create(NULL, 
    32       "Hello World!", 
    33       WS_OVERLAPPEDWINDOW,
    34       CRect(0,0,200,200)); 
    35   // Create a static label
    36   cs = new CStatic();
    37   cs->Create("hello world",
    38       WS_CHILD|WS_VISIBLE|SS_CENTER,
    39       CRect(50,80,150,150),
    40       this);
    41 }
```
The constructor for the **CStatic** item is called when the memory for
it is allocated, and then an explicit **Create** function is called to
create the **CStatic** control\'s window. The parameters used in the
**Create** function here are similar to those used for window creation
at Line 31. The first parameter specifies the text to be displayed by
the control. The second parameter specifies the style attributes. The
style attributes are discussed in detail in the next tutorial but here
we requested that the control be a child window (and therefore displayed
within another window), that it should be visible, and that the text
within the control should be centered. The third parameter determines
the size and position of the static control. The fourth indicates the
parent window for which this control is the child. Having created the
static control, it will appear in the application\'s window and display
the text specified.

### Conclusion

In looking at this code for the first time, it will be unfamiliar and
therefore potentially annoying. Don\'t worry about it. The only part in
the entire program that matters from an application programmer\'s
perspective is the **CStatic** creation code at lines 36 through 40. The
rest you will type in once and then ignore. In the next tutorial you
will come to a full understanding of what lines 36 through 40 do, and
see a number of options that you have in customizing a **CStatic**
control.
