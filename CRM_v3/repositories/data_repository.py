from sqlalchemy import func
from app import db

class DataRepository:
    __PER_PAGE = 10
    def get_page_data(self, model, page, search=None):
        offset = (page - 1) * self.__PER_PAGE
        
        if search:
            return model.query.filter(*search).limit(self.__PER_PAGE).offset(offset).all()
        else:
            return model.query.limit(self.__PER_PAGE).offset(offset).all()
        
    def get_total_pages(self, model, search=None):
        query = db.session.query(func.count())

        if search:
            query = query.filter(*search)

        total_count = query.select_from(model).scalar()
        total_pages = (total_count - 1) // self.__PER_PAGE + 1
        print(total_count, total_pages, query)
        return total_pages
    
    def search_by_id(self, model, selected_id):
        return model.query.filter_by(id = selected_id).first()