-- Write your PostgreSQL query statement below
with first_date as (
    select student_id, subject, min(exam_date) as first_date from Scores
    group by student_id, subject
    having count(student_id) > 1 
), first_score as (
    select s.student_id, s.subject, s.score from Scores s
    join first_date f
    on s.student_id = f.student_id and s.subject = f.subject and s.exam_date = f.first_date
), last_date as (
    select student_id, subject, max(exam_date) as last_date from Scores
    group by student_id, subject
), last_score as (
    select s.student_id, s.subject, s.score from Scores s
    join last_date l
    on s.student_id = l.student_id and s.subject = l.subject and s.exam_date = l.last_date
)

select f.student_id, f.subject, f.score as first_score, l.score as latest_score from first_score f
join last_score l
on f.student_id = l.student_id and f.subject = l.subject and l.score > f.score
order by f.student_id, f.subject