# Pyber Ride Share Analysis 55555555

## Overview
In this analysis our challenge is to summarize the ride sharing data by city type. We'll then showcase our analysis via visualization using multiple-line plot presenting total weekly fares for each city-type.

## Analysis Results
![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%205%20Challenge/Analysis/Pyber%20Summary%20DataFrame.png)

I.) [**The Analysis Summary:**](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%205%20Challenge/Analysis/Pyber%20Summary%20DataFrame.png) 

Refer above the summary of ride sharing data by each city type. 
1. **The Urban cities**, 
   1. as expected, has more riders leading to higher demand for drivers. However, more drivers means competition, leading to cheaper/competitive rides. The cheaper rides means lower average fare per ride and lower average fare per driver. 
   1. The total fare for these rides is higher bringing Pyber more profitability. With cheaper rides, the demands as well as the drivers will increase with time, helping Pyber capture the reasonable market share and speedy growth. This is apparent fromt the summary below. 

1. Whereas at the other extreme, **Rural cities**, 
   1. has very low demad for rides, so, there are fewer drivers. On an average, these rides are lot more expensive and drivers make more money per ride but they do not get too many rides in a day.
   1. The total fares are very low due to the rides being so expensive.

1. **Suburban cities**, 
   1. lies well between Urban and Rural model. This segment has reasonable demad for rides. So, there are lot more drivers than Rural cities. The general outlook of people in suburban areas is usually influenced by Urban cities (due to the fact that people work in Urban cities and live in Suburbs for a better lifestyle). On an average, these rides are affordable and drivers also make reasonable money per ride with decent number of rides in a day.
   1. The total fares are about half of the Urban cities. This segment suggests a high growth potential for Pyber.

##
![](https://raw.githubusercontent.com/neerajain9/RDS-BootCamp/master/Homework/Module%205%20Challenge/Analysis/PyBer_fare_by_city.png)

II.) [**The Total Weekly Fare by City-Type:**](https://github.com/neerajain9/RDS-BootCamp/blob/master/Homework/Module%205%20Challenge/Analysis/PyBer_fare_by_city.png) 

Refer the above line chart. The visualization for the weekly fares is in line with our Analysis Summary above.
1. For **Urban cities**, we notice some growth since January ($1661) to April ($2470) peaking during the last week of February and first week of March. However, there was samll dip at the starting of month March. there has been some peaks and vallyes and then started to flatten down toward the end of April. This segment showed some growth and maintained (at $2200) that to about 85%-90% of the peak patterns. Overall, this segment grew about 34% in revenues during these 4 months.
1. **Suburban Cities** at the other hand suggests 88% growth in overall revenues during this period. Our initial hypothesis in identifying this segment to be potential high growth segment seems to well established with this visualization.
1. **Urban Cities** shows some growth but at a very very low (to negligible) rate.


## Summary
To summarize our efforts and data visualization, it seems Pyber should focus on Suburban City segment as it suggest high growth patterns. 

The Urban segment could do better as well but there seems to be other competitors bringing in more and more competition affecting our bottom line growth rate. Driver's discounts could be introduced to steal away this market share but it would start a price-war amd eventually hurt all the service providers including Pyber.

At the other hand Rural segment could have high potiential but with this limited data it is hard to infer that. Perhaps, offering some discounts to drivers would help lower the cost of average ride and may encourage people to use Pyber more frequent. This being said, we still think that the segment would need some serious effort to get to that level and our hypothesis can only be proved by running some tests and collection more data for further analysis.