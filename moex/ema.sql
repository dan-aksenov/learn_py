with recursive t as (
    select dt, 
           0.5 as alpha,
           row_number() over (),
           raw_fi
    from stock_w_ma where ticker = 'SBER'        
),
ema as (
    select *, raw_fi as sales_ema from t 
    where row_number = 1
    union all
    select t2.dt, 
           t2.alpha, 
           t2.row_number, 
           t2.raw_fi, 
           t2.alpha * t2.raw_fi + (1.0 - t2.alpha) * ema.raw_fi as sales_ema
    from ema
    join t t2 on ema.row_number = t2.row_number - 1
)
select dt, raw_fi, sales_ema
from ema;	