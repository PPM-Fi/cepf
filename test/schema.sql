PRAGMA foreign_keys = ON; -- Enforce foreign key contraints for SQLite3

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS officer (
    id INT NOT NULL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE IF NOT EXISTS community (
    id INT NOT NULL PRIMARY KEY,
    type INT,
    name TEXT,
    location TEXT,
    communication_channel TEXT,
    phone_number TEXT,
    email TEXT,

    -- Engagement period example: Month
    -- Engagement multiplier example: 3
    -- Encodes values such as "Every 3 Months"
    engagement_period INT,
    engagement_period_multiplier INT,
    FOREIGN KEY (engagement_period) REFERENCES engagement_period(id),

    FOREIGN KEY (type) REFERENCES community_type(id)
);

CREATE TABLE IF NOT EXISTS community_type (
    id INT NOT NULL PRIMARY KEY,
    name TEXT,
    class TEXT,
    FOREIGN KEY (class) REFERENCES community_class(name)
);

CREATE TABLE IF NOT EXISTS community_class (
    id INT NOT NULL PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS engagement_period (
    id INT NOT NULL PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS appointment (
    id INT NOT NULL PRIMARY KEY,
    community INT,
    feedback INT,
    FOREIGN KEY (community) REFERENCES community(id),
    FOREIGN KEY (feedback) REFERENCES appointment_feedback(id)
);

CREATE TABLE IF NOT EXISTS appointment_feedback (
    id INT NOT NULL PRIMARY KEY,
    effectiveness INT, -- Rating appointments on a 1 to 5 rating system for effectiveness
    notes TEXT
);

-- Association table for the "appointment - officer" many-to-many relationship
CREATE TABLE IF NOT EXISTS appointment_officer (
    appointment INT,
    officer INT,
    FOREIGN KEY (appointment) REFERENCES appointment(id),
    FOREIGN KEY (officer) REFERENCES officer(id),
    PRIMARY KEY (appointment, officer)
);

COMMIT;
