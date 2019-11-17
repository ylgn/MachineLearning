import pandas
import matplotlib.pyplot as plt





df = pandas.read_csv('/Users/ylgn/Documents/MachineLearning/datasets/dataset1.csv', sep = ',')
df.rename( columns={'Unnamed: 0':'n'}, inplace=True )
print(df)

N = df.n
x1 = df.X1
x2 = df.X2
y = df.y
print(df.y[378])
#plt.scatter(x1, x2)

for n in N :
    if (y[n] == 0.0) :
        plt.scatter(x1[n], x2[n],color="red",marker = 'x')
        #plt.plot(x1,x2,color='red')
    else:
        plt.scatter(x1[n], x2[n],color="blue")
plt.show()
