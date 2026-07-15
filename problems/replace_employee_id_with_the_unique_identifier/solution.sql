# Use LEFT join for the same
SELECT eu.unique_id, e.name from Employees e left join EmployeeUNI eu on e.id=eu.id;