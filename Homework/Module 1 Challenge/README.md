# Kickstarting with Excel

## Overview of Project
Louise has collected reasonable amount of historical data about her fundraising activity across the globe. In this project she is trying to identify how different campaigns fared in relation to their launch dates and their funding goals.

### Purpose
To analyse the outcomes for "Theater/Plays" and steer up the fundraising campaigns to make her goals realistic, pledgings more affective, and focus the efforts to successful campaigns or how to convert failed campaign into successful ones.

## Analysis and Challenges
The real challenge in this activity is to setup appropriate funding goals that could be tied up to more realistic outcomes. Some more information about the other captured data elements would be helpful to draw out some solid and meaningful conclusions.

### Analysis of Outcomes Based on Launch Date

![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%201%20Challenge/Theater_Outcomes_vs_Launch.png)


First observation in this analysis is that the campaigns took first four month (Jan-Apr) since 2009 till 2017, to build up the number of successful outcomes which peaked in the month of May. But for some reasons it started to decline thereafter for reat of the year except a small increase in the month of October. In the month of December the outcomes had been the lowest, may be beacuse of the holiday season people were more involved with friends 'n family. But during this time of the year people are more generous in pledging so why did the number of outcomes dropped this low; there gotta be other reasons that we are not certain about.

Second obeservation is about the failed campaigns. It seems the failed outcomes had a similar pattern as of the successful ones. To conclude this observation, if we combine the two outcomes the overall patter of the outcomes doesn't change. We must identify what really happend in the month of May to see that spike and then the reasons why it started depleting.

Next, there had been 0% t0 8% cancellations. The highest in the month of Jan. So, it is assumed, that they realized issued in these campaigns and cancelled them before implementing. Although, blurb section suggest some possible reasons for the cancellation (only guesses though) but there could be multiple other reasons too.

Finally, the good news is that there had been more than 50% campaigns that were successful and these outcomes were as high as 68%.

### Analysis of Outcomes Based on Goals
![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%201%20Challenge/Outcomes_vs_Goals.png)
Firstly, based on goals established there were no "Plays" cancellations. So, it seems the goals were setup appropriatly.

Next, there were lot more successes with goals under $15,000. Between $15,000 and $20,000 the success to failure ratio was 50-50 which declined with an exception of the goal range from $35,000 and $45,000 (66.67: 33.33).

Next, the campaigns with goals over $45,000 was a disaster. The lower goals performed better statistically.

### Challenges and Difficulties Encountered
I encountered a minor hickup. To implement the range of goals in the same formula. I found a solution i.e. to use SUMPRODUCT function bu then it disturbed the rest of the formaul. So, to implement the goal range I used the selection twice that I am not very comfortable with. Other than this I did not encounter any major technical challenges and difficulties in specific to run these analysis.

From business standpoint, I wasn't sure if I should have looked at other data elements to draw out my conclusions. However, I did use some partially from this exercise's perspective. I am sure I would not and should miss any data element to draw out analysis in the real world.

## Results

**- What are two conclusions you can draw about the Outcomes based on Launch Date?**

1. We must identify the reasons for high points in May so that we could use those to deploy with other campaigns. What affects the downside of the outcomes especially in the month of December so that we could formulate some strategy to bring up these.

2. We should also identify the reasons for the failed outcomes in order to convert them into successes strategically.

**- What can you conclude about the Outcomes based on Goals?**

1. The smaller goals were achieved easily and were more succesful. Goals with less than $5,000 were 75% succesful than failures.

2. Setting up goals with $20,000 and higher isn't a good recomendation.

3. There had been couple of outliers in the gols ranging between $35,000 and $45,000. We are not sure what happend there. But certainly there weren't many campaigns in this range (only 9 in all). 

**- What are some limitations of this dataset?**

*   I wish there was more information about the captured data elements. Bringing those into the analysis would have been more helpful to draw out meaningful conclusions.

**- What are some other possible tables and/or graphs that we could create?**
* We could create Pivot char/table to compare outcomes by Parent Category
* We could create Pivot char/table to compare outcomes by Parent Category and Subcategory
* We could do some Descriptive Statistics based on succesful, failed, cancelled outcomes.
* We could create box & whisker's chart to figure out outliers and proposed goal ranges visually
* I am sure there's a lot more other analysis can be carried out based on what are we looking to find out and for what purpose. The analysis is based on the business requirements and we can then focus our approach appropriately.