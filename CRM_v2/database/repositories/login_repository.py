from database.repositories.common.datafetcher import DataFetcher

class Login(DataFetcher):
    def __init__(self):
        super().__init__()

    def get_login_user_data(self, data_type, id, password):
        query = f"SELECT * FROM {data_type} WHERE loginid = ? AND loginpassword = ?"
        row = (f"{id}", f"{password}")
        return self.fetch_one_data(query, row)
        # row로 fetchone