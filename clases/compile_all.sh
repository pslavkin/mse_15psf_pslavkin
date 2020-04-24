latexmk -c
pdflatex "\def\CurrentAudience{clase1}\input{clases}"
pdflatex "\def\CurrentAudience{clase1}\input{clases}"
mv clases.pdf clase1.pdf
latexmk -c
pdflatex "\def\CurrentAudience{clase2}\input{clases}"
pdflatex "\def\CurrentAudience{clase2}\input{clases}"
mv clases.pdf clase2.pdf
latexmk -c

