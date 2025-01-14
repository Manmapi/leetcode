-- Write your PostgreSQL query statement below
with unique_position as (
    select lat, lon from Insurance
    group by lat, lon
    having count(pid) = 1
), unique_company as (
    select pid from Insurance i
    join unique_position u
    on i.lat = u.lat and i.lon = u.lon
), same_tiv_15 as (
    select tiv_2015 from Insurance
    group by tiv_2015
    having count(1) > 1
), tiv as (
    select i1.tiv_2015, round(cast(sum(tiv_2016) as numeric), 2) as tiv_2016 from Insurance i1
    join unique_company u
    on i1.pid = u.pid
    join same_tiv_15 s
    on s.tiv_2015 = i1.tiv_2015
    group by i1.tiv_2015
)
-- select * from unique_company
select sum(tiv_2016) as tiv_2016 from tiv

