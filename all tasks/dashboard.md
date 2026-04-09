**Page 1 — Overview Dashboard**

Purpose: Provide a high-level summary of screen usage behavior.



1\. Age Band Distribution

Tool: Clustered Bar Chart

&nbsp;	Fields

&nbsp;	Axis - Age\_Band

&nbsp;	Values - Count of Index (or Count of Age)



Why: Shows how users are distributed across age groups.



2\. Primary Device Distribution

Tool: Donut Chart



&nbsp;	Fields

&nbsp;	Legend - Primary\_Device

&nbsp;	Values - Count of Index



Why: Shows proportion of device usage.



3\. Screen Time Level Distribution

Tool: Clustered Bar Chart



&nbsp;	Fields

&nbsp;	Axis → Screen\_Time\_Level

&nbsp;	Values → Count of Index



Why: Displays number of users with Low / Medium / High screen time.



4\. Urban vs Rural Users

Tool: Pie Chart



&nbsp;	Fields

&nbsp;	Legend → Urban\_or\_Rural

&nbsp;	Values → Count of Index



Why: Shows geographic distribution of users.



Filters (Slicers)

Tool: Slicer

Fields used:

Age\_Band

Gender

Device\_Type

Urban\_or\_Rural



Why: Allows users to filter the dashboard by demographic segments.



**Page 2 — Device \& Usage Behavior**

Purpose: Understand how device types influence screen usage.



1\. Average Screen Time by Device Type

Tool: Clustered Bar Chart



&nbsp;	Fields

&nbsp;	Axis → Device\_Type

&nbsp;	Values → Avg of Avg\_Daily\_Screen\_Time\_hr



Why: Shows which device type leads to higher screen usage.



2\. Device Type by Age Band

Tool: Stacked Bar Chart



&nbsp;	Fields

&nbsp;	Axis → Age\_Band

&nbsp;	Legend → Device\_Type

&nbsp;	Values → Count of Index



Why: Shows device preference across age groups.



3\. Usage Type Distribution

Tool: Donut Chart



&nbsp;	Fields

&nbsp;	Legend → Usage\_Type

&nbsp;	Values → Count of Index



Why: Displays ratio of Educational vs Recreational usage.



4\. Educational vs Recreational Ratio by Device

Tool: Clustered Bar Chart



&nbsp;	Fields

&nbsp;	Axis → Primary\_Device

&nbsp;	Values → Average of Educational\_to\_Recreational\_Ratio



Why: Shows which devices are used more for education or entertainment.



**Page 3 — Weekday vs Weekend Behavior**

Purpose: Analyze habit patterns and time-based usage differences.



1\. Average Screen Time: Weekday vs Weekend

Tool: Clustered Bar Chart



&nbsp;	Fields

&nbsp;	Axis → Day\_Type

&nbsp;	Values → Average of Avg\_Daily\_Screen\_Time\_hr



Why: Shows differences between weekday and weekend screen usage.



2\. Device Usage by Day Type

Tool: Stacked Bar Chart



&nbsp;	Fields

&nbsp;	Axis → Day\_Type

&nbsp;	Legend → Primary\_Device

&nbsp;	Values → Count of Index



Why: Shows which devices are used more on weekends vs weekdays.



3\. Screen Time Level by Day Type

Tool: Stacked Column Chart



&nbsp;	Fields

&nbsp;	Axis → Day\_Type

&nbsp;	Legend → Screen\_Time\_Level

&nbsp;	Values → Count of Index



Why: Shows distribution of low, medium, and high screen usage by day.



4\. Usage Type by Day Type

Tool: Stacked Column Chart



&nbsp;	Fields

&nbsp;	Axis → Day\_Type

&nbsp;	Legend → Usage\_Type

&nbsp;	Values → Count of Index



Why:	Shows whether weekends have more recreational usage.



**Page 4 — Cohort \& Segment Analysis**

Purpose: Identify high-risk user cohorts.



1\. Age Band × Device Type Heatmap

Tool: Matrix Visual 



&nbsp;	Fields

&nbsp;	Rows → Age\_Band

&nbsp;	Columns → Device\_Type

&nbsp;	Values → Count of Index



Why: Identifies which age groups use which device types the most.



2\. Average Screen Time by Age Band \& Device

Tool: Clustered Column Chart



&nbsp;	Fields

&nbsp;	Axis → Age\_Band

&nbsp;	Legend → Device\_Type

&nbsp;	Values → Average of Avg\_Daily\_Screen\_Time\_hr



Why: Shows high-usage cohorts.



3\. Engagement Risk Level by Age Band

Tool: Stacked Bar Chart



&nbsp;	Fields

&nbsp;	Axis → Age\_Band

&nbsp;	Legend → Engagement\_Risk\_Level

&nbsp;	Values → Count of Index



Why: Shows which age groups fall into higher engagement risk.



4\. Urban vs Rural Health Impact Heatmap



Tool: Matrix Visual



Fields

Rows → Urban\_or\_Rural

Columns → Health\_Impacts

Values → Count of Index



Why: Shows health impacts by location segments.



**Page 5 — Health Impact \& Risk Analysis**

Purpose: Understand health consequences of screen exposure.



1\. Health Impacts Distribution

Tool: Bar Chart



Fields

Axis → Health\_Impacts

Values → Count of Index



Why: Shows most common health issues related to screen usage.



2\. Health Impact by Screen Time Level

Tool: Stacked Bar Chart



Fields

Axis → Screen\_Time\_Level

Legend → Health\_Impacts

Values → Count of Index



Why: Shows relationship between screen exposure and health problems.



3\. Engagement Risk Level Distribution

Tool: Donut Chart



Fields

Legend → Engagement\_Risk\_Level

Values → Count of Index



Why: Displays proportion of users in each engagement risk category.



4\. Exceeded Recommended Limit by Age Band

Tool: Stacked Column Chart



Fields

Axis → Age\_Band

Legend → Exceeded\_Recommended\_Limit

Values → Count of Index



Why: Shows which age groups exceed recommended screen limits.







Power BI tools used:



Clustered Bar Chart



Stacked Bar Chart



Stacked Column Chart



Pie Chart



Donut Chart



Matrix (Heatmap)



Slicer (Filters)

