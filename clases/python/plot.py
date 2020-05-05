import matplotlib.pyplot as plt

fig      = plt.figure()

graph1Axe = fig.add_subplot(2,2,1)
graph1Ln1, = plt.plot([1,2,3],[4,5,6],'r-o')

graph1Axe.grid                     ( True     )
graph1Axe.set_xlim                 ( 0,4      )
graph1Axe.set_ylim                 ( 0,10     )
graph1Ln1.set_label                ( "recta1" )
graph1legendLn   = graph1Axe.legend (          )


data2_1=[6,5,4]
data2_2=[1,2,3]
t=[1,2,3]
graph2Axe           = fig.add_subplot(2,2,4)
graph2Ln1,graph2Ln2 = plt.plot(t,data2_1,'r-o', t,data2_2,'g-',)

graph2Axe.grid                      ( True       )
graph2Axe.set_xlim                  ( 0,4        )
graph2Axe.set_ylim                  ( 0,10       )
graph2Ln1.set_label                 ( "recta2_1" )
graph2Ln2.set_label                 ( "recta2_2" )
graph2legendLn   = graph2Axe.legend (            )

plt.show ( )
