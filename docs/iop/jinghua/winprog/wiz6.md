---
layout: article
title: Understanding the AppWizard and ClassWizard in Visual C++ Version 6.x by Marshall Brain
---

## Understanding Document Templates

One of the more interesting, and best hidden, features of any AppWizard
framework is something called *document templates* . In this tutorial
you will learn about document templates and see how you can add new ones
to your applications. By the end of the tutorial you will have used
document templates to create a single MDI application that can display
both text and drawing documents simultaneously.

### Creating a Text Editor

Let\'s start by using the AppWizard to create a second type of
application. In the previous tutorials we have created a drawing editor.
Here we will quickly create a text editor. It is interesting to note
that you can create a complete text editor - one with all the features
of Notepad, along with several others as well - without writing a single
line of code. Take the following steps:

-   In Visual C++, select the **New** option from the **File** menu,
    make sure the **Project** tab in the subsequent dialog is selected,
    and name the new project \"Ed\". Make sure the type is set to **MFC
    AppWizard (EXE)** and select an appropriate directory. Click **OK**
    and look over the AppWizard\'s options in the six configuration
    screens.
-   We want to change two things in the configuration screens: First we
    want to give a default file extension, and second we want to change
    the view class. In the fourth screen of the six, click the
    **Advanced** button and type \"tex\" into the **File Extension**
    field. In the sixth screen, click on **CEdView**, and at the bottom
    of the dialog change the **Base Class** to **CEditView** using the
    combo box.
-   Compile and run the program. You will find that you have a complete
    MDI text editor. You can load and save text files, cut, copy and
    paste text, print files, and so on.
-   If you look at the help page for the **CEditView** class, you will
    find that it automatically understands certain menu options. In
    particular, if you add menu options with the IDs of ID\_EDIT\_FIND,
    ID\_EDIT\_REPEAT, ID\_EDIT\_REPLACE and ID\_EDIT\_SELECT\_ALL, the
    program will *automatically* recognize these new options and perform
    them properly. You do not need to add anything but the menu options.
    Do that now and test the program.

This application was so easy to create because the **CEditView** class
has all of the behavior of a normal text editor built into it. There is
just one line of code that the AppWizard had to add to make the whole
thing work, and that line can be found in the **Serialize** function of
the document class. It looks like this:

    ((CEditView*)m_viewList.GetHead())->SerializeRaw(ar);

That line loads and saves text files. Just so you are aware of it, the
**CEditView** class violates the strict separation of document and view.
The **CEditView** class contains a normal **CEdit** control, and this
control holds the editor\'s data itself. Therefore, the data resides
inside the **CEditView** class rather than in the document class, and
the line of code above gets or sets that data. Because of this odd
structure, you will want to remove the **New Window** option from the
**Window** menu. Since the document does not hold the data, it is not
possible to have multiple views display the same document. This seems
like a small price to pay for the ease of using the **CEditView** class
to create quickie text editors.

Now that you have created a complete text editor, let\'s see what steps
are necessary to create a single MDI application that can display both
text and drawing documents. To do this, we will take the drawing program
from the previous tutorials and modify it so that it can also display
text documents. To do this, three steps are required:

-   Step 1: Start with the drawing program and add a new document and
    view class for the text editor
-   Step 2: Create a new document template for the new document type
-   Step 3: Add three new resources to the drawing editor

Once you have completed these three steps, the program will be able to
display both text and drawing documents simultaneously.

### Step 1: Add a new document and view class

Open the workspace file for the drawing editor (samp) in Visual C++.
Choose the **ClassWizard** option in the **View** menu. Click the **Add
Class** button and select **New**. You will see a dialog with several
fields. In the **Name** field type **CEdDoc** . In the **Base Class**
field choose **CDocument**. The ClassWizard will choose a file name of
EDDOC.CPP, and this name is fine. Click the **OK** button. Click the
**Add Class** button again to create another new class. Type **CEdView**
into the **Name** field and choose **CEditView** for the base class
type. The file name EDVIEW.CPP chosen by the ClassWizard is fine. Click
the **OK** button. Close the ClassWizard by clicking its **OK** button.

Now modify the **Serialize** function in the new document class (CEdDoc)
so it contains the line seen in the text editor:
```c
    ((CEditView*)m_viewList.GetHead())->SerializeRaw(ar);
```
The two new CPP files were automatically added to the drawing project by
the ClassWizard. You will add the header files to the CSampApp class in
the next step.

### Step 2: Add a new document template

Open the CSampApp class, which contains the application class for the
application derived from **CWinApp**, in the ClassView so that you can
see a list of its functions. Find the **InitInstance** function. Double
click on it. Look for the following lines:
```c
     CMultiDocTemplate* pDocTemplate;
     pDocTemplate = new CMultiDocTemplate(
        IDR_SAMPTYPE,
        RUNTIME_CLASS(CSampDoc),
        RUNTIME_CLASS(CChildFrame), // custom MDI child frame
        RUNTIME_CLASS(CSampView));
     AddDocTemplate(pDocTemplate);
```
These lines create a *document template*. The **CWinApp** class (see the
help file) has built into it the ability to hold a list of document
templates. When it holds more than one, it changes the behavior of the
application slightly. For example, the **New** option pops up a list
that lets the user choose what type of document he/she wishes to create.
What we want to do is change the program so that it contains two
templates: one for drawing documents, and another for text documents.
Modify the above code so that it looks like this:
```c
    CMultiDocTemplate* pDocTemplate;
    pDocTemplate = new CMultiDocTemplate(
        IDR_EDTYPE,
        RUNTIME_CLASS(CEdDoc),
        RUNTIME_CLASS(CChildFrame),          // custom MDI child frame
        RUNTIME_CLASS(CEdView));
    AddDocTemplate(pDocTemplate); 
    pDocTemplate = new CMultiDocTemplate(
        IDR_SAMPTYPE,
        RUNTIME_CLASS(CSampDoc),
        RUNTIME_CLASS(CChildFrame),          // custom MDI child frame
        RUNTIME_CLASS(CSampView));
    AddDocTemplate(pDocTemplate);
```
Note that a new document template has been created. The new one goes
first (more on the reason for that in a moment). It specifies
IDR\_EDTYPE, **CEdDoc** and **CEdView**. But what does that mean?

The purpose of a document template is to relate a resource type
(IDR\_EDTYPE), a document class, a view class, and a window class. When
the application framework needs to create a new instance of a document
for the user, it looks to the document template, which tells it to
create a new instance of the appropriate document, view and window
classes. The resource ID is used when the framework needs to change
resources. It identifies a specific menu, icon and string resource. So,
for example, when the user clicks on a window in the MDI shell, the
application framework brings that window to the foreground *and* it
changes the menu to the one appropriate for that window, according to
the window\'s document template.

We put the text document template first because, if the user attempts to
open a document whose extension is unknown to the application, the
application tries to open it under the first document template
registered. Since text documents are far more likely than drawing
documents, the text template is placed first in the list of document
templates.

*Be sure to include EDDOC.H and EDVIEW.H at the top of SAMP.CPP.*

### Step 3: Create resources

The new document template specifies a resource ID of IDR\_EDTYPE. If you
open the ResourceView and look through its resources, you will find that
it already contains three resources of type IDR\_SAMPTYPE as needed by
the drawing editor: a menu, an icon, and a string near the top of the
string table. The easiest way to create new resources for the text
editor type is to copy these three IDR\_SAMPTYPE resources to the
clipboard, paste them back, and then change their names to IDR\_EDTYPE
using the **Properties** option in the **View** menu. Then modify them
as appropriate. For example, to the IDR\_EDTYPE menu you will want to
add the ID\_EDIT\_FIND, ID\_EDIT\_REPEAT, ID\_EDIT\_REPLACE and
ID\_EDIT\_SELECT\_ALL options (also delete the **Option** menu that got
copied). You will also want to remove the **New Window** option from the
Window menu. Change the IDR\_EDTYPE icon as you see fit. Change the
IDR\_EDTYPE string so that it looks like this:

    \nEd\nEd\nEd Files (*.tex)\n.TEX\nEd.Document\nEd Document

For more information about this mysterious string, search for the
**GetDocString** function in the help file. It will explain what all
seven of the substrings do. Now that you understand the strings, modify
the IDR\_SAMPTYPE string as well so it contains a file extension:

    \nDrawing\nDrawing\nDrawing Files (*.drw)\n.DRW\nDrawing.Document\nDraw Document

Change the two strings in any way that you like.

### Step 4 : Build and execute

Build the new application and run it. When it starts you should see a
new dialog that lets you choose whether you want to create a text or
drawing document. Choose text, and verify that the text editor works
properly. Now choose **New** and create a drawing document. Draw
something. Note that when you change windows the menu bar changes as
appropriate.

### Conclusion

You can see that adding a new document template is easy, and there is
really no limit to the number of templates a single application might
have. As you create more complex applications, you will find this to be
an extremely useful feature of the AppWizard framework.
