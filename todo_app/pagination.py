from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class TodoListCreatePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 20
    limit_query_param = "limit"
    offset_query_param = "start"
    
class ListPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 20
    