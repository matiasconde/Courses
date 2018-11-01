## 2. Bar Plots ##

Exp_ordinal=wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]]

Exp_ordinal.plot.bar()


## 3. Horizontal Bar Plots ##

Exp_ordinal= wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]]
Exp_ordinal.plot.barh(title="Number of players in WNBA by level of experience")

## 4. Pie Charts ##

Exp_ordinal = wnba["Exp_ordinal"].value_counts()

Exp_ordinal.plot.pie()

## 5. Customizing a Pie Chart ##

Exp_ordinal = wnba["Exp_ordinal"].value_counts()

Exp_ordinal.plot.pie(figsize=(6,6),autopct="%.2f%%",title="Percentage of players in WNBA by level of experience")
plt.ylabel("")

## 6. Histograms ##

wnba["PTS"].plot.hist()

## 7. The Statistics Behind Histograms ##

from numpy import arange

a = wnba["Games Played"].describe()

wnba["Games Played"].plot.hist()


## 9. Binning for Histograms ##

from numpy import arange
wnba["Games Played"].plot.hist(range=(0,32), bins=8,title="The distribution of players by games played",xticks=arange(0,36,4),label="Games Played")
plt.xlabel('Games played')

## 10. Skewed Distributions ##

wnba["AST"].plot.hist()
wnba["FT%"].plot.hist()

assists_distro = "right skewed"
ft_percent_distro = "left skewed"

## 11. Symmetrical Distributions ##

wnba["Age"].plot.hist(color="r")
plt.xlabel("Age")
plt.show() # RED
wnba["Height"].plot.hist(color="y") # YELLOW
plt.xlabel("Height")
plt.show()
wnba["MIN"].plot.hist(color="b") # BLUE
plt.xlabel("MIN")
plt.show()

normal_distribution = "Height"