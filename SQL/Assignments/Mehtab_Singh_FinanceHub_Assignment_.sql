USE FinanceHub;

-- Question 1:
SELECT CONCAT(first_name, '', last_name) AS full_name, credit_score, annual_income, risk_profile FROM CUSTOMERS
WHERE credit_score > 700 AND annual_income>80000
ORDER BY credit_score DESC;


-- Question 2:
SELECT category, SUM(amount) AS total_transaction FROM transactions
WHERE transaction_date >=  '2024-01-01 00:00:00'  AND transaction_date<= '2024-12-31 23:59:59'
GROUP BY category
HAVING total_transaction>5000
ORDER BY total_transaction DESC;


-- Question 3:
SELECT
CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
l.loan_type,
l.loan_amount,
l.outstanding_balance,
l.monthly_emi,
MAX(lp.payment_date) AS last_payment_date
FROM Customers c
INNER JOIN Loans l
ON c.customer_id=l.customer_id
LEFT JOIN LoanPayments lp
ON l.loan_id=lp.loan_id
WHERE l.loan_status='Active'
GROUP BY
c.first_name,
c.last_name,
l.loan_type,
l.loan_amount,
l.outstanding_balance,
l.monthly_emi
ORDER BY l.outstanding_balance DESC;


-- Question 4:
SELECT 
	c.customer_id,
CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
SUM(a.current_balance) AS total_balance,
COUNT(a.account_id) AS number_of_accounts
FROM Customers c
-- Join Accounts table to get account details of customers
INNER JOIN Accounts a
ON c.customer_id= a.customer_id
GROUP BY 
c.customer_id,
c.first_name,
c.last_name
HAVING SUM(a.current_balance)>(
SELECT AVG(total_balance)
FROM (SELECT SUM(current_balance) AS total_balance
FROM Accounts
GROUP BY customer_id)
AS avg_balance)
ORDER BY total_balance DESC;


-- Question 5
SELECT 
CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
SUM(i.current_price) AS total_investment_value,
CASE
	WHEN SUM(i.current_price)> 100000
		THEN 'High Value'
	WHEN SUM(i.current_price) BETWEEN 50000 AND 100000
		THEN 'Medium Value'
	WHEN SUM(i.current_price) BETWEEN 20000 AND 49999
		THEN 'Low Value'
	ELSE 'New Investor'
END AS segment
FROM Customers c
-- Join Investments table to get customer investments
INNER JOIN Investments i 
ON c.customer_id=i.customer_id
GROUP BY
c.customer_id,
c.first_name,
c.last_name
ORDER BY total_investment_value DESC;


-- Question 6:
SELECT 
	c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(a.current_balance) AS total_balance,
    COUNT(a.account_id) AS number_of_accounts
FROM Customers c
INNER JOIN Accounts a
ON c.customer_id=a.customer_id
-- Exclude customers who have taken loans
WHERE NOT EXISTS(
SELECT 1
FROM Loans l
WHERE l.customer_id=c.customer_id)
GROUP BY
c.customer_id,
c.first_name,
c.last_name;

-- Question 7:
SELECT 
	CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    CONCAT(m.first_name," ",m.last_name) AS manager_name,
    e.department
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id=m.employee_id;


-- Question 8:
SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    cc.card_type,
    cc.credit_limit,
    cc.current_balance,
	-- Calculate utilisation percentage
    (cc.current_balance/cc.credit_limit)*100 AS utilisation_percentage,
    -- Rank cards within each card type based on utilisation percentage
    RANK() OVER (
		PARTITION BY cc.card_type
        ORDER BY (cc.current_balance/cc.credit_limit)*100 DESC
        )AS card_rank
FROM CreditCards cc
INNER JOIN Customers c
ON cc.customer_id=c.customer_id;


-- Question 9:
SELECT
	 MONTH(transaction_date) AS month,
     COUNT(transaction_id) AS number_of_transactions,
     SUM(amount) AS total_amount,
     AVG(amount) AS average_amount
FROM Transactions
-- Include only transactions from 2024
WHERE YEAR(transaction_date)=2024
GROUP BY month(transaction_date)
-- Sort months chronologically
ORDER BY month;


-- Question 10:
SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(ct.amount) AS total_travel_spending,
    COUNT(ct.card_transaction_id) AS number_of_travel_transaction,
    SUM(ct.reward_points_earned) AS total_reward_points
FROM CardTransactions ct
-- Join CreditCards table to connect transactions with customers
INNER JOIN CreditCards cc
ON ct.card_id=cc.card_id
-- Join Customers table to get customer details
INNER JOIN Customers c
ON cc.customer_id=c.customer_id
-- Include only travel category transactions
WHERE ct.merchant_category='Travel'
GROUP BY 
c.customer_id,
c.first_name,
c.last_name
ORDER BY total_travel_spending DESC
LIMIT 5;


-- Question 11:
SELECT 
	a.account_number,
    a.account_type,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    a.current_balance
FROM Accounts a
-- Join Customers table
INNER JOIN Customers c
ON a.customer_id=c.customer_id
-- Check for qualifying deposit transactions
WHERE EXISTS(
	SELECT 1
    FROM Transactions t
    WHERE t.account_id=a.account_id
    AND t.transaction_type='Deposit'
    AND t.amount>5000
    AND t.transaction_date BETWEEN '2024-01-15' AND '2024-03-15'
);


-- Question 12:
SELECT 
	'Account' AS product_type,
    account_number AS product_identifier,
    current_balance AS current_value
FROM Accounts
WHERE customer_id = 1004
UNION
SELECT
	'Loan' AS product_type,
    loan_id AS product_identifier,
    Outstanding_balance AS current_value
FROM Loans
WHERE customer_id=1004
UNION
SELECT
	'Credit Card' AS product_type,
    card_number AS product_identifier,
    current_balance AS current_value
FROM CreditCards
WHERE customer_id=1004
UNION
SELECT
	'Investment' AS product_type,
    investment_type AS product_identifier,
    current_price AS current_value
FROM Investments
WHERE customer_id=1004;


-- Question 13:
SELECT
	transaction_date,
    transaction_type,
    amount,
    -- Calculate running balance
    SUM(
		CASE
			WHEN transaction_type IN ('Deposit', 'Transfer in')
				THEN amount
			ELSE -amount
		END)
        OVER (
        ORDER BY transaction_date) AS running_date
FROM Transactions
WHERE account_id=5001
AND YEAR(transaction_date)=2024
ORDER BY transaction_date;
            

-- Question 14:
SELECT
	l.loan_type,
     -- Count total number of loans
    COUNT(DISTINCT l.loan_id) AS number_of_loans,
	-- Calculate total loan amount disbursed
    SUM(l.loan_amount) as total_disbursed_amount,
    -- Calculate total outstanding balance    
    SUM(l.outstanding_balance) AS total_outstanding_balance,
    -- Calculate average interest rate
    AVG(l.interest_rate) AS average_interest_rate,
    -- Calculate payment completion percentage
    ROUND(
		(SUM(lp.amount_paid)/SUM(l.loan_amount))*100,
        2) AS payment_completion_percentage
FROM loans l
-- Join LoanPayments table to get payment details
LEFT JOIN LoanPayments lp
ON l.loan_id=lp.loan_id
GROUP BY l.loan_type;


-- Question 15:
SELECT
	b.branch_name,
    COUNT(DISTINCT e.employee_id) AS total_employees,
    COUNT(DISTINCT a.customer_id) AS total_customers,
    ROUND(
    (COUNT(DISTINCT a.customer_id)*100)/ (SELECT COUNT(*) FROM Customers),
    2)
	AS customer_percentage
FROM Branches b
-- Join Employees table
LEFT JOIN Employees e
ON b.branch_id=e.branch_id
-- Join Accounts table using branch code
LEFT JOIN Accounts a
on b.branch_code=a.branch_code
GROUP BY 
	b.branch_id,
    b.branch_name;


-- Question 16
SELECT 
	CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(t.transaction_id) AS number_of_transactions,
    SUM(t.amount) AS total_transaction_amount,
    AVG(t.amount) AS average_transaction_amount
FROM Transactions t
-- Join Accounts table
INNER JOIN Accounts a
ON t.account_id=a.account_id
-- Join Customers table
INNER JOIN Customers c
ON a.customer_id=c.customer_id
GROUP BY 
	c.customer_id,
    c.first_name,
    c.last_name
-- Filter customers based on conditions
HAVING 
	COUNT(t.transaction_id)>5
    AND AVG(t.amount)>500;
    

-- Question 17
WITH MonthlyDisbursement AS (
    SELECT 
        DATE_FORMAT(disbursement_date, '%Y-%m') AS month,
        SUM(loan_amount) AS total_disbursed_amount
    FROM Loans
    -- Group data month-wise
    GROUP BY DATE_FORMAT(disbursement_date, '%Y-%m')
)
-- Compare each month with previous month
SELECT 
    month,
    total_disbursed_amount,
    LAG(total_disbursed_amount) OVER (
        ORDER BY month
    ) AS previous_month_amount,
    ROUND(
        (
            (
                total_disbursed_amount
                - LAG(total_disbursed_amount) OVER (ORDER BY month)
            )
            /
            LAG(total_disbursed_amount) OVER (ORDER BY month)
        ) * 100,
        2
    ) AS percentage_change

FROM MonthlyDisbursement
ORDER BY month;


-- Question 18
SELECT
	CONCAT(c.first_name, ' ', last_name) AS customer_name,
    COUNT(DISTINCT fa.alert_id) AS number_of_fraud_alerts,
    SUM(
		CASE
			WHEN fa.is_fraud_confirmed= TRUE THEN 1
            ELSE 0
            END
            ) AS confirmed_fraud_count,
	-- Calculate maximum credit card utilisation percentage
	MAX(
		(cc.current_balance/cc.credit_limit)* 100
        ) AS max_credit_card_utilisation,
	-- Determine overall risk level
	CASE 
		WHEN 
			SUM(
				CASE 
					WHEN fa.is_fraud_confirmed=TRUE THEN 1
                    ELSE 0
                    END)>0
                    OR 
                    MAX(
                    (cc.current_balance/ cc.credit_limit)*100
                    ) > 80
			THEN 'High'
            WHEN COUNT(DISTINCT fa.alert_id)>3
            THEN 'Medium'
            ELSE 'Low'
		END AS overall_risk_level
FROM Customers c
-- Join FraudAlerts table
LEFT JOIN FraudAlerts fa
ON c.customer_id=fa.customer_id
-- Join CreditCards table
LEFT JOIN CreditCards cc
ON c.customer_id=cc.customer_id
GROUP BY
	c.customer_id,
    c.first_name,
    c.last_name
-- Show only customers meeting risk conditions
HAVING
	COUNT(DISTINCT fa.alert_id)>3
    OR
    SUM(
		CASE
			WHEN fa.is_fraud_confirmed= TRUE THEN 1
            ELSE 0
		END)>0
        OR
        MAX((cc.current_balance/cc.credit_limit)*100
        )>80;


-- Question 19
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    c.risk_profile
FROM Customers c
-- Customer must have at least one credit card
WHERE EXISTS (
    SELECT 1
    FROM CreditCards cc    
    WHERE cc.customer_id = c.customer_id
)
-- Customer must have at least one active loan
AND EXISTS (
    SELECT 1
    FROM Loans l
    WHERE l.customer_id = c.customer_id
    AND l.loan_status = 'Active'
)
-- Customer must NOT have any investments
AND NOT EXISTS (
    SELECT 1
    FROM Investments i
    WHERE i.customer_id = c.customer_id
);


-- Question 20
SELECT 
    transaction_id,
    account_id,
    transaction_type,
    transaction_date,
    amount,
    balance_after
FROM Transactions
WHERE account_id = 5001
-- Date range filter
AND transaction_date BETWEEN '2024-01-01' AND '2024-03-31'
-- Amount condition
AND amount > 1000
-- Sort chronologically
ORDER BY transaction_date;
-- for account_id, transaction_date, and amount.
CREATE INDEX idx_transactions_account_date_amount
ON Transactions(account_id, transaction_date, amount);


-- Question 21
WITH RECURSIVE EmployeeHierarchy AS(
	SELECT
		e.employee_id,
        CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
        -- Manager name is NULL for top-level employees
        CAST(NULL AS CHAR(100)) AS manager_name,
        e.department,
        1 AS level
	FROM Employees e
    WHERE e.manager_id IS NULL
    UNION ALL
    SELECT
		emp.employee_id,
        CONCAT(emp.first_name, ' ', emp.last_name) AS employee_name,
        eh.employee_name as manager_name,
        emp.department,
        -- Increase hierarchy level
        eh.level + 1 AS level
	FROM Employees emp
    INNER JOIN EmployeeHierarchy eh
    ON emp.manager_id=eh.employee_id
    )
-- Display hierarchy report
SELECT 
	employee_name,
    manager_name,
    level, 
    department
FROM EmployeeHierarchy;


-- Question 22
SELECT 
    cb.customer_name,
    cb.risk_profile,
    cb.total_balance,
    -- Percentile rank within each risk profile
    PERCENT_RANK() OVER (
        PARTITION BY cb.risk_profile
        ORDER BY cb.total_balance
    ) AS percentile_rank
FROM (
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        c.risk_profile,
        SUM(a.current_balance) AS total_balance
    FROM Customers c
    INNER JOIN Accounts a
    ON c.customer_id = a.customer_id
    GROUP BY 
        c.customer_id,
        c.first_name,
        c.last_name,
        c.risk_profile
) AS cb;


-- Question 23
SELECT
	customer_id,
    loan_type,
    monthly_emi,
    -- Total EMI obligation for the customer
    SUM(monthly_emi) OVER (
		PARTITION BY customer_id)
        AS total_momthly_emi_obligation
FROM Loans
WHERE customer_id=1004
AND loan_status='Active';


-- Question 24
SELECT 
    'Incorrect Transaction Balance' AS issue_type,
    transaction_id AS affected_record_id,
    CONCAT(
        'Expected Balance: ',
        expected_balance,
        ', Actual Balance: ',
        balance_after
    ) AS details
FROM (
    SELECT 
        transaction_id,
        account_id,
        transaction_type,
        amount,
        balance_after,
        -- Calculate expected balance
        LAG(balance_after) OVER (
            PARTITION BY account_id
            ORDER BY transaction_date
        )
        +
        CASE
            WHEN transaction_type IN ('Deposit', 'Transfer In')
                THEN amount
            ELSE -amount
        END AS expected_balance
    FROM Transactions
) t
WHERE expected_balance IS NOT NULL
AND balance_after <> expected_balance;


-- Question 25
-- CTE 1: Customers by Risk Profile
WITH CustomerRiskProfile AS (
    SELECT 
        risk_profile,
        COUNT(customer_id) AS total_customers
    FROM Customers
    GROUP BY risk_profile
),
-- CTE 2: Monthly Transaction Summary
MonthlyTransactionFlow AS (
    SELECT 
        -- Total deposits
        SUM(
            CASE
                WHEN transaction_type = 'Deposit'
                THEN amount
                ELSE 0
            END
        ) AS total_deposits,
        -- Total withdrawals
        SUM(
            CASE
                WHEN transaction_type = 'Withdrawal'
                THEN amount
                ELSE 0
            END
        ) AS total_withdrawals,
        -- Net flow
        SUM(
            CASE
                WHEN transaction_type = 'Deposit'
                THEN amount
                ELSE -amount
            END
        ) AS net_flow
    FROM Transactions
    -- Dataset month filter
    WHERE MONTH(transaction_date) = 3
    AND YEAR(transaction_date) = 2024
),
-- CTE 3: Average Credit Card Utilisation
CardUtilisation AS (
    SELECT 
        card_type,
        AVG(
            (current_balance / credit_limit) * 100
        ) AS average_utilisation_percentage
    FROM CreditCards
    GROUP BY card_type
),
-- CTE 4: Loan Portfolio Health
LoanHealth AS (
    SELECT 
        ROUND(
            (
                SUM(
                    CASE
                        WHEN payment_status = 'Paid'
                        THEN 1
                        ELSE 0
                    END
                ) * 100.0
            )
            /
            COUNT(payment_id),
            2
        ) AS on_time_payment_percentage
    FROM LoanPayments
),
-- CTE 5: Top 3 Transaction Categories
TopTransactionCategories AS (
    SELECT 
        category,
        SUM(amount) AS total_volume
    FROM Transactions
    GROUP BY category
    ORDER BY total_volume DESC
    LIMIT 3
)
-- Final Dashboard Output
SELECT 
    -- Customer risk profile summary
    crp.risk_profile,
    crp.total_customers,
    -- Monthly transaction summary
    mtf.total_deposits,
    mtf.total_withdrawals,
    mtf.net_flow,
    -- Credit card utilisation
    cu.card_type,
    cu.average_utilisation_percentage,
    -- Loan portfolio health
    lh.on_time_payment_percentage,
    -- Top transaction categories
    ttc.category,
    ttc.total_volume
FROM CustomerRiskProfile crp
CROSS JOIN MonthlyTransactionFlow mtf
CROSS JOIN LoanHealth lh
LEFT JOIN CardUtilisation cu
ON 1 = 1
LEFT JOIN TopTransactionCategories ttc
ON 1 = 1;