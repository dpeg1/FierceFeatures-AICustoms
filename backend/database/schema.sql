CREATE TABLE lash_styles (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    face_shape TEXT NOT NULL,
    description TEXT
);

INSERT INTO lash_styles (name, face_shape, description) VALUES
('Doll Eye', 'Round', 'Opens up the eyes, great for round face shapes'),
('Cat Eye', 'Oval', 'Lifts the outer corners, ideal for oval faces'),
('Natural Volume', 'Square', 'Softens angles, suitable for square faces'),
('Wispy', 'Heart', 'Adds texture and dimension, flattering for heart-shaped faces');
