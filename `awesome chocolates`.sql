select * from sales;

select Saledate, Amount, Customers from sales;
select amount,customers, geoid from sales;

Select Saledate, Amount, Boxes, Amount/Boxes as 'Amount per box' from sales;

select * from sales 
where amount > 10000
order by amount desc;


select saledate, amount from sales
where amount > 10000 and year(saledate) = 2022
order by amount desc;

select * from sales 
where boxes between 0 and 50;

select saledate, amount, boxes, weekday(saledate) as 'day of week'
from sales
where weekday(saledate)=4;

select * from people
where team in ('delish' , 'jucies');

select * from people
where salesperson like '%B%';

select saledate, amount,
		case    when amount < 1000 then 'under 1k'
				when amount< 5000 then 'under 5k'
				when amount < 10000 then 'under 10k'
			else  '10k or more'
			end as 'amount category'
from sales;



select s.saledate, s.amount, p.Salesperson, pr.product, p.Team
from sales s
join people p on p.SPID=s.SPID
join products pr on pr.pid=s.pid;


select s.saledate, s.amount, p.Salesperson, pr.product, p.Team
from sales s
join people p on p.SPID=s.SPID
join products pr on pr.pid=s.pid
join geo g on g.GeoID = s.GeoID
where s.amount < 500
and g.Geo in ('New Zealand','India')
order by SaleDate;


select g.geo, sum(amount),avg(Amount),sum(boxes)
from sales s
join geo g on s.GeoID = g.GeoID
group by g.geo;


select pr.category, p.team, sum(boxes), sum(Amount)
from sales s
join people p on p.spid = s.spid
join products pr on pr.pid = s.pid
where p.Team <> ''
group by pr.category, p.team
order by pr.category, p.team;


select pr.product , sum(s.Amount) as 'total amount'
from sales s 
join products pr on pr.pid = s.pid 
group by pr.Product
order by 'total amount' desc
limit 10;