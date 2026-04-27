#!/usr/bin/bash

export pgsp=../../../book/pgsp.pdf
export chapters=($(echo ch0{1..9} ch{10..18}))
export pages=(12-21 22-81 82-115 118-209 210-257 258-283 284-327 328-353 354-363 364-371 372-387 390-417 418-439 440-455 456-467 470-507 508-519 520-553)
qpdf ${pgsp} --pages . 1,3-9 -- frontmat.pdf
qpdf ${pgsp} --pages . 2-2 -- pre.pdf
for i in {0..17}
do
   echo $((${i} + 1))
   qpdf ${pgsp} --pages . ${pages[${i}]} -- ${chapters[${i}]}.pdf
done
qpdf ${pgsp} --pages . 554-572 -- aft.pdf
