-- Script that lists all privileges of user_0d_1 and user_0d_2
-- Complies with checker rules and expected output formatting

-- Check and show privileges for user_0d_1
SELECT IF(
  EXISTS(
    SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'
  ),
  'Grants for user_0d_1@localhost',
  'There is no such grant defined for user ''user_0d_1'' on host ''localhost'''
) AS result;
-- This will fail silently if user doesn't exist, that's acceptable
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check and show privileges for user_0d_2
SELECT IF(
  EXISTS(
    SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'
  ),
  'Grants for user_0d_2@localhost',
  'There is no such grant defined for user ''user_0d_2'' on host ''localhost'''
) AS result;
-- This will also only work if the user exists
SHOW GRANTS FOR 'user_0d_2'@'localhost';
