# Page manipulation with qpdf

The `R Markdown` has a front page that is too small (paradoxically with many books) compared to the other pages in the book; this is to be amended 
by replacing it with page 2 to hold the front cover (extracted as .png and pull inside IceCream editor, which also can cut and paste pages of a 
.pdf).

```bash
export book=R\ Markdown-The\ Definitive\ Guide.pdf
qpdf "${book}" --pages . 2-2 -- 2.pdf
qpdf "${book}" --pages "${book}" 2-339 ./2.pdf 1 -- new.pdf
```
