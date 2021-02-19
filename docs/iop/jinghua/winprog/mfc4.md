---
layout: article
title: Introduction to MFC Programming with Visual C++ Version 6.x by Marshall Brain
---

## Message Maps

Any user interface object that an application places in a window has two
controllable features: 1) its appearance, and 2) its behavior when
responding to events. In the last tutorial you gained an understanding
of the **CStatic** control and saw how you can use style attributes to
customize the appearance of user interface objects. These concepts apply
to all the different control classes available in MFC.

In this tutorial we will examine the **CButton** control to gain an
understanding of message maps and simple event handling. We\'ll then
look at the **CScrollBar** control to see a somewhat more involved
example.

### Understanding Message Maps

As discussed in Tutorial 2, MFC programs do not contain a main function
or event loop. All of the event handling happens \"behind the scenes\"
in C++ code that is part of the **CWinApp** class. Because it is hidden,
we need a way to tell the invisible event loop to notify us about events
of interest to the application. This is done with a mechanism called a
*message map*. The message map identifies interesting events and then
indicates functions to call in response to those events.

For example, say you want to write a program that will quit whenever the
user presses a button labeled \"Quit.\" In the program you place code to
specify the button\'s creation: you indicate where the button goes, what
it says, etc. Next, you create a message map for the parent of the
button-whenever a user clicks the button, it tries to send a message to
its parent. By installing a message map for the parent window you create
a mechanism to intercept and use the button\'s messages. The message map
will request that MFC call a specific function whenever a specific
button event occurs. In this case, a click on the quit button is the
event of interest. You then put the code for quitting the application in
the indicated function.

MFC does the rest. When the program executes and the user clicks the
Quit button, the button will highlight itself as expected. MFC then
automatically calls the right function and the program terminates. With
just a few lines of code your program becomes sensitive to user events.

### The CButton Class

The **CStatic** control discussed in Tutorial 3 is unique in that it
cannot respond to user events. No amount of clicking, typing, or
dragging will do anything to a **CStatic** control because it ignores
the user completely. However, The **CStatic** class is an anomaly. All
of the other controls available in Windows respond to user events in two
ways. First, they update their appearance automatically when the user
manipulates them (e.g., when the user clicks on a button it highlights
itself to give the user visual feedback). Second, each different control
tries to send messages to your code so the program can respond to the
user as needed. For example, a button sends a *command message* whenever
it gets clicked. If you write code to receive the messages, then your
code can respond to user events.

To gain an understanding of this process, we will start with the
**CButton** control. The code below demonstrates the creation of a
button.
```c
    // button1.cpp
    #include <afxwin.h>
    #define IDB_BUTTON 100
    // Declare the application class
    class CButtonApp : public CWinApp
    {
    public:
     virtual BOOL InitInstance();
    };
    // Create an instance of the application class
    CButtonApp ButtonApp;  
    // Declare the main window class
    class CButtonWindow : public CFrameWnd
    { 
     CButton *button;
    public:
     CButtonWindow();
    };
    // The InitInstance function is called once
    // when the application first executes
    BOOL CButtonApp::InitInstance()
    {
     m_pMainWnd = new CButtonWindow();
     m_pMainWnd->ShowWindow(m_nCmdShow);
     m_pMainWnd->UpdateWindow();
     return TRUE;
    }
    // The constructor for the window class
    CButtonWindow::CButtonWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CButton Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     
     // Get the size of the client rectangle
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     
     // Create a button
     button = new CButton();
     button->Create("Push me",
         WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
         r,
         this,
         IDB_BUTTON);
    }
```
The code above is nearly identical to the code discussed in previous
tutorials. The **Create** function for the **CButton** class, as seen in
the MFC help file, accepts five parameters. The first four are exactly
the same as those found in the **CStatic** class. The fifth parameter
indicates the resource ID for the button. The resource ID is a unique
integer value used to identify the button in the message map. A constant
value IDB\_BUTTON has been defined at the top of the program for this
value. The \"IDB\_\" is arbitrary, but here indicates that the constant
is an ID value for a Button. It is given a value of 100 because values
less than 100 are reserved for system-defined IDs. You can use any value
above 99.

The style attributes available for the **CButton** class are different
from those for the **CStatic** class. Eleven different \"BS\" (\"Button
Style\") constants are defined. A complete list of \"BS\" constants can
be found using **Search** on CButton and selecting the \"button style\"
link. Here we have used the BS\_PUSHBUTTON style for the button,
indicating that we want this button to display itself as a normal
push-button. We have also used two familiar \"WS\" attributes: WS\_CHILD
and WS\_VISIBLE. We will examine some of the other styles in later
sections.

When you run the code, you will notice that the button responds to user
events. That is, it highlights as you would expect. It does nothing else
because we haven\'t told it what to do. We need to wire in a message map
to make the button do something interesting.

### Creating a Message Map

The code below contains a message map as well as a new function that
handles the button click (so the program beeps when the user clicks on
the button). It is simply an extension of the prior code.
```c
    // button2.cpp
    #include <afxwin.h>
    #define IDB_BUTTON 100
    // Declare the application class
    class CButtonApp : public CWinApp
    {
    public:
     virtual BOOL InitInstance();
    };
    // Create an instance of the application class
    CButtonApp ButtonApp;  
    // Declare the main window class
    class CButtonWindow : public CFrameWnd
    { 
     CButton *button;
    public:
     CButtonWindow();
     afx_msg void HandleButton();
     DECLARE_MESSAGE_MAP()    
    };
    // The message handler function
    void CButtonWindow::HandleButton()
    {
     MessageBeep(-1);
    }
    // The message map
    BEGIN_MESSAGE_MAP(CButtonWindow, CFrameWnd)
     ON_BN_CLICKED(IDB_BUTTON, HandleButton)
    END_MESSAGE_MAP()
    // The InitInstance function is called once
    // when the application first executes
    BOOL CButtonApp::InitInstance()
    {
     m_pMainWnd = new CButtonWindow();
     m_pMainWnd->ShowWindow(m_nCmdShow);
     m_pMainWnd->UpdateWindow();
     return TRUE;
    }
    // The constructor for the window class
    CButtonWindow::CButtonWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CButton Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     // Get the size of the client rectangle
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     // Create a button
     button = new CButton();
     button->Create("Push me",
         WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
         r,
         this,
         IDB_BUTTON);
    }
```
Three modifications have been made to the code:

1.  The class declaration for **CButtonWindow** now contains a new
    member function as well as a macro that indicates a message map is
    defined for the class. The **HandleButton** function, which is
    identified as a message handler by the use of the **afx\_msg** tag,
    is a normal C++ function. There are some special constraints on this
    function which we will discuss shortly (e.g., it must be **void**
    and it cannot accept any parameters). The DECLARE\_MESSAGE\_MAP
    macro makes the creation of a message map possible. *Both the
    function and the macro must be public.*
2.  The **HandleButton** function is created in the same way as any
    member function. In this function, we called the **MessageBeep**
    function available from the Windows API.
3.  Special MFC macros create a message map. In the code, you can see
    that the BEGIN\_MESSAGE\_MAP macro accepts two parameters. The first
    is the name of the specific class to which the message map applies.
    The second is the base class from which the specific class is
    derived. It is followed by an ON\_BN\_CLICKED macro that accepts two
    parameters: The ID of the control and the function to call whenever
    that ID sends a command message. Finally, the message map ends with
    the END\_MESSAGE\_MAP macro.

When a user clicks the button, it sends a command message containing its
ID to its parent, which is the window containing the button. That is
default behavior for a button, and that is why this code works. The
button sends the message to its parent because it is a child window. The
parent window intercepts this message and uses the message map to
determine the function to call. MFC handles the routing, and whenever
the specified message is seen, the indicated function gets called. The
program beeps whenever the user clicks the button.

The ON\_BN\_CLICKED message is the only interesting message sent by an
instance of the **CButton** class. It is equivilent to the ON\_COMMAND
message in the **CWnd** class, and is simply a convenient synonym for
it.

### Sizing Messages

In the code above, the application\'s window, which is derived from the
**CFrameWnd** class, recognized the button-click message generated by
the button and responded to it because of its message map. The
ON\_BN\_CLICKED macro added into the message map (search for the
**CButton** overview as well as the the ON\_COMMAND macro in the MFC
help file) specifies the ID of the button and the function that the
window should call when it receives a command message from that button.
Since the button automatically sends to its parent its ID in a command
message whenever the user clicks it, this arrangement allows the code to
handle button events properly.

The frame window that acts as the main window for this application is
also capable of sending messages itself. There are about 100 different
messages available, all inherited from the **CWnd** class. By browsing
through the member functions for the **CWnd** class in MFC help file you
can see what all of these messages are. Look for any member function
beginning with the word \"On\".

You may have noticed that all of the code demonstrated so far does not
handle re-sizing very well. When the window re-sizes, the frame of the
window adjusts accordingly but the contents stay where they were placed
originally. It is possible to make resized windows respond more
attractively by recognizing resizing events. One of the messages that is
sent by any window is a sizing message. The message is generated
whenever the window changes shape. We can use this message to control
the size of child windows inside the frame, as shown below:
```c
    // button3.cpp
    #include <afxwin.h>
    #define IDB_BUTTON 100
    // Declare the application class
    class CButtonApp : public CWinApp
    {
    public:
     virtual BOOL InitInstance();
    };
    // Create an instance of the application class
    CButtonApp ButtonApp;  
    // Declare the main window class
    class CButtonWindow : public CFrameWnd
    { 
     CButton *button;
    public:
     CButtonWindow();
     afx_msg void HandleButton();
     afx_msg void OnSize(UINT, int, int);
     DECLARE_MESSAGE_MAP()    
    };
    // A message handler function
    void CButtonWindow::HandleButton()
    {
     MessageBeep(-1);
    }
    // A message handler function
    void CButtonWindow::OnSize(UINT nType, int cx,
     int cy)
    {
     CRect r;
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     button->MoveWindow(r);
    }
    // The message map
    BEGIN_MESSAGE_MAP(CButtonWindow, CFrameWnd)
     ON_BN_CLICKED(IDB_BUTTON, HandleButton)
     ON_WM_SIZE()
    END_MESSAGE_MAP()
    // The InitInstance function is called once
    // when the application first executes
    BOOL CButtonApp::InitInstance()
    {
     m_pMainWnd = new CButtonWindow();
     m_pMainWnd->ShowWindow(m_nCmdShow);
     m_pMainWnd->UpdateWindow();
     return TRUE;
    }
    // The constructor for the window class
    CButtonWindow::CButtonWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CButton Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     // Get the size of the client rectangle
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     
     // Create a button
     button = new CButton();
     button->Create("Push me",
         WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
         r,
         this,
         IDB_BUTTON);
    }
```
To understand this code, start by looking in the message map for the
window. There you will find the entry ON\_WM\_SIZE. This entry indicates
that the message map is sensitive to sizing messages coming from the
**CButtonWindow** object. Sizing messages are generated on this window
whenever the user re-sizes it. The messages come to the window itself
(rather than being sent to a parent as the ON\_COMMAND message is by the
button) because the frame window is not a child.

Notice also that the ON\_WM\_SIZE entry in the message map has no
parameters. As you can see in the MFC documentation under the **CWnd**
class, *it is understood that the ON\_WM\_SIZE entry in the message map
will always call a function named **OnSize** , and that function must
accept the three parameters shown* . The **OnSize** function must be a
member function of the class owning the message map, and the function
must be declared in the class as an **afx\_msg** function (as shown in
the definition of the **CButtonWindow** class).

If you look in the MFC documentation there are almost 100 functions
named \"On\...\" in the **CWnd** class. **CWnd::OnSize** is one of them.
All these functions have a corresponding tag in the message map with the
form ON\_WM\_. For example, ON\_WM\_SIZE corresponds to **OnSize**. None
of the ON\_WM\_ entries in the message map accept parameters like
ON\_BN\_CLICKED does. The parameters are assumed and automatically
passed to the corresponding \"On\...\" function like **OnSize**.

To repeat, because it is important: The **OnSize** function always
corresponds to the ON\_WM\_SIZE entry in the message map. You must name
the handler function **OnSize**, and it must accept the three parameters
shown in the listing. You can find the specific parameter requirements
of any **On\...** function by looking up that function in the MFC help
file. You can look the function up directly by typing **OnSize** into
the search window, or you can find it as a member function of the
**CWnd** class.

Inside the **OnSize** function itself in the code above, three lines of
code modify the size of the button held in the window. You can place any
code you like in this function.

The call to **GetClientRect** retrieves the new size of the window\'s
client rectangle. This rectangle is then deflated, and the
**MoveWindow** function is called on the button. **MoveWindow** is
inherited from **CWnd** and re-sizes and moves the child window for the
button in one step.

When you execute the program above and re-size the application\'s
window, you will find the button re-sizes itself correctly. In the code,
the re-size event generates a call through the message map to the
**OnSize** function, which calls the **MoveWindow** function to re-size
the button appropriately.

### Window Messages

By looking in the MFC documentation, you can see the wide variety of
**CWnd** messages that the main window handles. Some are similar to the
sizing message seen in the previous section. For example, ON\_WM\_MOVE
messages are sent when a user moves a window, and ON\_WM\_PAINT messages
are sent when any part of the window has to be repainted. In all of our
programs so far, repainting has happened automatically because controls
are responsible for their own appearance. If you draw the contents of
the client area yourself with GDI commands (see the book \"[Windows NT
Programming: An Introduction Using
C++](http://www.iftech.com/index.asp?qmainframe=books.asp)\" for a
complete explanation) the application is responsible for repainting any
drawings it places directly in the window. In this context the
ON\_WM\_PAINT message becomes important.

There are also some event messages sent to the window that are more
esoteric. For example, you can use the ON\_WM\_TIMER message in
conjunction with the **SetTimer** function to cause the window to
receive messages at pre-set intervals. The code below demonstrates the
process. When you run this code, the program will beep once each second.
The beeping can be replaced by a number of useful processes.
```c
    // button4.cpp
    #include <afxwin.h>
    #define IDB_BUTTON 100
    #define IDT_TIMER1 200
    // Declare the application class
    class CButtonApp : public CWinApp
    {
    public:
     virtual BOOL InitInstance();
    };
    // Create an instance of the application class
    CButtonApp ButtonApp;  
    // Declare the main window class
    class CButtonWindow : public CFrameWnd
    { 
     CButton *button;
    public:
     CButtonWindow();
     afx_msg void HandleButton();
     afx_msg void OnSize(UINT, int, int);
     afx_msg void OnTimer(UINT);
     DECLARE_MESSAGE_MAP()    
    };
    // A message handler function
    void CButtonWindow::HandleButton()
    {
     MessageBeep(-1);
    }
    // A message handler function
    void CButtonWindow::OnSize(UINT nType, int cx, 
     int cy)
    {
     CRect r;
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     button->MoveWindow(r);
    }
    // A message handler function
    void CButtonWindow::OnTimer(UINT id)
    {
     MessageBeep(-1);
    }
    // The message map
    BEGIN_MESSAGE_MAP(CButtonWindow, CFrameWnd)
     ON_BN_CLICKED(IDB_BUTTON, HandleButton)
     ON_WM_SIZE()
     ON_WM_TIMER()
    END_MESSAGE_MAP()
    // The InitInstance function is called once
    // when the application first executes
    BOOL CButtonApp::InitInstance()
    {
     m_pMainWnd = new CButtonWindow();
     m_pMainWnd->ShowWindow(m_nCmdShow);
     m_pMainWnd->UpdateWindow();
     return TRUE;
    }
    // The constructor for the window class
    CButtonWindow::CButtonWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CButton Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     // Set up the timer
     SetTimer(IDT_TIMER1, 1000, NULL); // 1000 ms.
     // Get the size of the client rectangle
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     // Create a button
     button = new CButton();
     button->Create("Push me",
         WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
         r,
         this,
         IDB_BUTTON);
    }
```
Inside the program above we created a button, as shown previously, and
left its re-sizing code in place. In the constructor for the window we
also added a call to the **SetTimer** function. This function accepts
three parameters: an ID for the timer (so that multiple timers can be
active simultaneously, the ID is sent to the function called each time a
timer goes off), the time in milliseconds that is to be the timer\'s
increment, and a function. Here, we passed NULL for the function so that
the window\'s message map will route the function automatically. In the
message map we have wired in the ON\_WM\_TIMER message, and it will
automatically call the **OnTimer** function passing it the ID of the
timer that went off.

When the program runs, it beeps once each 1,000 milliseconds. Each time
the timer\'s increment elapses, the window sends a message to itself.
The message map routes the message to the **OnTimer** function, which
beeps. You can place a wide variety of useful code into this function.

### Scroll Bar Controls

Windows has two different ways to handle scroll bars. Some controls,
such as the edit control and the list control, can be created with
scroll bars attached. When this is the case, the master control handles
the scroll bars automatically. For example, if an edit control has its
scroll bars active then, when the scroll bars are used, the edit control
scrolls as expected without any additional code.

Scroll bars can also work on a stand-alone basis. When used this way
they are seen as independent controls in their own right. You can learn
more about scroll bars by referring to the **CScrollBar** section of the
MFC reference manual. Scroll bar controls are created the same way we
created static labels and buttons. They have four member functions that
allow you to get and set both the range and position of a scroll bar.

The code shown below demonstrates the creation of a horizontal scroll
bar and its message map.
```c
    // sb1.cpp
    #include <afxwin.h>
    #define IDM_SCROLLBAR 100
    const int MAX_RANGE=100;
    const int MIN_RANGE=0;
    // Declare the application class
    class CScrollBarApp : public CWinApp
    {
    public:
     virtual BOOL InitInstance();
    };
    // Create an instance of the application class
    CScrollBarApp ScrollBarApp;  
    // Declare the main window class
    class CScrollBarWindow : public CFrameWnd
    { 
     CScrollBar *sb;
    public:
     CScrollBarWindow();
     afx_msg void OnHScroll(UINT nSBCode, UINT nPos,
         CScrollBar* pScrollBar);
     DECLARE_MESSAGE_MAP()    
    };
    // The message handler function
    void CScrollBarWindow::OnHScroll(UINT nSBCode, 
     UINT nPos, CScrollBar* pScrollBar)
    {
     MessageBeep(-1);
    }
    // The message map
    BEGIN_MESSAGE_MAP(CScrollBarWindow, CFrameWnd)
     ON_WM_HSCROLL()
    END_MESSAGE_MAP()
    // The InitInstance function is called once
    // when the application first executes
    BOOL CScrollBarApp::InitInstance()
    {
     m_pMainWnd = new CScrollBarWindow();
     m_pMainWnd->ShowWindow(m_nCmdShow);
     m_pMainWnd->UpdateWindow();
     return TRUE;
    }
    // The constructor for the window class
    CScrollBarWindow::CScrollBarWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CScrollBar Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     
     // Get the size of the client rectangle
     GetClientRect(&r);
     // Create a scroll bar
     sb = new CScrollBar();
     sb->Create(WS_CHILD|WS_VISIBLE|SBS_HORZ,
         CRect(10,10,r.Width()-10,30),
         this,
         IDM_SCROLLBAR);
     sb->SetScrollRange(MIN_RANGE,MAX_RANGE,TRUE);
    }
```
Windows distinguishes between horizontal and vertical scroll bars and
also supports an object called a *size box* in the **CScrollBar** class.
A size box is a small square. It is formed at the intersection of a
horizontal and vertical scroll bar and can be dragged by the mouse to
automatically re-size a window. Looking at the code in listing 4.5, you
can see that the **Create** function creates a horizontal scroll bar
using the SBS\_HORZ style. Immediately following creation, the range of
the scroll bar is set for 0 to 100 using the two constants MIN\_RANGE
and MAX\_RANGE (defined at the top of the listing) in the
**SetScrollRange** function.

The event-handling function **OnHScroll** comes from the **CWnd** class.
We have used this function because the code creates a horizontal scroll
bar. For a vertical scroll bar you should use **OnVScroll**. In the code
here the message map wires in the scrolling function and causes the
scroll bar to beep whenever the user manipulates it. When you run the
code you can click on the arrows, drag the thumb, and so on. Each event
will generate a beep, but the thumb will not actually move because we
have not wired in the code for movement yet.

Each time the scroll bar is used and **OnHScroll** is called, your code
needs a way to determine the user\'s action. Inside the **OnHScroll**
function you can examine the first parameter passed to the message
handler, as shown below. If you use this code with the code above, the
scroll bar\'s thumb will move appropriately with each user manipulation.
```c
    // The message handling function
    void CScrollBarWindow::OnHScroll(UINT nSBCode,
     UINT nPos, CScrollBar* pScrollBar)
    {
     int pos;
     pos = sb->GetScrollPos();
     switch ( nSBCode )
     {
         case SB_LINEUP:
             pos -= 1;
             break;
         case SB_LINEDOWN:
             pos += 1;
             break;
         case SB_PAGEUP:
             pos -= 10;
             break;
         case SB_PAGEDOWN:
             pos += 10;
             break;
         case SB_TOP:
             pos = MIN_RANGE;
             break;
         case SB_BOTTOM:
             pos = MAX_RANGE;
             break;
         
         case SB_THUMBPOSITION:
             pos = nPos;
             break;
         default:
             return;
     }
     if ( pos < MIN_RANGE )
         pos = MIN_RANGE;
     else if ( pos > MAX_RANGE )
         pos = MAX_RANGE;
     sb->SetScrollPos( pos, TRUE );
    }
```
The different constant values such as SB\_LINEUP and SB\_LINEDOWN are
described in the **CWnd::OnHScroll** function documentation. The code
above starts by retrieving the current scroll bar position using
**GetScrollPos**. It then decides what the user did to the scroll bar
using a switch statement. The constant value names imply a vertical
orientation but are used in horizontal scroll bars as well: SB\_LINEUP
and SB\_LINEDOWN apply when the user clicks the left and right arrows.
SB\_PAGEUP and SB\_PAGEDOWN apply when the user clicks in the shaft of
the scroll bar itself. SB\_TOP and SB\_BOTTOM apply when the user moves
the thumb to the top or bottom of the bar. SB\_THUMBPOSITION applies
when the user drags the thumb to a specific position. The code adjusts
the position accordingly, then makes sure that it\'s still in range
before setting the scroll bar to its new position. Once the scroll bar
is set, the thumb moves on the screen to inform the user visually.

A vertical scroll bar is handled the same way as a horizontal scroll bar
except that you use the SBS\_VERT style and the **OnVScroll** function.
You can also use several alignment styles to align both the scroll bars
and the grow box in a given client rectangle.

### Understanding Message Maps

The message map structure is unique to MFC. It is important that you
understand why it exists and how it actually works so that you can
exploit this structure in your own code.

Any C++ purist who looks at a message map has an immediate question: Why
didn\'t Microsoft use virtual functions instead? Virtual functions are
the standard C++ way to handle what mesage maps are doing in MFC, so the
use of rather bizarre macros like DECLARE\_MESSAGE\_MAP and
BEGIN\_MESSAGE\_MAP seems like a hack.

MFC uses message maps to get around a fundamental problem with virtual
functions. Look at the **CWnd** class in the MFC help file. It contains
over 200 member functions, all of which would have to be virtual if
message maps were not used. Now look at all of the classes that subclass
the **CWnd** class. For example, go to the contents page of the MFC help
file and look at the visual object hierarchy. 30 or so classes in MFC
use **CWnd** as their base class. This set includes all of the visual
controls such as buttons, static labels, and lists. Now imagine that MFC
used virtual functions, and you created an application that contained 20
controls. Each of the 200 virtual functions in **CWnd** would require
its own virtual function table, and each instance of a control would
therefore have a set of 200 virtual function tables associated with it.
The program would have roughly 4,000 virtual function tables floating
around in memory, and this is a problem on machines that have memory
limitations. Because the vast majority of those tables are never used,
they are unneeded.

Message maps duplicate the action of a virtual function table, but do so
on an on-demand basis. When you create an entry in a message map, you
are saying to the system, \"when you see the specified message, please
call the specified function.\" Only those functions that actually get
overridden appear in the message map, saving memory and CPU overhead.

When you declare a message map with DECLARE\_MESSAGE\_MAP and
BEGIN\_MESSAGE\_MAP, the system routes all messages through to your
message map. If your map handles a given message, then your function
gets called and the message stops there. However, if your message map
does not contain an entry for a message, then the system sends that
message to the class specified in the second parameter of
BEGIN\_MESSAGE\_MAP. That class may or may not handle it and the proces
repeats. Eventually, if no message map handles a given message, the
message arrives at a default handler that eats it.

### Conclusion

All the message handling concepts described in this tutorial apply to
every one of the controls and windows available in NT. In most cases you
can use the ClassWizard to install the entries in the message map, and
this makes the task much easier. For more information on the
ClassWizard, AppWizard and the resource editors see the tutorials on
these topics on the [MFC Tutorials page](http://devcentral.iftech.com/learning/tutorials/submfc.asp).
