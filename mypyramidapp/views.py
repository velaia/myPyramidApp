from pyramid.view import view_config

from mypyramidapp.fake_data import get_orders


@view_config(route_name='home', renderer="templates/mytemplate.pt")
def my_view(request):
    orders = get_orders()
    return {'project': 'myPyramidApp', 'orders': orders}
