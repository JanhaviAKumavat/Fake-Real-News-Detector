-- ==========================================
-- CREATE DATABASE
-- ==========================================

CREATE DATABASE IF NOT EXISTS fake_news_detector;


USE fake_news_detector;




-- ==========================================
-- USERS TABLE
-- ==========================================


CREATE TABLE IF NOT EXISTS users
(

    id INT AUTO_INCREMENT PRIMARY KEY,


    full_name VARCHAR(100) NOT NULL,


    email VARCHAR(150) UNIQUE NOT NULL,


    password VARCHAR(255) NOT NULL,


    role VARCHAR(20) DEFAULT 'user',


    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);






-- ==========================================
-- PREDICTION HISTORY TABLE
-- ==========================================


CREATE TABLE IF NOT EXISTS prediction_history
(

    id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,


    news_text TEXT NOT NULL,


    prediction VARCHAR(50) NOT NULL,


    confidence FLOAT NOT NULL,


    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



    FOREIGN KEY(user_id)

    REFERENCES users(id)

    ON DELETE CASCADE

);







-- ==========================================
-- ADMIN USER
-- ==========================================

-- Default admin credentials:
-- Email: admin@fakenews.com
-- Password: admin123
--
-- Password should be stored as a hashed value
-- from Flask generate_password_hash()
--
-- Insert your hashed password here.



INSERT INTO users
(
    full_name,
    email,
    password,
    role
)

VALUES
(
'Website Admin',
'admin@fakenews.com',
'admin123',
'admin'
);

ON DUPLICATE KEY UPDATE

email=email;
