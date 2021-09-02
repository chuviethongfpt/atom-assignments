CREATE SCHEMA dim;

CREATE TABLE dim.Order_Transaction
(
    Order_ID TEXT PRIMARY KEY,
    Staff_Name TEXT NOT NULL,
    Staff_Code TEXT NOT NULL,
    Customer_Code TEXT NOT NULL,
    Advertising_Code TEXT,
    Document_Date DATE NOT NULL,
    Complete_Date DATE NOT NULL,
    Order_Status TEXT NOT NULL,
    Package_Status TEXT NOT NULL,
    Delivery_Status TEXT NOT NULL,
    Payment_Status TEXT NOT NULL,
    Return_Status TEXT NOT NULL
);

CREATE TABLE dim.Customer
(
    Customer_Code TEXT PRIMARY KEY,
    Source TEXT,
    Channel TEXT,
    District TEXT,
    City TEXT
);

CREATE TABLE dim.Advertising
(
    Advertising_Code TEXT PRIMARY KEY,
    Name TEXT,
    Period TEXT
);

CREATE TABLE dim.Inventory
(
    Mã_đơn_nhập_hàng TEXT PRIMARY KEY,
    Ngày_tạo_đơn_nhập_hàng DATE,
    Ngày_duyệt_đơn DATE,
    Ngày_hoàn_thành DATE,
    Chi_nhánh TEXT
);

CREATE TABLE dim.Production
(
    Mã_lô TEXT PRIMARY KEY,
    Ngày_sản_xuất DATE,
    Ngày_hết_hạn DATE,
    Tồn_kho TEXT
);

CREATE TABLE dim.Staff 
(
    Staff_Name TEXT NOT NULL,
    Staff_Code TEXT PRIMARY KEY,
    Type_of_Key_Person TEXT NOT NULL
);

CREATE TABLE dim.Line_item
(
    Order_ID TEXT NOT NULL, 
    Product_Code TEXT NOT NULL,
    Product_Type TEXT NOT NULL,
    Quantity INTEGER NOT NULL,
    Unit TEXT,
    Discount MONEY,
    Branch TEXT NOT NULL
);

CREATE TABLE dim.Product
(
    Product_Code TEXT PRIMARY KEY,
    Product_Name TEXT NOT NULL,
    Group_Product TEXT NOT NULL,
    Unit_Price MONEY NOT NULL,
    Brand TEXT
);

ALTER TABLE dim.Order_Transaction
ADD FOREIGN KEY (Customer_Code) REFERENCES dim.Customer (Customer_Code);
ALTER TABLE dim.Order_Transaction
ADD FOREIGN KEY (Advertising_Code) REFERENCES dim.Advertising (Advertising_Code);
ALTER TABLE dim.Order_Transaction
ADD FOREIGN KEY (Staff_Code) REFERENCES dim.Staff (Staff_Code);
ALTER TABLE dim.Line_item
ADD FOREIGN KEY (Order_ID) REFERENCES dim.Order_Transaction (Order_ID);
ALTER TABLE dim.Line_item
ADD FOREIGN KEY (Product_Code) REFERENCES dim.Product (Product_Code);
