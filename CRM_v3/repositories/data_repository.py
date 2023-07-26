from sqlalchemy import func

class DataRepository:
    __PER_PAGE = 10
    def get_page_data(self, model, page, search=None):
        offset = (page - 1) * 10
        
        if search:
            return model.query.filter(*search).limit(self.__PER_PAGE).offset(offset).all()
        else:
            return model.query.limit(self.__PER_PAGE).offset(offset).all()
        
    def get_total_pages(self, model, search=None):
        if search:
            count = model.query.with_entities(func.count()).filter(*search).scalar()
        else:
            count = model.query.with_entities(func.count()).scalar()
        
        result = count // self.__PER_PAGE + (count % self.__PER_PAGE > 0)
        return result
    
    def search_by_id(self, model, selected_id):
        return model.query.filter_by(id = selected_id).first()