-- Table: frequency(docid, term, count)

--select count(*) from frequency

-- part_a.txt
--select count(*) from frequency where docid = '10398_txt_earn'

-- part_b.txt
--select count(distinct term) from frequency where docid = '10398_txt_earn' and [count] = 1

-- part_c.txt
/*
select count(*)
from
(
    select term from frequency where docid = '10398_txt_earn' and [count] = 1
    union
    select term from frequency where docid = '925_txt_trade' and [count] = 1
) t
*/

-- part_d.txt
/*
select count(*)
from
(
    select distinct docid from frequency
    where (term = 'law' and [count] >= 1)
        or (term = 'legal' and [count] >= 1)
) t
*/

-- part_e.txt
/*
select count(*)
from
(
    select docid, count(docid) as cnt
    from frequency
    group by docid
) t
where cnt > 300
*/

-- part_f.txt
/*
select count(*)
from
(
    select docid from frequency where term = 'transactions' and [count] >= 1
    intersect
    select docid from frequency where term = 'world' and [count] >= 1
) t
*/

-- part_g.txt (matrix.db)
--select * from A
--select * from B
/*
select t.value
from
(
    select A.row_num, B.col_num, sum(A.value * B.value) as value
    from A, B
    where A.col_num = B.row_num
    group by A.row_num, B.col_num
) t
where t.row_num = 2 and t.col_num = 3
*/

-- part_h.txt
/*
select t.Score
from
(
    select A.docid as DocA, B.docid as DocB, sum(A.count * B.count) as Score
    from frequency A, frequency B
    where A.term = B.term
        and A.docid < B.docid
    group by A.docid, B.docid
) t
where t.DocA = '10080_txt_crude' and t.DocB = '17035_txt_earn'
*/

-- part_i.txt
/*
select x.Score
from
(
    with cte as
    (
        select * from frequency
        union
        select 'q' as docid, 'washington' as term, 1 as count
        union
        select 'q' as docid, 'taxes' as term, 1 as count
        union
        select 'q' as docid, 'treasury' as term, 1 as count
    )
    select A.docid as DocA, B.docid as DocB, sum(A.count * B.count) as Score
    from cte A, cte B
    where A.term = B.term
        and A.docid = 'q'
        and B.docid <> 'q'
    group by A.docid, B.docid
) x
order by x.Score desc
limit 1
*/