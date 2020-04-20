set style line 1 linecolor rgb '#FF0000' linetype 1 linewidth 3 pointtype 5 pointsize 1
set style line 2 linecolor rgb '#00FF00' linetype 1 linewidth 3 pointtype 5 pointsize 1
set style line 3 linecolor rgb '#0000FF' linetype 1 linewidth 3 pointtype 5 pointsize 1
set style line 4 linecolor rgb '#FFFF00' linetype 1 linewidth 3 pointtype 5 pointsize 1
set style line 5 linecolor rgb '#00FFFF' linetype 1 linewidth 3 pointtype 5 pointsize 1
set style line 6 linecolor rgb '#FF00FF' linetype 1 linewidth 3 pointtype 5 pointsize 1

set multiplot layout 3, 1
set tmargin 3

set ylabel "signal"
set title "captura"
set yrange [0:1023];
set autoscale
plot '< tail -n 100 log.txt' every ::1 using 1:2 with   lines linestyle 3 notitle, \
     '< tail -n 100 log.txt' every ::1 using 1:3 with   lines linestyle 4 notitle,



