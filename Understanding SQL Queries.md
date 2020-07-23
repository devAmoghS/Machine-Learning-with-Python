### Three SQL Concepts you Must Know to Pass the Data Science Interview

#### Credits: Thanks to Jay Feng for writing this [article](https://www.interviewquery.com/blog-three-sql-questions-you-must-know-to-pass/)

#### 1. Getting the first or last value for each user in a `transactions` table.

`transactions`

| column_name       | data_type     |
--- | --- |
| user_id       | int     |     
| created_at    | datetime|     
| product       | varchar |     

##### Question: Given the user transactions table above, write a query to get the first purchase for each user.

#### Solution:

We want to take a table that looks like this:

 user_id | created_at | product  
 --- | --- | ---  
  123    | 2019-01-01 | apple    
  456    | 2019-01-02 | banana   
  123    | 2019-01-05 | pear    
  456    | 2019-01-10 | apple   
  789    | 2019-01-11 | banana  

and turn it into this

 user_id | created_at | product   
 --- | --- | ---  
 123     | 2019-01-01 | apple      
 456     | 2019-01-02 | banana     
 789     | 2019-01-11 | banana
 
 The solution can be broken into two parts:
 - First make a table of `user_id` and the first purchase (i.e. minimum create date). We can get this by the following query
 
```
SELECT 
  user_id, MIN(created_at) AS min_created_at
FROM 
  transactions
GROUP BY 1
```

- Now all we have to do is join this table back to the original on two columns: `user_id` and `created_at`. <br>
The self join will effectively filter for the first purchase.<br> 
Then all we have to do is grab all of the columns on the left side table.

```
SELECT 
  t.user_id, t.created_at, t.product
FROM 
  transactions AS t
  INNER JOIN (
    SELECT user_id, MIN(created_at) AS min_created_at
    FROM transactions
    GROUP BY 1
  ) AS t1 ON (t.user_id = t1.user_id AND t.created_at = t1.min_created_at)
```

#### 2. Knowing the difference between a LEFT JOIN and INNER JOIN in practice.

 `users`
 
 
| column_name       | data_type     |
--- | --- |   
| id      | int     |     
| name    | varchar |     
| city_id | int     |

`city_id` is `id` in the `cities` table

`cities`               
| column_name       | data_type     |
--- | --- | 
| id      | int     |   
| name    | varchar |       

      
##### Question: Given the `users` and `cities` tables above, write a query to return the list of cities without any users.

This question aims to test the candidate's understanding of the LEFT JOIN and INNER JOIN

##### What is the actual difference between a LEFT JOIN and INNER JOIN?

**INNER JOIN**: returns rows when there is a match in __both tables__.<br> 
**LEFT JOIN**: returns all rows from the left table, __even if there are no matches in the right table__.

#### Solution:

We know that each user in the users table must live in a city given the city_id field.<br> 
However the `cities` table doesn’t have a `user_id` field. <br> 
In which if we run an INNER JOIN between these two tables joined by the city_id in each table, we’ll get all of the cities that have users and __all of the cities without users will be filtered out.__

But what if we run a LEFT JOIN between cities and users?

cities.name  | users.id
--- | --- | 
seattle      | 123
seattle      | 124
portland     | null
san diego    | 534
san diego    | 564

Here we see that since we are keeping all of the values on the LEFT side of the table, since there’s no match on the city of Portland to any users that exist in the database, the city shows up as NULL. <br>
Therefore now all we have to do is run a __WHERE filter to where any value in the users table is NULL.__

```
SELECT 
  cities.name, users.id
FROM 
  cities
  LEFT JOIN users ON users.city_id = cities.id
WHERE 
  users.id IS NULL
```

#### 3. Aggregations with a conditional statement

`transactions`
| column_name       | data_type     |
--- | --- | 
| user_id       | int     |     
| created_at    | datetime|     
| product       | varchar |     

##### Question: Given the same user transactions table as before,write a query to get the total purchases made in the morning versus afternoon/evening (AM vs PM) by day.

We are comparing two groups. Every time we have to compare two groups we must use a GROUP BY

In this case, we need to create a separate column to actually run our GROUP BY on, which in this case, is the difference between AM or PM in the `created_at` field.

```
CASE 
 WHEN HOUR(created_at) > 11 THEN 'PM' 
 ELSE 'AM' 
END AS time_of_day 
```

We can cast the created_at column to the hour and set the new column value time_of_day as AM or PM based on this condition. 

Now we just have to run a GROUP BY on the original `created_at` field truncated to the day AND the new column we created that differentiates each row value. <br> 
The last aggregation will then be the output variable we want which is total purchases by running the COUNT function.

```
SELECT
 DATE_TRUNC('day', created_at) AS date
 ,CASE 
   WHEN HOUR(created_at) > 11 THEN 'PM' 
   ELSE 'AM' 
  END AS time_of_day
 ,COUNT(*)
FROM 
 transactions
GROUP BY 1,2
```
### Bonus Questions

#### 4.Write an SQL query that makes recommendations using the pages that your friends liked. Assume you have two tables: 

`usersAndFriends`
| column_name       | data_type     |
--- | --- | 
| user_id       | int     |     
| friend    | int| 

`usersLikedPages`
| column_name       | data_type     |
--- | --- | 
| user_id       | int     |     
| page_id    | int| 

#### It should not recommend pages you already like.

#### 5.Write an SQL query that shows percentage change month over month in daily active users. Assume you have a table: 

`logins`
| column_name       | data_type     |
--- | --- | 
| user_id       | int     |     
| date    | date| 
