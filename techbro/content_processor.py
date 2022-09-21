from cart.models import Shopcart

def cartcount(request):
    count = Shopcart.objects.filter(user__username = request.user.username, paid = False)

    itemcount = 0

    for item in count:
        itemcount += item.c_item

    context = {
        'itemcount':itemcount
    }

    return context