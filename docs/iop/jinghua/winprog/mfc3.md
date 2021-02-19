---
layout: article
title: Introduction to MFC Programming with Visual C++ Version 6.x by Marshall Brain
---

## MFC Styles

*Controls* are the user interface objects used to create interfaces for
Windows applications. Most Windows applications and dialog boxes that
you see are nothing but a collection of controls arranged in a way that
appropriately implements the functionality of the program. In order to
build effective applications, you must completely understand how to use
the controls available in Windows. There are only six basic
controls-**CStatic**, **CButton** , **CEdit**, **CList**, **CComboBox**,
and **CScrollBar** -along with some minor variations (also note that
Windows 95 added a collection of about 15 enhanced controls as well).
You need to understand what each control can do, how you can tune its
appearance and behavior, and how to make the controls respond
appropriately to user events. By combining this knowledge with an
understanding of menus and dialogs you gain the ability to create any
Windows application that you can imagine. You can create controls either
programatically as shown in this tutorial, or through resource files
using the dialog resource editor. While the dialog editor is much more
convenient, it is extremely useful to have a general understanding of
controls that you gain by working with them programatically as shown
here and in the next tutorial.

The simplest of the controls, **CStatic**, displays static text. The
**CStatic** class has no data members and only a few member functions:
the constructor, the **Create** function for getting and setting icons
on static controls, and several others. It does not respond to user
events. Because of its simplicity, it is a good place to start learning
about Windows controls.

In this tutorial we will look at the **CStatic** class to understand how
controls can be modified and customized. In the following tutorial, we
examine the **CButton** and **CScrollBar** classes to gain an
understanding of event handling. Once you understand all of the controls
and classes, you are ready to build complete applications.

### The Basics

A **CStatic** class in MFC displays static text messages to the user.
These messages can serve purely informational purposes (for example,
text in a message dialog that describes an error), or they can serve as
small labels that identify other controls. Pull open a File Open dialog
in any Windows application and you will find six text labels. Five of
the labels identify the lists, text area, and check box and do not ever
change. The sixth displays the current directory and changes each time
the current directory changes.

**CStatic** objects have several other display formats. By changing the
*style* of a label it can display itself as a solid rectangle, as a
border, or as an icon. The rectangular solid and frame forms of the
**CStatic** class allow you to visually group related interface elements
and to add separators between controls.

A **CStatic** control is always a child window to some parent window.
Typically, the parent window is a main window for an application or a
dialog box. You create the static control, as discussed in Tutorial 2,
with two lines of code:
```c
    CStatic *cs;    
    ...  
    cs = new CStatic();  
    cs->Create("hello world",       
     WS_CHILD|WS_VISIBLE|SS_CENTER,      
     CRect(50,80, 150, 150),     
     this);
```
This two-line creation style is typical of all controls created using
MFC. The call to **new** allocates memory for an instance of the
**CStatic** class and, in the process, calls the constructor for the
class. The constructor performs any initialization needed by the class.
The **Create** function creates the control at the Windows level and
puts it on the screen.

The **Create** function accepts up to five parameters, as described in
the MFC help file. Choose the **Search** option in the **Help** menu of
Visual C++ and then enter **Create** so that you can select
**CStatic::Create** from the list. Alternatively, enter **CStatic** in
the search dialog and then click the **Members** button on its overview
page.

Most of these values are self-explanatory. The **lpszText** parameter
specifies the text displayed by the label. The **rect** parameter
controls the position, size, and shape of the text when it\'s displayed
in its parent window. The upper left corner of the text is determined by
the upper left corner of the **rect** parameter and its bounding
rectangle is determined by the width and height of the rect parameter.
The **pParentWnd** parameter indicates the parent of the **CStatic**
control. The control will appear in the parent window, and the position
of the control will be relative to the upper left corner of the client
area of the parent. The **nID** parameter is an integer value used as a
control ID by certain functions in the API. We\'ll see examples of this
parameter in the next tutorial.

The **dwStyle** parameter is the most important parameter. It controls
the appearance and behavior of the control. The following sections
describe this parameter in detail.

### CStatic Styles

All controls have a variety of display *styles*. Styles are determined
at creation using the **dwStyle** parameter passed to the **Create**
function. The style parameter is a bit mask that you build by or-ing
together different mask constants. The constants available to a
**CStatic** control can be found in the MFC help file (Find the page for
the **CStatic::Create** function as described in the previous section,
and click on the **Static Control Styles** link near the top of the
page) and are also briefly described below:

##### Valid styles for the CStatic class -

###### Styles inherited from CWnd:

-   WS\_CHILD Mandatory for CStatic.
-   WS\_VISIBLE The control should be visible to the user.
-   WS\_DISABLED The control should reject user events.
-   WS\_BORDER The control\'s text is framed by a border.

###### Styles native to CStatic:

-   SS\_BLACKFRAME The control displays itself as a rectangular border.
    Color is the same as window frames.
-   SS\_BLACKRECT The control displays itself as a filled rectangle.
    Color is the same as window frames.
-   SS\_CENTER The text is center justified.
-   SS\_GRAYFRAME The control displays itself as a rectangular border.
    Color is the same as the desktop.
-   SS\_GRAYRECT The control displays itself as a filled rectangle.
    Color is the same as the desktop.
-   SS\_ICON The control displays itself as an icon. The text string is
    used as the name of the icon in a resource file. The rect parameter
    controls only positioning.
-   SS\_LEFT The text displayed is left justified. Extra text is
    word-wrapped.
-   SS\_LEFTNOWORDWRAP The text is left justified, but extra text is
    clipped.
-   SS\_NOPREFIX \"&\" characters in the text string indicate
    accelerator prefixes unless this attribute is used.
-   SS\_RIGHT The text displayed is right justified. Extra text is
    word-wrapped.
-   SS\_SIMPLE A single line of text is displayed left justified. Any
    CTLCOLOR messages must be ignored by the parent.
-   SS\_USERITEM User-defined item.
-   SS\_WHITEFRAME The control displays itself as a rectangular border.
    Color is the same as window backgrounds.
-   SS\_WHITERECT The control displays itself as a filled rectangle.
    Color is the same as window backgrounds.

These constants come from two different sources. The \"SS\" (Static
Style) constants apply only to **CStatic** controls. The \"WS\" (Window
Style) constants apply to all windows and are therefore defined in the
**CWnd** object from which **CStatic** inherits its behavior. There are
many other \"WS\" style constants defined in **CWnd**. They can be found
by looking up the **CWnd::Create** function in the MFC documentation.
The four above are the only ones that apply to a **CStatic**object.

A **CStatic** object will always have at least two style constants or-ed
together: WS\_CHILD and WS\_VISIBLE. The control is not created unless
it is the child of another window, and it will be invisible unless
WS\_VISIBLE is specified. WS\_DISABLED controls the label\'s response to
events and, since a label has no sensitivity to events such as
keystrokes or mouse clicks anyway, specifically disabling it is
redundant.

All the other style attributes are optional and control the appearance
of the label. By modifying the style attributes passed to the
**CStatic::Create** function, you control how the static object appears
on screen. You can learn quite a bit about the different styles by using
style attributes to modify the text appearance of the **CStatic**
object, as discussed in the next section.

### CStatic Text Appearance

The code shown below is useful for understanding the behavior of the
**CStatic** object. It is similar to the listing discussed in Tutorial
2, but it modifies the creation of the **CStatic** object slightly.
Please turn to Tutorial 1 for instructions on entering and compiling
this code.
```c
    //static1.cpp
    #include <afxwin.h>

    // Declare the application class
    class CTestApp : public CWinApp
    {
    public:
     virtual BOOL InitInstance();
    };

    // Create an instance of the application class
    CTestApp TestApp;  

    // Declare the main window class
    class CTestWindow : public CFrameWnd
    { 
     CStatic* cs;
    public:
     CTestWindow();
    };

    // The InitInstance function is called
    // once when the application first executes
    BOOL CTestApp::InitInstance()
    {
     m_pMainWnd = new CTestWindow();
     m_pMainWnd->ShowWindow(m_nCmdShow);
     m_pMainWnd->UpdateWindow();
     return TRUE;
    }

    // The constructor for the window class
    CTestWindow::CTestWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CStatic Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     
     // Get the size of the client rectangle
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     
     // Create a static label
     cs = new CStatic();
     cs->Create("hello world",
         WS_CHILD|WS_VISIBLE|WS_BORDER|SS_CENTER,
         r,
         this);
    }
```
The code of interest in listing 3.1 is in the function for the window
constructor, which is repeated below with line numbers:
```c
        CTestWindow::CTestWindow()
     { 
         CRect r;
         
         // Create the window itself
    1        Create(NULL, 
             "CStatic Tests", 
             WS_OVERLAPPEDWINDOW,
             CRect(0,0,200,200));
         // Get the size of the client rectangle
    2        GetClientRect(&r);
    3        r.InflateRect(-20,-20);
         // Create a static label
    4        cs = new CStatic();
    5        cs->Create("hello world",
             WS_CHILD|WS_VISIBLE|WS_BORDER|SS_CENTER,
             r,
             this);
     }
```
The function first calls the **CTestWindow::Create** function for the
window at line 1. This is the **Create** function for the **CFrameWnd**
object, since **CTestWindow** inherits its behavior from **CFrameWnd**.
The code in line 1 specifies that the window should have a size of 200
by 200 pixels and that the upper left corner of the window should be
initially placed at location 0,0 on the screen. The constant
**rectDefault** can replace the **CRect** parameter if desired.

At line 2, the code calls **CTestWindow::GetClientRect**, passing it the
parameter **&r**. The **GetClientRect** function is inherited from the
**CWnd** class (see the side-bar for search strategies to use when
trying to look up functions in the Microsoft documentation). The
variable **r** is of type **CRect** and is declared as a local variable
at the beginning of the function.

Two questions arise here in trying to understand this code: 1) What does
the **GetClientRect** function do? and 2) What does a **CRect** variable
do? Let\'s start with question 1. When you look up the
**CWnd::GetClientRect** function in the MFC documentation you find it
returns a structure of type **CRect** that contains the size of the
client rectangle of the particular window. It stores the structure at
the address passed in as a parameter, in this case **&r**. That address
should point to a location of type **CRect**. The **CRect** type is a
class defined in MFC. It is a convenience class used to manage
rectangles. If you look up the class in the MFC documentation, you will
find that it defines over 30 member functions and operators to
manipulate rectangles.

In our case, we want to center the words \"Hello World\" in the window.
Therefore, we use **GetClientRect** to get the rectangle coordinates for
the client area. In line 3 we then call **CRect::InflateRect**, which
symmetrically increases or decreases the size of a rectangle (see also
CRect::DeflateRect). Here we have decreased the rectangle by 20 pixels
on all sides. Had we not, the border surrounding the label would have
blended into the window frame, and we would not be able to see it.

The actual **CStatic** label is created in lines 4 and 5. The style
attributes specify that the words displayed by the label should be
centered and surrounded by a border. The size and position of the border
is determined by the **CRect** parameter **r** .

By modifying the different style attributes you can gain an
understanding of the different capabilities of the **CStatic** Object.
For example, the code below contains a replacement for the
**CTestWindow** constructor function in the first listing.
```c
    CTestWindow::CTestWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CStatic Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     
     // Get the size of the client rectangle
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     
     // Create a static label
     cs = new CStatic();
     cs->Create("Now is the time for all good men to \
    come to the aid of their country",
         WS_CHILD|WS_VISIBLE|WS_BORDER|SS_CENTER,
         r,
         this);
    }
```
The code above is identical to the previous except the text string is
much longer. As you can see when you run the code, the **CStatic**
object has wrapped the text within the specified bounding rectangle and
centered each line individually.

If the bounding rectangle is too small to contain all the lines of text,
then the text is clipped as needed to make it fit the available space.
This feature of the **CStatic** object can be demonstrated by decreasing
the size of the rectangle or increasing the length of the string.

In all the code we have seen so far, the style SS\_CENTER has been used
to center the text. The **CStatic** object also allows for left or right
justification. Left justification is created by replacing the SS\_CENTER
attribute with an SS\_LEFT attribute. Right justification aligns the
words to the right margin rather than the left and is specified with the
SS\_RIGHT attribute.

One other text attribute is available. It turns off the word wrap
feature and is used often for simple labels that identify other controls
(see figure 3.1 for an example). The SS\_LEFTNOWORDWRAP style forces
left justification and causes no wrapping to take place.

### Rectangular Display Modes for CStatic

The **CStatic** object also supports two different rectangular display
modes: solid filled rectangles and frames. You normally use these two
styles to visually group other controls within a window. For example,
you might place a black rectangular frame in a window to collect
together several related editable areas. You can choose from six
different styles when creating these rectangles: SS\_BLACKFRAME,
SS\_BLACKRECT, SS\_GRAYFRAME, SS\_GRAYRECT, SS\_WHITEFRAME, and
SS\_WHITERECT. The RECT form is a filled rectangle, while the FRAME form
is a border. The color names are a little misleading-for example,
SS\_WHITERECT displays a rectangle of the same color as the window
background. Although this color defaults to white, the user can change
it with the Control Panel and the rectangle may not be actually white on
some machines.

When a rectangle or frame attribute is specified, the **CStatic** \'s
text string is ignored. Typically an empty string is passed. Try using
several of these styles in the previous code and observe the result.

### Fonts

You can change the font of a **CStatic** object by creating a **CFont**
object. Doing so demonstrates how one MFC class can interact with
another in certain cases to modify behavior of a control. The **CFont**
class in MFC holds a single instance of a particular Windows font. For
example, one instance of the **CFont** class might hold a Times font at
18 points while another might hold a Courier font at 10 points. You can
modify the font used by a static label by calling the **SetFont**
function that **CStatic** inherits from **CWnd**. The code below shows
the code required to implement fonts.
```c
    CTestWindow::CTestWindow()
    { 
     CRect r;
     // Create the window itself
     Create(NULL, 
         "CStatic Tests", 
         WS_OVERLAPPEDWINDOW,
         CRect(0,0,200,200));
     // Get the size of the client rectangle
     GetClientRect(&r);
     r.InflateRect(-20,-20);
     // Create a static label
     cs = new CStatic();
     cs->Create("Hello World",
         WS_CHILD|WS_VISIBLE|WS_BORDER|SS_CENTER,
         r,
         this);
     
     // Create a new 36 point Arial font
     font = new CFont;
     font->CreateFont(36,0,0,0,700,0,0,0,
                    ANSI_CHARSET,OUT_DEFAULT_PRECIS,
                    CLIP_DEFAULT_PRECIS,
                    DEFAULT_QUALITY,
                    DEFAULT_PITCH|FF_DONTCARE,
                    "arial");                                     
     // Cause the label to use the new font
     cs->SetFont(font);
    }
```
The code above starts by creating the window and the **CStatic** object
as usual. The code then creates an object of type **CFont**. The font
variable should be declared as a data member in the **CTestWindow**
class with the line \"CFont \*font\". The **CFont::CreateFont** function
has 15 parameters (see the MFC help file), but only three matter in most
cases. For example, the 36 specifies the size of the font in points, the
700 specifies the density of the font (400 is \"normal,\" 700 is
\"bold,\" and values can range from 1 to 1000. The constants FW\_NORMAL
and FW\_BOLD have the same meanings. See the FW constants in the API
help file), and the word \"arial\" names the font to use. Windows
typically ships with five True Type fonts (Arial, Courier New, Symbol,
Times New Roman, and Wingdings), and by sticking to one of these you can
be fairly certain that the font will exist on just about any machine. If
you specify a font name that is unknown to the system, then the
**CFont** class will choose the default font seen in all the other
examples used in this tutorial.

For more information on the **CFont** class see the MFC documentation.
There is also a good overview on fonts in the API on-line help file.
Search for \"Fonts and Text Overview.\"

The **SetFont** function comes from the **CWnd** class. It sets the font
of a window, in this case the **CStatic** child window. One question you
may have at this point is, \"How do I know which functions available in
**CWnd** apply to the **CStatic** class?\" You learn this by experience.
Take half an hour one day and read through all the functions in **CWnd**
. You will learn quite a bit and you should find many functions that
allow you to customize controls. We will see other **Set** functions
found in the **CWnd** class in the next tutorial.

### Conclusion

In this tutorial we looked at the many different capabilities of the
**CStatic** object. We left out some of the **Set** functions inherited
from the **CWnd** class so they can be discussed in Tutorial 4 where
they are more appropriate.

### Looking up functions in the Microsoft Documentation

In Visual C++ Version 5.x, looking up functions that you are unfamiliar
with is very simple. All of the MFC, SDK, Windows API, and C/C++
standard library functions have all been integrated into the same help
system. If you are uncertain of where a function is defined or what
syntax it uses, just use the **Search** option in the Help menu. All
occurrences of the function are returned and you may look through them
to select the help for the specific function that you desire.

### Compiling multiple executables

This tutorial contains several different example programs. There are two
different ways for you to compile and run them. The first way is to
place each different program into its own directory and then create a
new project for each one. Using this technique, you can compile each
program separately and work with each executeable simultaneously or
independently. The disadvantage of this approach is the amount of disk
space it consumes.

The second approach involves creating a single directory that contains
all of the executables from this tutorial. You then create a single
project file in that directory. To compile each program, you can edit
the project and change its source file. When you rebuild the project,
the new executable reflects the source file that you chose. This
arrangement minimizes disk consumption, and is generally preferred.
