add_products_sql = """
INSERT INTO products(name, price, description) VALUES
('mlieko', 22.9, 'napoj zivocisneho povodu'),
('chlieb', 1.89, 'pekarsky vyrobok z psnicovej muky'),
('maslo', 3.49, 'tucny mliecny vyrobok'),
('vajcia', 2.99, 'balenie 10 kusov cerstvych vajec'),
('syr eidam', 4.20, 'polotuhy kravsky syr'),
('jogurt', 0.89, 'biely naturalny jogurt 150g'),
('kuracie prsia', 6.50, 'cerstve kuracie prsia 500g'),
('ryza', 1.49, 'dlhozrnna biela ryza 1kg'),
('cestoviny', 1.29, 'spagety z tvrdej psenice 500g'),
('paradajky', 1.99, 'cerstve paradajky 500g');
"""


add_orders_sql = """
INSERT INTO orders(description) VALUES
('objednavka kancelarskeho papiera A4'),
('dodavka tlaciarenskych tonerových kaziet'),
('nakup kancelarskeho nabytku - stoly a stolicke'),
('objednavka pocitacovych mysí a klavesníc'),
('servis a oprava firemnych pocitacov'),
('objednavka prezentacnych materialov'),
('nakup kancelarskeho spotrebneho materialu'),
('dodavka cistiacich prostriedkov do kancelarie'),
('objednavka firemnych vizitiek a razitok'),
('nakup projektora a premietacieho platna');
"""

add_clients_sql = """
INSERT INTO customers(name, surname)
VALUES
('Adam', 'Novak'),
('Peter', 'Horvath'),
('Jana', 'Kováčová'),
('Martin', 'Svoboda'),
('Lucia', 'Blaho'),
('Tomáš', 'Krajči'),
('Zuzana', 'Marková'),
('Michal', 'Beneš'),
('Eva', 'Šimková'),
('Rastislav', 'Polák');
"""
