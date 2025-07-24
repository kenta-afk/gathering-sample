DROP TABLE IF EXISTS todos;


CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO todos (task, completed) VALUES
  ('Sample Todo', FALSE),
  ('Another Todo', TRUE);