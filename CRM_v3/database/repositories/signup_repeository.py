from database.repositories.common.datafetcher import DataFetcher

class Signup(DataFetcher):
    def __init__(self):
        super().__init__()

    def check_id_existence(self,data_type, id):
        query = f"SELECT LoginId FROM {data_type} WHERE LoginId = ?"
        row = (f"{id}", )
        return self.fetch_one_data(query, row)
    
    def insert_admin_signup_data(self, id, password):
        query = f"""
                INSERT INTO admin (LoginId, LoginPassword) VALUES (?, ?)
                """
        row = (f"{id}", f"{password}")
        return self.insert_data(query, row)
    
    def insert_user_signup_data(self, id, name, gender, birthdate, age, address, loginid, loginpassword):
        query = f"""
                INSERT INTO user
                (Id, Name, Gender, Birthdate, Age, Address, LoginId, LoginPassword)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
        row = (id, name, gender, birthdate, age, address, loginid, loginpassword)
        return self.insert_data(query, row)