---
layout: article
title: Understanding the AppWizard and ClassWizard in Visual C++ Version 6.x by Marshall Brain
---

## Synchronizing Views

In the previous tutorial you learned how to modify the document and view
classes to create a simple drawing editor. There is one subtle problem
with that program, however. In this tutorial you will learn how to solve
that problem using the view\'s **OnUpdate** function.

To demonstrate the problem, run the application that you created in the
previous tutorial. Draw something in the default window. Now choose the
**New Window** option in the **Window** menu. This option opens a second
view on the same document. This second window will display the same
thing that the first window does because both share the same document.
Now choose the **Tile** option in the **Window** menu. You can see that
both views are identical. Now draw into one of the views. What you will
find is that the views will not be synchronized. What you draw into one
view does not appear in the other. However, if you iconify the
application and then expand the icon, you will find that the views are
once again identical. Both receive exposure events, and both draw from
the same document data, so they must look the same.

What we would like to do is modify the code so that, when you draw in
one view, all views attached to the same document are immediately
updated as well. The framework already contains the functions necessary
to do this-all you have to do is wire them in properly.

The **CDocument** class maintains a list of all views attached to the
document. It also contains a function called **UpdateAllViews** . This
function, when called, calls the **OnUpdate** function of each view
attached to the document. By default the **OnUpdate** function does
nothing, but you can modify it to do anything you like. Optionally you
can pass the **OnUpdate** function two programmer-defined parameters to
further customize its activities.

What we would like to create here is a mechanism that causes all views
attached to a document to paint the last point added to the data
structure whenever any of the views for that document adds a new point.
To do this, first modify the **OnMouseMove** function in the view class
so that it contains a call to **UpdateAllViews**, as shown below:

```c
    void CSampView::OnMouseMove(UINT nFlags, CPoint point) 
    {
        CSampDoc* pDoc = GetDocument();
        ASSERT_VALID(pDoc);
        if (nFlags == MK_LBUTTON)
        {
            CClientDC dc(this);
            dc.Rectangle(point.x, point.y, 
                point.x+w, point.y+w);
            pDoc->x.Add(point.x);
            pDoc->y.Add(point.y);
            pDoc->SetModifiedFlag();
            pDoc->UpdateAllViews(this, 0, 0);
        }
        CView::OnMouseMove(nFlags, point);
    }
```
This call to **UpdateAllViews** indicates that the document should call
the **OnUpdate** function in all views attached to it *except* the one
indicated by **this**. It does this because the current view has already
drawn the point and there is no reason to do it a second time. The
latter two parameters in the call to **UpdateAllViews** will be passed
directly to **OnUpdate**. We do not have any use for these parameters in
this simple example so we pass zeros. It would not hurt to read about
both **CDocument::UpdateAllViews** and **CView::OnUpdate** in the MFC
help file. Also read about **CView::OnInitialUpdate** while you are
there.

Now use the ClassWizard to override the **OnUpdate** function. Choose
the **ClassWizard** option in the **View** menu. Make sure that the
**Message Maps** tab is selected. Make sure that **CSampView** is the
class selected in the Class Name field. Click on **CSampView** in the
**Object IDs** list. Search down until you find **OnUpdate** in the
**Messages** list. This function is a virtual function and we can
override it with the ClassWizard. Select **OnUpdate** in the list, click
the **Add Function** button and then click the **Edit Code** button.
Modify the function so that it looks like this:

```c
    void CSampView::OnUpdate(CView* pSender, LPARAM lHint, CObject* pHint) 
    {
        CSampDoc* pDoc = GetDocument();
        ASSERT_VALID(pDoc);
        int i = pDoc->x.GetSize();
        if (i > 0)
        {
            i--;
            CClientDC dc(this);
            dc.Rectangle(pDoc->x[i],
                pDoc->y[i],
                pDoc->x[i]+w,
                pDoc->y[i]+w);
        }
    }
```
The goal of this function is to get the last point in the data structure
and draw it. It therefore gets the size of one of the arrays, checks to
make sure that the array is not empty, and then draws the last point.
The **if** statement is necessary because the **OnInitialUpdate**
function gets called when the view is created, and by default it calls
**OnUpdate**. You could override this function to remove the default
behavior and the **if** statement would no longer be necessary. However,
it is not a bad safety feature.

Build and execute the application. Choose the **New Window** option in
the **Window** menu, followed by the **Tile** option. Draw in one of the
windows and you will find that both views update simultaneously. This is
proper behavior, and will work regardless of the number of views that
are open on the same document. It is also very efficient.

There are other ways in which to use the **UpdateAllViews/OnUpdate** to
accomplish the same thing. For example, **OnMouseMove** might draw
nothing and let the **OnUpdate** function handle all drawing. Or you
might pass the new point as one of the parameters. Experiment with
different techniques until you find the one you like best.
